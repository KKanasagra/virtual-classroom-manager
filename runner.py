from main import *

if __name__ == "__main__":
    classroom_manager = VirtualClassRoomManager()
    print('\n')
    print("Welcome to the Virtual Classroom Manager!")

    while True:
        print("\nCommands:")
        print("1. add_classroom [class_name]")
        print("2. add_student [student_ID] [class_name]")
        print("3. schedule_assignment [class_name] [assignment_details]")
        print("4. submit_assignment [student_ID] [class_name] [assignment_details]")

        print("\nAdditional Functionalities") 

        print("5. remove_classroom [class_name]")
        print("6. list_classroom ")
        print("7. students_in_class [class_name]")
        print("8. exit \n")


        user_input = input("Enter a command: ").strip().split()


        if user_input[0] == "add_classroom":
            if len(user_input) != 2:
                print("Usage: add_classroom [class_name]")
            else:
                class_name = user_input[1]
                classroom_manager.create_Room(class_name)
            print('')
            print('########################################################################################################')


        elif user_input[0] == "add_student":
            if len(user_input) != 3:
                print("Usage: add_student [student_ID] [class_name]")
            else:
                student_ID = user_input[1]
                class_name = user_input[2]
                student = Student(student_ID, class_name)
                classroom_manager.enroll_student(student, class_name)
            print('')
            print('########################################################################################################')


        elif user_input[0] == "schedule_assignment":
            if len(user_input) < 3:
                print("Usage: schedule_assignment [class_name] [assignment_details]")
            else:
                class_name = user_input[1]
                assignment_details = " ".join(user_input[2:])
                classroom_manager.schedule_assignment(class_name, assignment_details)
            print('')
            print('########################################################################################################')


        elif user_input[0] == "submit_assignment":
            if len(user_input) < 4:
                print("Usage: submit_assignment [student_ID] [class_name] [assignment_details]")
            else:
                student_ID = user_input[1]
                class_name = user_input[2]
                assignment_details = " ".join(user_input[3:])
                classroom_manager.submit_assignment(student_ID, class_name, assignment_details)
            print('')
            print('########################################################################################################')

        # For Additional Functionalities

        elif user_input[0] == "remove_classroom":
            if len(user_input) != 2:
                print("Usage: remove_classroom [class_name]")
            else:
                class_name = user_input[1]
                classroom_manager.remove_Room(class_name) 
            print('')
            print('########################################################################################################')

        elif user_input[0] == "list_classroom":
            if len(user_input) != 1:
                print("Usage: list_classroom")
            else:
                classroom_manager.list_Room()
            print('')
            print('########################################################################################################')

        elif user_input[0] == "students_in_class":
            if len(user_input) != 2:
                print("Usage: students_in_class [class_name]")
            else:
                class_name = user_input[1]
                classroom_manager.student_in_classroom(class_name)
            print('')
            print('########################################################################################################')

        elif user_input[0] == "exit":
            print("Exiting the Virtual Classroom Manager.")
            break

        else:
            print("Invalid command. Please try again.")
