import os 

from Contact import Contact 
from Commands import Commands


#Dictionary to store contact information
contact_dictionary = {"name":{"relationship":"", "telephone_number":""}}
#List of relation types 
relation_type = ["family", "friend", "coworker"]


#Master Loop for Running the program
while True:
    print("Welcome to your address book.")
    print("Enter 'add contact' to add a contact.")
    print("Enter 'del contact' to delete a contact.")
    print("Enter 'search' to search for a contact.")
    response = input("What would you like to do?  ")
    
    #Response to add a contact
    if response.lower() == "add contact":
        Commands.add_contact()
        continue
    #Response to delete a contact
    elif response.lower() == "del contact":
        Commands.del_contact()
        continue
    #Response to search for a contact
    elif response.lower() == "search":
        Commands.search()
        continue
    #Response to quit program
    elif response.lower() == "quit":
        break
    






