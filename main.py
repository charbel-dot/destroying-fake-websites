from destroy import spam
import os, time

while True: # infinite loop to keep sending data to the website's server
    try:
        spam()

    except ImportError: # handling packages not found and instaling them
        print("Could not found required packages!\nDo you want to install them?(y/n)")
        response = str(input(""))

        if response == 'y' or response == 'Y':
            os.system("pip install requests && pip install threading")

        elif response == 'n' or response == 'N':
            time.sleep(0.5)
            os.system("\nExiting the program..")
