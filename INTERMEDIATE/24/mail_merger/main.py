placeholder = "[name]"


with open("day_24/mail_merger/input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("day_24/mail_merger/input/letters/starting_letter.txt") as start_letter:
    letter_content = start_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(placeholder, stripped_name)
        with open(f"day_24/mail_merger/output/to_be_sent/invite_for_{stripped_name}.txt", mode="w") as letter_finished:
            letter_finished.write(new_letter)

