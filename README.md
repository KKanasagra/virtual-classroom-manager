# Virtual Classroom Manager

The Virtual Classroom Manager is a Python program that allows you to manage virtual classrooms, enroll students, schedule assignments, and more. This README provides an overview of the program and its functionality.

### Prerequisites

- Python (version 3.9.4) or higher

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/KKanasagra/virtual-classroom-manager.git
   cd virtual-classroom-manager
   python main.py

### Usage
The Virtual Classroom Manager allows you to perform various actions related to virtual classrooms. You can use the following commands:

### Commands
1. add_classroom [class_name]: Create a new classroom.
2. add_student [student_ID] [class_name]: Enroll a student in a classroom.
3. schedule_assignment [class_name] [assignment_details]: Schedule an assignment for a classroom.
4. submit_assignment [student_ID] [class_name] [assignment_details]: Submit an assignment by a student.

Additional Functionalities
5. remove_classroom [class_name]: Remove a classroom.
6. list_classroom: List all available classrooms.
7. students_in_class [class_name]: List students in a specific classroom.
8. exit: Exit the Virtual Classroom Manager.

### Logging
The program uses logging to provide information, warnings, and errors related to its operation. Logs are displayed with timestamps and log levels for debugging and monitoring.

