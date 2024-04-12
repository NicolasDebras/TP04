from service.display import printtask, printReport
from service.utils import addTask, removeTask,getNewId,saveData
from models.note import Note


def isChecked(note)-> bool:
    if note.isChecked:
        return True
    return False


def chooseAction(arg, listNote: list[Note], contentOrid = None):
    match arg:
        case "done":
            printtask(filter(isChecked, listNote))
        case "all":
            printtask(listNote)
        case "report":
            printReport(filter(isChecked, listNote))
        case "add":
            newBase=addTask(Note(getNewId(listNote), contentOrid), listNote)
            saveData(newBase)
        case "delete":
            newBase=removeTask(contentOrid,listNote)
            saveData(newBase)
        case "check":
            #pintlistoftaskdone(listNote)
            contentOrid=int(contentOrid)
            for i in range(len(listNote)):
                if(listNote[i].id==contentOrid):
                    listNote[i].check_note()
            saveData(listNote)
            return
        case _:
            printtask(listNote)