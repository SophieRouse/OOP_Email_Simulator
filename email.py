### --- OOP Email Simulator --- ###

# --- Email Class --- #
# A class, constructor and methods are used to create a new Email object.
class Email:

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # The class variable is declared, with default value, for emails. 
    has_been_read = False 

    # This is a method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# This is an empty list to store the email objects.
inbox = []

# --- Functions --- #
# populate_inbox() allows emails to fill the inbox.

def populate_inbox():
    # 3 sample emails are created and added to the Inbox list. 
    sample1 = Email("sample1@email.com", "Welcome to HyperionDev!", "Hi")
    sample2 = Email("sample2@email.com", "Great work on the bootcamp!", "Well Done")
    sample3 = Email("sample3@email.com", "Your excellent marks!", "10/10")
    inbox.extend([sample1, sample2, sample3])

def list_emails():
    # This is a function which prints the email’s subject_line, along with a corresponding number.
    print("\n")
    for count, email in enumerate(inbox):
        print(count, email.subject_line)

def read_email(index):
    # This is a function which displays a selected email.
    print("\n")
    if index <= len(inbox):
        selected_email = inbox[index]
        print(selected_email.email_address)
        print(selected_email.subject_line)
        print(selected_email.email_content)
        # Once displayed, the class method is called to set its 'has_been_read' variable to True and lets the user know this.
        selected_email.mark_as_read()
        print(f"\nEmail from {selected_email.email_address} marked as read.\n")
        return 0
    else:
        print("Please enter a valid email index")
        return -1

# --- Email Program --- #

# The function to populate the Inbox is called for further use in the program.
populate_inbox()

# The menu allows for the user to select what they'd like to do with their email.
menu = True

# A While True is used to ensure the user gives a correct input of either 1, 2 or 3. 

while True:
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')
       
    if user_choice == "1":
        # This logic allows the user to read an email.
        while True:
            list_emails()
            index = input("\nPlease enter the number of the email you want to read:")
            if index.isnumeric():
                index = int(index)
                valid = read_email(index)
            else:
                print("Please enter an index integer")
                valid = -1
            if valid == 0:
                break

    elif user_choice == "2":
        # This logic allows the user to view unread emails 
        for email in inbox:
            if not email.has_been_read:
                print(email.subject_line)    

    elif user_choice == "3":
        # This logic allows the user to quit the appplication
        exit()

    else:
        print("Oops - incorrect input.")

