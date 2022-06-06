from tkinter import *

#criar a janela/window
janela = Tk()
janela.geometry('400x167+90+90')
janela.config(background='#B0C4DE')

#criar a função
def IMC():
    if entry1.get().replace('.', '', 1).isnumeric() and entry2.get().replace('.', '', 1).isnumeric():
        label3['text'] = float(entry1.get()) / (float(entry2.get())**2)
    else:
        label3['text'] = 'Valor Invalido!'

#criar os widgets
frame1 = Frame(janela, background='#87CEEB', pady=8, padx=8)
frame2 = Frame(janela, background='#B0C4DE', pady=8, padx=8)
label1 = Label(frame1, text='Peso:', font='Arial 15', background='#87CEEB')
label2 = Label(frame1, text='Altura:', font='Arial 15', background='#87CEEB')
label3 = Label(frame2, text='', font='Arial 16', background='#B0C4DE')
entry1 = Entry(frame1, font='Arial 15')
entry2 = Entry(frame1, font='Arial 15')
btn1 = Button(frame2, text='IMC', font='Arial 17', background='#6495ED', command=IMC)

#organizar os widgets/layout
frame1.pack()
frame2.pack()
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
btn1.grid(row=4, column=0)
label3.grid(row=5, column=0)

#executar a janela
janela.mainloop()