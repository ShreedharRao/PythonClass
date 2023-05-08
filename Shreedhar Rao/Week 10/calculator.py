import customtkinter as ctk

currentText = "0"
num = 0
op = ""
def addText(str):
    global currentText
    if float(currentText) == 0 and str != '.' and '.' not in currentText:
        currentText = ""
        currentText = currentText + str
    elif str == '.' and '.' in currentText:
        currentText = currentText
    else:
        currentText = currentText + str

    updateText()

def updateText():
    global currentText
    if len(currentText) ==0:
        currentText ="0"
    if len(currentText) > 12:
        currentText = currentText[:12]
    calcLabel.configure(text=currentText)

def performOperation():
    global currentText
    global num
    global op

    currentNum = float(currentText)

    if op == '+':
        result = num + currentNum
        currentText = str(result)
    if op == '-':
        result = num - currentNum
        currentText = str(result)
    if op == 'X':
        result = num * currentNum
        currentText = str(result)
    if op == '/':
        if currentNum == 0:
            currentText = "0"
        else:
            result = num / currentNum
            currentText = str(result)

    num = float(currentText)
    updateText()

def CE():
    global currentText
    global num
    global op
    currentText = "0"
    num = 0
    op = ""
    updateText()

def C():
    global currentText
    currentText = "0"
    updateText()

def Back():
    global currentText
    currentText = currentText[0:len(currentText)-1>0]
    updateText()

def plus_minus():
    global currentText
    if currentText =="0":
        return
    if '-' in currentText:
         currentText = currentText.replace('-', ' ')
    else:
        currentText = '-' + currentText
    updateText()

def operations(str):
    global currentText
    global num
    global op

    if op == "":
        num = float(currentText) #store current number
        currentText = "0" #doesn't show new number
    else:
        performOperation()

    if str != '=':
        op = str
        currentText = '0'
    else:
        op = "str"

app = ctk.CTk()
app.geometry("350x502")
app.title("Calculator")

app.configure(bg_color="white",
              fg_color="white")

calcFrame = ctk.CTkFrame(app, width=340, height=70,
                         bg_color="white",
                         fg_color="white")

calcFrame.grid(row=0, column=0, padx=5, pady=5)

calcLabel = ctk.CTkLabel(calcFrame, text="0", width=340, height=50,
                         anchor="ne",
                         bg_color="white", font=ctk.CTkFont(size=50))

calcLabel.grid(row=0, column=0, padx=2, pady=2)

btnFrame = ctk.CTkFrame(app, width=340, height=400,
                        bg_color="white",
                        fg_color="white")

btnFrame.grid(row=1, column=0, padx=5, pady=5)

# row = 0


btnCE = ctk.CTkButton(btnFrame, width=75, height=65,
                      text="CE",
                      bg_color="white", fg_color="gray",
                      anchor="center", font=ctk.CTkFont(size=30),
                      command= CE)

btnCE.grid(row=0, column=0, padx=2, pady=2)

btnC = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="C",
                     bg_color="white", fg_color="gray",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command= C)

btnC.grid(row=0, column=1, padx=2, pady=2)

btndel = ctk.CTkButton(btnFrame, width=75, height=65,
                       text="del",
                       bg_color="white", fg_color="gray",
                       anchor="center", font=ctk.CTkFont(size=30),
                       command=lambda: Back())

btndel.grid(row=0, column=2, padx=2, pady=2)

btnDiv = ctk.CTkButton(btnFrame, width=75, height=65,
                       text="➗",
                       bg_color="white", fg_color="gray",
                       anchor="center", font=ctk.CTkFont(size=30),
                       command=lambda: operations('/'))

btnDiv.grid(row=0, column=3, padx=2, pady=2)

btn7 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="7",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("7"))

btn7.grid(row=1, column=0, padx=2, pady=2)

btn8 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="8",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("8"))

btn8.grid(row=1, column=1, padx=2, pady=2)

btn9 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="9",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("9"))

btn9.grid(row=1, column=2, padx=2, pady=2)

btnmult = ctk.CTkButton(btnFrame, width=75, height=65,
                        text="X",
                        bg_color="white", fg_color="gray",
                        anchor="center", font=ctk.CTkFont(size=30),
                       command=lambda: operations('X'))

btnmult.grid(row=1, column=3, padx=2, pady=2)

btn4 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="4",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("4"))

btn4.grid(row=2, column=0, padx=2, pady=2)

btn5 = ctk.CTkButton(btnFrame, width=75, height=65, text="5",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("5"))

btn5.grid(row=2, column=1, padx=2, pady=2)

btn6 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="6",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("6"))

btn6.grid(row=2, column=2, padx=2, pady=2)

btnsub = ctk.CTkButton(btnFrame, width=75, height=65,
                       text="-",
                       bg_color="white", fg_color="gray",
                       anchor="center", font=ctk.CTkFont(size=30),
                       command=lambda: operations('-'))

btnsub.grid(row=2, column=3, padx=2, pady=2)

btn1 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="1",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("1"))

btn1.grid(row=3, column=0, padx=2, pady=2)

btn2 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="2",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("2"))

btn2.grid(row=3, column=1, padx=2, pady=2)

btn3 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="3",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("3"))

btn3.grid(row=3, column=2, padx=2, pady=2)

btnadd = ctk.CTkButton(btnFrame, width=75, height=65,
                       text="+",
                       bg_color="white", fg_color="gray",
                       anchor="center", font=ctk.CTkFont(size=30),
                       command=lambda: operations('+'))

btnadd.grid(row=3, column=3, padx=2, pady=2)

btnplus_minus = ctk.CTkButton(btnFrame, width=75, height=65,
                          text="+/-",
                          text_color="black", bg_color="white", fg_color="gray75",
                          anchor="center", font=ctk.CTkFont(size=30),
                                command=lambda: plus_minus())
btnplus_minus.grid(row=4, column=0, padx=2, pady=2)

btn0 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="0",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("0"))

btn0.grid(row=4, column=1, padx=2, pady=2)

btnperiod = ctk.CTkButton(btnFrame, width=75, height=65,
                          text=".",
                          text_color="black", bg_color="white", fg_color="gray75",
                          anchor="center", font=ctk.CTkFont(size=30),
                          command=lambda: addText("."))

btnperiod.grid(row=4, column=2, padx=2, pady=2)

btnequal = ctk.CTkButton(btnFrame, width=75, height=65,
                         text="=",
                         bg_color="white", fg_color="gray",
                         anchor="center", font=ctk.CTkFont(size=30),
                       command=lambda: operations('='))

btnequal.grid(row=4, column=3, padx=2, pady=2)

app.mainloop()
