import os 
import json
import time

#Dictionary to store contact information
contact_dict = {}

#Assigning the address book data to a file to save dictionary data
if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as f:
        contact_dict = json.load(f)
else:
    with open("contacts.json", "w") as f:
        json.dump(contact_dict, f)

#Function to add a contact
def add_contact():
    input_name = input("Enter the contact's name:  ")
    input_telephone_number = input("Enter the contact's phone number:  ")
    contact_dict[input_name] = input_telephone_number
    print("Added " + input_name + " with telephone number " + input_telephone_number)
    with open("contacts.json", 'a') as f:
        json.dump(contact_dict, f)
    time.sleep(1)
    

#Function to delete a contact
def del_contact():
    contact = input("Enter the name of the contact to delete:  ")
    if contact in contact_dict:
        del contact_dict[contact]
        print("Deleted " + contact)
    else:
        print("Contact does not exist.")
        time.sleep(1)


#Function to display contacts
def list_contacts():
    print(contact_dict)
    time.sleep(1.2)


#Master Loop for Running the program
while True:
    print("Welcome to your address book.")
    print("Enter '0' to add a contact.")
    print("Enter '1' to delete a contact.")
    print("Enter '2' to display all contacts.")
    print("Enter '3' to quit")
    response = input("What would you like to do?  ")
    #Make sure the user's input is an integer
    try:
        response = int(response)
    #If not an integer raise a ValueError
    except ValueError:
        print("Invalid input.  Please try again...")
        time.sleep(1)
        continue
        
    #Response to add a contact
    if response == 0:
        add_contact()
        
    #Response to delete a contact
    elif response == 1:
        del_contact()
        
    #Response to show all contacts
    elif response == 2:
        list_contacts()
        
    #Response to quit program
    elif response == 3:
        break
    
    else:
        print("Invalid option.  Please try again!")
        time.sleep(1)
        

