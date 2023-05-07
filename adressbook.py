from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value=None):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)


class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        
    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        
    def edit_phone(self, new_phone: Phone):
        self.phones = new_phone
        
    def delete_phone(self, phone_index: int):
        del self.phones[phone_index]
        
    def __str__(self):
        phones = ", ".join([str(phone) for phone in self.phones])
        return f"{self.name}: {phones}"

        

class AddressBook(UserDict):
    def add_record(self, record: Record):
        key = record.name.value
        self.data[key] = record

