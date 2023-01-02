
def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Sorry,check the order of the arguments and try again"
        except KeyError:
            return "You entered the wrong name"

    return wrapper


contacts = {}


@input_error
def hello(*args):
    return f"How can I help you?"


@input_error
def add(*args):
    contacts[args[0]] = args[1]
    return "Contact {args[0]} was added successfully"


@input_error
def phone(*args):
    return contacts[args[0]]


@input_error
def show_all(*args):
    for name, phone in contacts.items():
        print(f"Name: {name}, phone: {phone}")


@input_error
def change(*args):
    if args[0] in contacts:
        contacts[args[0]] = args[1]
    else:
        return f"This contact is not listed "
    return f"Contact {args[0]} was successfully changed"


@input_error
def bye(*args):
    contacts.clear()
    return f"Good bye!"


@input_error
def bye1(*args):
    contacts.clear()
    return f"Good bye!"


@input_error
def bye2(*args):
    contacts.clear()
    return f"Good bye!"


COMMANDS = {add: "add",
            phone: "phone",
            show_all: "show_all",
            change: "change",
            hello: "hello",
            bye1: "exit",
            bye2: "good bye",
            bye: "close"
           }


def command_parser(user_input: str):
    for command, key_word in COMMANDS.items():
        if user_input.startswith(key_word):
            return command, user_input.replace(key_word, "").strip().split(" ")
    return None, None


def main():
    while True:
        user_input = input(">>>")
        if user_input == ".":
            break
        command, data = command_parser(user_input)

        if not command:
            print("Sorry, unknown command")
        else:
            print(command(*data))


if __name__ == "__main__":
    main()