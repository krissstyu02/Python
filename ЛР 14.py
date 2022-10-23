import tkinter

def click1():
    tempfar = entry.get()
    ans= (float(tempfar)-32)/1.8
    label2.config(text =ans)

def click2():
    window.quit()

window = tkinter.Tk ()
label1 = tkinter.Label (window, text ='Температура в Фаренгейтах:')
label1.pack()
entry = tkinter.Entry (window)
entry.pack()
label2 = tkinter.Label(window)
label2.pack()
button1 = tkinter.Button (window, text ='Переобразовать', command =click1)
button1.pack()
button2 = tkinter.Button(window, text ='Выход', command =click2)
button2.pack()
window.mainloop()