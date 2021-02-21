
from tkinter import *
from tkinter.ttk import Combobox, Spinbox

def clicked():
    print(var.get())
    print(var_r.get())
    print(type(price_resize.get()))
    print(float(price_resize.get())*4)
    print(season.get())


window = Tk()
window.title("Create PDF")
window.geometry('400x570')

# Категория
season_text = Label(window, text='Категория')
season = Combobox(window)
season['value'] = ("Все платья", "Весна", "Лето", "Осень", "Зима")
season.current(0)
season_text.grid(column=0, row=0, sticky=W, padx=10, pady=10)
season.grid(column=1, row=0, sticky=W, padx=10, pady=10)

# Отображение цены
view_price_text = Label(window, text='Отображение цены')
view_price = Combobox(window)
view_price['value'] = ("Отобразить", "Без цены")
view_price.current(1)
view_price_text.grid(column=0, row=1, sticky=W, padx=10, pady=10)
view_price.grid(column=1, row=1, sticky=W, padx=10, pady=10)

# Наличие
quantity_text = Label(window, text='Наличие')
quantity = Combobox(window)
quantity['value'] = ("Все", "Только в наличии")
quantity.current(1)
quantity_text.grid(column=0, row=2, sticky=W, padx=10, pady=10)
quantity.grid(column=1, row=2, sticky=W, padx=10, pady=10)

# Ткань
if_material_text = Label(window, text="С тканью")
if_material = Combobox(window)
if_material['value'] = ("С тканью", "Скрыть")
if_material.current(0)
if_material_text.grid(column=0, row=3, sticky=W, padx=10, pady=10)
if_material.grid(column=1, row=3, sticky=W, padx=10, pady=10)

# Отображать состав
if_characteristics_text = Label(window, text='Отображать состав')
if_characteristics = Combobox(window)
if_characteristics['value'] = ("Отобразить", "Скрыть")
if_characteristics.current(0)
if_characteristics_text.grid(column=0, row=4, sticky=W, padx=10, pady=10)
if_characteristics.grid(column=1, row=4, sticky=W, padx=10, pady=10)

# Отобразить лого (Sale New)
if_create_logo_text = Label(window, text='Отображать SALE NEW')
if_create_logo = Combobox(window)
if_create_logo['value'] = ("Отобразить", "Не отображать")
if_create_logo.current(1)
if_create_logo_text.grid(column=0, row=5, sticky=W, padx=10, pady=10)
if_create_logo.grid(column=1, row=5, sticky=W, padx=10, pady=10)

# Надбавка
var_r = IntVar()
var_r.set(0)
if_price_resize_text = Label(window, text="Надбавка")
if_price_resize = Spinbox(window, from_=0, to=100, width=5, textvariable=var_r)
if_price_resize_text.grid(column=0, row=6, sticky=W, padx=10, pady=10)
if_price_resize.grid(column=1, row=6, sticky=W, padx=10, pady=10)

# Множитель курса
price_resize_text = Label(window, text="Множитель курса")
price_resize = Spinbox(window, from_=0, to=100, format="%10.2f", increment=0.01, width=7)
price_resize.set('{:10.2f}'.format(1))
price_resize_text.grid(column=0, row=7, sticky=W, padx=10, pady=10)
price_resize.grid(column=1, row=7, sticky=W, padx=10, pady=10)

# Отображение Валюты
if_price = Label(window, text='Отобразить валюту')
valute = Combobox(window)
valute['value'] = ('Нет', 'BY', 'RUR', 'EUR', 'USD')
valute.current(0)
if_price.grid(column=0, row=8, sticky=W, padx=10, pady=10)
valute.grid(column=1, row=8, sticky=W, padx=10, pady=10)

# Изменять размеры
var_dr = IntVar()
var_dr.set(0)
descr_resize_text = Label(window, text="Изменить размер")
descr_resize = Spinbox(window, from_=-10, to=10, width=5, textvariable=var_dr)
descr_resize_text.grid(column=0, row=9, sticky=W, padx=10, pady=10)
descr_resize.grid(column=1, row=9, sticky=W, padx=10, pady=10)

# Качество PDF
proc_text = Label(window, text="Качество PDF")
var = IntVar()
var.set(50)
proc = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
proc_text.grid(column=0, row=10, sticky=W, padx=10, pady=10)
proc.grid(column=1, row=10, sticky=W, padx=10, pady=10)

btn = Button(window, text="Запустить", command=clicked)
btn.grid(column=1, row=11, padx=10, pady=10)


window.mainloop()