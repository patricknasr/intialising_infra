def main():
    try:
        # Taking three inputs from the user
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))

        # Calculating the sum
        total = num1 + num2 + num3

        # Displaying the sum
        print(f"The sum of the numbers is: {total}")
    
    except ValueError:
        # Error handling for non-integer inputs
        print("Please enter valid integer numbers.")

if __name__ == "__main__":
    main()
