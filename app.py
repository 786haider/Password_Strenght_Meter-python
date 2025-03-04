# Password_Strenght_Meter

import re
import secrets
import string

def generate_strong_password(length=12):
    """
    Generate a strong, random password with a mix of characters.
    
    Args:
        length (int): Desired password length (default 12)
    
    Returns:
        str: A randomly generated strong password
    """
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = '!@#$%^&*'
    
    # Ensure at least one character from each required set
    password = [
        secrets.choice(uppercase_letters),
        secrets.choice(lowercase_letters),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]
    
    # Fill the rest of the password with random characters
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password.extend(secrets.choice(all_characters) for _ in range(length - 4))
    
    # Shuffle the password characters
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def check_password_strength(password):
    """
    Evaluate password strength based on multiple criteria.
    
    Args:
        password (str): Password to evaluate
    
    Returns:
        dict: Password evaluation results
    """
    # Initialize score and feedback
    score = 0
    feedback = []
    
    # Length Check (8-16 characters recommended)
    if len(password) >= 8:
        score += 1
        if len(password) >= 12:
            score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one uppercase letter.")
    
    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one lowercase letter.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Blacklist Common Passwords
    common_passwords = [
        'password', '123456', 'qwerty', 'admin', 
        'letmein', 'welcome', 'monkey', 'password123'
    ]
    if any(common_pass in password.lower() for common_pass in common_passwords):
        score = min(score - 1, 0)
        feedback.append("❌ Avoid common password patterns.")
    
    # Determine Strength Rating
    if score == 5:
        strength = "Strong 💪"
        status_message = "✅ Excellent! Your password is highly secure."
    elif score == 4:
        strength = "Moderate 🟡"
        status_message = "⚠️ Good password, but consider adding complexity."
    else:
        strength = "Weak 🚨"
        status_message = "❌ Weak Password - Please improve using suggestions."
    
    return {
        'score': score,
        'strength': strength,
        'status_message': status_message,
        'feedback': feedback
    }

def main():
    """
    Main function to interact with password strength checker.
    """
    print("🔐 Password Strength Meter")
    print("-" * 30)
    
    while True:
        print("\nOptions:")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            password = input("Enter your password: ")
            result = check_password_strength(password)
            
            print(f"\nStrength: {result['strength']}")
            print(result['status_message'])
            
            if result['feedback']:
                print("\nImprovement Suggestions:")
                for suggestion in result['feedback']:
                    print(suggestion)
        
        elif choice == '2':
            generated_password = generate_strong_password()
            print(f"\n🎲 Generated Strong Password: {generated_password}")
            result = check_password_strength(generated_password)
            print(f"Strength: {result['strength']}")
        
        elif choice == '3':
            print("Thank you for using the Password Strength Meter! 👋")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()