from tkinter import *
import secrets

root = Tk()
root.title("Dice Roller")


def rollD4():
    generator = secrets.SystemRandom()
    result = generator.randrange(1, 5)

    for child in resultFrame.winfo_children():
        child.destroy()
    resultLbl = Label(resultFrame, text=result)
    resultLbl.pack(fill=X)


def rollD6():
    generator = secrets.SystemRandom()
    result = generator.randrange(1, 7)

    for child in resultFrame.winfo_children():
        child.destroy()
    resultLbl = Label(resultFrame, text=result)
    resultLbl.pack(fill=X)


def rollD8():
    generator = secrets.SystemRandom()
    result = generator.randrange(1, 9)

    for child in resultFrame.winfo_children():
        child.destroy()
    resultLbl = Label(resultFrame, text=result)
    resultLbl.pack(fill=X)


def rollD10():
    generator = secrets.SystemRandom()
    result = generator.randrange(1, 11)

    for child in resultFrame.winfo_children():
        child.destroy()
    resultLbl = Label(resultFrame, text=result)
    resultLbl.pack(fill=X)


def rollD12():
    generator = secrets.SystemRandom()
    result = generator.randrange(1, 13)

    for child in resultFrame.winfo_children():
        child.destroy()
    resultLbl = Label(resultFrame, text=result)
    resultLbl.pack(fill=X)


def rollD20():
    generator = secrets.SystemRandom()
    result = generator.randrange(1, 21)

    for child in resultFrame.winfo_children():
        child.destroy()
    resultLbl = Label(resultFrame, text=result)
    resultLbl.pack(fill=X)

# Frame Setup


titleFrame = Frame(root)
buttonFrame = Frame(root)
resultFrame = Frame(root)

titleFrame.pack(side=TOP)
buttonFrame.pack()
resultFrame.pack(fill=X)

# Frame 1 - Title

title = Label(titleFrame, text="Dice Roller", font=('Helvetica', 10, 'bold'))
title.pack(pady=10, padx=10)

# Frame 2 - Buttons

D4 = Button(buttonFrame, text="Roll D4", bg="green", command=rollD4)
D6 = Button(buttonFrame, text="Roll D6", bg="gainsboro", command=rollD6)
D8 = Button(buttonFrame, text="Roll D8", bg="gainsboro", command=rollD8)
D10 = Button(buttonFrame, text="Roll D10", bg="gainsboro", command=rollD10)
D12 = Button(buttonFrame, text="Roll D12", bg="gainsboro", command=rollD12)
D20 = Button(buttonFrame, text="Roll D20", bg="gainsboro", command=rollD20)

D4.grid(row=0, column=0, padx=5, pady=5)
D6.grid(row=0, column=1, padx=5, pady=5)
D8.grid(row=0, column=2, padx=5, pady=5)
D10.grid(row=1, column=0, padx=5, pady=5)
D12.grid(row=1, column=1, padx=5, pady=5)
D20.grid(row=1, column=2, padx=5, pady=5)


# Frame 3 - Result

root.mainloop()