from tkinter import *

window = Tk()
window.title("Simple interest calculator")
window.geometry("400x400")
window.configure(bg="lightcyan")

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t) / 100
    interest = round(i,2)
    message=Label(result_frame,text="Interest is."+str(p)+"at rate of interest"+str(r)+"M for"+str(t)+" years is Rs."+str(interest),bg="lightcyan",font=("Calibri",12),width=55)
    message.place(x=20,y=40)
    message.pack()

heading_label = Label(window,text="Simple interest calculator",fg="black",bg="lightcyan",font=("Calibri",20),bd=5)
heading_label.place(x=50,y=20)

principle = Label(window,text="Principle",fg="black",bg="lightcyan",font=("Calibri",12),bd=1)
principle.place(x=20,y=90)

principle_entry = Entry(window,text="",bd=2,width=15)
principle_entry.place(x=150,y=92)

rate = Label(window,text="Rate of Interest",fg="black",bg="lightcyan",font=("Calibri",12),bd=1)
rate.place(x=20,y=140)

roi_entry = Entry(window,text="",bd=2,width=15)
roi_entry.place(x=20,y=140)

time = Label(window,text="Time",fg="black",bg="lightcyan",font=("Calibri",12))
time.place(x=150,y=187)

time_entry = Entry(window,text="",bd=2,width=15)
time_entry.place(x=150,y=142)

calculate_button = Button(window,text="Calculate",fg="black",bg="cyan",bd=4,command=calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result",bg="grey",font=("Calibri",12))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

show_label = Label(result_frame,text="Your result will be displayed here",bg="lightcyan",font=("Calibri",12),width=55)
show_label.place(x=20,y=20)
show_label.pack()

show_label.destroy()
