from tkinter import *
from tkinter import ttk
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator

def read_text_x():
    global x
    x = int(entx.get())
    return(x)

def read_text_y():
    global y
    y = int(enty.get())
    return(y)

def read_text_else():
    global R, i_sh, o_sh
    R = int(entrad.get())
    i_sh = int(entin.get())
    o_sh = int(entout.get())
def selected():
    global reg
    reg = int(number.get())
    return(reg)
def directory():
    global d
    d = str(file.get())
    return(d)
def graph():
    try:
        photo = pyfits.open(d)
        scidata = photo[0].data
        if reg == 1:
            for i in range(x-R,x+R+1):
                xc.append(i)
                data_x.append(scidata[y-1][i-1])
            plt.figure()
            plt.plot(xc, data_x)
            plt.xlabel("coordinate")
            plt.ylabel("flux")
            plt.title("grafic X")
            plt.show()
            xc.clear()
            data_x.clear()
        elif reg == 2:
            for i in range(y-R,y+R+1):
                yc.append(i)
                data_y.append(scidata[i - 1][x - 1])
            plt.figure()
            plt.plot(yc, data_y)
            plt.xlabel("coordinate")
            plt.ylabel("flux")
            plt.title("grafic Y")
            plt.show()
            yc.clear()
            data_y.clear()
        elif reg == 3:
            A = np.arange(x - R, x + R + 1, 1)
            B = np.arange(y - R, y + R + 1, 1)
            A, B = np.meshgrid(A,B)
            X = np.arange(x-R,x+R+1, 1)
            Y = np.arange(y-R, y+R+1, 1)
            Z = np.zeros([len(X),len(Y)])
            a = X[0]
            b = Y[0]
            for i in range(len(Y)):
                b += 1
                a = X[0]
                for j in range(len(X)):
                    Z[i][j]=scidata[b - 2][a - 1]
                    a +=1
            fig = (plt.figure())
            ax = fig.add_subplot(projection='3d')
            surf = ax.plot_surface(A, B, Z, cmap=cm.plasma)
            ax.set_xlabel('Номер пикселя')
            ax.set_ylabel('Номер пикселя')
            ax.set_zlabel('Изменение энергии')
            plt.title('Профиль 3d')
            fig.colorbar(surf, shrink=0.5, aspect=2)
            plt.show()
    except NameError:
        lbl_Er["text"] = 'Вставьте в поле директорию\n к вашему файлу!'
def Energy():
    try:
        photo = pyfits.open(d)
        scidata = photo[0].data
        global Energ
        global lbl_En
        global entout
        global entin
        x = int(entx.get())
        y = int(enty.get())
        r = int(entrad.get())
        R1 = int(entin.get())
        R2 = int(entout.get())
        R = abs(R2 - R1)

        count_1 =0
        Sum = 0
        count = 0
        Noise = 0
        Energ = 0

        exp = float(photo[0].header['exptime'])

        for i in range(x - r, x + r):
            for j in range(y - r, y + r):
                if (i-x)**2 + (j-y)**2 <= r**2:
                    Sum += scidata[j][i]
                    count_1 +=1
        Sum = float(Sum) / exp

        for i in range(x-R2, x+R2):
            for j in range(y-R2, y+R2):
                if (r ** 2 < (i - x) ** 2 + (j - y) ** 2) and ((i - x) ** 2 + (j - y) ** 2 <= R2 ** 2):
                    count += 1
                    Noise += scidata[j][i]

        Noise = float(Noise) / (count * exp)
        Energ = Sum - Noise*count_1
        lbl_En["text"] = Energ

    except NameError:
        lbl_Er["text"] = 'Вставьте в поле директорию\n к вашему файлу!!'
    except ValueError:
        lbl_Er["text"] = 'Заполните пустые поля!'

xc = []
yc = []
data_x = []
data_y = []
x = 0
y = 0
R = 0
i_sh = 0
o_sh = 0
reg = 0

root = Tk()
root.title('Astrocalc')
root.geometry('850x500')
root.resizable(False, False)
photo = pyfits.open('v523cas60s-001(1).fit')

for c in range(10):
    root.columnconfigure(index=c)
for r in range(10):
    root.rowconfigure(index=r)

title = ttk.Label(text = 'ASTROCALC', background='black', foreground='white')
title.grid(row=0, column=2, columnspan=2,ipady=10,padx=5, pady=5)

coord_x = ttk.Label(text = 'Введите координату <x>')
coord_y = ttk.Label(text = 'Введите координату <y>')
coord_x.grid(row=1, column=1)
coord_y.grid(row=1, column=4)

entx = ttk.Entry()
enty = ttk.Entry()
entx.grid(row=2, column=1)
enty.grid(row=2, column=4)

btnx = ttk.Button(text='Ввод коорд. х', command=read_text_x)
btny = ttk.Button(text='Ввод коорд. у', command=read_text_y)
btnx.grid(row=3, column=1)
btny.grid(row=3, column=4)

rad = ttk.Label(text = 'Введите радиус звезды')
entrad = ttk.Entry()


out = ttk.Label(text = 'Введитe внешний фон')
entout = ttk.Entry()


IN = ttk.Label(text = 'Введитe внтренний фон')
entin = ttk.Entry()


rad.grid(row=4, column=1, pady=10, padx=5)
entrad.grid(row=4, column=2, pady=10, padx=5)


out.grid(row=5, column=1, pady=10, padx=5)
entout.grid(row=5, column=2, pady=10, padx=5)


IN.grid(row=6, column=1, pady=10, padx=5)
entin.grid(row=6, column=2, pady=10, padx=5)

btn_else = ttk.Button(text='Ввод данных звезды', command=read_text_else)
btn_else.grid(row=5, column=3)

file_text = ttk.Label(text = 'Введитe путь к файлу')
file_text.grid(row=7, column=2)

file = ttk.Entry()
file.grid(row=7, column=3)

btn_file= ttk.Button(text='Ввод директории', command=directory)
btn_file.grid(row=7, column=4)

radio = ttk.Label(text = 'Выберите что хотите построить')
radio.grid(row=8, column=3)

number = StringVar(value='0')
rdbtn1 = ttk.Radiobutton(text='График по Х', value=1, variable=number, command=selected)
rdbtn2 = ttk.Radiobutton(text='График по Y', value=2, variable=number, command=selected)
rdbtn3 = ttk.Radiobutton(text='Трехмерный график', value=3, variable=number, command=selected)

rdbtn1.grid(row=9, column=1)
rdbtn2.grid(row=9, column=3)
rdbtn3.grid(row=9, column=5)

btn_graph = ttk.Button(text='построить', command=graph)
btn_graph.grid(row=10, column=3)

btn_En = ttk.Button(text="Энергия звезды", command=Energy)
btn_En.grid(row=5, column=5)

lbl_En = ttk.Label()
lbl_En.grid(row=6, column=5)

lbl_Er = ttk.Label(foreground='red')
lbl_Er.grid(row=11, column=3)

root.mainloop()
#C:\Users\Anton\first_project\venv\v523cas60s-001(1).fit