import tkinter as tk
import random
def play(u_ch):
    av_ch=["Rock", "Paper", "Scissors"]
    c_ch=random.choice(av_ch)
    if u_ch==c_ch:
        o="Both same, Round tie!"
    elif u_ch=="Rock":
        if c_ch=="Paper":
            o="Paper covers rock, Computer wins!"
        else:
            o="Rock smashes scissors, You win!"
    elif u_ch=="Paper":
        if c_ch=="Scissors":
            o="Paper covers rock, You win!"
        else:
            o="Scissors cuts paper, Computer wins!"
    elif u_ch=="Scissors":
        if c_ch=="Rock":
            o="Rock smashes scissors, Computer wins!"
        else:
            o="Scissors cuts paper, You win!"
    else:
        o="Error!"
    result=tk.Label(window, text=o)
    result.pack()
window=tk.Tk()
window.title("Rock Paper Scissors")
label=tk.Label(window, text="Choose your move:")
label.pack()
rock=tk.Button(window, text="Rock", width=20, command=lambda: play("Rock"))
rock.pack()
paper=tk.Button(window, text="Paper", width=20, command=lambda: play("Paper"))
paper.pack(pady=2)
scissors=tk.Button(window, text="Scissors", width=20, command=lambda: play("Scissors"))
scissors.pack()
window.mainloop()
