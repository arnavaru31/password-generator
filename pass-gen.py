import random
import string

def generate_strong_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generates a strong, random password with a specified length and character sets.

    Args:
        length (int): The desired length of the password. Must be at least 8.
        use_letters (bool): If True, include lowercase and uppercase letters.
        use_numbers (bool): If True, include numbers.
        use_symbols (bool): If True, include symbols.

    Returns:
        str: A randomly generated password.
        None: If the length is less than 8 or no character sets are selected.
    """
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None
    
    if not any([use_letters, use_numbers, use_symbols]):
        print("At least one character set (letters, numbers, or symbols) must be selected.")
        return None

    all_characters = ""
    if use_letters:
        all_characters += string.ascii_letters
    if use_numbers:
        all_characters += string.digits
    if use_symbols:
        all_characters += string.punctuation

    if not all_characters:
        print("No characters available to generate a password.")
        return None

    # Ensure the password contains at least one character from each selected set
    password = []
    if use_letters:
        password.append(random.choice(string.ascii_letters))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters from all selected sets
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choices(all_characters, k=remaining_length))

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    # Example usage:
    password = generate_strong_password(length=16)
    if password:
        print("Generated Password:", password)

    # You can customize the password generation like this:
    # password_with_no_symbols = generate_strong_password(length=10, use_symbols=False)
    # if password_with_no_symbols:
    #     print("Password with no symbols:", password_with_no_symbols)
