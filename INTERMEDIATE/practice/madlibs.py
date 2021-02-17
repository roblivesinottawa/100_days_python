person_name = input("Person's name: ")
sickness = input("sickness: ")
noun = input("noun: ")
body_part = input("body part: ")
# adjective = input("adjective: ")
another_body_part = input("body part: ")
medicine = input("medicine: ")
favorite_drink = input("favorite drink: ")
noun2 = input("noun: ")

print("A doctor visit")

madlib = f"Patient: Thank you very much for seeing me, Doctor {person_name}. \
Doctor: What seems to be the problem, young {sickness}?\
Patient: When I move my {noun}, it hurts.\
Doctor: Then, don't move your {body_part}.\
Patient: Also, my {another_body_part} aches. Could you give me some {medicine}?\
Doctor: That may not be necessary, yet. Let me take a look. Open your {favorite_drink} wide. Good. Now, I'm going to listen to your {noun2} beat. Breathe in and out, slowly."

print(madlib)