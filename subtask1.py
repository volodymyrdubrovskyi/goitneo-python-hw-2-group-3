# ввод с командной строки (с терминала)
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# декоратор функции add_contact
def add_contact_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
    return inner

# добавление контакта
@add_contact_error
def add_contact(args, contacts):
        name, phone = args
        contacts[name] = phone
        return "Contact added."

# декоратор функции change_contact
def change_contact_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me existing name, and a new phone, please."
    return inner

# изменение контакта
@change_contact_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Name doesn't find."

# вывод всех контактов в терминал
def show_all(contacts):
    res = ''
    for contact, phone_number in contacts.items():
        res = (f"{contact:>15} : {phone_number:<20}") if not res else res + '\n' + (f"{contact:>15} : {phone_number:<20}")
    return res    

# поиск контакта
def show_phone(args, contacts):
        name = args[0]
        if name in contacts.keys():
            return contacts[name]
        else:
            return "Didn't find"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            else:
                print("Invalid command.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()