alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in text:
    n = alphabet.index(letter)
    position = n + shift
    if position > 25:
      m =(position % 25) - 1
      cipher_text += alphabet[m]
    else:
      cipher_text += alphabet[position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in text:
        n = alphabet.index(letter)
        position = n - shift
        if position > 25:
            m = (position % 25) + 1
            cipher_text += alphabet[m]
        else:
            plain_text += alphabet[position]
    print(f"The encoded text is {plain_text}")

def direction_choice():
    if direction == "encode":
      encrypt(plain_text=text, shift_amount=shift)
    else:
      decrypt(cipher_text=text, shift_amount=shift)

def start():
    global direction
    global text
    global shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

def restart():
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    while choice == "yes":
        start()
    while choice == "no":
        break
start()
direction_choice()
restart()