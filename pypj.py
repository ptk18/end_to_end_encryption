from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import base64

class End_to_End_Encryption:
    def __init__(self):
        #super().__init__()
        #create window
        window = tk.Tk()
        window.title("End-To-End Encryption")
        window.maxsize(730,410)
        window.minsize(730,410)
        window.config(bg="#BCDFE4")

        #create left_frame 
        left_frame = Frame(window, width=200,height=400,bg="#F5F5F5",bd=2)
        left_frame.grid(row=0,column=0,padx=20,pady=20)

        #create right_frame 
        right_frame = Frame(window, width=650,height=400,bg="#F5F5F5")
        right_frame.grid(row=0,column=1,padx=20,pady=20)

        #create frames and label in the left_frame
        reset_bt= Button(left_frame,text="RESET",font=("Roboto", 10,"bold"),bg="#BCDFE4",command=self.reset)
        reset_bt.grid(row=1,column=0,padx=10, pady=10, sticky=NSEW)


        middle_frame=Frame(left_frame,width=180)
        middle_frame.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)
        Label(middle_frame, text="Enter Secrect Code",font=("Roboto", 10)).grid(row=0,column=0,padx=5, pady=2.5,sticky=NSEW)
        self.secrect_code = StringVar()
        self.sec_cdEntry = Entry(middle_frame,textvariable=self.secrect_code,show="*")
        self.sec_cdEntry.grid(row=1,column=0,padx=5, pady=2.5,sticky=NSEW)
       # print(self.secrect_code.get())


        #create frame within left_frame
        tool_bar= Frame(left_frame,width=180, height=185,bg="white")
        tool_bar.grid(row=3,column=0,padx=10,pady=10,sticky=NSEW)

        self.enp_dep_btn=Button(tool_bar,text="ENCRYPT-DECRYPT",)
        self.enp_dep_btn.grid(row=0,column=0,padx=5,pady=10,sticky=NSEW)
        self.dec_bn_btn=Button(tool_bar,text="DECIMAL-BINARY",command=self.Decimal_Binary)
        self.dec_bn_btn.grid(row=1,column=0,padx=5,pady=10,sticky=NSEW)
        self.dec_hex_btn=Button(tool_bar,text="DECIMAL-HEXADECIMAL",command=self.Decimal_Hexa)
        self.dec_hex_btn.grid(row=2,column=0,padx=5,pady=10,sticky=EW)
        self.txt_ms_btn=Button(tool_bar,text="TEXT-MORSE CODE",command=self.Txt_Morse)
        self.txt_ms_btn.grid(row=3,column=0,padx=5,pady=10,sticky=NSEW)


        #Right Frame
        display_frame=Frame(right_frame,width=600,height=300,bg="#F5F5F5")
        display_frame.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        Label(display_frame,text="Enter Your Text Below",bg="#F5F5F5",font=("Roboto", 15)).grid(row=0,column=0,padx=5,pady=5,sticky=W)

        self.text_area = scrolledtext.ScrolledText(display_frame,width=47, height=14,font=("Roboto", 12))
        self.text_area.grid(row=1,column=0,padx=5,pady=5)

        Button(right_frame,text="ENCRYPT",fg="black",command=self.processEncrypt).grid(row=2,column=0,padx=10,pady=5,sticky=NSEW)
        Button(right_frame,text="DECRYPT",command=self.processDecrypt).grid(row=2,column=1,padx=10,pady=5,sticky=NSEW)

        #there will be warning dialog box for worng password
        self.active_btn=self.enp_dep_btn
        self.enp_dep_btn.bind("<Enter>", self.on_enter)
        self.enp_dep_btn.bind("<Leave>", self.on_leave)


        window.mainloop()

    def processEncrypt(self):
        self.active_btn = self.enp_dep_btn
        self.clicked(self.active_btn)
        password = self.sec_cdEntry.get()
        if password == "ptk":
            newWindow1 = Tk()
            newWindow1.geometry("300x180")
            newWindow1.title("Encryption")
            Label(newWindow1,text="ENCRYPTION",bg="#BCDFE4",justify=LEFT,font=("Roboto", 12)).grid(row=0,column=0,sticky=NSEW)
            text=Text(newWindow1,height=10,width=38)
            text.grid(row=1,column=0)
            print(self.text_area.get("1.0",'end-1c'))
            encode_msg = self.text_area.get("1.0",'end-1c').encode("ascii")
            base64_bytes = base64.b64encode(encode_msg)
            encrypt = base64_bytes.decode("ascii")
            text.insert(END,encrypt)
            newWindow1.grab_set()
        
        elif password == "":
            messagebox.showerror("encryption","Enter Password")
        
        else:
            messagebox.showerror("encryption","Invalid Password")
        

    def processDecrypt(self):
        self.active_btn = self.enp_dep_btn
        self.clicked(self.active_btn)
        password = self.sec_cdEntry.get()
        if password == "ptk":
            newWindow2 = Tk()
            newWindow2.geometry("300x180")
            newWindow2.title("Decryption")
            Label(newWindow2,text="DECRYPTION",bg="#BCDFE4",justify=LEFT,font=("Roboto", 12)).grid(row=0,column=0,sticky=NSEW)
            text=Text(newWindow2,height=10,width=38)
            text.grid(row=1,column=0)
            print(self.text_area.get("1.0",'end-1c'))
            decode_msg = self.text_area.get("1.0",'end-1c').encode("ascii")
            base64_bytes = base64.b64decode(decode_msg)
            decrypt = base64_bytes.decode("ascii")
            text.insert(END,decrypt)
            newWindow2.grab_set()
          
        elif password == "":
            messagebox.showerror("decryption","Enter Password")
        
        else:
            messagebox.showerror("decryption","Invalid Password")

#____________Decimal_Binray_______________#
    def Decimal_Binary(self):
        self.active_btn = self.dec_bn_btn
        self.clicked(self.active_btn)
        password = self.sec_cdEntry.get()
        if password == "ptk":
            newWindow3 = Tk()
            newWindow3.geometry("300x180")
            newWindow3.title("Dec-Bin")
            Label(newWindow3,text="Decimal To Binary",bg="#BCDFE4",justify=LEFT,font=("Roboto", 12)).grid(row=0,column=0,sticky=NSEW)
            text=Text(newWindow3,height=10,width=38)
            text.grid(row=1,column=0)

            try:
                num=int(self.text_area.get("1.0",'end-1c'))
                binary = self.Dec_Bin_helper(num)
                text.insert(END,binary)
                newWindow3.grab_set()
            except:
                raise TypeError

        elif password == "":
            messagebox.showerror("Dec-Bin","Enter Password")
        
        else:
            messagebox.showerror("Dec-Bin","Invalid Password")

    def Dec_Bin_helper(self,num):
        if num <=1 :
            return num
        else:
            temp = num//2
            return f"{self.Dec_Bin_helper(temp)}" + f"{num%2}"

#____________Decimal_Hexa_______________#
            
    def Decimal_Hexa(self):
        self.active_btn = self.dec_hex_btn
        self.clicked(self.active_btn)
        password = self.sec_cdEntry.get()
        if password == "ptk":
            newWindow4 = Tk()
            newWindow4.geometry("300x180")
            newWindow4.title("Dec-Hexa")
            Label(newWindow4,text="Decimal To Hexadecimal",bg="#BCDFE4",justify=LEFT,font=("Roboto", 12)).grid(row=0,column=0,sticky=NSEW)
            text=Text(newWindow4,height=10,width=38)
            text.grid(row=1,column=0)

            try:
                num=int(self.text_area.get("1.0",'end-1c'))
                hexa = self.Dec_Hexa_helper(num)
                text.insert(END,hexa)
                newWindow4.grab_set()
            except:
                raise TypeError

        elif password == "":
            messagebox.showerror("Dec-Hexa","Enter Password")
        
        else:
            messagebox.showerror("Dec-Hexa","Invalid Password")

    def Dec_Hexa_helper(self,num):
        conversion_table =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        if num <= 0:
            return num
        
        reminder = num%16
        return f"{self.Dec_Hexa_helper(num//16)}" + conversion_table[reminder]

#_______________Text-Morse Code_____________#
    def Txt_Morse(self):
        
        self.active_btn = self.txt_ms_btn
        self.clicked(self.active_btn)
        password = self.sec_cdEntry.get()
        if password == "ptk":
            newWindow5 = Tk()
            newWindow5.geometry("300x180")
            newWindow5.title("Text-Morse")
            Label(newWindow5,text="Text To Morse Code",bg="#BCDFE4",justify=LEFT,font=("Roboto", 12)).grid(row=0,column=0,sticky=NSEW)
            text=Text(newWindow5,height=10,width=38)
            text.grid(row=1,column=0)

            message=self.text_area.get("1.0",'end-1c')
            morse = self.Txt_Morse_helper(message.upper())
            text.insert(END,morse)
            newWindow5.grab_set()
        

        elif password == "":
            messagebox.showerror("Text-Morse","Enter Password")
        
        else:
            messagebox.showerror("Text-Morse","Invalid Password")

    def Txt_Morse_helper(self,message):
        # Dictionary representing the morse code chart
        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}
        morse = ''
        for letter in message:
            if letter != ' ':
                morse += MORSE_CODE_DICT[letter] + ' '
            else:
                morse += ' '
        return morse
 
#-----------------Reset Func-------------------#
    def reset(self):
        '''self.secrect_code.set("sth here")'''
        #print(self.secrect_code.get())
        self.sec_cdEntry.delete(0,END)
        self.text_area.delete(1.0,END)

    def on_enter(self,e):
        self.active_btn['background'] = '#BCDFE4'

    def on_leave(self,e):
        self.active_btn['background'] = 'SystemButtonFace'

    def clicked(self,e):
        self.active_btn.configure(bg="#BCDFE4")
        

End_to_End_Encryption()
