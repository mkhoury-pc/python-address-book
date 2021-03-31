#Class for executing various commands
class Commands:
    #Method to add a contact
    def add_contact():
        input_name = input("Enter the contact's name:  ")
        input_telephone_number = input("Enter the contact's phone number:  ")
        contact_dictionary[input_name] = input_telephone_number
    
    #Method to delete a contact
    def del_contact():
        name = input("Enter the name of the contact to delete:  ")
        del contact_dictionary[name]

    #Method to search for a contact
    def search():
        name = input("Enter the name of the contact you are looking for:  ")
        if name in contact_dictionary:
            print("Name: %s, Phone: %s"%(name, contact_dictionary [name], contact_dictionary [name] ["telephone_number"]))
        else:
            print("Contact does not exist.")
            