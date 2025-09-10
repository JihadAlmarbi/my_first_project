def my_file():
    with open("my_file.txt", "w") as file:
        file.write('Mohammed Al-Haddad\n')
        file.close
    file = open("my_file.txt", 'r')
    return file
