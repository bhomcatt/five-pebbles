from tkinter import *
root = Tk()
root.title("fatcat")
root.geometry("500x500")
root.configure(background = "#ebdec9")
label_month = Label(root)
label_profit = Label(root)
label_max_profit = Label(root)
label_min_profit = Label(root)


month = ("enero","febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
profit = (2000, 45000, 7000, 97000, 12000, 456000, 65000, 1000, 3000, 7000, 9000)

label_month["text"] = "month: "+str(month)
label_profit["text"] = "profit: "+str(profit)


def maxprofit ():
    max_profit=max(profit)
    max_profit_index = profit.index(max_profit)
    max_profit_month = month[max_profit_index]
    label_max_profit['text'] = "maximo de ventas: "+str(max_profit)+", se recibio en el mes de: "+str(max_profit_month)
    

def minprofit ():
    min_profit=min(profit)
    min_profit_index = profit.index(min_profit)
    min_profit_month = month[min_profit_index]
    label_min_profit['text'] = "minimo de ventas: "+str(min_profit)+", se recibio en el mes de: "+str(min_profit_month)

label_month.place(relx=0.5,rely=0.2,anchor=CENTER)
label_profit.place(relx=0.5,rely=0.3,anchor=CENTER)

btn_max = Button(root, text="maximo de ventas",command=maxprofit,bg="royal blue",fg = "white")
btn_max.place(relx=0.5,rely=0.4,anchor=CENTER)

label_max_profit.place(relx=0.5,rely=0.5,anchor=CENTER)

btn_min= Button(root, text="minimo de ventas",command=minprofit,bg="royal blue",fg = "white")
btn_min.place(relx=0.5,rely=0.6,anchor=CENTER)

label_min_profit.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()