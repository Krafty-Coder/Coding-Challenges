def subtract_sum(number):
    try:
        number in range(10, 10000)
    except:
        ValueError('Number is not in range')
        quit()
    for n in number:
        n += int(n)

    n -= number
    if n in range(10, 10000):
        print(n)
        return n

    print(n)
    return n

