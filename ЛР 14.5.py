import tkinter
import math
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

html_template1 = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Текст в формате html</h2>
<p>
"""
html_template2 = """.</p>
</body>
</html>
"""
def saveastxt():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
        window.title('Калькулятор - ' + path + ".txt")
    except:
        return
    with open(path + ".txt", 'w') as f:
        f.write("Результат вычислений = "+str(label3.cget("text")))
        f.close()

def saveashtml():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
        window.title('Калькулятор - ' + path + ".html")
    except:
        return
    with open(path + ".html", 'w') as f:
        f.write(html_template1)
        f.write("Результат вычислений = "+str(label3.cget("text")))
        f.write(html_template2)
        f.close()

def but1():

    if entry1.get().isdigit():
        r = float(entry1.get())
        try:
            vol = ((r * r * r) * (math.pi) * 4) / 3
            label4.config(text=(vol))
        except:
            label4.config(text="Ошибка, некорректный ввод!")
    else:
        label4.config(text="Ошибка, некорректный ввод!")

def but2():
    selection = comboExample.get()
    if selection=="Сохранить в txt":
        saveastxt()
    else :
        saveashtml()



window = tkinter.Tk()
window.geometry("400x250")
window.title("Editor")

label1 = tkinter.Label(window, text='Введите радиус:')
label1.place(x=15, y=8, width=100, height=50)

entry1 = tkinter.Entry(width=30, borderwidth=2, relief="solid")
entry1.place(x=170, y=20, width=200, height=25)

label3 = tkinter.Label(window, text='Результат вычислений:')
label3.place(x=10, y=48, width=150, height=50)

label4 = tkinter.Label(width=30, borderwidth=2, relief="solid")
label4.place(x=170, y=60, width=200, height=25)

button1 = Button(text="Вычислить", font=('Coutier', 9, 'bold italic'), command=but1)
button1.place(x=100, y=100, width=150, height=30)

button2 = Button(text="Сохранить", font=('Coutier', 9, 'bold italic'), command=but2)
button2.place(x=0, y=170, width=150, height=30)

comboExample = ttk.Combobox(window,
                            values=[
                                    "Сохранить в txt",
                                    "Сохранить в html"])
comboExample.place(x=180, y=170, width=150, height=30)
comboExample.current(1)


window.mainloop()