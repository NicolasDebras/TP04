import json
from models.note import Note
def loadData():
    data = ""
    with open('./data/data.json') as f:
        data = f.read()
    parsed_json = json.loads(data)
    metros = [Note(**note_dict) for note_dict in parsed_json]
    return metros

def saveData(base):
    base2=[]
    for i in range(len(base)):
        if(type(base[i])==dict):
            base2.append(base[i])
        else:
            base2.append(base[i].__dict__)

    json_object = json.dumps(base2, indent=4)
    with open('./data/data.json', 'w') as f:
        f.write(json_object)


def addTask(note: Note, base):
    base.append(note.__dict__)
    return base


def removeTask(id, base):
    delete = 0
    for i in range(len(base)):
        if base[i].id == id:
            delete = i
    base.pop(delete)
    return base


def getNewId(base):
    if len(base) == 0:
        return 0
    note = base[-1]
    return note.id + 1
