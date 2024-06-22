import time as AdolfHitler
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import keyboard
from pynput.mouse import Button,Controller
def change():
    global AdolfHitlerWork
    AdolfHitlerWork = not AdolfHitlerWork
    
AdolfHitlerWork = False

def auto():
    while True:
        if AdolfHitlerWork:
            mouse = Controller() # да блять какого хуя она не работает?*? :?()??
            mouse.press(Button.left)
            AdolfHitler.sleep(wow/1000)       
negry = Tk()
negry.title("Параметры автокликера")
negry.geometry("600x300")

def validate_numbers():
        num = ent.get()
        if num:
            if num.isdigit():
                lab4.config(
                    text="Подходит",
                    foreground="green",
                )
                return True
            else:
                lab4.config(
                    text="Дожно быть число",
                    foreground="red",
                )
                return False
        else:
            lab4.config(
                text="Поле не должно быть пустым!",
                foreground="red",
            )
            return False
            


lab1 = Label(negry, text="Aктивация автокликера на:", font="Arial 14")
lab2 =Label(negry,text="Итервал нажатия:", font="Arial 14")
lab3 =Label(negry,text="мс", font="Arial 14")
lab4 =ttk.Label(negry,text=" ",font="Arial 10" )
    
lab1.grid(row=1,column=1)
lab2.grid(row=2,column=1,pady=20)
lab3.grid(row=2, column=3,padx=3)
lab4.grid(row=3, column=2,padx=3)
    

def selected(event):
    sel =combobox.get()
    print (sel)
    keyboard.add_hotkey(f'{sel}', change)

def numb(event):
    global wow
    wow=int(ent.get())
    print (wow)
    


r = ('F1','F2','F3','F4','F5','F6','F7','F8')
var = StringVar(value=r[0])
combobox = ttk.Combobox(negry, textvariable = var)
combobox['values'] = r
combobox['state'] = 'readonly'
combobox.grid(row=1,column=2, padx=10)
combobox.bind("<<ComboboxSelected>>",selected)
    
    
        
ent = Entry(negry,width=20,bd=3,validatecommand=validate_numbers,validate="focus")
ent.grid(row =2, column=2,pady=20)
ent.bind("<FocusOut>",numb)




            
class button1:
    def text(event):
        if(validate_numbers()==True):
            messagebox.showinfo(title="Уведомление",message="Успешно изменено!")
            negry.destroy()
            auto()
        else:
            messagebox.showerror(title="Уведомление",message="Ошибка!")
    btn=ttk.Button(negry,text="Применить",width=30,)
    btn.bind("<Button-1>",text)
    btn.grid(row =4, column=2, padx=10, pady=5)








negry.mainloop()
 