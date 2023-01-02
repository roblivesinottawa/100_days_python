import os.path

filename = 'practice/new_example.txt'


if not os.path.isfile(filename):
    print("file does not exist")
else:
    with open(filename) as f:
        content = f.read()

    # for line in content:
    #     print(line)

    print(content)

