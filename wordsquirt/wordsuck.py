from tinydb import TinyDB, Query
from os.path import expanduser
import sys

DB_FILE_PATH = expanduser("~/.wordsquirt.json")

db_handle = TinyDB(DB_FILE_PATH)

sys.argv.pop(0)
trigger = sys.argv.pop(0)
save_string = " ".join(sys.argv)

db_handle.insert({"trigger" : trigger, "text" : save_string})
