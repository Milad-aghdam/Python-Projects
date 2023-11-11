# Contact Book App
This is a simple Python script that allows you to create and manage a contact book using a command-line interface. You can add, edit, view, and delete contacts using the menu options. The contacts are stored in a dictionary and displayed as a table using pandas and termcolor modules.

## Requirements
To run this script, you need to have Python 3 and the following modules installed:

- collections
- pandas
- termcolor

You can install them using pip:

``` python
pip install pandas
pip install termcolor
```

## Usage
To run the script, navigate to the directory where the script is located and execute the following command:
```bash
python contact_book.py
```

You will see a welcome message and a menu with five options:
``` bash
Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit
```

To choose an option, enter the corresponding number and press enter. Follow the instructions on the screen to perform the desired action. For example, to add a new contact, enter 1 and provide the name, phone, and email of the contact. To view the existing contacts, enter 3 and see the table of contacts. To exit the program, enter 5.

## Example
Here is an example of how the script works:

```bash 
Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit

Please choose an option: 1

Enter contact name: Alice
Enter contact phone: 1234567890
Enter contact email: alice@example.com

Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit

Please choose an option: 1

Enter contact name: Bob
Enter contact phone: 0987654321
Enter contact email: bob@example.com

Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit

Please choose an option: 3

List of contacts
   Names      Phones          Emails
0  Alice  1234567890  alice@example.com
1    Bob  0987654321    bob@example.com
--------------------------------------------------

Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit

Please choose an option: 2

Enter contact name: Alice
Enter contact phone: 1111111111
Enter contact email: alice@new.com
Contact updated successfully!

Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit

Please choose an option: 3

List of contacts
   Names      Phones         Emails
0  Alice  1111111111   alice@new.com
1    Bob  0987654321   bob@example.com
--------------------------------------------------

Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit

Please choose an option: 4

Enter contact name: Bob
Contact deleted successfully!

Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit

Please choose an option: 3

List of contacts
   Names      Phones        Emails
0  Alice  1111111111  alice@new.com
--------------------------------------------------

Welcome to contact book app
1. Add Contact
2. Edit Contact
3. View Contact
4. Delete contact
5. Exit

Please choose an option: 5
```