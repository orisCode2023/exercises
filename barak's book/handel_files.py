import sys
def writing_from_file_to_file():
    first_file = open(r'/Users/ori/Projects/kodkod/Python/file1.txt' , 'r')
    second_file = open(r'/Users/ori/Projects/kodkod/Python/file2.txt' , 'a')
    subject = first_file.readline()
    second_file.write(subject)
    second_file.close()
    x = open(r'/Users/ori/Projects/kodkod/Python/file2.txt' , 'r')
    new_file = x.readline()
    print(new_file)

