# Dictionary defined
students = [
    {
        "name": "Tina",
        "hometown": "Portland",
        "favorite_food": "puppy chow"
    },
    {
        "name": "Klaus",
        "hometown": "Frankfurt",
        "favorite_food": "pizza"
    },
    {
        "name": "Julia",
        "hometown": "Houston",
        "favorite_food": "shrimp"
    }
]
hometown_food = ' '
#Function to print all students
def list_names(students):
    for i, student in enumerate(students):
        print(f"{i+1}. {student['name']}")
#Function to display students details by index serach or name search
def get_name_by_index_Or_Name():
    student_num =0
    while True:
            view_choice = input('How would you like to view student details by name or number?\nPlease type  a "name" or a  "number"')
            #Serach by index
            if view_choice == 'number' or view_choice == 'Number':
             while True:
                try:
                    print('Please enter a number from 1 to ',len(students))
                    student_num = int(input()) - 1

                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                if student_num < 0:
                    print('Please enter valid number!')
                    continue
                if student_num > len(students):
                    print('Please enter valid number!')
                    continue
                for i, student in enumerate(students):
                    if student_num == i:
                        print(f"Student {student_num + 1} is  {student['name']}.")

                        hometown_food = input("Would like to  see that student's hometown or favorite food ? ")
                        if hometown_food == 'town':
                             # print(f"\tName: {student['name']}")
                            print(f"\t{student['name']} is from {student['hometown']}.")
                            break
                        elif hometown_food == 'food':
                            print(f"\t{student['name']}'s favorite food is {student['favorite_food']}.")
                            break
                        else:
                            print('Please provide valid choice!')
                            continue
                while True:
                    choice = input('Would you like to continue search by number(y/n)!')
                    if choice == 'y':
                        break
                    elif choice == 'n':
                        print("Good bye...")
                        return
                    else:
                        print('Please enter valid choice')
                        continue
             # Serach by name
            elif view_choice == 'Name' or view_choice == 'name':
                while True:
                    option1 = input('Welcome ! Which student would you like to learn more about ?Enter full  name ')
                    # check for proper capitalization
                    option1 = option1.strip().title()
                    if option1.islower():
                        option1 = option1.title()

                    # check for extra spaces
                    option1 = ' '.join(option1.split())
                    # Only character name allowed
                    if option1.isdigit():
                        print('Please enter alphabetic characters only. Try again.')
                        continue
                    if not option1:
                        print('Error: You must enter a name to search.')
                    else:
                        found = False
                        for student in students:
                            if student["name"].lower() == option1.lower():
                                found = True
                                while True:
                                # Once you have name ask for food or home town in name search')
                                            print(f"Student is {student['name']}.what would you like to know?")
                                            town_Or_Food = input('Enter: '"Hometown" ' ' 'or' ' '"Favorite Food"'')
                                            if town_Or_Food == 'town':
                                                # print(f"\tName: {student['name']}")
                                                print(f"\t{student['name']} is from {student['hometown']}.")
                                                break
                                            elif town_Or_Food == 'food':
                                                print(f"\t{student['name']}'s favorite food is  {student['favorite_food']}.")
                                                break
                                            else:
                                                print('Please provide valid choice!')
                                                continue

                        if not found:
                            print(f'Error: Name "{option1}" not found in the list.')
                            # Option to itreate thorugh the choice again in case you want to see another student's information
                    while True:
                        choice = input('\t\n\twould you like to learn about another student by name (y/n)?')
                        if choice == 'y':
                             print("Continue...")
                             break
                        elif choice == 'n':
                             print("Good bye...")
                             return
                        else:
                             print('Please enter valid choice')
                             continue
            else:
                print("Invalid choice. Please try again.")
                continue
# list_names(students)
# students = []
def get_new_student():
    name = input("Enter the student's name: ")
    hometown = input("Enter the student's hometown: ")
    favorite_food = input("Enter the student's favorite food: ")

# create a new dictionary to store the student's information
    student = {"name": name, "hometown": hometown, "favorite_food": favorite_food}

# add the student to the list of students
    students.append(student)

    print(f"Student {name} has been added.")
    return
#Main Code
#Header
print('*' *50)
print('Student database using dictionary'.upper())
print('*' *50)
while True:
    choice = input( "Please select which action you'd like to do\n\t1.Type 'add' to create a new student.\n\t2.Type 'view' to look at existing students.\n\t3.Type 'quit' to exit the program. ")

    if choice == "add":
        get_new_student()

    elif choice == "view":
        list_names(students)
        get_name_by_index_Or_Name()
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


