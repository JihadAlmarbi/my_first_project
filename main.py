from hello import hello
from rand import master
from handling_file import my_file
def read():
    for line in my_file():
        print (line)

def main():
    # hello()
    print ('the owner of this program is :\n')
    read()
    print ('\n_________\n')
    print("the dinner on ",master())
    print ('\n_________\n')
if "__main__" == __name__:
    main()