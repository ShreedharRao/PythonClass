import customtkinter as ctk

app = ctk.CTk()
app. geometry("400x600")
app.title("Money Conversion")

app.configure(bg_color="white", fg_color="white")

convFrame = ctk.CTkFrame(app, width=350, height=80,
                         bg_color="white",
                         fg_color="grey")
convFrame.grid(row=0, column=0, padx=7, pady=7)

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
                       anchor="center", font=ctk.CTkFont(size=30))

btndel.grid(row=0, column=2, padx=2, pady=2)

btnDiv = ctk.CTkButton(btnFrame, width=75, height=65,
                       text="➗",
                       bg_color="white", fg_color="gray",
                       anchor="center", font=ctk.CTkFont(size=30))

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
                        anchor="center", font=ctk.CTkFont(size=30))

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
                       anchor="center", font=ctk.CTkFont(size=30))

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
                       anchor="center", font=ctk.CTkFont(size=30))

btnadd.grid(row=3, column=3, padx=2, pady=2)

btndouble = ctk.CTkButton(btnFrame, width=75, height=65,
                          text="+/-",
                          text_color="black", bg_color="white", fg_color="gray75",
                          anchor="center", font=ctk.CTkFont(size=30))
btndouble.grid(row=4, column=0, padx=2, pady=2)

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
                         anchor="center", font=ctk.CTkFont(size=30))

btnequal.grid(row=4, column=3, padx=2, pady=2)







app.mainloop()