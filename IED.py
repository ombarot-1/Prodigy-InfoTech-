import numpy as np
from PIL import Image

def ConvertRGB(img):
    try:
        return Image.open(img).convert('RGB')
    except FileNotFoundError:
        print('Error: Image not found!')
        exit(1)

def SaveImage(img, path):
    try:
        img.save(path)
    except Exception:
        print('Error: Could not save image.')
        exit(1)

def ImageToMatrix(img):
    return np.array(img)

def MatrixToImage(matrix):
    return Image.fromarray(matrix.astype('uint8'))

def EncryptedImg(matrix, key):
    EncryptedMatrix = (matrix + key) 
    return EncryptedMatrix

def DecryptedImg(matrix, key):
    DecryptedMatrix = (matrix - key) 
    return DecryptedMatrix

def get_valid_path():
    img_path = input('Enter the path of the image: ')
    img = ConvertRGB(img_path)
    if img is not None:
        return img
    else:
        print('Error: Image not found!')
        exit(1)

def get_valid_key():
    try:
        key = int(input('Enter your key (0-255): '))
        if 0 <= key <= 255:
            return key
        else:
            print('Error: Enter a number between 0 and 255!')
            exit(1)
    except ValueError:
        print('Error: Digits only allowed!')
        exit(1)

def get_valid_choice():
    try:
        choice = int(input('Enter 1 for Encryption or 2 for Decryption: '))
        if choice in [1, 2]:
            return choice
        else:
            print('Error: Enter either 1 or 2!')
            exit(1)
    except ValueError:
        print('Error: Digits only allowed!')
        exit(1)

def ImageEncryptDecrypt():
    choice = get_valid_choice()
    
    img = get_valid_path()
    key = get_valid_key()
    Matrix = ImageToMatrix(img)
    output_path = input('Enter the name for the saved image (include .png extension): ')

    if choice == 1:
        EncryptedMatrix = EncryptedImg(Matrix, key)
        RealImage = MatrixToImage(EncryptedMatrix)
    else:
        DecryptedMatrix = DecryptedImg(Matrix, key)
        RealImage = MatrixToImage(DecryptedMatrix)

    SaveImage(RealImage, output_path)
    print(f'Image saved as {output_path}')

ImageEncryptDecrypt()
