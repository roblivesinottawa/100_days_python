alphabet = ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 
'i' ,'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's' ,'t',
'u', 'v', 'w', 'x' ,'y', 'z', 'a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 
'i' ,'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's' ,'t',
'u', 'v', 'w', 'x' ,'y', 'z']

direction = input("type 'encode' to encrypt, type 'decode' to decrypt: >>> ")
text = input("type your message: >>> ").lower()
shift = int(input("type the shift number: >>> "))


def encrypt(_text, _shift):
    cipher = ""
    for char in _text:
        position = alphabet.index(char)
        newposition = position + _shift
        cipher += alphabet[newposition]
    print(f"the encoded message is {cipher}")


def decrypt(_text, _shift):
    decipher = ""
    for char in _text:
        position = alphabet.index(char)
        newposition = position - _shift
        decipher += alphabet[newposition]
    print(f"the decoded text is {decipher}")



if direction == "encode":
    encrypt(_text=text, _shift=shift)
elif direction == "decode":
    decrypt(_text=text, _shift=shift)
