#Class for executing various commands
class Commands:
    #Method to add a contact
    def add_contact():
        input_name = input("Enter the contact's name:  ")
        input_relation = int(input("Enter a relationship group number (0:family, 1:friends, 2:coworkers:  "))
        input_telephone_number = input("Enter the contact's phone number:  ")
        Contact(input_name, relation_type[input_relation], input_telephone_number)
    
    #Method to delete a contact
    def del_contact():
        name = input("Enter the name of the contact to delete:  ")
        del contact_dictionary [name]

    #Method to search for a contact
    def search():
        name = input("Enter the name of the contact you are looking for:  ")
        if name in contact_dictionary:
            print("Name: %s, Relation: %s, Phone: %s"%(name, contact_dictionary [name] ["relation"], contact_dictionary [name] ["telephone_number"]))
        else:
            print("Contact does not exist.")
            