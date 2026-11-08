alphabet = list("abcdefghijklmnopqrstuvwxyz")

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    return encrypted_text


def decrypt(original_text, shift_amount):
    return encrypt(original_text, -shift_amount)

def caesar(direction, text, shift):
    if direction == "encode":
        return encrypt(text, shift)
    elif direction == "decode":
        return decrypt(text, shift)
    else:
        return "Invalid option"
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' or 'decode': ").lower()
    text = input("Enter your message: ").lower()
    shift = int(input("Enter shift number: "))
    result = caesar(direction, text, shift)
    print("Result:", result)
    restart = input("Go again? (y/n): ").lower()
    if restart != "y":
        should_continue = False
print("Goodbye!")