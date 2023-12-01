def pattern1(level):

    for i in range(1, level + 1):
        print()
        for j in range(i):
            print('*', end = '')

def pattern2(level):

    for i in range(level, 0, -1):
        print()
        for j in range(i):
            print('*', end = '')

def pattern3(level):

    counter = level
    for i in range(level + 1):
        print(' ' * counter + '*' * i)
        counter -= 1

def pattern4(level):

    counter = 0
    for i in range(level, 0 ,-1):
        print(' ' * counter + '*' * i)
        counter += 1

def pattern5(level):

    # first loop for number of lines
    for i in range(level + 1):
        #second loop for spaces
        for j in range(level - i):
            print (" ",end='')
        # this loop is for printing stars
        for k in range(2 * i - 1):
            print("*", end='')
        print()


if __name__ == '__main__':
    userInput = int(input('Enter the level: '))
    pattern1(userInput)
    print()
    pattern2(userInput)
    print()
    pattern3(userInput)
    print()
    pattern4(userInput)
    print()
    pattern5(userInput)
    print()

    def pattern6(userInput):
        
        num = int(input('Enter number for pattern'))
        pattern = '*'
        string = pattern * num
        x = 0

        for i in string:
            x = x + 1
            print(string[0:x])