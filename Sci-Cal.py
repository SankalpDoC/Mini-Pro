import math

def main():
    print("Welcome to Scientific Calculator\n")

    while True:
        print("Please choose an operation:")
        print("1. Square root")
        print("2. Factorial")
        print("3. Natural logarithm")
        print("4. Power")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            square_root()
        elif choice == "2":
            factorial()
        elif choice == "3":
            natural_logarithm()
        elif choice == "4":
            power()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid input, please try again.")

def square_root():
    x = float(input("Enter a number: "))
    result = math.sqrt(x)
    print(f"The square root of {x} is {result}\n")

def factorial():
    x = int(input("Enter a number: "))
    result = math.factorial(x)
    print(f"The factorial of {x} is {result}\n")

def natural_logarithm():
    x = float(input("Enter a number: "))
    result = math.log(x)
    print(f"The natural logarithm of {x} is {result}\n")

def power():
    x = float(input("Enter a base number: "))
    y = float(input("Enter an exponent: "))
    result = math.pow(x, y)
    print(f"{x} raised to the power of {y} is {result}\n")

if __name__ == "__main__":
    main()