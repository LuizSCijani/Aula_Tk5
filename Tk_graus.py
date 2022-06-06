from tkinter import *

#criar a janela/window
janela = Tk()
janela.config(background='#B0C4DE')

#criar a função
def Converte():
    if entry.get().isnumeric():
        label2['text'] = float(entry.get()) * 1.8 + 32
    else:
        label2['text'] = 'Valor Invalido!'

#criar os widgets
frame1 = Frame(janela, background='#87CEEB', pady=8, padx=8)
frame2 = Frame(janela, background='#B0C4DE', pady=8, padx=8)
label1 = Label(frame1, text='Cº', font='Arial 17', background='#87CEEB')
label2 = Label(frame2, text='', font='Arial 16', background='#B0C4DE')
entry = Entry(frame1, font='Arial 20')
btn = Button(frame2, text='Converte ºF', font='Arial 17', background='#6495ED', command=Converte)

#organizar os widgets/layout
frame1.pack()
frame2.pack()
label1.grid(row=0, column=0)
entry.grid(row=0, column=1)
btn.grid(row=0, column=0)
label2.grid(row=0, column=1)

#executar a janela
janela.mainloop()