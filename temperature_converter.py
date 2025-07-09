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
    temperature = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result:.2f}°F")


def convert_fahrenheit_to_celsius():
    temperature = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is {result:.2f}°C")


def convert_celsius_to_kelvin():
    temperature = float(input("Enter temperature in Celsius: "))
    result = celsius_to_kelvin(temperature)
    print(f"{temperature}°C is {result:.2f} K")


def convert_kelvin_to_celsius():
    temperature = float(input("Enter temperature in Kelvin: "))
    result = kelvin_to_celsius(temperature)
    print(f"{temperature} K is {result:.2f}°C")


def convert_fahrenheit_to_kelvin():
    temperature = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_kelvin(temperature)
    print(f"{temperature}°F is {result:.2f} K")
   

def convert_kelvin_to_fahrenheit():    
    temperature = float(input("Enter temperature in Kelvin: "))
    result = kelvin_to_fahrenheit(temperature)
    print(f"{temperature} K is {result:.2f}°F")


def main():
    print("Welcome to the Temperature Converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = input("Choose an option (1-6): ")

    if choice == "1":
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
        print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()