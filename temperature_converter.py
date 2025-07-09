def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_celsius_to_fahrenheit():
    temperature = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temperature)
    print(f"{temp}°C is {result:.2f}°F")






def main():
    print("Welcome to the Temperature Converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")


if __name__ == "__main__":
    main()