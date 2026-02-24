#Movie-main.py
"""
Name: Neel Srivastava
Project: Sorting Movies
Date: 23/2/26
Summary: This program manages a list of movies. Users can add, remove, display,
and sort movies by title, year viewed, rating, or duration. The program
uses different sorting algorithms and includes input checks to prevent crashes.
"""

class Movie:
    """
    Initializes a new Movie object with the provided attributes.

    :param title: The name of the movie.
    :param year_viewed: The year the user watched the movie.
    :param rating: The user's rating on a scale of 1 to 5.
    :param duration: The length of the movie in hours.
    """
    def __init__(self, title, year_viewed, rating, duration):
        self.title = title
        self.year_viewed = year_viewed
        self.rating = rating
        self.duration = duration


class Array:
    """
    A dynamic array that stores Movie objects.

    Starts with a fixed capacity and automatically doubles in size
    when the array becomes full. Only the filled portion (up to self.size)

    :param capacity: The initial maximum number of elements. Defaults to 5.
    """

    """
    Initializes the Array with a given starting capacity.

    :param capacity: The initial maximum number of elements. Defaults to 5.
    """
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity

    """
    Adds a new Movie object to the end of the array.

    If the array is at full capacity, it is doubled in size before
    the new item is inserted.

    :param item: The Movie object to add.
    """
    def append(self, item):
        # If the array is full, double its capacity before adding
        if self.size == self.capacity:
            self._grow()
        self.data[self.size] = item
        self.size += 1

    """
    Doubles the capacity of the array when it is full.

    Creates a new list twice the current capacity, copies all
    existing elements into it, and replaces the old list.
    """
    def _grow(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        # Copy each existing element into the new larger array
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    """
    Removes the Movie at the given index and shifts remaining elements left.
    Prints an error message if the index is out of range.

    :param index: The index of the Movie to remove.
    """
    def remove(self, index):
        # Check that the given index is within the valid range
        if index < 0 or index >= self.size:
            print("\nInvalid selection.\n")
            return
        # Shift every element after the removed index one position to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        # Clear the last slot and reduce the size count
        self.data[self.size - 1] = None
        self.size -= 1

    """
    Sorts the movies alphabetically by title using Selection Sort.
    In each pass, the smallest title in the unsorted portion is found
    and swapped into its correct position.
    """

    def selection_sort_title(self):
        # Outer loop: move the boundary of the sorted portion forward one step each pass
        for i in range(self.size):
            min_idx = i
            # Inner loop: find the movie with the smallest title in the unsorted portion
            for j in range(i + 1, self.size):
                # Compare titles in lowercase
                if self.data[j].title.lower() < self.data[min_idx].title.lower():
                    min_idx = j
            # Swap the found minimum with the first unsorted element
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]

    """
    Sorts the movies from earliest to latest by year viewed using Insertion Sort.
    Each element is taken from the unsorted portion and inserted into
    its correct position within the already-sorted portion.
    """
    def insertion_sort_year(self):
        # Start from the second element
        for i in range(1, self.size):
            key = self.data[i]
            j = i - 1
            # Shift elements that are greater than key one position to the right
            while j >= 0 and self.data[j].year_viewed > key.year_viewed:
                self.data[j + 1] = self.data[j]
                j -= 1
            # Place the key in its correct sorted position
            self.data[j + 1] = key

    """
    Sorts the movies from shortest to longest duration using Bubble Sort.
    Repeatedly steps through the array, compares the adjacent movies, and
    swaps them if they are out of order. Each pass places the next
    longest duration at the end of the unsorted portion.
    """
    def bubble_sort_duration(self):
        # Outer loop: each pass bubbles the next largest value to its correct position
        for i in range(self.size - 1):
            # Inner loop: compare adjacent pairs; reduce range since end is already sorted
            for j in range(self.size - 1 - i):
                # If the left movie has a longer duration than the right, swap them
                if self.data[j].duration > self.data[j + 1].duration:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    """
    Sorts the movies from lowest to highest rating using Quick Sort.
    
    Picks a pivot element and partitions the array so all lower-rated movies
    come before it and all higher-rated movies come after, then recursively
    sorts each partition. Calls itself until the full array is sorted.
    
    :param low: The starting index of the sub-array to sort. Defaults to 0.
    :param high: The ending index of the sub-array to sort. Defaults to size - 1.
    """
    def quick_sort_rating(self, low=None, high=None):
        # Set default bounds on the first call
        if low is None:
            low = 0
        if high is None:
            high = self.size - 1
        # Only sort if there are at least two elements in the current sub-array
        if low < high:
            pi = self._partition(low, high)
            # Recursively sort the elements before and after the partition index
            self.quick_sort_rating(low, pi - 1)
            self.quick_sort_rating(pi + 1, high)

    """
    Picks a pivot and sorts everything being higher/lower than the pivot.
    Calls until the list is sorted.

    :param low: The starting index of the sub-array.
    :param high: The ending index of the sub-array (used as the pivot).

    :return: The final index of the pivot after partitioning.
    """
    def _partition(self, low, high):
        # Use the last element's rating as the pivot value
        pivot = self.data[high].rating
        i = low - 1
        # Move elements with a rating <= pivot to the left of the pivot
        for j in range(low, high):
            if self.data[j].rating <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        # Place the pivot in its final sorted position
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1


"""
Prints all movies in the array as a formatted table.

Displays a numbered list with columns for title, year viewed, rating,
and duration. If the array is empty, a message is shown instead.

:param movies: The Array object containing Movie objects to display.
"""
def print_table(movies):
    # If there are no movies, notify the user and exit early
    if movies.size == 0:
        print("\nNo movies to display.\n")
        return
    print()
    print(f"{'#':<4} {'Title':<30} {'Viewed':<10} {'Rating':<8} {'Duration (hrs)'}")
    print(f"{'--':<4} {'-'*29:<30} {'-'*9:<10} {'-'*6:<8} {'-'*14}")
    # Print each movie with a 1-based sequence number
    for i in range(movies.size):
        m = movies.data[i]
        print(f"{i+1:<4} {m.title:<30} {m.year_viewed:<10} {m.rating:<8} {m.duration}")
    print()


"""
Prints the main menu
"""
def print_menu():
    print("MENU")
    print("  L  List all movies")
    print("  A  Add a movie")
    print("  E  remove a movie")
    print("  D  arrange by Duration")
    print("  T  arrange by Title")
    print("  V  arrange by year Viewed")
    print("  R  arrange by Rating")
    print("  Q  Quit")


"""
Prompts the user to enter details for a new movie and adds it to the array.

Collects and validates the title, year viewed, rating, and duration.
Each field is re-prompted until valid input is provided. The new movie
is always appended to the end of the array.

:param movies: The Array object to add the new Movie into.
"""
def add_movie(movies):
    title = input("Enter a movie's name: ").strip()
    # Reject an empty title and return without adding anything
    if not title:
        print("\nInvalid movie name.\n")
        return

    # Keeps prompting until the user enters a valid year
    while True:
        year_input = input(f"Enter the year you saw {title} [like 2016]: ").strip()
        try:
            year = int(year_input)
            # Reject years outside a reasonable range
            if year < 1900 or year > 2026:
                print("Please enter a valid year.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric year.")

    # Keeps prompting until the user enters a valid rating
    while True:
        rating_input = input(f"Enter your rating for {title} [1, 2, 3, 4, 5]: ").strip()
        try:
            rating = int(rating_input)
            # Rating must be between 1 and 5 inclusive
            if rating < 1 or rating > 5:
                print("Please enter a rating between 1 and 5.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    # Keep prompting until the user enters a valid duration
    while True:
        duration_input = input(f"Enter the duration (hours) for {title} [1, 2, 3, 4, 5]: ").strip()
        try:
            duration = float(duration_input)
            # Duration must be a positive number and no greater than 10 hours
            if duration <= 0 or duration > 10:
                print("Please enter a valid duration (e.g. 1.5).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric duration.")

    movies.append(Movie(title, year, rating, duration))
    print(f"\n'{title}' added.\n")


"""
Displays the current movie list and prompts the user to remove one by number.

Validates the user's selection and removes the chosen movie from the array.
If the array is empty, a message is shown and the function returns early.

:param movies: The Array object to remove the Movie from.
"""
def remove_movie(movies):
    # If there are no movies, there is nothing to remove
    if movies.size == 0:
        print("\nNo movies to remove.\n")
        return
    print_table(movies)
    # Keep prompting until the user enters a valid sequence number
    while True:
        choice = input(f"...which movie to remove (1-{movies.size})? ").strip()
        try:
            index = int(choice) - 1  # Convert 1-based input to 0-based index
            # Reject numbers outside the valid range
            if index < 0 or index >= movies.size:
                print(f"Please enter a number between 1 and {movies.size}.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    removed_title = movies.data[index].title
    movies.remove(index)
    print(f"\n'{removed_title}' removed.\n")


"""
Crates the movie array and runs the menu loop, accepting user input
and dispatching to the appropriate function or sort method until the
user chooses to quit.
"""
def main():
    movies = Array(capacity=5)

    # Main program loop: keep showing the menu until the user quits
    while True:
        print_menu()
        choice = input("...your choice: ").strip().upper()

        # Check which menu option the user selected and call the appropriate function
        if choice == 'L':
            print_table(movies)
        elif choice == 'A':
            print()
            add_movie(movies)
        elif choice == 'E':
            print()
            remove_movie(movies)
        elif choice == 'T':
            movies.selection_sort_title()
            print("\nMovies arranged by Title.\n")
            print_table(movies)
        elif choice == 'V':
            movies.insertion_sort_year()
            print("\nMovies arranged by Year Viewed.\n")
            print_table(movies)
        elif choice == 'R':
            movies.quick_sort_rating()
            print("\nMovies arranged by Rating.\n")
            print_table(movies)
        elif choice == 'D':
            movies.bubble_sort_duration()
            print("\nMovies arranged by Duration.\n")
            print_table(movies)
        elif choice == 'Q':
            print("\nGoodbye!\n")
            break  # Exit the main loop and end the program
        else:
            # Handle any input that doesn't match a valid menu option
            print("\nInvalid option. Please try again.\n")


if __name__ == "__main__":
    main()
