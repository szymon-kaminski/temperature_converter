def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_celsius_to_fahrenheit():
    temperature = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result:.2f}°F")


def convert_fahrenheit_to_celsius():
    temperature = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is {result:.2f}°C")


def main():
    print("Welcome to the Temperature Converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        convert_celsius_to_fahrenheit()
    elif choice == "2":
        convert_fahrenheit_to_celsius()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()