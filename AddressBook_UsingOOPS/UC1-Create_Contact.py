# UC1- Creating Person's Contact details
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


if __name__ == "__main__":
    print("*****Welcome to the AddressBook Problem ********\n")
    contact = Contact("Shubham", "Singh", "Rampuri Colony", "Saharanpur", "UP", 247001, 7675748385, "Shubham@gmail.com")

try:
    print(contact)
except Exception as ex:
    print(ex)
