 alphabet = ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 
'i' ,'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's' ,'t',
'u', 'v', 'w', 'x' ,'y', 'z', 'a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 
'i' ,'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's' ,'t','u', 'v', 'w', 'x' ,'y', 'z']

def caesar(_text,_shift, _direction):
    deciphered = ""
    if _direction == "decode":
            _shift *= -1
    for char in _text:
        if char in alphabet:
            position = alphabet.index(char)
            newposition = position + _shift
            deciphered += alphabet[newposition]
        else:
            deciphered += char
    print(f"the {_direction}d text is {deciphered}")

should_continue = True
while should_continue:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt: >>> ")
    text = input("type your message: >>> ").lower()
    shift = int(input("type the shift number: >>> "))
    shift = shift % 26
    caesar(_text=text,_shift=shift, _direction=direction)

    result = input("type 'yes' if you want to go again. Otherwisem type 'no'. >>> ")
    if result == 'no':
        should_continue = False
        print("goodbye")





