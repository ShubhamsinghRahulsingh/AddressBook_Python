# UC6-Create Multiple AddressBook with multiple contacts in each AddressBook

my_contacts_list = []
addressbook = {}


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
    check_ = 0
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
            check_ = 1
    if check_ == 0:
        print("Person with such name not found")



def delete_contact():
    check = 0
    delete_name = input("Enter the person's name whose contact you want to delete:")
    for i in my_contacts_list:
        if i.get("first_name") == delete_name:
            my_contacts_list.remove(i)
            print("Contact Deleted Successfully")
            check = 1
    if check == 0:
        print("Person with such name not found")


def create_addressbook():
    mylist = list(my_contacts_list)
    addressbook_name = input("Enter the Name you want to give to AddressBook:")
    addressbook.update({addressbook_name: mylist})
    my_contacts_list.clear()
    del mylist
    print("AddressBook Created Successfully")


def display_addressbook():
    for item in addressbook:
        print("AddressBook Name is:", item)
        for data in addressbook.values():
            for new_data in data:
                for x, y in new_data.items():
                    print(x, ":", y)
                print("---------------------------------------")
        print("*****************************************")








def main():
    flag = True
    while flag:
        print("Welcome to the AdrressBook Problem")
        print("1.Add person details\n2.Display person Details\n3.Edit Contact\n4.Delete Contact\n5.Create AddressBook\n"
              "6.Display AddressBook\n7.Exit")
        select = int(input("Select from the above option : "))
        match select:
            case 1:
                add_contacts()
            case 2:
                display_details()
            case 3:
                edit_contact()
            case 4:
                delete_contact()
            case 5:
                create_addressbook()
            case 6:
                display_addressbook()
            case 7:
                flag = False
                break


main()