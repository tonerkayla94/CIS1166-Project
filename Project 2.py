def Detect(codewords):
    bits = split(codewords)
    parityBits = ""
    '''check P4 first:'''
    P4 = int(bits[3])
    D5 = int(bits[2])
    D6 = int(bits[1])
    D7 = int(bits[0])
    if((P4 + D5 + D6 + D7) % 2 == 1):
        parityBits += "1"
    else:
        parityBits += "0"

    '''check P2 second:'''
    P2 = int(bits[5])
    D3 = int(bits[4])

    if((P2 + D3 + D6 + D7) % 2 == 1):
        parityBits += "1"
    else:
        parityBits += "0"


    '''check P1 last:'''
    P1 = int(bits[6])

    if((P1 + D3 + D5 + D7) % 2 == 1):
        parityBits += "1"
    else:
        parityBits += "0"


    if(parityBits == "000"):
        return "correct codeword recieved"

    errorBit = binaryToDecimal(int(parityBits))

    if(errorBit == 3):
        if(D3 == '0'):
            bits[4] = '1'
        else:
            bits[4] = '0'

    elif(errorBit == 5):
        if (D5 == '0'):
            bits[2] = '1'
        else:
            bits[2] = '0'

    elif(errorBit == 6):
        if (D6 == '0'):
            bits[1] = '1'
        else:
            bits[1] = '0'

    elif(errorBit == 7):
        if (D7 == '0'):
            bits[0] = '1'
        else:
            bits[0] = '0'

    correctCodeword = ''.join(bits)
    return correctCodeword

def split(codeword):
    return [char for char in str(codeword)]

def binaryToDecimal(binary):
    binaryDigits = split(binary)
    decimal = 0

    for i in range(len(binaryDigits)):
        digit = binaryDigits.pop()
        if (digit == '1'):
           decimal = decimal + pow(2,i)
    return decimal

if __name__ == '__main__':
    userBinaryCode = str(input("enter received 7-bit Hamming Code with even parity. \n"))
    while(len(userBinaryCode)!= 7):
        userBinaryCode = input("user error. enter received 7-bit Hamming Code with even parity. ")
    print("code sent was: " + Detect(userBinaryCode))