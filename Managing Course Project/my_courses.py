"""
Name: Neel Srivastava
Date: 27 / 3 / 26
Project: Managing Course List
Summary:
A program that helps you manage your semester courses.
It allows you to list, add, drop, and sort courses
using a menu-driven interface.
"""

from arraylist import ArrayList
from arraysortedlist import ArraySortedList
from arrays import Array


def create_course_list():
    """Creates and returns an empty ArrayList to store course names."""
    return ArrayList()


def list_courses(course_list):
    """Prints all courses in the list, or a message if the list is empty."""
    if course_list.isEmpty():
        print("Your course list is empty.")
    else:
        print("Course list:")
        for course in course_list:
            print(course)


def add_course(course_list):
    """Prompts the user for a course name and adds it to the course list."""
    course_name = input("Enter the course name: ")
    course_list.insert(len(course_list), course_name)


def find_course(course_list, course_name):
    """Searches the course list for a given name and returns its index, or -1 if not found."""
    for i in range(len(course_list)):
        if course_list[i] == course_name:
            return i
    return -1


def drop_course(course_list):
    """
    Prompts the user for a course name and removes it from the list if found.
    Prints an error message if the course does not exist.
    """
    course_name = input("Enter the course name to drop: ")
    index = find_course(course_list, course_name)
    if index != -1:
        course_list.pop(index)
    else:
        print(f'"{course_name}" is not found in your course list.')
    list_courses(course_list)


def bubble_sort_ascending(course_list):
    """Sorts the course list in ascending alphabetical order using bubble sort."""
    n = len(course_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if course_list[j] > course_list[j + 1]:
                course_list[j], course_list[j + 1] = course_list[j + 1], course_list[j]


def bubble_sort_descending(course_list):
    """Sorts the course list in descending alphabetical order using bubble sort."""
    n = len(course_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if course_list[j] < course_list[j + 1]:
                course_list[j], course_list[j + 1] = course_list[j + 1], course_list[j]


def sort_ascending(course_list):
    """Sorts the course list in ascending order and prints the result."""
    bubble_sort_ascending(course_list)
    list_courses(course_list)


def sort_descending(course_list):
    """Sorts the course list in descending order and prints the result."""
    bubble_sort_descending(course_list)
    list_courses(course_list)


def print_menu():
    """Prints the main menu of options for the user to choose from."""
    print("\nPlease choose 1 of the following options:")
    print("1. List all courses")
    print("2. Add a course")
    print("3. Drop a course")
    print("4. Sort courses in ascending order of course name")
    print("5. Sort courses in descending order of course name")
    print("6. Exit")


def get_user_option():
    """Prompts the user to enter a menu option and returns their input."""
    return input("Enter your option: ")


def handle_option(option, course_list):
    """
    Calls the appropriate function based on the user's menu choice.
    Returns False if the user selects Exit, True otherwise.
    """
    if option == "1":
        list_courses(course_list)
    elif option == "2":
        add_course(course_list)
    elif option == "3":
        drop_course(course_list)
    elif option == "4":
        sort_ascending(course_list)
    elif option == "5":
        sort_descending(course_list)
    elif option == "6":
        return False
    else:
        print("Invalid option. Please enter a number between 1 and 6.")
    return True


def main():
    """Initializes the course list and runs the main menu loop until the user exits."""
    course_list = create_course_list()
    running = True

    while running:
        print_menu()
        option = get_user_option()
        running = handle_option(option, course_list)


if __name__ == "__main__":
    main()