import random
import string
import pyperclip

password_history = []  # Store generated passwords for reference


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols, avoid_ambiguous):
    # Define character sets
    uppercase_letters = "ABCDEFGHJKLMNPQRSTUVWXYZ" if avoid_ambiguous else string.ascii_uppercase
    lowercase_letters = "abcdefghijkmnpqrstuvwxyz" if avoid_ambiguous else string.ascii_lowercase
    numbers = "23456789" if avoid_ambiguous else string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/~" if avoid_ambiguous else string.punctuation

    # Build the pool of characters based on user preferences
    all_characters = ""
    if use_uppercase:
        all_characters += uppercase_letters
    if use_lowercase:
        all_characters += lowercase_letters
    if use_numbers:
        all_characters += numbers
    if use_symbols:
        all_characters += symbols

    if not all_characters:
        raise ValueError( "At least one character type must be selected." )

    # Generate password
    password = ''.join( random.choice( all_characters ) for _ in range( length ) )

    # Ensure the password includes at least one of each selected character type
    while ((use_uppercase and not any( char in uppercase_letters for char in password )) or
           (use_lowercase and not any( char in lowercase_letters for char in password )) or
           (use_numbers and not any( char in numbers for char in password )) or
           (use_symbols and not any( char in symbols for char in password ))):
        password = ''.join( random.choice( all_characters ) for _ in range( length ) )

    # Copy to clipboard
    pyperclip.copy( password )
    password_history.append( password )  # Save to history

    # Strength Meter
    strength, feedback = check_password_strength( length, use_uppercase, use_lowercase, use_numbers, use_symbols )

    return password, strength, feedback


def check_password_strength(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    # Estimate strength based on length and variety of characters
    variety_count = sum( [use_uppercase, use_lowercase, use_numbers, use_symbols] )
    if length >= 12 and variety_count >= 3:
        return "Strong", "Your password is very secure."
    elif length >= 8 and variety_count >= 2:
        return "Moderate", "Your password is fairly secure but could be longer or more complex."
    else:
        return "Weak", "Your password is weak; consider using more characters or types."


def user_input():
    # User inputs for password settings
    length = int( input( "Enter the desired password length (min 6): " ) )
    if length < 6:
        print( "Password length should be at least 6 characters." )
        return user_input()

    use_uppercase = input( "Include uppercase letters? (y/n): " ).strip().lower() == 'y'
    use_lowercase = input( "Include lowercase letters? (y/n): " ).strip().lower() == 'y'
    use_numbers = input( "Include numbers? (y/n): " ).strip().lower() == 'y'
    use_symbols = input( "Include symbols? (y/n): " ).strip().lower() == 'y'
    avoid_ambiguous = input( "Avoid ambiguous characters (like O, 0, I, l)? (y/n): " ).strip().lower() == 'y'

    if not (use_uppercase or use_lowercase or use_numbers or use_symbols):
        print( "You must select at least one character type." )
        return user_input()

    return length, use_uppercase, use_lowercase, use_numbers, use_symbols, avoid_ambiguous


# Main function to interact with the user
def main():
    while True:
        # Get user preferences
        length, use_uppercase, use_lowercase, use_numbers, use_symbols, avoid_ambiguous = user_input()

        # Generate the password
        password, strength, feedback = generate_password( length, use_uppercase, use_lowercase, use_numbers,
                                                          use_symbols, avoid_ambiguous )

        # Display the results
        print( "\nGenerated Password:", password )
        print( "Password Strength:", strength )
        print( "Feedback:", feedback )
        print( "Password has been copied to clipboard." )

        # Show password history
        print( "\nPassword History:" )
        for i, pw in enumerate( password_history, 1 ):
            print( f"{i}: {pw}" )

        # Ask if the user wants to generate another password
        retry = input( "\nGenerate another password? (y/n): " ).strip().lower()
        if retry != 'y':
            break


# Run the main function
main()
