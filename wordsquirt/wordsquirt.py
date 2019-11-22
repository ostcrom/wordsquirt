from tinydb import TinyDB, Query
from os.path import expanduser
import sys

DB_FILE_PATH = expanduser("~/.wordsquirt.json")

db_handle = TinyDB(DB_FILE_PATH)

query_handle = Query()

try:
    input_string = sys.argv[1]
    query_result = db_handle.search(query_handle.trigger == input_string).pop()
    print(query_result["text"])
except IndexError:
    pass
