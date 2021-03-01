#Class for executing various commands
class Commands:
    def add_contact():
        input_name = input("Enter the contact's name: ")
        input_relation = int(input("Enter a relationship group number (0:family, 1:friends, 2:coworkers"))
        input_telephone_number = input ("Enter the contact's phone number: ")