import tkinter as tk
import random as r

#bandeau de couleurs
couleurs = ["black"]
bandeau = [0,0,0,0,0,0,0,0,0,0]
coord = []

#pencil
pen = "white"

#events
#pencils change
def pen_purple() :
    global pen
    pen = "purple"
    
def pen_blue() :
    global pen
    pen = "blue"
    
def pen_red() :
    global pen
    pen = "red"


#clicks/bind event
def callclick(event) :
    for c in coord :
        if c[0]<event.x<=c[1] :
            canvas.create_rectangle(c[0],0,c[1],100,fill=pen)

#creation de fenetre
window = tk.Tk()
window.title("Bandeau de couleurs")

#canvas
canvas = tk.Canvas(window,width = 900,height = 100)
canvas.pack()

#buttons
frame1 = tk.Frame(window,borderwidth=2)
frame1.pack(side="top", fill="both", ipadx=10, ipady=10, expand=0)

#creation du bandeau
def create_bandeau(list) :
    x=0
    for i in range(len(list)) :
        x1 = x
        x2 = x+100
        canvas.create_rectangle(x1,0,x2,100, fill=couleurs[list[i]],outline="black")
        coord.append((x1,x2))
        x+=100 

create_bandeau(bandeau)

def reset_btn_callback():
    create_bandeau(bandeau)

violet_button = tk.Button(window,text="reset", command=reset_btn_callback).pack(side="left", padx=10, pady=10)

violet_button = tk.Button(window,text="violet", command=pen_purple).pack(side="right", padx=10, pady=10)
blue_button = tk.Button(window,text="bleu", command=pen_blue).pack(side="right", padx=10, pady=10)
rouge_button = tk.Button(window,text="rouge", command=pen_red).pack(side="right", padx=10, pady=10)

#attribution des events 
canvas.bind("<Button-1>", callclick) 

#affiche de la fenetre
window.mainloop()
