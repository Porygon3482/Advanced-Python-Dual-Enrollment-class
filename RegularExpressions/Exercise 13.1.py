"""
Author: Neel Srivastava
Date: 17/5/26
Exercise: Regular Expression - Phone Numbers
Summary: Program that prints the names and phones with the area code of "408"
"""
import re

#reads the phone file, then prints the names and phones with the area code of "408"
def extract_numbers_with_408(filename):
    with open (filename, "r") as file:
        # Looks in every line in the file
        for line in file:
            line = line.strip()
            if not line:
                continue
            # matches name and phone with "408"

            match = re.match(r'^(.+):\s*(408-\d{3}-\d{4})', line)
            if match:
                name = match.group(1)
                phone = match.group(2)
                print(f"{name} {phone}")

if __name__ == "__main__":
    extract_numbers_with_408("phones.txt")






