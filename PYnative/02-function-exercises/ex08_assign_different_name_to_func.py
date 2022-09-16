"""Module to depict assignment of different name to a function"""

def display_student(name,age):
    """Function to display name & age of student"""
    print(f"Name: {name}\nAge: {age}\n")

def main():
    """First function to be called"""
    display_student("Emma",26)
    # Assign new name to function.
    show_student = display_student
    # Call func using new name.
    show_student("Adrian",20)

if __name__ == "__main__":
    main()
