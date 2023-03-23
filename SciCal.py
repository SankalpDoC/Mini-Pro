import math
import logging

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_logarithm(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    # configure logging
    logging.basicConfig(filename='SciCalLogs.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    while True:
        print("Scientific Calculator Menu:")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Logarithm")
        print("4. Power")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        # log user's choice
        logging.debug(f"User chose option {choice}")

        if choice == 1:
            x = float(input("Enter the number to find its square root: "))
            # log input value
            logging.info(f"Calculating square root of {x}")
            result = square_root(x)
            print(f"The square root of {x} is {result}")
            # log output value
            logging.info(f"Result: {result}")
        elif choice == 2:
            x = int(input("Enter the number to find its factorial: "))
            # log input value
            logging.info(f"Calculating factorial of {x}")
            result = factorial(x)
            print(f"The factorial of {x} is {result}")
            # log output value
            logging.info(f"Result: {result}")
        elif choice == 3:
            x = float(input("Enter the number to find its natural logarithm: "))
            # log input value
            logging.info(f"Calculating natural logarithm of {x}")
            result = natural_logarithm(x)
            print(f"The natural logarithm of {x} is {result}")
            # log output value
            logging.info(f"Result: {result}")
        elif choice == 4:
            x = float(input("Enter the base: "))
            b = float(input("Enter the exponent: "))
            # log input values
            logging.info(f"Calculating {x} raised to the power of {b}")
            result = power(x, b)
            print(f"{x} raised to the power of {b} is {result}")
            # log output value
            logging.info(f"Result: {result}")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
            # log error message
            logging.error("Invalid choice")

if __name__ == '__main__':
    main()
