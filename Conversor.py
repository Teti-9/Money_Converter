from tkinter import *
from tkinter import messagebox


def conversor():
    global currency
    global usd_label
    global eur_label
    global real_label
    USFlag = PhotoImage(
        file="directory/icons"
    )
    EUFlag = PhotoImage(
        file="directory/icons"
    )
    BRFlag = PhotoImage(
        file="directory/icons"
    )
    usd_label = IntVar()
    eur_label = IntVar()
    real_label = IntVar()
    currency = Toplevel(root)
    currency.title("Conversão")
    currency.geometry("350x310")
    currency.config(bg="white")

    l_1 = Label(
        currency,
        font=("SF Pro Text", 22),
        text="Conversor de Moeda",
        width=24,
        height=2,
        bg="#1968e6",
        fg="White",
    )
    l_1.pack()

    l_ustext = Label(
        currency,
        font=("SF Pro Text", 18),
        text="USD",
        width=20,
        bg="white",
        fg="black",
    )
    l_ustext.place(x=-70, y=90)

    l_usimg = Label(
        currency,
        image=USFlag,
        bg="white",
    )
    l_usimg.image = USFlag
    l_usimg.place(x=8, y=90)

    l_eutext = Label(
        currency,
        font=("SF Pro Text", 18),
        text="EUR",
        width=20,
        bg="white",
        fg="black",
    )
    l_eutext.place(x=-70, y=140)

    l_euimg = Label(
        currency,
        image=EUFlag,
        bg="white",
    )
    l_euimg.image = EUFlag
    l_euimg.place(x=8, y=140)

    l_realtext = Label(
        currency,
        font=("SF Pro Text", 18),
        text="REAL",
        width=20,
        bg="white",
        fg="black",
    )
    l_realtext.place(x=-67, y=190)

    l_brimg = Label(
        currency,
        image=BRFlag,
        bg="white",
    )
    l_brimg.image = BRFlag
    l_brimg.place(x=8, y=190)

    l_us = Label(
        currency,
        font=("SF Pro Text", 18),
        textvariable=usd_label,
        width=20,
        bg="white",
        fg="black",
    )
    l_us.place(x=115, y=90)

    l_eu = Label(
        currency,
        font=("SF Pro Text", 18),
        textvariable=eur_label,
        width=20,
        bg="white",
        fg="black",
    )
    l_eu.place(x=115, y=140)

    l_real = Label(
        currency,
        font=("SF Pro Text", 18),
        textvariable=real_label,
        width=20,
        bg="white",
        fg="black",
    )
    l_real.place(x=115, y=190)

    b_voltar = Button(
        currency,
        text="Voltar",
        font=("SF Pro Text", 20),
        width=24,
        height=1,
        bg="#1968e6",
        fg="White",
        command=voltar,
    )
    b_voltar.pack(side=BOTTOM)

    if e_coin.get() == "usd" or e_coin.get() == "USD" or e_coin.get() == "Usd":
        usd = float(e_value.get()) * 1
        usd_label.set(("{:.2f}".format(usd)))
        eur = float(e_value.get()) * 0.86
        eur_label.set(("{:.2f}".format(eur)))
        real = float(e_value.get()) * 5.61
        real_label.set(("{:.2f}".format(real)))
    elif e_coin.get() == "eur" or e_coin.get() == "EUR" or e_coin.get() == "Eur":
        usd = float(e_value.get()) * 1.17
        usd_label.set(("{:.2f}".format(usd)))
        eur = float(e_value.get()) * 1
        eur_label.set(("{:.2f}".format(eur)))
        real = float(e_value.get()) * 6.54
        real_label.set(("{:.2f}".format(real)))
    elif e_coin.get() == "real" or e_coin.get() == "REAL" or e_coin.get() == "Real":
        usd = float(e_value.get()) * 0.18
        usd_label.set(("{:.2f}".format(usd)))
        eur = float(e_value.get()) * 0.15
        eur_label.set(("{:.2f}".format(eur)))
        real = float(e_value.get()) * 1
        real_label.set(("{:.2f}".format(real)))


def voltar():
    e_value.delete(0, END)
    e_coin.delete(0, END)
    e_coin.insert(0, "USD/EUR/REAL")
    e_value.insert(0, "VALOR")
    moeda_label.set("Moeda")
    valor_label.set("Valor")
    l_country_flag.configure(image=QMFlag)
    l_country_flag.image = QMFlag
    l_country_flag.place(x=10, y=27)
    l_cifrao.configure(image=cifrao)
    l_cifrao.image = cifrao
    l_cifrao.place(x=3, y=125)
    if b_apply["state"] == DISABLED:
        b_apply["state"] = NORMAL
        b_convert["state"] = DISABLED
    currency.destroy()


def entryvalue():
    global valor
    global moeda
    USFlag = PhotoImage(
        file="directory/icons"
    )
    EUFlag = PhotoImage(
        file="directory/icons"
    )
    BRFlag = PhotoImage(
        file="directory/icons"
    )
    moeda = e_coin.get()
    try:
        valor = float(e_value.get())
        moedas = ("USD", "EUR", "REAL", "usd", "eur", "real", "Usd", "Eur", "Real")
        if not e_coin.get():
            messagebox.showerror(title="Erro!", message="Insira uma moeda correta!")
        elif e_coin.get() not in moedas:
            messagebox.showerror(title="Erro!", message="Insira uma moeda correta!")
        elif not e_value.get():
            messagebox.showerror(title="Erro!", message="Insira um valor correto!")
        elif e_value.get() == "VALOR":
            messagebox.showerror(title="Erro!", message="Insira um valor correto!")
        elif e_coin.get() == "USD" or e_coin.get() == "usd" or e_coin.get() == "Usd":
            moeda_label.set(moeda.upper())
            l_country_flag.configure(image=USFlag)
            l_country_flag.image = USFlag
            l_country_flag.place(x=20, y=27)
            valor_label.set(valor)
            if b_apply["state"] == NORMAL:
                b_apply["state"] = DISABLED
                b_convert["state"] = NORMAL
        elif e_coin.get() == "EUR" or e_coin.get() == "eur" or e_coin.get() == "Eur":
            moeda_label.set(moeda.upper())
            l_country_flag.configure(image=EUFlag)
            l_country_flag.place(x=20, y=27)
            l_country_flag.image = EUFlag
            valor_label.set(valor)
            if b_apply["state"] == NORMAL:
                b_apply["state"] = DISABLED
                b_convert["state"] = NORMAL
        elif e_coin.get() == "REAL" or e_coin.get() == "real" or e_coin.get() == "Real":
            moeda_label.set(moeda.upper())
            l_country_flag.configure(image=BRFlag)
            l_country_flag.image = BRFlag
            l_country_flag.place(x=20, y=27)
            valor_label.set(valor)
            if b_apply["state"] == NORMAL:
                b_apply["state"] = DISABLED
                b_convert["state"] = NORMAL
    except ValueError:
        messagebox.showerror(title="Erro!", message="Insira um valor correto!")


def value():
    global valor
    global e_value
    global e_coin
    global b_convert
    global b_apply
    global valor_label
    global moeda
    global moeda_label
    global l_country_flag
    global l_cifrao
    global QMFlag
    global cifrao
    QMFlag = PhotoImage(
        file="directory/icons"
    )
    cifrao = PhotoImage(
        file="directory/icons"
    )
    valor = ""
    moeda = ""
    valor_label = IntVar()
    moeda_label = IntVar()

    l_empty = Label(root, bg="white", width=50, height=1)
    l_empty.pack()

    l_country_flag = Label(root, image=QMFlag, bg="white")
    l_country_flag.image = QMFlag
    l_country_flag.place(x=10, y=27)

    l_country = Label(
        root,
        textvariable=moeda_label,
        font=("SF Pro Text", 35),
        fg="black",
        bg="white",
        height=1,
    )
    l_country.pack()

    l_empty1 = Label(root, bg="white", width=50, height=1)
    l_empty1.pack()

    l_cifrao = Label(root, image=cifrao, bg="white")
    l_cifrao.image = cifrao
    l_cifrao.place(x=3, y=125)

    l_value = Label(
        root,
        font=("SF Pro Text", 35),
        textvariable=valor_label,
        height=2,
        bg="White",
        fg="Black",
    )
    l_value.pack()

    b_convert = Button(
        root,
        text="Converter",
        font=("SF Pro Text", 20),
        width=24,
        height=1,
        bg="#1968e6",
        fg="White",
        state=DISABLED,
        command=conversor,
    )
    b_convert.pack()

    l_empty2 = Label(root, bg="white", width=50, height=1)
    l_empty2.pack()

    b_apply = Button(
        root,
        text="Aplicar valores",
        font=("SF Pro Text", 20),
        width=24,
        height=1,
        bg="#1968e6",
        fg="White",
        state=NORMAL,
        command=entryvalue,
    )
    b_apply.pack()

    l_empty2 = Label(root, bg="white", width=50, height=1)
    l_empty2.pack()

    e_coin = Entry(root, font=("SF Pro Text", 26), bg="white", fg="black")
    e_coin.insert(0, "USD/EUR/REAL")
    e_coin.pack()

    l_empty3 = Label(root, bg="white", width=50, height=1)
    l_empty3.pack()

    e_value = Entry(root, font=("SF Pro Text", 26), bg="white", fg="black")
    e_value.insert(0, "VALOR")
    e_value.pack()

    moeda_label.set("Moeda")
    valor_label.set("Valor")


def mainscreen():
    global root
    global icon
    root = Tk()
    root.title("Conversor de Moedas")
    root.geometry("320x495")
    root.config(bg="white")
    icon = PhotoImage(
        file="directory/icons"
    )
    root.iconphoto(True, icon)
    value()
    root.mainloop()


mainscreen()
