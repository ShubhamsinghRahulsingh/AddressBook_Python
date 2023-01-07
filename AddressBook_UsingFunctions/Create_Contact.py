# UC1- Creating Person's Contact details

def create_contact():
    my_header = ["FirstName", "LastName", "Address", "City", "State", "Zip_Code", "Phone_Number", "Email"]
    my_details = ["Shubham", "Singh", "Rampuri Colony", "Saharanpur", "UP", 247001, 7567445673, "shubham@gmail.com"]
    my_contact = {k: v for (k, v) in zip(my_header, my_details)}
    for x, y in my_contact.items():
        print(x, ":", y)


create_contact()
