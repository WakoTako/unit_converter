def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def main():
    print("Welcome to the Multi-Unit Converter!")
    print("Available conversions: \n1. Temperature (Celsius <-> Fahrenheit)\n2. Length (Meters <-> Feet)\n3. Weight (Kilograms <-> Pounds)")

    while True:
        choice = input("\nChoose conversion type (1 for Temperature, 2 for Length, 3 for Weight, or 'q' to quit): ").strip()

        if choice == '1':
            temp_choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").strip().upper()
            if temp_choice == 'C':
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
            elif temp_choice == 'F':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")

        elif choice == '2':
            length_choice = input("Convert (M)eters to Feet or (F)eet to Meters? ").strip().upper()
            if length_choice == 'M':
                meters = float(input("Enter length in meters: "))
                print(f"{meters} meters is {meters_to_feet(meters)} feet")
            elif length_choice == 'F':
                feet = float(input("Enter length in feet: "))
                print(f"{feet} feet is {feet_to_meters(feet)} meters")

        elif choice == '3':
            weight_choice = input("Convert (K)ilograms to Pounds or (P)ounds to Kilograms? ").strip().upper()
            if weight_choice == 'K':
                kg = float(input("Enter weight in kilograms: "))
                print(f"{kg} kg is {kilograms_to_pounds(kg)} pounds")
            elif weight_choice == 'P':
                pounds = float(input("Enter weight in pounds: "))
                print(f"{pounds} pounds is {pounds_to_kilograms(pounds)} kilograms")

        elif choice.lower() == 'q':
            print("Exiting converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
