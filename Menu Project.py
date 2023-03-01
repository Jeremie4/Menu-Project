import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("360x640")
app.minsize(360, 640)
app.maxsize(360, 640)
app.title("Menu Project - Jeremie Marquis")

total = 0
ran = False

def cancel_order():
    global total, ran
    total = 0
    ran = True
    main()

def place_order():
    global total
    if checkbox_1.get() == 1:
        total += 8.5
    if checkbox_2.get() == 1:
        total += 6
    if checkbox_3.get() == 1:
        total += 6.75
    if checkbox_4.get() == 1:
        total += 5.3
    if checkbox_5.get() == 1:
        total += 2.5
    if checkbox_6.get() == 1:
        total += 3
    if checkbox_7.get() == 1:
        total += 3
    if checkbox_9.get() == 1:
        total += 1.2
    if checkbox_10.get() == 1:
        total += 2.5
    
    label_4 = customtkinter.CTkLabel(master=app, text=("    Order Placed    \n     Total: $" + str(round(total, 2))), justify=customtkinter.LEFT)
    label_4.place(relx=0.5, rely=0.925, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app, text="Cancel Order", command=cancel_order)
    button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)
    """text_1 = customtkinter.CTkTextbox(master=app, width=200, height=70)
    text_1.place(relx=0.5, rely=0.925, anchor=tkinter.CENTER)
    text_1.insert("0.0", "Order Placed\n Total: $" + str(round(total, 2)))"""


def main():
    global checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5, checkbox_6, checkbox_7, checkbox_8, checkbox_9, checkbox_10
    if ran:
        label_4 = customtkinter.CTkLabel(master=app, text=("Order Cancelled"), justify=customtkinter.LEFT)
        label_4.place(relx=0.5, rely=0.925, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=app, text="Place Order", command=place_order)
    button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)


    label_1 = customtkinter.CTkLabel(master=app, text="Main Dishes", justify=customtkinter.LEFT)
    label_1.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

    checkbox_1 = customtkinter.CTkCheckBox(master=app, text="Burger ($8.50)")
    checkbox_1.place(relx=0.33, rely=0.1, anchor=tkinter.W)
    checkbox_2 = customtkinter.CTkCheckBox(master=app, text="Corn Dog ($6.00)")
    checkbox_2.place(relx=0.33, rely=0.15, anchor=tkinter.W)
    checkbox_3 = customtkinter.CTkCheckBox(master=app, text="Chicken Nuggets ($6.75)")
    checkbox_3.place(relx=0.33, rely=0.2, anchor=tkinter.W)
    checkbox_4 = customtkinter.CTkCheckBox(master=app, text="Nachos ($5.30)")
    checkbox_4.place(relx=0.33, rely=0.25, anchor=tkinter.W)


    label_2 = customtkinter.CTkLabel(master=app, text="Sides", justify=customtkinter.LEFT)
    label_2.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    checkbox_5 = customtkinter.CTkCheckBox(master=app, text="Fries ($2.50)")
    checkbox_5.place(relx=0.33, rely=0.4, anchor=tkinter.W)
    checkbox_6 = customtkinter.CTkCheckBox(master=app, text="Onion Rings ($3.00)")
    checkbox_6.place(relx=0.33, rely=0.45, anchor=tkinter.W)
    checkbox_7 = customtkinter.CTkCheckBox(master=app, text="Potato Wedges ($4.00)")
    checkbox_7.place(relx=0.33, rely=0.5, anchor=tkinter.W)


    label_3 = customtkinter.CTkLabel(master=app, text="Drinks", justify=customtkinter.LEFT)
    label_3.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    checkbox_8 = customtkinter.CTkCheckBox(master=app, text="Water (Free)")
    checkbox_8.place(relx=0.33, rely=0.65, anchor=tkinter.W)
    checkbox_9 = customtkinter.CTkCheckBox(master=app, text="Fountain Drink ($1.20)")
    checkbox_9.place(relx=0.33, rely=0.7, anchor=tkinter.W)
    checkbox_10 = customtkinter.CTkCheckBox(master=app, text="Milk Shake ($2.50)")
    checkbox_10.place(relx=0.33, rely=0.75, anchor=tkinter.W)

    app.mainloop()
main()