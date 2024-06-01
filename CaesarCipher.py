def e(text, shift):
    ans = ''
    for alphabet in range(len(text)):
        x = text[alphabet]
        if x.isupper():
            ans += chr((ord(x) + shift - 65) % 26 + 65)
        elif x.islower():
            ans += chr((ord(x) + shift - 97) % 26 + 97)
        else:
            ans += x  
    return ans 

def d(text, shift):
    return e(text, -shift)

def  CaesarCipher():
    try:
        choice = int(input('Enter 1 for encryption and 2 for decryption:'))
        if choice != 1 and choice != 2:
            print('Error:Only enter either 1 or 2!')
            return
    except:
        print('Error:Enter only digits!')
        return

    text = input('Enter your text: ')

    try:
        shift = int(input('Enter your Shift (between 0 to 25):'))
        if shift > 25 or shift < 0:
            print('Error:Only enter shift between 0 to 25!')
            return
    except:
        print('Error:Only enter "Digit" value!')
        return

    if choice == 1:
        print(f'Encrypted text:{e(text, shift)}')
    else:
        print(f'Decrypted text:{d(text, shift)}')

CaesarCipher()
