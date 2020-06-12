import os
def filepath(a):
    if os.stat(a).st_size == 0:
        print('File is empty')
    else:
        print('File is not empty')
file=('C:/Users/user/Desktop/ram.txt')
filepath(file)
        