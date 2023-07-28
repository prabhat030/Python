
from age_package import age_calculator, age_verify, age_categorize, age_convert, age_compare
from datetime import datetime

def get_birth_date():
    while True:
        try:
            year = int(input("Enter the birth year: "))
            month = int(input("Enter the birth month: "))
            day = int(input("Enter the birth day: "))
            birth_date = datetime(year, month, day)
            return birth_date
        except ValueError:
            print("Invalid date. Please enter a valid date.")

def main():
    while True:
        print("\n----- Age Package Menu -----")
        print("1. Calculate Age")
        print("2. Verify Age")
        print("3. Categorize Age")
        print("4. Convert Age")
        print("5. Compare Ages")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            birth_date = get_birth_date()
            age = age_calculator.calculate_age(birth_date)
            print(f"The calculated age is: {age} years.")
        elif choice == '2':
            age = int(input("Enter the age to verify: "))
            minimum_age = int(input("Enter the minimum required age: "))
            if age_verify.is_of_age(age, minimum_age):
                print("The person is of the required age.")
            else:
                print("The person is not of the required age.")
        elif choice == '3':
            age = int(input("Enter the age to categorize: "))
            category = age_categorize.categorize_age(age)
            print(f"The person falls into the category: {category}")
        elif choice == '4':
            age = int(input("Enter the age to convert: "))
            print(f"{age} years is equal to:")
            print(f"{age_convert.years_to_months(age)} months.")
            print(f"{age_convert.years_to_days(age)} days.")
            # Add more conversion options here if needed.
        elif choice == '5':
            age1 = int(input("Enter age of Individual 1: "))
            age2 = int(input("Enter age of Individual 2: "))
            result = age_compare.compare_ages(age1, age2)
            print(result)
        elif choice == '6':
            print("Exiting the Age Package Menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()