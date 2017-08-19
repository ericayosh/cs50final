import cs50 

def check(cardType, length, one_numbers, two_numbers, four_numbers):
    if cardType == "American":
        if length != 15:
            return False
        if two_numbers != 34 and two_numbers != 37:
            return False
    elif cardType == "Mastercard":
        if length != 16:
            return False
        if two_numbers != 51 and two_numbers != 52 and two_numbers != 53 and two_numbers != 54 and two_numbers != 55:
            return False
    elif cardType == "Visa":
        if length != 16 and length !=13:
            return False
        if one_numbers != 4:
            return False
    else:
    # discover  cardType == "Discover":
        if length != 16:
            return False
        if four_numbers != 6011 and two_numbers != 37:
            return False
    
    return True


def Luhn(Account):
# take a string input called account, and returns a boolean True or False #

    # reverse the order
    Account = Account[::-1]
    
    #turn the string into a list
    digits = [int(x) for x in Account]
    # keep to original last digit of the account as the check digit
    check_digit = digits[0]
    #turn the first digit (really the last digit in the account) to 0.
    digits[0] = 0
    
    #tranform every other digit in the account number, if doubling the digit makes it greater than 9 subtract 9
    even_total  = 0
    for digit in digits[1::2]:
        new_digit = int(digit)*2
        if int(new_digit) > 9: 
            new_digit = new_digit - 9
        even_total = even_total + new_digit

    odd_total= 0     
    # sum the even numbers in the card number    
    for digit in digits[2::2]:
        odd_total = odd_total+ int(digit)

    # sum the tranformed even numbers and add the odd numbers, multiply by 9 and mod 10.
    total = ((even_total+odd_total)*9)%10
    print("total: {}, check digit : {}".format(total, check_digit) ) 

    # if the check digit does not match the results of the algorithm return false, the card is not valid
    # if the check digit matches the results return valid
    if check_digit == total:
        return True
    else:
        return False