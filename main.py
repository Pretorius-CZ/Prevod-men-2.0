from tkinter import *
import requests


# Barvy
main_color = "#14085f"

# Okno
window = Tk()
window.title("Převodník měn v.2.0")
window.minsize(450, 120)
window.resizable(False, False)
window.config(bg=main_color)

# Funkce
def count():
    try:
        currency_from = drop_down_from.get()
        currency_to = drop_down_to.get()
        amount = int(user_input.get())

        url = (f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount="
               f"{amount}")

        payload = {}
        headers = {
            "apikey": "c1ka4cc65JFsQ9KySllcO9tYk4n6nJhw"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        data_result = response.json()
        result_label.config(text=round(data_result["result"], 2))
        kurz_label.config(text=f'Současný kurz je {round(data_result["info"]["rate"], 2)} {currency_to} / {currency_from}')
        empty_label.config(text="")
    except:
        empty_label.config(text="Zadejte prosím částku")


# Uživatelský vstup
user_input = Entry(width=27, font=("Calibri", 12), justify=CENTER)
# user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10, pady=(7, 0))

# Tlačítko převodu
count_button = Button(text="Převeď", font=("Calibri", 12), command=count)
count_button.grid(row=0, column=2, padx=10, pady=(10, 0))

# Labels
result_label = Label(text="", font=("Calibri", 12), bg=main_color, fg="white")
result_label.grid(row=1, column=0)

kurz_label = Label(font=("Calibri", 12), bg=main_color, fg="yellow")
kurz_label.grid(row=2, column=0)

empty_label = Label(font=("Calibri", 12), bg=main_color, fg="white")
empty_label.grid(row=3, column=0)


# Roletky
drop_down_from = StringVar(window)
drop_down_from.set("EUR")
drop_down_from_options = OptionMenu(window, drop_down_from, "EUR", "CZK", "USD", "CHF", "AUD")
drop_down_from_options.grid(row=0, column=1, padx=10, pady=(10, 0))

drop_down_to = StringVar(window)
drop_down_to.set("CZK")
drop_down_to_options = OptionMenu(window, drop_down_to, "CZK",  "EUR", "USD", "CHF", "AUD")
drop_down_to_options.grid(row=1, column=1, padx=10, pady=(10, 0))


# Cyklus
window.mainloop()
