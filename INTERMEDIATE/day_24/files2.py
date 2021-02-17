# read the file

# file = open("example.txt")
with open("example.txt") as file:
    contents = file.read()
    print(contents)


# write to the file
# this code deletes what is on the file and replace it with new content
# change a to append which will add to the file
with open("example.txt", mode="a") as filename:
    filename.write("""Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
    Est natus quis quam eveniet reprehenderit cum quidem accusantium 
    suscipit minima, alias illo autem consequuntur nobis, 
    inventore, explicabo similique. Soluta, illum neque.""")
    

# create a new file
# file can be written directly from terminal
with open("new_example.txt", mode="w") as file:
    file.write("Hello, World")
