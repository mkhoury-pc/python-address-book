import os 
import json

#Dictionary to store contact information
contact_dictionary = {}

#Assigning the address book data to a file to save dictionary data
address_book_data = "address_book_data.json"

#Function to add a contact
def add_contact():
    input_name = input("Enter the contact's name:  ")
    input_telephone_number = input("Enter the contact's phone number:  ")
    contact_dictionary[input_name] = input_telephone_number
    with open(address_book_data, 'a') as f:
        f.write(json.dumps(contact_dictionary))
    

#Function to delete a contact
def del_contact():
    contact = input("Enter the name of the contact to delete:  ")
    if contact in contact_dictionary:
        del contact_dictionary[name]
    else:
        print("Contact does not exist.")


#Function to search for a contact
def search():
    name = input("Enter the name of the contact you are looking for:  ")
    if name in contact_dictionary:
        print("Name: %s, Phone: %s"%(name, contact_dictionary [name], contact_dictionary [name] ["telephone_number"]))
    else:
        print("Contact does not exist.")

#Master Loop for Running the program
while True:
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
        
    #Response to add a contact
    if response == 0:
        add_contact()
        
    #Response to delete a contact
    elif response == 1:
        del_contact()
        
    #Response to search for a contact
    elif response == 2:
        search()
        
    #Response to quit program
    elif response == 3:
        break
    
    else:
        print("Invalid option.  Please try again!")
        

