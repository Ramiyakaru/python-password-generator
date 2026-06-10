import random
import string

def build_password(letters_count, digits_count, symbols_count):
    """Core logic to assemble and shuffle the password characters."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password_list = [] #create a empty list

    all_letters = lower + upper #Merges uppercase and lowercase letters into a single pool
    password_list += [random.choice(all_letters) for _ in range(letters_count)] #+= (In-place addition)

    password_list += [random.choice(digits) for _ in range(digits_count)]

    password_list += [random.choice(symbols) for _ in range(symbols_count)]

    random.shuffle(password_list) #shuffle the list
    
    return "".join(password_list) #join command

def get_integer_input(prompt): #Defines a helper function
    """Function to ensure the user enters a valid number."""
    while True: #creates an infinite loop
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number or 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def interactive_password_generator():
    print("--- Welcome to the Advanced Password Generator ---")
    print("Choose an option:")
    print("1. Generate a fully random secure password")
    print("2. Customize character counts")
    
    choice = input("Enter choice (1 or 2): ").strip()
    if choice == "1": #If the user typed "1", enter the random password generation track.
        # Fully random track
        length = get_integer_input("Enter the total password length (min 4): ")
        if length < 4:
            print("Password too short for secure criteria. Defaulting to 12.")
            length = 12
            
       
        all_chars = string.ascii_letters + string.digits + string.punctuation 
        password_list = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        password_list += [random.choice(all_chars) for _ in range(length - 4)] #Uses a list comprehension
        random.shuffle(password_list)
        print(f"\nYour Secure Random Password: {''.join(password_list)}")

    elif choice == "2": #If the user typed "2", enter the custom track.
        #fully custom track
        print("\n--- Custom Password Configuration ---")
        total_length = get_integer_input("Enter total desired password length: ")
        
        letters = get_integer_input("How many letters? ")
        digits = get_integer_input("How many numbers? ")
        symbols = get_integer_input("How many special characters? ")

       
        allocated_chars = letters + digits + symbols
        
        if allocated_chars != total_length:
            print(f"\n[Error] Character breakdown ({allocated_chars}) does not match total length ({total_length}).")
            print("Please try again and ensure the math adds up!")
            return

        # Build the custom password
        custom_pwd = build_password(letters, digits, symbols)
        print(f"\nYour Custom Password: {custom_pwd}")
        
    else:
        print("Invalid choice. Exiting program.")

# Run the program
if __name__ == "__main__":
    interactive_password_generator()
