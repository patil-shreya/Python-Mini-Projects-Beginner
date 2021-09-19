alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction_call, input_text, shift_amount):
    final_text = ""
    for char in input_text:
        if char in alphabet: 
            char_index = alphabet.index(char)
            if direction_call == "encode":
                new_char_index = char_index + shift_amount
                if new_char_index > 25:
                    new_char_index %= 26
            elif direction_call == "decode":
                new_char_index = char_index - shift_amount
                if new_char_index < 0:
                    new_char_index %= 26
                    new_char_index -= 26
            new_char = alphabet[new_char_index]
            final_text += new_char
        else:
            final_text += char 
        
    print(f"The {direction_call}d text is {final_text}")

import art

print(art.logo)

restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction_call=direction, input_text=text, shift_amount=shift)

    want_to_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if want_to_continue == "no":
        restart = False
        print("Goodbye...Have a nice day!!")  
