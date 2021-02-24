
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Spinbox
from tkinter.filedialog import askdirectory


def open_path_csv():
    filename = askdirectory()
    return filename


def on_closing():
    if messagebox.askokcancel("Quit", "PDF is create."):
        window.quit()

def clicked():

    data = {'filename': open_path_csv(),
            'season': season.get(),
            'view_price': view_price.get(),
            'quantity': quantity.get(),
            'if_material': if_material.get(),
            'if_characteristics': if_characteristics.get(),
            'if_create_brand': if_create_brand.get(),
            'if_create_logo': if_create_logo.get(),
            'if_price_resize': float(if_price_resize.get()),
            'price_resize': float(price_resize.get()),
            'valute': valute.get(),
            'descr_resize': int(descr_resize.get()),
            'proc': int(proc.get())
            }

    import maket_GUIT
    maket_GUIT.main(data)
    on_closing()


window = Tk()
window.title("Create PDF")
window.geometry('400x600')

# Категория
season_text = Label(window, text='Категория')
season = Combobox(window)
season['value'] = ("Все платья", "Весна 2021", "Лето 2021", "Осень 2021", "Зима 2021")
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

# Отобразить бренд
if_create_brand_text = Label(window, text='Отображать бренд')
if_create_brand = Combobox(window)
if_create_brand['value'] = ("Да", "Нет")
if_create_brand.current(0)
if_create_brand_text.grid(column=0, row=5, sticky=W, padx=10, pady=10)
if_create_brand.grid(column=1, row=5, sticky=W, padx=10, pady=10)

# Отобразить лого (Sale New)
if_create_logo_text = Label(window, text='Отображать SALE NEW')
if_create_logo = Combobox(window)
if_create_logo['value'] = ("Отобразить", "Не отображать")
if_create_logo.current(1)
if_create_logo_text.grid(column=0, row=6, sticky=W, padx=10, pady=10)
if_create_logo.grid(column=1, row=6, sticky=W, padx=10, pady=10)

# Надбавка
if_price_resize_text = Label(window, text="Надбавка")
if_price_resize = Spinbox(window, from_=0, to=100, format="%10.2f", increment=0.01, width=7)
if_price_resize.set('{:10.2f}'.format(0.00))
if_price_resize_text.grid(column=0, row=7, sticky=W, padx=10, pady=10)
if_price_resize.grid(column=1, row=7, sticky=W, padx=10, pady=10)

# Множитель курса
price_resize_text = Label(window, text="Множитель курса")
price_resize = Spinbox(window, from_=0, to=100, format="%10.2f", increment=0.01, width=7)
price_resize.set('{:10.2f}'.format(1.00))
price_resize_text.grid(column=0, row=8, sticky=W, padx=10, pady=10)
price_resize.grid(column=1, row=8, sticky=W, padx=10, pady=10)

# Отображение Валюты
if_price = Label(window, text='Отобразить валюту')
valute = Combobox(window)
valute['value'] = ('Нет', 'BY', '₽', '€', '$')
valute.current(0)
if_price.grid(column=0, row=9, sticky=W, padx=10, pady=10)
valute.grid(column=1, row=9, sticky=W, padx=10, pady=10)

# Изменять размеры
var_dr = IntVar()
var_dr.set(0)
descr_resize_text = Label(window, text="Изменить размер")
descr_resize = Spinbox(window, from_=-10, to=10, width=5, textvariable=var_dr)
descr_resize_text.grid(column=0, row=10, sticky=W, padx=10, pady=10)
descr_resize.grid(column=1, row=10, sticky=W, padx=10, pady=10)

# Качество PDF
proc_text = Label(window, text="Качество PDF")
var = IntVar()
var.set(50)
proc = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
proc_text.grid(column=0, row=11, sticky=W, padx=10, pady=10)
proc.grid(column=1, row=11, sticky=W, padx=10, pady=10)

btn = Button(window, text="Запустить", command=clicked)
btn.grid(column=1, row=12, padx=10, pady=10)


window.mainloop()