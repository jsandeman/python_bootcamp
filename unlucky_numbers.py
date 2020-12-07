for i in range(1, 21):
    if i == 4 or i == 13:
        desc = ' is unlucky!'
    elif i % 2 == 0:
        desc = ' is even.'
    else:
        desc = ' is odd.'
    print(f'{i} {desc}')
