def spiralize(number):
    return_value = (number-1)//2

    return (16*return_value*return_value*return_value+ 30*return_value*return_value+26*return_value+3)//3

