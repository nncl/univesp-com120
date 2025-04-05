def display_file_content():
    file = open("text.txt", "r")
    print(file.read())

    file.seek(0)
    print(file.readline())

    file.seek(0)
    print(file.readlines())

    file.close()

display_file_content()