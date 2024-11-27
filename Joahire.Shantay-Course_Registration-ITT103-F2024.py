# creating a class called course , this represents a course that will have an ID, name and fee associated
#with it. The init method is used to initialise a new instance of the course class which takes 3 parameters.
#this class is used to represent a single course with its course id, name and the fee that correlates
class Course:
    def __init__(self, course_id, name, fee): # this is used to set up the initial values an object will have when it's created under this class
        self.course_id = course_id # self.course_id will hold whatever id is inputted for that specific instance
        self.name = name # hold the name of the course
        self.fee = fee #fee associated with that course

#this class is used to represent a single student with its student id, name and the email that correlates
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = [] # this list is to hold all courses the student enrolls in
        self.balance = 0  #initialised to 0

#function that enrolls a student in a course if the course is not in the list of courses in self.courses
#the new course added will be appended to the list balance will be calculated except in the case where the course was already in the list
    def enroll(self, course):
        #checks if the course is already in the list of enrolled courses
        if course not in self.courses:
            self.courses.append(course)
            self.balance += course.fee
        else:
            raise ValueError("Student is already enrolled in this course!")
#this function returns the value of self.balance which stores the balance of all courses
    def get_total_fee(self):
        return self.balance

#This class manages student registration and course enrollments and an object will be made from this class
# which will be used to call all functions of this class. The init method creates a new object that will have empty
#list to store available courses and empty dictionary to store students.
class RegistrationSystem:
    def __init__(self):
        self.courses = {}
        self.students = {}

# this function first checks if the course is already in the dictionary of self.courses and if it is it raises a value error
#if not it adds a new object of course with the given attributes and adds it to the self.courses dictionary
    def add_course(self, course_id, name, fee):
        if course_id in self.courses:
            raise ValueError("Course ID already exists.")
        self.courses[course_id] = Course(course_id, name, fee) #adds the course to the dictionary

#this function first checks if the student is already in the dictionary of 'self.students' and if there is a value error
#is raised to prevent duplicates. If not, the student is added to the dictionary of self.students.
    def register_student(self, student_id, name, email):
        if student_id in self.students:
            raise ValueError("🚫Student ID already exists.")
        self.students[student_id] = Student(student_id, name, email)

#This function first checks if the student is already enrolled then checks if the course is in the list of available courses.
#If both these checks pass, the 'student' and 'course' object is retrieved and then
# the course is used as an argument to call the 'enroll' method which adds the course to the list of enrolled courses
    def enroll_in_course(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("🚫Student not found.")
        if course_id not in self.courses:
            raise ValueError("🚫Course not found.")

        student = self.students[student_id]
        course = self.courses[course_id]
        student.enroll(course)

#This function first checks if the student is already present in the self.students dictionary, if not a value error is raised
# if the student is found then the program checks if the amount is less than 40% ad if so an error is raised.
#if the requirements is met, the amount is subtracted from the balance.
    def calculate_payment(self, student_id, amount):
        if student_id not in self.students:
            raise ValueError("🚫Student not found.")

        student = self.students[student_id] #retrieves 'student' object from self.students dictionary
        minimum_payment = 0.4 * student.get_total_fee()
        print(f"Your minimum required payment is ${minimum_payment}")
        if amount < 0.4 * student.get_total_fee():
            raise ValueError("💰Please pay at least is 40% of the balance.")

        student.balance -= amount

#this function first checks if the student exist using the student id and if it does then the balance is returned
#from the 'self.students' dictionary
    def check_student_balance(self, student_id):
        if student_id not in self.students:
            raise ValueError("🚫Student not found.")

        return self.students[student_id].balance

#this function returns a list of tuple with all the details from the self.courses dictionary. It then uses a for loop
# to iterate over all the value(course) of self.courses.
    def show_courses(self):
        return [(course.course_id, course.name, course.fee) for course in self.courses.values()]

#this function returns a list of tuple with the details from the self.students dict. It then uses a for loop
#to iterate over the value (student) of self.students
    def show_registered_students(self):
        return [(student.student_id, student.name, student.email) for student in self.students.values()]

#this function first checks if the course exist and if not it raises a value error. if it does exist, it checks
#if the course entered is in the list of available courses and  returns the list of students using a for loop
#to iterate over each value in self.students using a tuple containing the student id and name

    def show_students_in_course(self, course_id):
        if course_id not in self.courses:
            raise ValueError("🚫Course not found.")

        return [
            (student.student_id, student.name)
            for student in self.students.values()
            if self.courses[course_id] in student.courses
        ]

#this function first checks if the student exist in the dict of self.students and if not an error message is displayed
# it then takes the specific student from the self.students dictionary using the ID as an argument
# and returns the course details in a tuple for each course in the student is enrolled in
    def show_courses_for_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("🚫Student not found.")

        student = self.students[student_id]
        return [(course.course_id, course.name, course.fee) for course in student.courses]


def main(): #the program starts executing here
    system = RegistrationSystem() #an object of the registration system class assigned to the variable system
    print("🌼🌼Welcome to the registration system🌼🌼")

    while True: #infinite loop
        print("⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇OPTIONS⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇")
        print("1. Add Course")
        print("2. Register Students")
        print("3. Enroll in Courses")
        print("4. Make Payments")
        print("5. Check Student's Balance")
        print("6. Show Courses")
        print("7. Show Registered Students")
        print("8. Show Students in Course")
        print("9. Show Courses students are enrolled in")
        print("10. Exit")

        choice = input("Please select an option ranging from (1-9): ")
        print('⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇')
#Choice 1 prompts the user for the course id and name then initiates a while loop that prompts for a fee until
#untill a numerical value is inputted. After which it adds the course using the 'add_course' method of the 'system' object
# to the dictionary of courses.
        if choice == "1":
            course_id = input("Enter the Course ID: ")
            name = input("Enter the Course Name: ")
            while True:
                try:
                    fee = float(input("Enter the Course Fee: "))
                    break
                except ValueError :
                    print("🚫Invalid input detected! Please input a numeric value for the fee")
            system.add_course(course_id, name, fee)
            print(f"Course {name} has been added successfully.")

#Choice 2 prompts for the input of student id, name and email and then proceeds to use error handling in order
#to register the student by calling the 'register_student' method of the 'system' object  and display any
# error that occurs which is stored in the variable e
        elif choice == "2":
            student_id = input("Enter the Student's ID: ")
            name = input("Enter the Student's Name: ")
            email = input("Enter the Student's Email: ")
            try:
                system.register_student(student_id, name, email)
                print(f"The student {name},{student_id} has been registered successfully.")
            except ValueError as e:
                print(e)

#Choice 3 prompts the user for the students id and course id and then proceeds to use error handling in order to
#attempt to enroll a student using the enroll_in_class method of the system object. In the case of an enrollment
#error, the error stored in variable e will be displayed to the user
        elif choice == "3":
            student_id = input("Enter the Student's ID: ")
            course_id = input("Enter the Course ID: ")
            try:
                system.enroll_in_course(student_id, course_id) #input values passed as arguments
                print(f"The Student {student_id} has been enrolled in {course_id} successfully.")
            except ValueError as e:
                print(e)

#Choice 4 prompts the user for a student id and an amount to pay.It then proceeds to calculate the payment using the
#'calculate_payment' method of the 'system' object. If an error occurs ( such as invalid input amount) it is caught
# and then displayed to the user
        elif choice == "4":
            student_id = input("Enter the Student's ID: ")
            try:
                amount = float(input("Enter the Payment Amount: "))
                system.calculate_payment(student_id, amount)
                print(f" Your payment has been processed successfully.{student_id} is now registered successfully")
            except ValueError as e:
                print(e)

#Choice 5 prompts the user to input the student id. The balance is then calculated using the 'check_student_balance' method
#of the 'system' object. If an error occurs (such as student ID not found, it is captured, stored in 'e' and displayed to the user
        elif choice == "5":
            student_id = input("Enter the Student's ID: ")
            try:
                balance = system.check_student_balance(student_id)
                print(f"Student's balance: {balance}")
            except ValueError as e:
                print(e)

#Choice 6 calls the 'show_courses' method and displays a message to the user to show the available courses.
# A for loop is then used to iterate over the available courses and display their ID, name and fee.
# the indexing ([0],[1],[2]) is used to access different elements in the courses tuple.
        elif choice == "6":
            courses = system.show_courses()
            print(" These are the available courses:")
            for course in courses:
                print(f"ID: {course[0]}, Name: {course[1]}, Fee: {course[2]}")

#Choice 7 calls the 'show_registered_students method for the 'system' object and displays a message to show registered students.
#A for loop is then used to iterate over all the students stores in the list and display their ID, name and email to the user
# The indexing ([0],[1],[2]) is used to access the different elements of each student tuple.
        elif choice == "7":
            students = system.show_registered_students()
            print("Registered Students:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}")
#Choice 8 collects input (course id) and uses it to show the list of enrolled students by calling the 'show_students_in_course' method
#of the 'system' object. A for loop is then used to iterate over each student in the specified course and prints their name and ID
#the indexing is used to access each element of each student tuple ([0] for ID and [1] for name). if an error occurs
#it will be caught and then displayed to the user.
        elif choice == "8":
            course_id = input("Enter the Course ID: ")
            try:
                enrolled_students = system.show_students_in_course(course_id)
                print(f"Students enrolled in course {course_id}:")
                for student in enrolled_students:
                    print(f"ID: {student[0]}, Name: {student[1]}")
            except ValueError as e:
                print(e)

#Choice 9 collects input (student id) and uses it to show the list of courses a student is enrolled in using the 'show_courses_for_student' method
# in the 'system' object. It then uses a for loop to iterate over each course printing the ID , name and fee for the specified student
#The indexing is used to access each element of the course tuple and in the case of an error (such as invalid ID) and displays it to the user
        elif choice == "9":
            student_id = input("Enter Student ID: ")
            try:
                courses = system.show_courses_for_student(student_id)
                print(f"Courses enrolled by student {student_id}:")
                for course in courses:
                    print(f"ID: {course[0]}, Name: {course[1]}, Fee: {course[2]}")
            except ValueError as e:
                print(e)

#Choice 10 is the exit option the exits the system by breaking the while loop that controls the main menu option
        elif choice == "10":
            print("Exiting the system.🐾🐾🐾🐾")
            break
#this else statements ends the nested if statements and displays a message if the user enters an invalid choice for the main menu
        else:
            print("🚫Invalid choice. Please choose a number that corresponds with your choice (1-9).")

if __name__ == "__main__":
    main()
