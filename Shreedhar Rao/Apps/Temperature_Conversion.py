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
    #if len(currentText) > 0:
        #currentText="0"
    if len(currentText) > 12:
        currentText = (currentText[:12])
    ConvLabel.configure(text=currentText)

def Fahrenheit():
    global currentText
    F= int(currentText)*1
    currentText = str(F)
    updateText()

def Celsius():
    global currentText
    C= int(currentText)*1
    currentText = str(C)
    updateText()

def Kelvin():
    global currentText
    K= int(currentText)*1
    currentText = str(K)
    updateText()

app = ctk.CTk()
app.geometry("450x560")
app.title("Conversion Calculater")

app.configure(bg_color="white",
              fg_color="white")

ConvFrame = ctk.CTkFrame(app, width=340, height=70,
                         bg_color="white",
                         fg_color="white")

ConvFrame.grid(row=0, column=0, padx=5, pady=5)

ConvLabel = ctk.CTkLabel(ConvFrame, text="0", width=340, height=50,
                         anchor="ne",
                         bg_color="white", font=ctk.CTkFont(size=50))

ConvLabel.grid(row=0, column=0, padx=2, pady=2)

btnFrame = ctk.CTkFrame(app, width=340, height=400,
                        bg_color="white",
                        fg_color="white")

btnFrame.grid(row=1, column=0, padx=5, pady=5)

btndel = ctk.CTkButton(btnFrame, width=75, height=65,
                       text="del",
                       bg_color="white", fg_color="gray",
                       anchor="center", font=ctk.CTkFont(size=30))

btndel.grid(row=0, column=3, padx=2, pady=2)

btn7 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="7",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("7"))

btn7.grid(row=0, column=0, padx=2, pady=2)

btn8 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="8",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("8"))

btn8.grid(row=0, column=1, padx=2, pady=2)

btn9 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="9",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("9"))

btn9.grid(row=0, column=2, padx=2, pady=2)

btn4 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="4",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("4"))

btn4.grid(row=1, column=0, padx=2, pady=2)

btn5 = ctk.CTkButton(btnFrame, width=75, height=65, text="5",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("5"))

btn5.grid(row=1, column=1, padx=2, pady=2)

btn6 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="6",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("6"))

btn6.grid(row=1, column=2, padx=2, pady=2)

btn1 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="1",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("1"))

btn1.grid(row=2, column=0, padx=2, pady=2)

btn2 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="2",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("2"))

btn2.grid(row=2, column=1, padx=2, pady=2)

btn3 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="3",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("3"))

btn3.grid(row=2, column=2, padx=2, pady=2)

btn0 = ctk.CTkButton(btnFrame, width=75, height=65,
                     text="0",
                     text_color="black", bg_color="white", fg_color="gray75",
                     anchor="center", font=ctk.CTkFont(size=30),
                     command=lambda: addText("0"))

btn0.grid(row=3, column=1, padx=2, pady=2)

btnperiod = ctk.CTkButton(btnFrame, width=75, height=65,
                          text=".",
                          text_color="white", bg_color="white", fg_color="gray",
                          anchor="center", font=ctk.CTkFont(size=30),
                          command=lambda: addText("."))

btnperiod.grid(row=2, column=3, padx=2, pady=2)


btnFahrenheittC = ctk.CTkButton(btnFrame, width=75, height=65,
                        text="Fahrenheit to Celsius",
                        text_color="gold", fg_color="blue",
                        anchor="center", font=ctk.CTkFont(size=20),
                        command=lambda: ())
btnFahrenheittC.grid(row=5, column=0, padx=2, pady=2)

btnFahrenheittK = ctk.CTkButton(btnFrame, width=75, height=65,
                        text="Fahrenheit to Kevlin",
                        text_color="gold", fg_color="green",
                        anchor="center", font=ctk.CTkFont(size=20),
                        command=lambda: ())
btnFahrenheittK.grid(row=5, column=1, padx=2, pady=2)
btnCelsiustK = ctk.CTkButton(btnFrame, width=75, height=65,
                        text="Celsius",
                        text_color="gold", fg_color="green",
                        anchor="center", font=ctk.CTkFont(size=20),
                        command=lambda: ())
btnCelsiustK.grid(row=5, column=1, padx=2, pady=2)

btnKelvintF = ctk.CTkButton(btnFrame, width=75, height=65,
                        text="Kelvin to Fahrenheit",
                        text_color="white", fg_color="red",
                        anchor="center", font=ctk.CTkFont(size=20),
                        command=lambda: ())
btnKelvintF.grid(row=5, column=2, padx=2, pady=2)
btnKelvintC = ctk.CTkButton(btnFrame, width=75, height=65,
                        text="Kelvin to Celsius",
                        text_color="white", fg_color="red",
                        anchor="center", font=ctk.CTkFont(size=20),
                        command=lambda: ())
btnKelvintC.grid(row=6, column=2, padx=2, pady=2)


app.mainloop()