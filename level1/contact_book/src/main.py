from collections import defaultdict
import pandas as pd
from termcolor import colored

class ContactBook():
    def __init__(self):
        """
        Create a dictionary to store contacts.
        """
        self.contact = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: str = None):
        """
        Adds a new contact to the self.contact dictionary.

        Parameters
        ----------
        name (str) :The name of the contact. Must be unique and not already in self.contact.
        phone (str) : The phone number of the contact.
        email (str, optional) The email address of the contact.
        """
        if name in self.contact:
            print("Contact Already Existed!")
            return
        
        self.contact[name]["phone"] = phone
        self.contact[name]["email"] = email
        
    def view_contact(self):
        """
        Prints a table of the contacts in the self.contact dictionary.
        """
        names = []
        phones = []
        emails = []
        
        for name, info in self.contact.items():
            names.append(name)
            phones.append(info["phone"])
            emails.append(info["email"])
        
        data = {'Names': names, "Phones": phones, "Emails":emails}
        df = pd.DataFrame(data)
        print(colored(df, "yellow"))
        print("-" * 50)
            
    def delete_contact(self, name):
        """
        Deletes a contact from the self.contact dictionary.

        Parameters
        ----------
        name (str) : The name of the contact to be deleted. Must be in self.contact.
        """
        if name in self.contact:
            del self.contact[name]
            print(colored("Contact deleted successfully!", "green"))
        else:
            print(colored("Contact not found!", "red"))
    
    def updated_contact(self, name, phone=None, email=None):
        """Updates a contact in the self.contact dictionary.

        Parameters
        ----------
        name (str): The name of the contact to be updated. Must be in self.contact.
        phone (str, optional): The new phone number of the contact. Defaults to None.
        email (str, optional): The new email address of the contact. Defaults to None.
        """
        if name in self.contact:
            if phone:
                self.contact[name]['phone'] = phone
            if email:
                self.contact[name]['email'] = email     
            print(colored("Contact updated successfully!", "green"))
        else:
            print(colored("Contact not found!", "red"))
    

if __name__ == "__main__":
    book = ContactBook()


while True:
    print(colored("\n\nWelcome to contact book app", "green"))
    print(colored("1. Add Contact", "cyan"))
    print(colored("2. Edit Contact", "yellow"))
    print(colored("3. View Contact", "magenta"))
    print(colored("4. Delete contact", "blue"))
    print(colored("5. Exit", "red"))
    
    input_from_user = input(colored("\n\nPlease choose an option: ", "black"))
    if input_from_user == "5":
        break
    
    elif input_from_user == "1":
        name = input(colored("\nEnter contact name: ", "black"))
        phone = input(colored("\nEnter contact phone: ", "black"))
        email = input(colored("\nEnter contact email: ", "black"))
        
        book.add_contact(name, phone, email)
    
    elif input_from_user == "2":
        name = input(colored("\nEnter contact name: ", "black"))
        phone = input(colored("\nEnter contact phone: ", "black"))
        email = input(colored("\nEnter contact email: ", "black"))
        
        book.updated_contact(name, phone, email)
        
    elif input_from_user == "3":
        print(colored("\n\nList of contacts", "black"))
        book.view_contact()
    
    elif input_from_user == "4":
        name = input(colored("\nEnter contact name: ", "black"))
        book.delete_contact(name)
        
    else:
        print(colored("Your input is invalid", "red"))
