FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_FREEZING_POINT = 32


def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT


def main():
    try:
        temp_str = input("Enter the temperature to convert: ").strip()
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = (
        input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    )

    if unit == "F":
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    else:
        raise ValueError(
            "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."
        )


if __name__ == "__main__":
    main()
