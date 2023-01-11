# UC3- Editing Person's contact details using their firstname
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

    def edit_contacts(self):
        check = 0
        edit_name = input("Enter the name whose detail you want to Edit:")
        for i in contacts_list:
            if i.first_name == edit_name:
                print("Enter what you want to edit\n1.FirstName,2.LastName,3.Address,4.City,5.State,6.ZipCode,"
                      "7.PhoneNumber,8.Email")
                choice = int(input())
                match choice:
                    case 1:
                        i.first_name = input("Enter the new FirstName:")
                    case 2:
                        i.last_name = input("Enter the new LastName:")
                    case 3:
                        i.address = input("Enter the new Address:")
                    case 4:
                        i.city = input("Enter the new city:")
                    case 5:
                        i.state = input("Enter the new State:")
                    case 6:
                        i.zip_code = input("Enter the new ZipCode:")
                    case 7:
                        i.phone_number = input("Enter the new PhoneNumber:")
                    case 8:
                        i.email = input("Enter the new Email:")
                print("Contact Updated Successfully")
                check = 1
        if check == 0:
            print("Person with such name not found")


if __name__ == "__main__":
    address = AddressBook()
    contacts_list = []
    print("*****Welcome to the AddressBook Problem ********\n")
    flag = True
    while flag:
        print("1.Add Contacts\n2.Display Contacts\n3.Edit Contacts\n4.Exit")
        select = int(input("Select from the above option : "))
        match select:
            case 1:
                address.add_contacts()
            case 2:
                for item in contacts_list:
                    print(str(item), "\n****************************")
            case 3:
                address.edit_contacts()
            case 4:
                flag = False
                break


