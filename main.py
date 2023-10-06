import logging                      # For Providing logging funcitionality to the code


# Creating a Student class
class Student:
    def __init__(self, student_ID, student_class):
        self.student_ID = student_ID
        self.student_class = student_class


# Creating a ClassRoom class
class ClassRoom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.class_students = {}  
        self.class_assignments = []

    # Method for enrolling students into classroom
    def enroll(self, student):
        student_ID = student.student_ID
        if student_ID not in self.class_students:
            self.class_students[student_ID] = student
        else:
            print(f"Student {student_ID} is already enrolled in '{self.class_name}'.")

    # Method for listing students in class
    def list_students(self):
        print(f"Students in ClassRoom '{self.class_name}'")
        for student_ID, student in self.class_students.items():
            print(f"Student : {student_ID}")  

    # Method for assignment scheduling 
    def schedule_assignment(self, assignment_description):
        self.class_assignments.append(assignment_description)


    def __str__(self):
        return f"ClassRoom: {self.class_name}"
    

# Creating Assignment class
class Assignment:
    def __init__(self, assignment_description):
        self.assignment_description = assignment_description
        self.is_submitted = False


# ----------------------------------------------------------------------------------------------        


# Creating VirtualClassRoomManager class for managing Virtual classroom related activites.
class VirtualClassRoomManager:
    def __init__(self):
        self.classes = []
        
        # the code enables logging for our program and helps in debugging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%H:%M:%S')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    # Method for classroom creation
    def create_Room(self, class_name):
        if not any(cls.class_name == class_name for cls in self.classes):
            classroom = ClassRoom(class_name)
            self.classes.append(classroom)
            self.logger.info(f"Classroom '{class_name}' has been created.")
        else:
            self.logger.warning(f"Classroom '{class_name}' already exists.")

    # Method for classroom removal
    def remove_Room(self, class_name):
        for cls in self.classes:
            if cls.class_name == class_name:
                self.classes.remove(cls)
                self.logger.info(f"Classroom '{class_name}' has been removed.")
                return
        self.logger.warning(f"Classroom '{class_name}' not found.")

    # Method for listing classroom
    def list_Room(self):
        for classs in self.classes:
            print(classs)

    # Method for finding classroom
    def find_Room(self, class_name):
        for classs in self.classes:
            if classs.class_name == class_name:
                return classs
        return None


    # Method for Adding/Enrolling students into classroom
    def enroll_student(self, student, class_name):
        classroom = self.find_Room(class_name)
        if classroom:
            student_ID = student.student_ID

            # Check if the student is already enrolled in the class
            if student_ID in classroom.class_students:
                self.logger.warning(f"Student {student_ID} is already enrolled in '{class_name}'.")
            else:
                classroom.enroll(student)
                self.logger.info(f"Student {student_ID} has been enrolled in '{class_name}'.")

        else:
            self.logger.warning(f"Classroom '{class_name}' not found.")

    # Method for listing students in classroom
    def student_in_classroom(self, class_name):
        classroom = self.find_Room(class_name)

        if classroom:
            classroom.list_students()
        else:
            self.logger.warning(f"Classroom '{class_name}' not found.")

    # Method for scheduling assignment
    def schedule_assignment(self, class_name, assignment_description):
        classroom = self.find_Room(class_name)
        if classroom:
            classroom.schedule_assignment(assignment_description)
            self.logger.info(f"Assignment for '{class_name}' has been scheduled.")
        else:
            self.logger.warning(f"Classroom '{class_name}' not found.")

    # Method for assignment submission
    def submit_assignment(self, student_ID, class_name, assignment_description):
        classroom = self.find_Room(class_name)
        if classroom:
            if student_ID in classroom.class_students:
                student = classroom.class_students[student_ID]
                assignment = Assignment(assignment_description)
                assignment.is_submitted = True
                self.logger.info(f"Assignment submitted by Student {student_ID} in '{class_name}'.")
            else:
                self.logger.warning(f"Student ID '{student_ID}' not found in '{class_name}'.")
        else:
            self.logger.warning(f"Classroom '{class_name}' not found.")
