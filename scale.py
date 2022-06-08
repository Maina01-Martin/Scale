from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+"degrees C")


window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length =600,
              orient=VERTICAL,
              font=('Arial',25),
              tickinterval=10,
              resolution=5,
              fg="red",
              bg="dodgerblue")
scale.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()
