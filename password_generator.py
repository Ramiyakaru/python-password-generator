import random
import string
def generate_strong_password(length=12):
    if length < 4:
        print("Password length must be at least 4 to ensure strong security criteria.")
        return None

    #Define character pools using the string module
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    #creating a pool of all characters
    all_characters = lower + upper + digits + symbols

    #ensure at least one character from each category
    password_required = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    #Fill the remaining length of the password with random choices from the entire pool
    password_remaining = [random.choice(all_characters) for _ in range(length - 4)]

    #Combine and shuffle to remove any predictable patterns
    complete_password_list = password_required + password_remaining
    random.shuffle(complete_password_list)

    #Convert the list back into a single string
    final_password = "".join(complete_password_list)
    
    return final_password

#Example usage
if __name__ == "__main__":
    print("--- Advanced Password Generator ---")
    desired_length = 16
    generated_pwd = generate_strong_password(desired_length)
    
    if generated_pwd:
        print(f"Generated Secure Password ({desired_length} characters): {generated_pwd}")
