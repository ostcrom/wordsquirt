from pynput import keyboard
from tinydb import TinyDB, Query
from os.path import expanduser
from time import sleep
from cheatsheetgenerator import CheatSheetGenerator


#
# query_handle = Query()

class WSDaemon():
    def __init__(self, options):
        self.kb_listener = keyboard.Listener(on_press = self.listener_on_press)
        self.kb_controller = keyboard.Controller()
        self.buffer_arr = []
        self.buffer_limit = int(options['buffer_limit'])
        self.expansion_file = options['expansion_file']
        self.trigger_prefix = options['trigger_prefix']
        self.cheatsheet_file = options['cheatsheet_file']
        self.expansion_arr = []
        self.load_keywords()

    def init_db(self):
        ##Try to close DB, then load a new copy.
        try:
            self.db_handle.close()
        except:
            pass

        self.db_handle = TinyDB(self.expansion_file, sort_keys=True, indent=1)


    def start(self):
        self.kb_listener.start()

    def listener_on_press(self, key_obj):
        self.update_buffer(key_obj)
        self.parse_buffer()

    def update_buffer(self, key_obj):
        if isinstance(key_obj, keyboard.KeyCode):
            ##Drop oldest character from buffer if we're over limit.
            char = key_obj.char
            if len(self.buffer_arr) + 1 > self.buffer_limit + len(self.trigger_prefix):
                self.buffer_arr.pop(0)
            ##Add character to buffer
            self.buffer_arr.append(char)
        ##Delete the last character if backspace is pressed and array is not empty.
        elif key_obj == keyboard.Key.backspace and len(self.buffer_arr):
            self.buffer_arr.pop()

    def parse_buffer(self):
        buffer_string = "".join(self.buffer_arr)
        for expansion in self.expansion_arr:
            if buffer_string.endswith(self.trigger_prefix + expansion["trigger"]):
                self.execute_expansion(expansion["trigger"], str(expansion["text"]))
                ##Ideally I think the buffer should be cleared, but the typing
                ##appears to occur asyncronously. So even if I clear the buffer
                ##after calling the "press" functions, the keypresses don't
                ##appear to register until returning to the main loop.
                ##However, in practice it doesn't seem to cause an issue.

    def load_keywords(self):
        self.init_db()
        del self.expansion_arr[:]

        for row in iter(self.db_handle):

            self.expansion_arr.append(row)
        self.create_cheatsheet()

    def save_expansion(self, trigger, expansion):
        if not self.validate_unique_trigger(trigger):
            return False
        self.db_handle.insert({"trigger" : trigger, "text" : expansion})
        self.load_keywords()
        return True

    def delete_expansion(self, trigger):
        trigger_query = Query()
        ##Only try to delete if it already exists...
        if validate_unique_trigger(trigger):
            self.db_handle.remove(trigger_query == trigger)

    def validate_unique_trigger(self, trigger):
        trigger_query = Query()
        ##If there are no results we want to evaluate to true, false if
        ##anything is returned:
        return not self.db_handle.search(trigger_query.trigger == trigger)

    def execute_expansion(self, trigger, expansion):
        ##Erase the typed trigger, spit out the expansion.
        delete_length = len(self.trigger_prefix + trigger)
        for i in range(delete_length):
            self.kb_controller.press(keyboard.Key.backspace)

        for char in expansion:
            self.kb_controller.press(char)

    def create_cheatsheet(self):
        cs_generator = CheatSheetGenerator(self.cheatsheet_file)
        for expansion in self.expansion_arr:

            trigger = expansion["trigger"]
            text = expansion["text"]
            cs_generator.add_entry(trigger, text)

        cs_generator.write_output()
