from adressbook import AddressBook, Record, Phone, Name

USERS = AddressBook()


def handle_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user"
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner



def hello_user():
    return "Whats up"

def unknown_command(user_input):
    return f"unknown_command {user_input}"

def close_app():
    exit('Good Bye')

def add_user(name: str, phone: str) -> str:
    name_field = Name(name)
    phone_field = Phone(phone)
    if name in USERS:
        record = USERS[name]
        record.add_phone(phone_field)
        return f"Phone {phone} added for {name}"
    else:
        record = Record(name_field)
        record.add_phone(phone_field)
        USERS.add_record(record)
        return f"User {name} added with phone {phone}"

def change_phone(name: Name, new_phone: Phone) -> str:
    if name in USERS:
        record = USERS[name]
        old_phone = record.phones[0]
        record.phones[0] = new_phone
        USERS[name] = record
        return f'User {name} has new number: {new_phone}, old phone number: {old_phone}'
    else:
        return f'This user: {name} is not in your phone book'
    

def show_all() -> str:
    if not USERS:
        return 'No users in the phone book'
    result = ''
    for record in USERS.values():
        result += str(record) + '\n'
    return result

def show_phone(name_str: str) -> str:
    name_field = Name(name_str)
    if name_field.value in USERS:
        record = USERS[name_field.value]
        return f"{name_field.value}'s phone number is {record.phones[0]}"
    else:
        return f"No phone number found for {name_field.value}"

UI_HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'phone': show_phone,
    'show all': show_all,
    'exit': close_app,
    'good bye': close_app,
    'close': close_app,
}


def parse_input(user_input):
    parts = user_input.split()
    user_input_name = parts[0]
    if user_input_name == 'show' and 'all' in parts:
        user_input_name = 'show all'
        user_input_args = []
    elif user_input_name == 'good' and 'bye' in parts:
        user_input_name = 'good bye'
        user_input_args = []
    elif len(parts)>1:
        user_input_args = parts[1:]
    else:
        user_input_args=[]
    return user_input_name, user_input_args

def main():
    while True:
        user_input = input("Enter command: ")
        if not user_input:
            continue
        command, args = parse_input(user_input)
        if command not in UI_HANDLERS:
            print(unknown_command(user_input))
        else:
            result = UI_HANDLERS[command](*args)
            print(result)
        

if __name__ == '__main__':
    main()