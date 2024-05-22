from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        if not value.isalpha():
           raise ValueError('The name must contain only letters')
        super().__init__(value)
   

class Phone(Field):
    # реалізація класу
    
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError ('Phone mast contain only numbers and 10 digits')
        super().__init__(value)
		

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        # реалізація класу
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone (self, old_phone, new_phone):
        found = False
        for phone in self.phones:
            
            if phone.value == old_phone:
                phone.value = new_phone
                found = True
                break
        if not found:
            raise ValueError ('Old number not found')
    def find_phone (self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return "Number is not exist"
                
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу

    def add_record(self, record):
        if record.name.value in self.data:
            self.data[record.name.value].pnone.extend(record.phones)
        else:
            self.data[record.name.value] = record

    def find (self, name):
        return self.data.get(name)
    
    def delete (self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError ('Record is not found')        

 


book = AddressBook()
john_record = Record("John")
john_record.add_phone("0000000000")
john_record.add_phone("2222222222")
john_record.add_phone("1111111111")
print (john_record)
book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
for name, record in book.data.items():
    print(record)
john = book.find("John")
john.edit_phone("1111111111", "1112223333")
print(john)
found_phone = john.find_phone("0000000000")
print(f"{john.name}: {found_phone}")
book.delete("John")

