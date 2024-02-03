if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # Creating a tuple
    t = tuple(integer_list)

    # Printing the result of hash(t)
    print(hash(t))
