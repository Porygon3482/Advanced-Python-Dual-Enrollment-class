"""
Author: Neel Srivastava
Date: 16/5/26
Exercise: Regular Expression - House Numbers
Summary: Program that reads only the house numbers from a file containing addresses
"""
import re
#import os

def extract_house_numbers(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            match = re.match(r'^(\d+)', line)
            if match:
                print(match.group(1))

if __name__ == "main":
    extract_house_numbers("address.txt")

#print(os.getcwd())