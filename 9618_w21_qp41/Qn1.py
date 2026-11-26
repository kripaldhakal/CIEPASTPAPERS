"""def Unknown(X, Y):
    if X < Y:
        print(X+Y)
        return (Unknown(X+1, Y)*2)
    elif X == Y:
        return 1
    else:
        print(X+Y)
        return (Unknown(X-1, Y) // 2)"""

def Unknown(X, Y):
    Total = 1

    while X != Y:
        if X < Y:
            print(X + Y)
            X = X + 1
            Total = Total * 2
        else:
            print(X+Y)
            X = X - 1
            Total = int(Total/2)

    return Total

print('For 10 and 15')
print(Unknown(10, 15))
print('')

print('For 10 and 10')
print(Unknown(10, 10))
print('')

print('For 15 and 10')
print(Unknown(15, 10))