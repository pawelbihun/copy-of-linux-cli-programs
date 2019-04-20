import sys

file_name = sys.argv
i = 1                               # i=1 to avoid print a source code from the first argument of file_name

while i < len(file_name):           # check how many arguments hava a list file_name
    with open(file_name[i]) as f:   # open another file with i index
        content = f.read()
        print(content)
    i += 1
    print("")                       # separate another file with a new empty line
