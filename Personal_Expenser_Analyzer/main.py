from tkinter import *
from tkinter import filedialog, ttk
import pandas as pd

TITLE_FONT = ("Helvetica",20,"normal")
SUBTITLE_FONT = ("Helvetica",10,"normal")
BACKGROUND_COLOR = "lightblue"
categories = []
data = {}

def sum_expenses(df):
    total_expenses = [float(expense.replace(",", ".")) for expense in df["Monto"].tolist()]
    return sum(total_expenses)

def filter_category():
    transactions.delete(0,END)
    selection = combo.get()
    category_data = data[data["Categoría"] == selection]
    total_expenses_label.config(text=f"- Total Expenses: R${sum_expenses(category_data)}")

    for _,row in category_data.iterrows():
        transactions.insert(END,f"{row["Fecha"]} | {row["Descripción"]}")

def show_all():
    transactions.delete(0,END)
    total_expenses_label.config(text=f"- Total Expenses: R${sum_expenses(data)}")
    df = pd.DataFrame(data)

    for i,r in df.iterrows():
        transactions.insert(END, f"{r["Fecha"]} | {r["Descripción"]}")

def read_csv_file(file_path):

    try:
        global data
        data = pd.read_csv(file_path,encoding='utf-8')
    except Exception as e:
        print(f"Error reading CSV: {e}")
    else:
        global categories
        categories = data["Categoría"].unique().tolist()


def open_csv_file():
    file_path = filedialog.askopenfilename(title="Select a CSV file",defaultextension=".csv",
                                           filetypes=[("CSV Files","*.csv"),("All Files","*.*")])
    if file_path:
        global combo
        read_csv_file(file_path)
        description_text.destroy()
        import_button.destroy()

        #Labels
        label1 = Label(text="Filter for Categories:",background=BACKGROUND_COLOR,font=SUBTITLE_FONT)
        label1.grid(column=0,row=2, padx=10, pady=25)

        result_label = Label(text="Results:", bg=BACKGROUND_COLOR, highlightthickness=0,font=("Helvetica",10,"bold"))
        result_label.grid(column=0, row=4,pady=5)

        total_expenses_label.config(text=f"- Total Expenses: R$",bg=BACKGROUND_COLOR,highlightthickness=0)
        total_expenses_label.grid(column=0,row=6,sticky="w")

        transactions_label.config(text="- Transactions:",bg=BACKGROUND_COLOR,highlightthickness=0)
        transactions_label.grid(column=0,row=7,pady=10,sticky="w")

        #Combobox
        combo.config(values=categories, state="readonly")  # readonly evita escritura
        combo.set("Select a category")
        combo.grid(column=1,row=2)

        #Listbox
        transactions.grid(column=0,row=8,columnspan=3,sticky="ew")

        #Button
        filter_button = Button(text="Filter",highlightthickness=0,command=filter_category)
        filter_button.grid(column=2,row=2)

        show_all_button = Button(text="Show All",highlightthickness=0,command=show_all)
        show_all_button.grid(column=2,row=3)

        #Separators
        ttk.Separator(window,orient="horizontal",).grid(sticky="ew",row=3,columnspan=2,padx=10,pady=5)

#Window/Root
window = Tk()
window.title("Personal Expense Analyzer")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#Combobox
combo = ttk.Combobox(window)

#Listbox
transactions = Listbox(window)

#Labels
title = Label(text="Personal Expense Analyzer",bg=BACKGROUND_COLOR,font=TITLE_FONT)
title.grid(column=0,row=0,columnspan=3)

description_text = Label(padx=20,pady=20,text="Click the button to import a CSV file",bg=BACKGROUND_COLOR,font=SUBTITLE_FONT)
description_text.grid(column=0,row=2)

total_expenses_label = Label()
transactions_label = Label()

#Import Button
import_image =PhotoImage(file="images/file.png")
import_button = Button(image=import_image,highlightthickness=0,command=open_csv_file,bg=BACKGROUND_COLOR)
import_button.grid(column=0,row=3)

#Separator
ttk.Separator(window,orient="horizontal",).grid(sticky="ew",row=1,columnspan=3,padx=10,pady=5)



window.mainloop()