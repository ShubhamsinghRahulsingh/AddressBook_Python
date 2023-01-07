# UC1- Creating Person's Contact details

def create_contact():
    my_header = ["FirstName", "LastName", "Address", "City", "State", "Zip", "Phone_Number", "Email"]
    my_details = ["Shubham", "Singh", "Rampuri Colony", "Saharanpur", "UP", 247001, 7567445673, "shubham@gmail.com"]
    my_contact = {k: v for (k, v) in zip(my_header, my_details)}
    for x in my_contact:
        print(x, ":", end=" ")
        print(my_contact[x])


create_contact()
