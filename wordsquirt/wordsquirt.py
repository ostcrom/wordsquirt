from os import system, path
import configparser
import rumps
from wsdaemon import WSDaemon

CONFIG_LOCATION = path.expanduser("~/.wordsquirtconf")
DEFAULT_OPTIONS = {
'expansion_file' : path.expanduser("~/.wordsquirt"),
'trigger_prefix' : ',,',
'buffer_limit' : 10
}
APP_TITLE = "✒️💦"
ADD_EX_LABEL = "Add New Text Expansion"
EDIT_EX_LABEL = "Edit Expansion File"
RELOAD_EX_LABEL = "Reload Expansion File"
EDIT_CONF_LABEL = "Edit Config File"

class WordSquirt(rumps.App):
    def __init__(self):
        super(WordSquirt, self).__init__(APP_TITLE)
        self.config_obj = configparser.ConfigParser()
        self.load_options()
        self.menu = [ADD_EX_LABEL,EDIT_EX_LABEL, RELOAD_EX_LABEL,EDIT_CONF_LABEL]

        self.wsdaemon = WSDaemon(self.config_obj['options'])
        self.wsdaemon.kb_listener.start()

    @rumps.clicked(ADD_EX_LABEL)
    def add_expansion(self, _):
        window = rumps.Window("Specify trigger shortcut (do not include prefix):", "Specify New Trigger")
        first_prompt = window.run()
        trigger = first_prompt.text
        if not self.wsdaemon.validate_unique_trigger(trigger):
            rumps.alert(f"Expansion with trigger {trigger} already exists!")
            return False
        elif len(trigger) > self.wsdaemon.buffer_limit:
            rumps.alert(f"Trigger \"{trigger}\" too long, max length is {self.wsdaemon.buffer_limit} characters")
            return False
        window = rumps.Window(f"Specify expansion for {trigger}:", "Specify New Expansion")
        second_prompt = window.run()
        expansion = second_prompt.text
        self.wsdaemon.save_expansion(trigger,expansion)

    @rumps.clicked(EDIT_EX_LABEL)
    def edit_expansions(self, _):
        target = self.config_obj['options']['expansion_file']
        system(f"open {target}")


    @rumps.clicked(EDIT_CONF_LABEL)
    def edit_preferences(self, _):
        system(f"open {CONFIG_LOCATION}")

    @rumps.clicked(RELOAD_EX_LABEL)
    def reload_expansions(self, _):
        self.wsdaemon.load_keywords()
        rumps.alert("Expansions reloaded.")

    def load_options(self):
        if not path.exists(CONFIG_LOCATION):
            self.set_option_defaults()
        else:
            self.config_obj.read(CONFIG_LOCATION)

            must_save = False
            for option in DEFAULT_OPTIONS:
                if not self.config_obj.has_option('options', option):
                    self.config_obj.set('options', option, str(DEFAULT_OPTIONS[option]))
                    must_save = True
            if must_save:
                with open(CONFIG_LOCATION, 'w') as configfile:
                    self.config_obj.write(configfile)

    def set_option_defaults(self):
        self.config_obj['options'] = DEFAULT_OPTIONS

        with open(CONFIG_LOCATION, 'w') as configfile:
            self.config_obj.write(configfile)

if __name__ == "__main__":
    WordSquirt().run()
