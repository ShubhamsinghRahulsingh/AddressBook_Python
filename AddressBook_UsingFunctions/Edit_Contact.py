# UC3- Editing Person's detail using Name using Console

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


def edit_contact():
    edit_name = input("Enter the person's name whose detail you want to edit:")
    for i in my_contacts_list:
        if i.get("first_name") == edit_name:
            print("Enter what you want to edit\n1.FirstName,2.LastName,3.Address,4.City,5.State,6.ZipCode,"
                           "7.PhoneNumber,8.Email")
            choice = int(input())
            match choice:
                case 1:
                    i["first_name"] = input("Enter the new FirstName:")
                case 2:
                    i["last_name"] = input("Enter the new LastName:")
                case 3:
                    i["address"] = input("Enter the new Address:")
                case 4:
                    i["city"] = input("Enter the new city:")
                case 5:
                    i["state"] = input("Enter the new State:")
                case 6:
                    i["zip_code"] = input("Enter the new ZipCode:")
                case 7:
                    i["phone_number"] = input("Enter the new PhoneNumber:")
                case 8:
                    i["email"] = input("Enter the new Email:")
                    break
            print("Contact Updated Successfully")
        else:
            print("Person with such name not found")


def main():
    flag = True
    while flag:
        print("Welcome to the AdrressBook Problem")
        print("1.Add person details\n2.Display person Details\n3.Edit Contact\n4.Exit")
        select = int(input("Select from the above option : "))
        match select:
            case 1:
                add_contacts()
            case 2:
                display_details()
            case 3:
                edit_contact()
            case 4:
                flag = False
                break


main()