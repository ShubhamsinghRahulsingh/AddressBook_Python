# UC2- Adding new Contact using console
class Contact:

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        """
            Description: Constructor of Contacts Class
            Parametres: Takes class fields
            Returns: None, Just initialize the values of object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        """
            Description: To return textual content of the Contacts class Object
            Parameters: Takes Instance (Object) of class as arguments
            Returns: Returns String Representation of object, understandable by User
        """
        return f"Full Name is: {self.first_name} {self.last_name}\nFull Address is: {self.address},{self.city}," \
               f"{self.state},{self.zip_code}\nPhone Number: {self.phone_number}\nEmail: {self.email}"


class AddressBook:
    def add_contacts(self):
        """
            Description: Adding Contact Details form Console & storing that details as an object of Contacts Class
            Parameters: None
            Returns: None, just adding this object to list
        """
        try:
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            address = input("Enter the address: ")
            city = input("Enter city name: ")
            state = input("Enter the state name: ")
            zip_code = input("Enter the zip code: ")
            phone_number = input("Enter phone_number: ")
            email = input("Enter email address: ")
            contact_obj = Contact(first_name, last_name, address,
                                   city, state, zip_code, phone_number, email)
            contacts_list.append(contact_obj)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    contacts_list = []
    print("*****Welcome to the AddressBook Problem ********\n")
    flag = True
    while flag:
        print("1.Add Contacts\n2.Display Contacts\n3.Exit")
        select = int(input("Select from the above option : "))
        match select:
            case 1:
                address = AddressBook()
                address.add_contacts()
            case 2:
                for item in contacts_list:
                    print(str(item))
            case 3:
                flag = False
                break


