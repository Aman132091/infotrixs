import os
import csv
import datetime
import colorama
from itertools import groupby
colorama.init()





def title():
    line_1 = colorama.Fore.RED+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    title =       "Contact Management System"
    line_2 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


    print("")
    print("\n\n" + line_1.center(209))
    print(title.center(202))
    print(line_2.center(204) + "\n\n")
    print("")

                          


class contact_functions:
    contact_fields = ["Name", "Mobile_No"]
    contact_database = "contacts.csv"
    contact_information = []

    def __init__(self):
        self.contact_information = []


    def create(self):
        os.system('cls')
        title()
        print("     Create Contact:")
        print("     --------------")
        print("")

        while True:
            contact_information = []
            for field in self.contact_fields:
                contact_details = input(colorama.Fore.RED + "   Enter " + field + ": " + colorama.Fore.WHITE)
                print("")
                contact_information.append(contact_details)

            name = contact_information[0]
            mobile_no = contact_information[1]

            with open(self.contact_database, 'r') as file:
                reader = csv.reader(file)
                for data in reader:
                    if len(data) > 0 and (data[0].lower() == name.lower() or data[1] == mobile_no):
                        print("Name or Mobile Number already exists. Please enter unique values.")
                        break
                else:
                    if len(mobile_no) != 10:
                        print("Invalid Mobile Number. The number should be exactly of 10 digits.")
                        continue
                    date = datetime.datetime.today()
                    formatted_date = date.strftime("%B %d %Y")
                    contact_information.append(formatted_date)

                    with open(self.contact_database, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(contact_information)

                    print("")
                    print("Contact created successfully".center(130))
                    print("\n")
                    break


    def view(self):
        os.system('cls')
        title()
        print("View Contacts: ".center(10))
        print("----------".center(10))
        print("")

        count = 0
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data1 in read:
                if len(data1) > 0:
                    count = count + 1
            print("Total contacts: ", count)
            print('')

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            if os.path.getsize(self.contact_database) == 0:
                print("Contact list is empty, Please create contacts".center(130))
            else:
                for fields in self.contact_fields:
                    print('{0:<10}'.format(fields).center(10), end="\t\t")

                print('{0:<10}'.format("Date"))
                print('{:<10}\t\t{:<10}\t\t{:<10}'.format(                   
                     '-----', '-------------', '--------'))
                print("")

                for data in read:
                    for item in data:
                        print('{:<10}'.format(item).center(10), end="\t\t")

                    print("")

        print("\n")
        input("\n\n\t\t\t\t\t\t\t Press enter key to continue........".center(120))
        os.system('cls')


     
    def search(self):
        os.system('cls')
        title()

        print("Search contacts:".center(10))
        print("--------------------".center(10))
        print("")

        contact_match = False
        search_criteria = input(" Search by  (Name or Number): ")
        search_value = input("Enter search value: ")
        print("")

        for field in self.contact_fields:
            print('{0:<10}'.format(field).center(10), end="\t\t")

        print('{0:<10}'.format("Date"))
        print('{:<10}\t\t{:<10}\t\t{:<10}'.format(
            '-----', '-------------', '--------'))
        print("")

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_criteria.lower() == "name":
                        name = data[0]
                        if search_value.lower() in name.lower():
                            contact_match = True
                            print('{:<10}\t\t{:<10}\t\t{:<10}'.format(
                                data[0], data[1], data[2]).center(10))
                    elif search_criteria.lower() == "number":
                        number = data[1]
                        if search_value.lower() in number.lower():
                            contact_match = True
                            print('{:<10}\t\t{:<10}\t\t{:<10}'.format(
                                data[0], data[1], data[2]).center(10))
                    else:
                        # Add additional criteria checks here if needed
                        pass

        if not contact_match:
            print("")
            print("Sorry, Not Found".center(120))

        print("")

    def delete(self):
         os.system('cls')
         title()

         print(" Delete contacts: ".center(10))
         print("------------------".center(10))
         print("")

         self.contact_match = 'false'
         delete_value = input("Enter Name: ")
         update_list = []

         with open(self.contact_database, 'r') as file:
             read = csv.reader(file)
             for data in read:
                 if len(data) > 0:
                     if delete_value != data[0]:
                         update_list.append(data)
                     else:
                         self.contact_match = 'true'


         if self.contact_match == 'true':
             with open(self.contact_database, 'w') as file:
                 write = csv.writer(file)
                 write.writerows(update_list)
                 print("\n\n")
                 print("Contact is deleted".center(120))
                 print("\n\n")


         if self.contact_match == 'false':
             print("Sorry! Contact not found.")
             print("")

    def edit(self):
        os.system('cls')
        title()

        print("Edit contact:".center(10))
        print("----------------".center(10))
        print("")

        contact_match = False
        search_value = input("Enter Name: ")
        print("")

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            contacts = list(read)

        field_index = -1
        for index, field in enumerate(self.contact_fields):
            if field == "Name":
                field_index = index

        for i, contact in enumerate(contacts):
            if len(contact) > 0:
                if search_value == contact[field_index]:
                    contact_match = True
                    print("Found contact:")
                    for field, value in zip(self.contact_fields, contact):
                        print('{0:<10}'.format(field).center(10), end="\t\t")
                    print("\n")
                    for field, value in zip(self.contact_fields, contact):
                        print('{0:<10}'.format(value).center(10), end="\t\t")
                    print("\n")

                    print("Enter new values:")
                    for field in self.contact_fields:
                        if field != "Name":
                            contact_details = input("Enter " + field + ": ")
                            contact[self.contact_fields.index(field)] = contact_details
                    print("")

        if not contact_match:
            print("")
            print("Sorry, contact not found".center(120))
            print("")
            return

        with open(self.contact_database, 'w', newline='') as file:
            write = csv.writer(file)
            write.writerows(contacts)
        print("\n")
        print("Contact is updated successfully".center(130))
        print("\n")

        input("\n\t\t\t\t\t\t press enter key to continue...".center(120))
        os.system('cls')


contact_class = contact_functions()

os.system('cls')
title()

while True:

    print("1. Create Contact\n".center(100))
    print("2. View Contact\n".center(98))
    print("3. Search Contact\n".center(100))
    print("4. Delete Contact\n".center(100))
    print("5. Edit Contact\n".center(98))
    print("6. Exit\n".center(90))
    
    print("______________________".center(100))
    option = int(input( "\t\t\t\t\t Choose Your Option : " + colorama.Fore.WHITE ))

    if option == 1:
        while True:
            contact_class.create()
            ans = input("\n\n\t\t\t\t\tDo you want to create another contact number ?[Y/N]: " + colorama.Fore.WHITE)

            if ans == 'Y' or ans == 'y':
                continue
            else:
                break

        os.system('cls')
        title()
    if option == 2:
        contact_class.view()
        title()
    if option == 3:
        while True:
            contact_class.search()
            print("")
            ans = input(
                "\n\n\n\t\t\t\t\tDo you want to create another contact number ?[Y/N]: ")

            if ans == 'Y' or ans == 'y':
                continue
            else:
                break

        os.system('cls')
        title()

    if option == 4:
        while True:
           contact_class.delete()
           ans = input("\t\t\t\t\tDo you want to delete another contacts?[Y/N]: ")

           if ans == 'Y' or ans == 'y':
               continue
           else:
               break
        os.system('cls')
        title()

    if option == 5:
        while True:
            contact_class.edit()
            ans = input(
                "\t\t\t\t\tDo you want to Edit another contact number ?[Y/N]: ")

            if ans == 'Y' or ans == 'y':
                continue
            else:
                break

        os.system('cls')
        title()
        
    if option == 6:
         os.system('cls')
         print("\n\n")
         line_1 = "****************************************"
         msg    =     "Thankyou! For using our system"
         line_2 = "****************************************"
         print("\n\n")
         print(line_1.center(140))
         print(msg.center(140))
         print(line_2.center(140))
         break
    if option > 6 or option < 1:
        os.system('cls')
        print("\n\n\n")
        print("Invalid selection. Please seletct a valid option.".center(140))
        print("\n\n")

        input("Press enter key to continue.....".center(140))
        os.system('cls')
        title()