import re
import requests
import customtkinter as ctk

exchanges_dict = {}

def showCurrency(choice):
    global exchanges_dict
    currency1_choice = currency1.get()
    currency2_choice = currency2.get()

    currency1_value = currency1_entry.get()

    #changing currency name based on the code given by the combobox
    currency1_name.configure(text=f"{exchanges_dict[currency1.get()]}")
    currency2_name.configure(text=f"{exchanges_dict[currency2.get()]}")

    if currency1_value != "" and currency1.get() != currency2.get():
        currency1_value = float(currency1_value)
        response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{currency1_choice}-{currency2_choice}")

        #checking if request was sucessful (should return 200)
        if response.status_code == 200:
            response = response.json() 
            exchange_rate = float(response[f'{currency1_choice}{currency2_choice}']['bid'])
            # print(type(exchange_rate))
            # print(exchange_rate)

            exchange_rate = exchange_rate * currency1_value

            currency2_label.configure(text=f"{exchange_rate:.2f}")
        else:
            print("Não foi possível converter esse valor! Selecione outra moeda!")
    else:
        print("Informe o valor da operação ou coloque moedas diferentes")

def addExchanges(currency1, currency2):
    global exchanges_dict
    response_exchanges = requests.get("https://economia.awesomeapi.com.br/xml/available/uniq").text
    # print(response_exchanges.text)
    exchanges = re.findall(pattern="<(\w+)>([^<]+)", string=response_exchanges) #formatting the list
    
    exchanges_names = []
    exchanges_codes= []
    for code, exchange in exchanges: #filling the list
        exchanges_names.append(exchange)
        exchanges_codes.append(code)

    exchanges_dict = {} #creating a dict to store the value of names and codes
    for i in range(len(exchanges_names)):
        exchanges_dict[exchanges_codes[i]] = exchanges_names[i]

    currency1.configure(values=exchanges_codes)
    currency2.configure(values=exchanges_codes)

    

# ====================
#     INTERFACE
# ====================

app = ctk.CTk()
app.geometry("640x310")
app.title("Cotação de Moedas")
app.resizable("False", "False")

# grid config
app.grid_columnconfigure(1, weight=2, minsize=310)
app.grid_columnconfigure(2, weight=2, minsize=310)

app.rowconfigure(2, minsize=100)
app.rowconfigure(3,  minsize=100)

title_label = ctk.CTkLabel(app,
    text="CONVERSOR DE MOEDAS",
    font=("Arial", 24, "bold"),
)
title_label.grid(row=1, column=1, columnspan=2, padx=10, pady=20, sticky="nsew")

currency1 = ctk.CTkComboBox(app,
    font=("Arial", 24),
    height=50,
    command=showCurrency,
    justify="center",
    dropdown_font=("Arial", 18),
    border_width=0,
    )
currency1.set("BRL")
currency1.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

currency_value = ctk.StringVar(value=0)
currency_value.trace_add("write", lambda *args: showCurrency(currency1_entry.get()))

currency1_entry = ctk.CTkEntry(app,
    textvariable=currency_value,
    font=("Arial", 24, "bold"),
    height=50,
    justify="center"
    )
currency1_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

currency1_name = ctk.CTkLabel(app, 
    text="Real Brasileiro (R$)",
    font=("Arial", 16),
    height=50,
)
currency1_name.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

currency2 = ctk.CTkComboBox(app, 
    font=("Arial", 24),
    command=showCurrency,
    height=50,
    justify="center",
    dropdown_font=("Arial", 18),
    border_width=0,
    )
currency2.set("USD") #default value for combobox
currency2.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

currency2_label = ctk.CTkLabel(app, 
    text="$0.00",
    font=("Arial", 24, "bold")
    )
currency2_label.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

currency2_name = ctk.CTkLabel(app, 
    text="Dolar",
    font=("Arial", 16),
    height=50,
)
currency2_name.grid(row=4, column=2, padx=10, pady=10, sticky="ew")

addExchanges(currency1, currency2) #filling the combobox

app.mainloop()