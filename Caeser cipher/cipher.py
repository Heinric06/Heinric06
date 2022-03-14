from tkinter import *
from tkinter import messagebox

main = Tk()
main.title("Caesar cipher")
main.resizable(height = False, width = False)

def encrypt():
    
    a = 5
    string = text.get()
    cipher = ''
    for x in string:
        if x == '':
            cipher=cipher+ x
        elif x.isupper():
            cipher=cipher+chr((ord(x)+a-65)% 26+ 65)
        else: 
            cipher=cipher+chr((ord(x)+a-97)% 26+ 97)
    messagebox.showerror("complete",cipher )
    text.delete(0, "end")
    return cipher

label1 = Label(main, text="Please enter text to be encrypted")
label1.grid(row=1, column=1)
text = Entry(main)
text.grid(row=1, column=2)


# label1 = Label (main, text="Your text has been encypted.").grid(row=2, column=2)

# noteif = Label (main, text="Your encypted text is:").grid(row=5, column=3)
# noteif.config(fg="green", text="Account has been registered...")
btn = Button(main, text="Encrypt", command= encrypt)
btn.grid(row=2, column=1)




main.mainloop()


























# def encrypt(text,s):
#     result = ""
#    # transverse the plain text
#     for i in range(len(text)):
#         char = text[i]
#         # Encrypt uppercase characters in plain text
        
#         if (char.isupper()):
#             result += chr((ord(char) + s-65) % 26 + 65)
#         # Encrypt lowercase characters in plain text
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
#         return result
# #check the above function
# text = "CEASER CIPHER DEMO"
# s = 5

# print ("Plain Text : " + text)
# print ("Shift pattern : " + str(s))
# print ("Cipher: " + encrypt(text,s))

