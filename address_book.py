import os 
import pickle

from contact import Contact 
from commands import Commands

#Dictionary to store contact information
contact_dictionary = {}

master_loop_run = True
#Assigning the address book data to a file to save dictionary data
address_book_data = "addressbook.data"

#Determine if dictionary data file exists, if it does load contents into dictionary
if os.path.exists(address_book_data):
    f = open(address_book_data, "rb")
    contact_dictionary = pickle.load(f)
#If the file does not exist prompt to create one
else:
    file_question = input("Contact file not found.  Create one?  'y' or 'n'    ")
    if file_question == "y":
        f = open(address_book_data, "wb")
        pickle.dump(contact_dictionary, f)
        f.close()
    elif file_question == "n":
        master_loop_run = False


#Master Loop for Running the program
while master_loop_run:
    print("Welcome to your address book.")
    print("Enter '0' to add a contact.")
    print("Enter '1' to delete a contact.")
    print("Enter '2' to search for a contact.")
    print("Enter '3' to quit")
    response = input("What would you like to do?  ")
    #Make sure the user's input is an integer
    try:
        response = int(response)
    #If not an integer raise a ValueError
    except ValueError:
        print("Invalid input.  Please try again...")
        continue
    #Response to add a contact
    if response == 0:
        Commands.add_contact()
        continue
    #Response to delete a contact

    elif response == 1:
        Commands.del_contact()
        continue
    #Response to search for a contact
    elif response == 2:
        Commands.search()
        continue
    #Response to quit program
    elif response == 3:
        break
    else:
        print("Invalid option.  Please try again!")
        continue
    






