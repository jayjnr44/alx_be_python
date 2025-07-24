#
# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def main():
    """Main function to interact with the user."""
    temp_input = input("Enter the temperature value: ").strip()
    unit_input = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Input validation for numeric temperature
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Conversion logic
    if unit_input == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    elif unit_input == "F":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    else:
        raise ValueError(
            "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."
        )


if __name__ == "__main__":
    main()
