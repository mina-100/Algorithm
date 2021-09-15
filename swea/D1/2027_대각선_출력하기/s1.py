for i in range(5):
    printing = ''
    for j in range(5):
        if i == j:
            printing += '#'
        else:
            printing += '+'
    print(printing)
