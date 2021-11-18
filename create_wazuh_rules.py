#
# /!\ This script must be run as root
#

def change_path():
    while (True):
        print("Type the new path :")
        new_path = input()
        print("")
        if (new_path == "q" or new_path == "quit"):
            return ""
        try:
            f = open(new_path, "r")
            print("New path is : " + new_path)
            return new_path
        except:
            print("Wrong path !")

def add_rule():
    print("ADD")

def main():
    
    PATH_RULES_FILE = "/var/ossec/etc/rules/local_rules.xml"

    print("Default rules file'path is : " + PATH_RULES_FILE)
    print("Type change_path to modify it.\n\n")

    while (True):

        print("> ", end="")
        user_input = input()
        
        if (user_input == "change_path"):
            res = change_path()
            if res != "":
                PATH_RULES_FILE = res

        elif (user_input == "add_rule"):
            add_rule()
        elif (user_input == "q" or user_input == "quit"):
            return
        elif (user_input == "path"):
            print(PATH_RULES_FILE)
        else:
            print("Can't understand the command")

main()
