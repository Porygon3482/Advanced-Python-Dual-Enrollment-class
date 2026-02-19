#Calculate_Exponent.py
"""
Name: Neel Srivastava
Assignment: Calculate_Exponent
Date: 9/2/26
Summary: Calculates exponent and time complexity using a loop and
a recursive function
"""


"""
re-engineered "pow" function using a loop; calculates the result of raising a number by a power

:param number: the base to be raised by.
:param exponent, the non negative exponent to raise the base by.

:return: the result of the base to the power of the exponent

"""
def expo(number, exponent):
    result = 1

    for _ in range(exponent):
        result *= number
    return result


"""
recursive function; calculates the result of raising a number by a power using recursion

:param number: the base to be raised by.
:param exponent: the non negative exponent to raise the base by;

:return: the result of the base to the power of the exponent

"""
def expo_r(number, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return number
    return number * expo_r(number, exponent - 1)

"""
Main program.

Takes user input and tests the loop and recursive methods.
prints error if the user inputted exponent is a negative number
"""
def main():
    num = float(input("Enter a number "))
    exp = int(input("Enter an exponent "))

    if exp < 0:
        print("Error: non-negative exponent")
    else:
        print("\nRecursive Result:", expo_r(num, exp))
        print("exponent Result:", expo(num, exp))
        print("Time Complexity (both): O(n)")

if __name__ == "__main__":
    main()








