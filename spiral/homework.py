def spiralize(number):
    n = (number-1)//2

    return (16*n*n*n+ 30*n*n+26*n+3)//3

