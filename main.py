# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return

def read_from_file(name):
    try:
        with open(name , "r") as file:
            contents = file.read()
            if len(contents) == 0:
                print("file is empty!!")
                return False
            print(contents)
            return True

    except FileNotFoundError:
        print("file not found")
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    name = input("Plz enter the name of the file! :")
    if len(name) == 0:
        print("plz enter a the name ")
        name = input("Plz enter the name of the file! :")

    read_from_file(name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
