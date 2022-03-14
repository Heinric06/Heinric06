from pydoc import text


def encrypt(string,a):
    cipher =''
    for i in string:
        if i == '':
            cipher=cipher+i
        elif i.isupper():
            cipher=cipher+chr((ord(i)+a-65)% 26+ 65)
        else: 
            cipher=cipher+chr((ord(i)+a-97)% 26+ 97)
    return cipher


text = input("enter some text:")
a = int(input("enter number:"))
print(text)
print(encrypt(text,a))