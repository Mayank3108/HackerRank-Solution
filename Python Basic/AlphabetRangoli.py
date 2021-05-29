
def print_rangoli(size):
    import string
    # size= int(input())

    center = size - 1

    for i in range(size - 1, 0, -1):
        row = ['-'] * (2 * size - 1)
        for j in range(size - i):
            row[center - j] = row[center + j] = string.ascii_lowercase[j + i]
        print ('-'.join(row))

    for i in range(0, size):
        row = ['-'] * (2 * size - 1)
        for j in range(0, size - i):
            row[center - j] = row[center + j] = string.ascii_lowercase[j + i]
        print ('-'.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)