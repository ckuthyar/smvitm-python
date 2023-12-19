import MFO
import os
import time
i = 0
print("Hello and wellcome.")
print("in this app, you can remove, overwrite, create and read files in a folder where you open this app.")
print("After you type your file name,\nyou must type '.py' or '.txt'.\nOtherwise you cannot open the file that you have created.")
print("Definition of '.py' and '.txt' and:")
print("After you write the file name, if you type '.py' the file you created will be python file.")
print("Which means you can only write python code on that file.")
print("instead of '.py' if you write '.txt', you can write any text that you want to.\n")
print("Note: When you use 'execute a file' mode, please type a valid text file\nthat is saved with a python")
mode = input("Enter the mode: ")
while True:
    mode_lower = mode.lower()
    match(mode_lower):
        case "overwrite":
            f1 = input("What file to write: ")
            print("Write '\ n' without space if you want to write the content in new line.")
            print("Note: if you enter a file that does not exist,\nthe file that you entered will be created \n and the content is written.")
            f2 = input("What to write: ")
            MFO.wfile(f1, f2)
            print("Process finished")
        case "create":
            c1 = input("What is the name of file that should be created: ")
            MFO.cfile(c1)
            print("Process finished")
        case "remove":
            print("Please enter the valid file name, otherwise you will get an error.")
            r = input("Which file to remove: ")
            os.remove(r)
            print("Process finished")
        case "read":
            reader_inp = input("Enter the file name that should be readed: ")
            re = MFO.rfile(reader_inp)
            print("The contents of the file are:")
            print("\n"+re)
        case "show list of files":
            files = os.listdir()
            print("The files and folder available in this folder are:\n")
            for file in files:
                print(file)
        case "execute a file":
            i = input("Enter file name: ")
            f = open(i, "r")
            c = f.read()
            print(f"Execution of file '{i}': ")
            exec(c)
            print()
    breaker1 = input("Do you want to close this app: ")
    breaker2 = breaker1.lower()
    if breaker2 == "yes":
        break
    print()
print("the app will close in 7 seconds.")
time.sleep(7)
