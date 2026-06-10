import random #import random module which contains functions for generating pseudo-random numbers, picking random elements from a list, or shuffling data.
import string #imports a utility module that contains pre-defined constants of common text characters (like the entire alphabet, digits, and punctuation). Using this saves you from manually typing out pools of characters and risking typos.

def build_password(letters_count, digits_count, symbols_count): #password function that get 3 inputs and generate a mixed string using those inputs 
    """Core logic to assemble and shuffle the password characters.""" #this is something new I learned. these are Docstrings. a specialized comment used in python to mention what a fucntion do
    lower = string.ascii_lowercase #defining lowercase characters: "abcdefghijklmnopqrstuvwxyz"
    upper = string.ascii_uppercase #defining uppercase characters: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = string.digits #defining numerical characters: "0123456789"
    symbols = string.punctuation #defining special characters: "!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"

    password_list = [] #create a empty list

    all_letters = lower + upper #Merges uppercase and lowercase letters into a single pool (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ).
    
    password_list += [random.choice(all_letters) for _ in range(letters_count)] #+= (In-place addition): This appends elements to our existing list. It uses a list comprehension to pick a random letter letters_count times and adds them to password_list.

    password_list += [random.choice(digits) for _ in range(digits_count)] #+= (In-place addition): This appends elements to our existing list. It uses a list comprehension to pick a random digit digits_count times and adds them to password_list.

    password_list += [random.choice(symbols) for _ in range(symbols_count)] #+= (In-place addition): This appends elements to our existing list. It uses a list comprehension to pick a random symbol symbols_count times and adds them to password_list.

    random.shuffle(password_list) #shuffle the list to make it more random
    
    return "".join(password_list) #join command will convert the list format like ['a', '4', '!', 'B'] to a single string. "" will specify no spaces or commas between characters  

def get_integer_input(prompt): #Defines a helper function that takes a string argument (prompt), which is the question we want to ask the user.
    """Function to ensure the user enters a valid number."""
    while True: #creates an infinite loop
        try: #Opens a try block. Python will attempt to run the code indented inside this block. If an error occurs, it jumps to the except block instead of crashing.
            value = int(input(prompt)) #Shows the question on the screen and waits for the user to type something (which always comes back as text/string).
            if value < 0: #Checks if the user entered a negative number. If they did, it prints a warning and uses continue, which skips the rest of the loop and starts the while True loop over from the top
                print("Please enter a positive number or 0.")
                continue
            return value #If the number is valid and positive, this line executes. return sends the integer back and breaks out of the function completely, ending the loop.
        except ValueError:
            print("Invalid input. Please enter a whole number.") #If the int() conversion failed because the input wasn't a valid number, Python skips the rest of the try block and lands here. It prints an error message, and since there is no return here, the while True loop starts over to ask the user again.


def interactive_password_generator():
    print("--- Welcome to the Advanced Password Generator ---") #Prints the user welcoming text and the main menu choices.
    print("Choose an option:")
    print("1. Generate a fully random secure password")
    print("2. Customize character counts")
    
    choice = input("Enter choice (1 or 2): ").strip() #Captures the menu choice. .strip() is a string method that removes any accidental leading or trailing spaces the user might have typed

    if choice == "1": #If the user typed "1", enter the random password generation track.
        # Fully random track
        length = get_integer_input("Enter the total password length (min 4): ") #Calls our safety function get_integer_input() to ask for the length. It guarantees length will be an integer.
        if length < 4: #A fallback check. If the user forces a small number like 2, the program overrides it and sets it to 12 to maintain security standards.
            print("Password too short for secure criteria. Defaulting to 12.")
            length = 12 #set password length to 12 characters
            
        # 1 upper, 1 lower, 1 digit, 1 symbol, then fill the rest randomly
        all_chars = string.ascii_letters + string.digits + string.punctuation #Creates a master pool of all possible letters (upper + lower), digits, and symbols.
        password_list = [ #creates a list with exactly one mandatory character from each group to guarantee strength
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        password_list += [random.choice(all_chars) for _ in range(length - 4)] #Uses a list comprehension to fill the remaining length - 4 characters completely randomly from the master all_chars pool.
        random.shuffle(password_list) #shuffle the password_list to remove predictability
        print(f"\nYour Secure Random Password: {''.join(password_list)}") #connect the list elements together into a single string inside an f-string and prints the final result to the screen.

    elif choice == "2": #If the user typed "2", enter the custom track.
        print("\n--- Custom Password Configuration ---")
        total_length = get_integer_input("Enter total desired password length: ") #Asks the user what the exact total size of the final password must be.
        
        letters = get_integer_input("How many letters? ")
        digits = get_integer_input("How many numbers? ")
        symbols = get_integer_input("How many special characters? ")

        # Validation: Check if the character counts match the requested length
        allocated_chars = letters + digits + symbols #Sums up all the individual character counts the user requested.
        
        if allocated_chars != total_length: #check if allocated_chars is equal to total_length
            print(f"\n[Error] Character breakdown ({allocated_chars}) does not match total length ({total_length}).")
            print("Please try again and ensure the math adds up!")
            return #The program logs an error and uses return to stop executing the function completely.

        # Build the custom password
        custom_pwd = build_password(letters, digits, symbols) #If the math is perfect, it calls our first function build_password(), hands it the specific numbers, and receives the finished, shuffled password string back.
        print(f"\nYour Custom Password: {custom_pwd}")
        
    else:
        print("Invalid choice. Exiting program.") #Runs if the user typed something other than "1" or "2" at the main menu

# Run the program
if __name__ == "__main__": #Validates if this file is being executed directly. If it is, it fires up the interactive_password_generator() function, starting your program interface!
    interactive_password_generator()