def paint(height, width, cover=5):
    cans = (height * width) / cover
    return f"you will need {round(cans)} cans of paint."


h = int(input("what's the height of the wall? >> "))
w = int(input("what's the width of the wall? >> "))
print(paint(h, w))