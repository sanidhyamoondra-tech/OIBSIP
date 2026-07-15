def calculate_bmi(weight, height):
    """Calculates BMI and returns the value and category."""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal"
    elif 25.0 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"
        
    return round(bmi, 2), category

def main():
    print(" Welcome to the BMI Calculator ")
    
    while True:
        try:
            
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
            
            
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be positive numbers. Please try again.\n")
                continue
                
            
            bmi_value, category = calculate_bmi(weight, height)
            print(f"\nResult: Your BMI is {bmi_value}")
            print(f"Category: {category}\n")
            
            
            again = input("Would you like to calculate another BMI? (yes/no): ").lower()
            if again != 'yes' and again != 'y':
                print("Exiting calculator. Stay healthy!")
                break
                
        except ValueError:
            print("Error: Invalid input. Please enter numeric values only.\n")

if __name__ == "__main__":
    main()