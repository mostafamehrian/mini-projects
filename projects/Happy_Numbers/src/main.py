def is_happy(n : int) -> bool:
    '''
    a func that is check number tath is the number happy or not 
    
    :param n: input number
    
    :return: true if number is happy false if is not
    
    '''
    seen = set()
    while (n != 1) and (n not in seen):
        seen.add(n)
        n = sum([int(i) **2 for i in str(n)])
        
    if n == 1:
        print("number is happy number")
    else:
        print(" number is not happy")

if __name__=="__main__":
    # assert is_happy(7) is True
    # assert is_happy(45) is False
    # assert is_happy(44) is True
    get_number = int(input("enter a number for checking is number is happ or not? "))
    is_happy(get_number)
    