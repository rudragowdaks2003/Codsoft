import json
import os

CONTACTS_FILE = 'contacts.json'

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            contacts_data = json.load(file)
            return [Contact(**data) for data in contacts_data]
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump([contact.__dict__ for contact in contacts], file, indent=4)

def print_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts.append(Contact(name, phone, email, address))
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for contact in contacts:
        print(contact)

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if search_term in contact.name or search_term in contact.phone]
    if not results:
        print("No contacts found.")
    else:
        for contact in results:
            print(contact)

def update_contact(contacts):
    search_term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term in contact.name or search_term in contact.phone:
            print(f"Current details: {contact}")
            name = input("Enter new name (or press Enter to keep current): ")
            phone = input("Enter new phone number (or press Enter to keep current): ")
            email = input("Enter new email address (or press Enter to keep current): ")
            address = input("Enter new address (or press Enter to keep current): ")
            
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            if address:
                contact.address = address
            
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_term = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term in contact.name or search_term in contact.phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print_menu()
        choice = input("Choose an option (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
