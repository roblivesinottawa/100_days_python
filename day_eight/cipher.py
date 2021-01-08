# step one
alphabet = 'abcdefghijklmnopqrstuvwxyz'
partial_one = ""
partial_two = ""
new_alphabet = ""
message = input("enter message you wish to translate: ").lower()
key = int(input("enter the number you want to shift it by: "))

# step two
if key == 0:
    new_alphabet = alphabet
elif key > 0:
    partial_one = alphabet[:key]
    partial_two = alphabet[key:]
    new_alphabet = partial_two + partial_one
else:
    partial_one = alphabet[:(26+key)]
    partial_two = alphabet[(26+key):]
    new_alphabet = partial_two + partial_one


# step three
encrypted = ""
for message_index in range(0, len(message)):
    if message[message_index] == " ":
        encrypted += " "
    for alphabet_index in range(0, len(new_alphabet)):
        if message[message_index] == alphabet[alphabet_index]:
            encrypted += new_alphabet[alphabet_index]


print(encrypted)
