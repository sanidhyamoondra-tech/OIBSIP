import random
import string

def get_yes_no(prompt):
    """Helper function to get a clean yes/no input from the user."""
    while True:
        choice = input(prompt).lower().strip()
        if choice in ['y', 'yes']: return True
        if choice in ['n', 'no']: return False
        print("Invalid input. Please enter 'y' or 'n'.")

def generate_password():
    print("\n--- Random Password Generator ---")
    
    
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("Error: Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number.")

    
    print("\nSelect character types to include (you must choose at least 2):")
    while True:
        use_upper = get_yes_no("Include Uppercase letters? (y/n): ")
        use_lower = get_yes_no("Include Lowercase letters? (y/n): ")
        use_nums = get_yes_no("Include Numbers? (y/n): ")
        use_syms = get_yes_no("Include Symbols? (y/n): ")
        
        
        selections = sum([use_upper, use_lower, use_nums, use_syms])
        if selections >= 2:
            break
        print("\nError: You must select at least 2 character types. Let's try again.\n")

    
    pool = ""
    guaranteed_chars = []
    
    if use_upper:
        pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_nums:
        pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if use_syms:
        pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))

    remaining_length = length - len(guaranteed_chars)
    random_chars = [random.choice(pool) for _ in range(remaining_length)]
    
    
    password_list = guaranteed_chars + random_chars
    random.shuffle(password_list)
    password = "".join(password_list)
    
    print(f"\n>>> Your Generated Password: {password} <<<\n")

def main():
    while True:
        generate_password()
        if not get_yes_no("Would you like to generate another password? (y/n): "):
            print("Exiting generator. Stay secure!")
            break

if __name__ == "__main__":
    main()