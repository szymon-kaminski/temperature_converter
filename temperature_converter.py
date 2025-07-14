def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def convert_celsius_to_fahrenheit():
    try:    
        temperature = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def convert_fahrenheit_to_celsius():
    try:
        temperature = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def convert_celsius_to_kelvin():
    try:    
        temperature = float(input("Enter temperature in Celsius: "))
        result = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is {result:.2f} K")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def convert_kelvin_to_celsius():
    try:
        temperature = float(input("Enter temperature in Kelvin: "))
        result = kelvin_to_celsius(temperature)
        print(f"{temperature} K is {result:.2f}°C")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def convert_fahrenheit_to_kelvin():
    try:
        temperature = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_kelvin(temperature)
        print(f"{temperature}°F is {result:.2f} K")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def convert_kelvin_to_fahrenheit():
    try:    
        temperature = float(input("Enter temperature in Kelvin: "))
        result = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} K is {result:.2f}°F")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        

def main():
    print("Welcome to the Temperature Converter!")

    while True:
        print("\nWhat would you like to convert?")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("Q. Quit")
        choice = input("Choose an option (1-6 or q for quit): ")

        if choice.lower() in ["q", "quit", "exit"]:
            print("Exiting the program. Goodbye!")
            return
        elif choice == "1":
            convert_celsius_to_fahrenheit()
        elif choice == "2":
            convert_fahrenheit_to_celsius()
        elif choice == "3":
            convert_celsius_to_kelvin()
        elif choice == "4":
            convert_kelvin_to_celsius()
        elif choice == "5":
            convert_fahrenheit_to_kelvin()
        elif choice == "6":
            convert_kelvin_to_fahrenheit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6 or q to qiut.")
        again = input("\nWuld you like to convert another temperature? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()