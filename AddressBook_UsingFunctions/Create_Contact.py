class Contact:

    def __init__(self, first_name, last_name, address, city, state, zip, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Full Name is: {self.first_name} {self.last_name}\nFull Address is: {self.address},{self.city}," \
               f"{self.state},{self.zip}\nPhone Number: {self.phone_number}\nEmail: {self.email}"

if __name__ == "__main__":

    contact = Contact("Shubham", "Singh", "Rampuri Colony", "Saharanpur", "UP", 247001, 7675748385, "Shubham@gmail.com")

try:
    print(contact)
except Exception as ex:
    print(ex)

