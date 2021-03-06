import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id=0

def init():
    global entries, next_id
    try:

        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        #entries[0]['id']+1
        for each_d in entries:
            if each_d['id'] > next_id:
                next_id = each_d['id']+1
    except:
        print("Couldn't open", GUESTBOOK_ENTRIES_FILE)
        entries = []


def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()

    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "id":str(next_id)}
    entries.insert(0, entry) ## add to front of list
    next_id += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

    #next_id += 1

def delete_entry(_id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for each_d in entries:
        if str(each_d['id']) == str(_id):
            entries.remove(each_d)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
