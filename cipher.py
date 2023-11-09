# enter alphabet
abc = "abcdefghijklmnopqrstuvw"
 
#shift amount
shift = int(input("Please enter the number of spaces to shift as an integer:"))
 
#what is the sentence
text = input("Enter the text to encrypt")
 
#convert text to lower case
lowercase_text = text.lower()
 
#empty string for the encrypted text
encrypted_text = ""
 
for char in text:
    if char in abc:
        char_index = abc.find(char)
        encrypted_char = abc[(char_index + shift) % len(abc)]
        encrypted_text += encrypted_char
    else:
        # If the character is not in the alphabet, leave it unchanged
        encrypted_text += char

# Print the encrypted text
print("Encrypted text:", encrypted_text)