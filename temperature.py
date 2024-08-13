def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
def get_user_input():
    print("Temperature Conversion Program")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("5: Fahrenheit to Kelvin")
    print("6: Kelvin to Fahrenheit")
    
    conversion_type = int(input("Choose the conversion type (1-6): "))
    temperature = float(input("Enter the temperature value to convert: "))
    
    return conversion_type, temperature

def convert_temperature(conversion_type, temperature):
    if conversion_type == 1:
        return celsius_to_fahrenheit(temperature)
    elif conversion_type == 2:
        return fahrenheit_to_celsius(temperature)
    elif conversion_type == 3:
        return celsius_to_kelvin(temperature)
    elif conversion_type == 4:
        return kelvin_to_celsius(temperature)
    elif conversion_type == 5:
        return fahrenheit_to_kelvin(temperature)
    elif conversion_type == 6:
        return kelvin_to_fahrenheit(temperature)
    else:
        return None

def main():
    conversion_type, temperature = get_user_input()
    result = convert_temperature(conversion_type, temperature)
    
    if result is not None:
        print(f"The converted temperature is: {result}")
    else:
        print("Invalid conversion type selected.")

if __name__ == "__main__":
    main()
