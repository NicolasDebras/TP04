from datetime import datetime

def printReport(listnotedone):
    print("# Report")
    print("## Tasks done:")

    for element in listnotedone:
        formattted_date = datetime.utcfromtimestamp(element.checkDateTs)
        print("- " + element.content + " ("  + formattted_date.strftime('%Y-%m-%d') + ")")

def printonetask(onetask):
    print(onetask.content)

def printtask(listtask):
    i = 1

    for element in listtask:
        string = "["
        if element.id < 10:
            string += "0" + str(element.id)
        else :
            string += str(element.id)
        string += "]["
        if (not element.isChecked):
            string += " "
        else:
            string += "X"
        string += "] " + element.content + " (" + element.calculate_amount_of_time()  + ")"
        print(string)
        i = i + 1
