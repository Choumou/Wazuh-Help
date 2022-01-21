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

def add_rule(path):

    parameters = {}
    while True:
        print("Enter new rule's ID : ", end="")
        new_id = input()
        if (new_id == "q" or new_id == "quit"):
            return

        try:
            if (int(new_id, 10) < 100000):
                print("This ID is too small... Try again")
                continue
            elif (int(new_id, 10) > 999999):
                print("This ID is too big... Try again")
                continue
            f = open(path, "r")
            content = f.read()
            comp_str = "<rule id=\"" + new_id + "\""
            if (comp_str in content):
                print("This rule's ID already exists... Try again")
                continue
            f.close()
            print("New rule's ID is " + new_id + ".\n")
            parameters["id"] = new_id
            break

        except:
            print("This input is not a valid ID... Try again")
            continue

    while True:
        print("Enter new rule's level : ", end="")
        new_level = input()
        if (new_id == "q" or new_id == "quit"):
            return

        try:
            if (int(new_level, 10) > 13 or int(new_level, 10) < 0):
                print("Level must be in range 0, 13... Try again")
                continue
            print("New rule's level is " + new_level + ".\n")
            parameters["level"] = new_level
            break
        except:
            print("This input is not a valid level... Try again")
            continue

    print("Enter new rule's description : ", end="")
    description = input()
    parameters["description"] = description
    print("New rule's description is " + description + ".\n")

    list_param = ["if_sid", "field", "options", "match"]
    while True:
        print("Parameters : id_sid, field, options, match.")
        print("Enter new parameter you want for this rule (Enter \"done\" if you add all parameters you want) : ")
        param = input()
        if (param == "q" or param == "quit"):
            return

        if (param == "done"):
            break

        if (param not in list_param):
            print("Bad parameter... Try again")
            continue

        if (param == "if_sid"):

            while True:
                print("Enter the value of if_sid parameter : ")
                if_sid = input()
                if (param == "q" or param == "quit"):
                    return
                try:
                    int(if_sid, 10)
                    print("if_sid : " + if_sid)
                    parameters[param] = if_sid
                    break
                except:
                    print("This input is not a valid if_sid... Try again")

        elif (param == "field"):
            print("Enter type of the field you want for this rule : ")
            field_name = input()
            param += " " + field_name + "=\""
            print("Enter the name of this field : ")
            field_value = input()
            param += field_value + "\""
            print("Enter the value of this field : ")
            value = input()
            parameters[param] = value

        else:
            print("Enter the value of the current parameters : ")
            value = input()
            parameters[param] = value

    for p in parameters:
        print(p + " : " + parameters[p])

    print("\nDo you confirm the creation of the rule (y/n) : ")
    r = input()
    if (r != "y" and r != "yes"):
        print("Quiting creation of the rule...")
        return

    print("\nCreation of the rule and writing in file : " + path + "...")
    to_write = "  <rule id=\"" + parameters["id"] + "\" level=\"" + parameters["level"] + "\">\n"
    for p in parameters:
        if (p == "id" or p == "level"):
            continue
        finish_line = p.split(' ')[0]
        to_write += "\t<" + p + ">" + parameters[p] + "</" + finish_line + ">\n"
    to_write += "  </rule>"

    f = open(path, 'r')
    file_content = f.read()
    li = file_content.rsplit("</group>", 1)
    file_content = ''.join(li)
    f.close()
    f = open(path, 'w+')
    file_content += "\n" + to_write + "\n</group>"
    f.write(file_content)
    f.close()

    print("Rule writed in file : " + path + ".")


def print_help():
    print("Help :")
    print("change_path : Change the path where rules can be added")
    print("path : Print the current path")
    print("add_rule : Add a rule in the current path")
    print("quit, q : Quit the programm")


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
            add_rule(PATH_RULES_FILE)
        elif (user_input == "q" or user_input == "quit"):
            return
        elif (user_input == "path"):
            print(PATH_RULES_FILE)
        elif (user_input == "h" or user_input == "help"):
            print_help()
        else:
            print("Can't understand the command")

main()
