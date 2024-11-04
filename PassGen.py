import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Create the character pool based on user preferences
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters  # Adds both lowercase and uppercase letters
    if use_numbers:
        character_pool += string.digits         # Adds digits 0-9
    if use_symbols:
        character_pool += string.punctuation    # Adds common symbols

    # Ensure that at least one character type is selected
    if not character_pool:
        raise ValueError("At least one character type must be selected")

    # Generate a random password from the character pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    # Get user input for password length and character types
    try:
        length = int(input("Enter the desired password length: "))
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")

if __name__ == "__main__":
    main()
