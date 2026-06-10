import random #import random module which contains functions for generating pseudo-random numbers, picking random elements from a list, or shuffling data.
import string #imports a utility module that contains pre-defined constants of common text characters (like the entire alphabet, digits, and punctuation). Using this saves you from manually typing out pools of characters and risking typos.

def generate_strong_password(length=12): #create function and create a default argument of 12 character length
    if length < 4: #conditional clause to check the length. if less than 4 characters, the generated password didn't meet the conditions
        print("Password length must be at least 4 to ensure strong security criteria.") #prints a warning message
        return None #and exits the programs without crashing

    #Define character pools using the string module
    lower = string.ascii_lowercase #defining lowercase characters: "abcdefghijklmnopqrstuvwxyz"
    upper = string.ascii_uppercase #defining uppercase characters: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = string.digits #defining numerical characters: "0123456789"
    symbols = string.punctuation #defining special characters: "!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`"
    
    #creating a pool of all characters
    all_characters = lower + upper + digits + symbols

    #ensure at least one character from each category
    password_required = [ #create a list containing exactly 4 characters. By calling random.choice() on each individual pool, the final password will have at least one character from each pool
        random.choice(lower), #This function takes a sequence (like a string or a list) and randomly extracts exactly one lowercase letter from it.
        random.choice(upper), #This function takes a sequence (like a string or a list) and randomly extracts exactly one uppercase letter from it.
        random.choice(digits), #This function takes a sequence (like a string or a list) and randomly extracts exactly one numerical character from it.
        random.choice(symbols) #This function takes a sequence (like a string or a list) and randomly extracts exactly one special character from it.
    ]

    #Fill the remaining length of the password with random choices from the entire pool
    password_remaining = [random.choice(all_characters) for _ in range(length - 4)] #to fill the remaining slots. length - 4 time loop will run to generate random choices from all_characters list

    #Combine and shuffle to remove any predictable patterns
    complete_password_list = password_required + password_remaining #create a new list by combining password_required and password_remaining
    random.shuffle(complete_password_list) #shuffle the list to make it more random

    #Convert the list back into a single string
    final_password = "".join(complete_password_list) #join command will convert the list format like ['a', '4', '!', 'B'] to a single string. "" will specify no spaces or commas between characters  
    
    return final_password

#Example usage
if __name__ == "__main__": #python idiom. it checks if the script is running directly 'py rev1.py' or if imported as a module. when running directly python assigns the string "__main__" to the __name__ variable. 
    print("--- Advanced Password Generator ---") #prints to show the start of script
    desired_length = 16 #we can set the desired length of generated password
    generated_pwd = generate_strong_password(desired_length) #calls the generate_strong_password function with desired_length
    
    if generated_pwd: #check if password was successfully returned 
        print(f"Generated Secure Password ({desired_length} characters): {generated_pwd}") #prints the generated password