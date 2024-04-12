import sys
import models.note
import service.utils
from service.choose import isChecked,chooseAction


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data=service.utils.loadData()
    if(len(sys.argv) == 1):
        print("Erreur il manque des arguments")
    else:
        val1 = sys.argv[2] if len(sys.argv) == 3 else None

        chooseAction(sys.argv[1], data, val1)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
