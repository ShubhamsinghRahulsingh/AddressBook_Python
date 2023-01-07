# UC2- Adding contact details using Console

my_contacts_list = []


def add_contacts():
    my_contact_dict = {}
    first_name = input("Enter the First name: ")
    last_name = input("Enter the Last name: ")
    address = input("Enter the Address: ")
    city = input("Enter the City: ")
    state = input("Enter the State: ")
    zip_code = int(input("Enter the Zip Code: "))
    phone_number = int(input("Enter the Phone Number : "))
    email = input("Enter the Email : ")

    my_contact_dict["first_name"] = first_name
    my_contact_dict["last_name"] = last_name
    my_contact_dict["address"] = address
    my_contact_dict["city"] = city
    my_contact_dict["state"] = state
    my_contact_dict["zip_code"] = zip_code
    my_contact_dict["phone_number"] = phone_number
    my_contact_dict["email"] = email

    my_contacts_list.append(my_contact_dict)


def display_details():
    for i in my_contacts_list:
        print('First Name : ', i.get('first_name'))
        print('Last Name : ', i.get('last_name'))
        print('Address : ', i.get('address'))
        print('City : ', i.get('city'))
        print('State : ', i.get('state'))
        print('Zip-code : ', i.get('zip_code'))
        print('Phone Number : ', i.get('phone_number'))
        print('Email : ', i.get('email'))
        print('************************************************')


def add_multiple_contacts():
    flag = True
    while flag:
        print("1.Add person details")
        print("2.Display person Details ")
        print("3.Exit")

        select = int(input("Select from the above option : "))
        match select:
            case 1:
                add_contacts()
            case 2:
                display_details()
            case 3:
                flag = False
                break


add_multiple_contacts()