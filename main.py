from tkinter import *
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
import PIL.Image

# Function
def menu(frame,food, price, varNum, varFood, bg, row, tab,command):
    formatted_price = "{:.2f}".format(price)
    menu = Checkbutton(frame, text=f"{food}{tab}${formatted_price}", variable=varNum, onvalue=1, offvalue=0, font=("arial",18,"bold"),bg=f"#{bg}" , command=command).grid(row=row, column=0, sticky=W)
    txt = Entry(frame,font=("arial",18,"bold"), textvariable= varFood, width=6, justify="right", state= DISABLED)
    txt.grid(row=row,column=1)
    return txt


def frameTitle(frame, text, bg, row):
    title = Label(frame, font=("Tahoma", 18, "bold"), text=f"{text}",bg=f"#{bg}")
    title.grid(row=row,column=0)


def chkFries():
    if(var1.get() == 1):
        txtFries.configure(state=NORMAL)
        varFries.set("")
    elif(var1.get() == 0):
        txtFries.configure(state=DISABLED)
        varFries.set("0")

def chkHamburger():
    if(var3.get() == 1):
        txtHamburger.configure(state=NORMAL)
        varHamburger.set("")
    elif(var3.get() == 0):
        txtHamburger.configure(state=DISABLED)
        varHamburger.set("0")

def chkOnion():
    if(var4.get() == 1):
        txtOnion.configure(state=NORMAL)
        varOnion.set("")
    elif(var4.get() == 0):
        txtOnion.configure(state=DISABLED)
        varOnion.set("0")

def chkChicken():
    if(var5.get() == 1):
        txtChicken.configure(state=NORMAL)
        varChicken.set("")
    elif(var5.get() == 0):
        txtChicken.configure(state=DISABLED)
        varChicken.set("0")

def chkFish():
    if(var6.get() == 1):
        txtFish.configure(state=NORMAL)
        varFish.set("")
    elif(var6.get() == 0):
        txtFish.configure(state=DISABLED)
        varFish.set("0")

def chkBeefSand():
    if(var7.get() == 1):
        txtBeefSand.configure(state=NORMAL)
        varBeefSand.set("")
    elif(var7.get() == 0):
        txtBeefSand.configure(state=DISABLED)
        varBeefSand.set("0")

def chkChickenSand():
    if(var8.get() == 1):
        txtChickenSand.configure(state=NORMAL)
        varChickenSand.set("")
    elif(var8.get() == 0):
        txtChickenSand.configure(state=DISABLED)
        varChickenSand.set("0")

def chkHashBrown():
    if(var9.get() == 1):
        txtHashBrown.configure(state=NORMAL)
        varHashBrown.set("")
    elif(var9.get() == 0):
        txtHashBrown.configure(state=DISABLED)
        varHashBrown.set("0")

def chkToastedBagel():
    if(var10.get() == 1):
        txtToastedBagel.configure(state=NORMAL)
        varToastedBagel.set("")
    elif(var10.get() == 0):
        txtToastedBagel.configure(state=DISABLED)
        varToastedBagel.set("0")

def chkPancakes():
    if(var11.get() == 1):
        txtPancakes.configure(state=NORMAL)
        varPancakes.set("")
    elif(var11.get() == 0):
        txtPancakes.configure(state=DISABLED)
        varPancakes.set("0")

def chkPineapple():
    if(var12.get() == 1):
        txtPineapple.configure(state=NORMAL)
        varPineapple.set("")
    elif(var12.get() == 0):
        txtPineapple.configure(state=DISABLED)
        varPineapple.set("0")

def chkChocolate():
    if(var13.get() == 1):
        txtChocolate.configure(state=NORMAL)
        varChocolate.set("")
    elif(var13.get() == 0):
        txtChocolate.configure(state=DISABLED)
        varChocolate.set("0")

def chkTea():
    if(var14.get() == 1):
        txtTea.configure(state=NORMAL)
        varTea.set("")
    elif(var14.get() == 0):
        txtTea.configure(state=DISABLED)
        varTea.set("0")

def chkCola():
    if(var15.get() == 1):
        txtCola.configure(state=NORMAL)
        varCola.set("")
    elif(var15.get() == 0):
        txtCola.configure(state=DISABLED)
        varCola.set("0")
    
def chkCoffee():
    if(var16.get() == 1):
        txtCoffee.configure(state=NORMAL)
        varCoffee.set("")
    elif(var16.get() == 0):
        txtCoffee.configure(state=DISABLED)
        varCoffee.set("0")

def chkOrange():
    if(var17.get() == 1):
        txtOrange.configure(state=NORMAL)
        varOrange.set("")
    elif(var17.get() == 0):
        txtOrange.configure(state=DISABLED)
        varOrange.set("0")

def chkWater():
    if(var18.get() == 1):
        txtWater.configure(state=NORMAL)
        varWater.set("")
    elif(var18.get() == 0):
        txtWater.configure(state=DISABLED)
        varWater.set("0")

def chkCone():
    if(var22.get() == 1):
        txtCone.configure(state=NORMAL)
        varCone.set("")
    elif(var22.get() == 0):
        txtCone.configure(state=DISABLED)
        varCone.set("0")

def chkShake():
    if(var23.get() == 1):
        txtShake.configure(state=NORMAL)
        varShake.set("")
    elif(var23.get() == 0):
        txtShake.configure(state=DISABLED)
        varShake.set("0")

def chkStrawberry():
    if(var24.get() == 1):
        txtStrawberry.configure(state=NORMAL)
        varStrawberry.set("")
    elif(var24.get() == 0):
        txtStrawberry.configure(state=DISABLED)
        varStrawberry.set("0")

def chkHanuman():
    if(var19.get() == 1):
        txtHanuman.configure(state=NORMAL)
        varHanuman.set("")
    elif(var19.get() == 0):
        txtHanuman.configure(state=DISABLED)
        varHanuman.set("0")

def chkAngkor():
    if(var20.get() == 1):
        txtAngkor.configure(state=NORMAL)
        varAngkor.set("")
    elif(var20.get() == 0):
        txtAngkor.configure(state=DISABLED)
        varAngkor.set("0")

def chkAnchor():
    if(var21.get() == 1):
        txtAnchor.configure(state=NORMAL)
        varAnchor.set("")
    elif(var21.get() == 0):
        txtAnchor.configure(state=DISABLED)
        varAnchor.set("0")

def costofmeal():
    meal11 = float(varFries.get())
    meal12 = float(varHamburger.get())
    meal13 = float(varOnion.get())
    meal14 = float(varChicken.get())
    meal15 = float(varFish.get())
    meal16 = float(varBeefSand.get())
    meal17 = float(varChickenSand.get())
    meal18 = float(varHashBrown.get())
    meal19 = float(varToastedBagel.get())
    meal20 = float(varPancakes.get())
    meal21 = float(varPineapple.get())
    meal22 = float(varChocolate.get())
    meal23 = float(varCone.get())
    meal24 = float(varShake.get())
    meal25 = float(varStrawberry.get())
    meal26 = float(varTea.get())
    meal27 = float(varCola.get())
    meal28 = float(varCoffee.get())
    meal29 = float(varOrange.get())
    meal30 = float(varWater.get())
    meal31 = float(varHanuman.get())
    meal32 = float(varAngkor.get())
    meal33 = float(varAnchor.get())

    
    total = meal11 * 8.99 + meal12 * 5.49 + meal13 * 4.99 + meal14 * 6.99 + meal15 * 4.99 + meal16 * 5.99 + meal17 * 4.99 + meal18 * 3.99 + meal19 * 1.99  + meal20 * 4.99 + meal21 * 4.99 + meal22 * 3.99 + meal23 * 1.99 + meal24 * 4.99 + meal25 * 4.99 + meal26 * 2.49 + meal27 * 1.99 + meal28 * 2.99 + meal29 * 3.5 + meal30 * 1.99 + meal31 * 1.49 + meal32 * 0.75 + meal33 * 0.99
    return total


def reset():
    varFries.set("0")
    varSalad.set("0")
    varHamburger.set("0")
    varOnion.set("0")
    varChicken.set("0")
    varFish.set("0")
    varBeefSand.set("0")
    varChickenSand.set("0")

    varHashBrown.set("0")
    varToastedBagel.set("0")
    varPancakes.set("0")
    varPineapple.set("0")
    varChocolate.set("0")

    varTea.set("0")
    varCola.set("0")
    varCoffee.set("0")
    varOrange.set("0")
    varWater.set("0")

    varCone.set("0")
    varShake.set("0")
    varStrawberry.set("0")


# Canvas
window = Tk()
window.geometry("1425x825+0+0")
window.title("Self-Order System")

window.configure(bg='white')

# Top Frame
Tops = Frame(window, width = 1350, height= 100, bd=12, relief="raised",bg="lightblue")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=("Tahoma", 50, "bold"), text="\t     Self Order System\t", bg="lightblue")
lblTitle.grid(row=0,column=0)


#Logo
LogoImageObject = Image.open("C:/Users/User/Desktop/Fall Semester/COSC 121 ComSciA/Python_Coding/FinalProject/1.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)
LogoLabel = ttk.Label(Tops, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")


# Bottom Main Frame
BottomMainFrame = Frame(window, width = 1425, height= 725, bd=12, relief="raised")
BottomMainFrame.pack(side=BOTTOM)


f1 = Frame(BottomMainFrame, width =500, height= 725, bd=12, relief="raised",bg="#dda15e")
f1.pack(side=LEFT)


f2 = Frame(BottomMainFrame, width = 500, height= 725, bd=12, relief="raised")
f2.pack(side=LEFT)

f2Top = Frame(f2, width = 525, height= 425, bd=5, relief="raised",bg="#2a9d8f")
f2Top.pack(side=TOP)
f2Bottom = Frame(f2, width = 525, height= 300, bd=5, relief="raised", bg="#a1c181")
f2Bottom.pack(side=BOTTOM)

f3 = Frame(BottomMainFrame, width = 500, height= 725, bd=12, relief="raised",bg="#b5838d")
f3.pack(side=RIGHT)

from variable import * 

# ==========================Frame 1 ================
frameTitle(f1, "Fast Food Meal and Vegetarian\n\n", "dda15e", 0)

txtFries = menu(f1,"French Fries", 8.99, var1, varFries, "dda15e", 1, "\t",chkFries)
txtHamburger = menu(f1,"Hamburger", 5.49, var3, varHamburger, "dda15e", 3, "\t", chkHamburger)
txtOnion=  menu(f1,"Onion", 4.99, var4, varOnion, "dda15e", 4, "\t\t", chkOnion)
txtChicken = menu(f1,"Chicken Salad", 6.99, var5, varChicken, "dda15e", 5, "\t", chkChicken)

frameTitle(f1, "\nSandwich\n", "dda15e", 6)
txtFish = menu(f1,"Fish Sandwich", 4.99, var6, varFish, "dda15e", 7, "\t", chkFish)
txtBeefSand = menu(f1,"Beef Sandwich", 5.99, var7, varBeefSand, "dda15e", 8, "\t", chkBeefSand)
txtChickenSand = menu(f1,"Chicken Sandwich", 4.99, var8, varChickenSand, "dda15e", 9, " ", chkChickenSand)

lblspace = Label(f1, text="\n\n\n\n\n\n\n",bg="#dda15e")
lblspace.grid(row=10, column=0)


# ===============================Frame 2 ==========================
frameTitle(f2Top, "Dessert\t\t\t     \n", "2a9d8f", 0)

txtHashBrown = menu(f2Top,"Hash Brown", 3.99, var9, varHashBrown, "2a9d8f", 1, "\t",chkHashBrown)
txtToastedBagel = menu(f2Top, "ToastedBagel", 1.99, var10, varToastedBagel, "2a9d8f", 2, "\t", chkToastedBagel)
txtPancakes = menu(f2Top, "Pancakes", 4.99, var11, varPancakes, "2a9d8f", 3, "\t", chkPancakes)
txtPineapple = menu(f2Top, "Pineapple", 4.99, var12, varPineapple, "2a9d8f", 4, "\t", chkPineapple)
txtChocolate = menu(f2Top, "Chocolate", 3.99, var13, varChocolate, "2a9d8f", 5, "\t", chkChocolate)

lblspace = Label(f2Top, text="\n\n",bg="#2a9d8f")
lblspace.grid(row=6, column=0)


# ===============================Frame 3 TOP ===============================
frameTitle(f3, "Drinks                    \n", "b5838d", 0)
txtTea = menu(f3, "Tea", 2.49, var14, varTea, "b5838d", 1, "\t", chkTea)
txtCola = menu(f3, "Cola", 1.99, var15, varCola, "b5838d", 2, "\t", chkCola)
txtCoffee = menu(f3, "Coffee", 2.99, var16, varCoffee, "b5838d", 3, "\t", chkCoffee)
txtOrange = menu(f3, "Orange", 3.50, var17, varOrange, "b5838d", 4, "\t", chkOrange)
txtWater = menu(f3, "Water", 1.99, var18, varWater, "b5838d", 5, "\t", chkWater)


# ======================= Frame 2 Bottom =======================
frameTitle(f2Bottom, "\nShakes\t\t                      \n", "a1c181",0)
txtCone = menu(f2Bottom, "Vanilla Cones", 1.99, var22, varCone, "a1c181", 1, "\t", chkCone)
txtShake = menu(f2Bottom, "Vanilla Shakes", 4.99, var23, varShake, "a1c181", 2, "\t", chkShake)
txtStrawberry = menu(f2Bottom, "Strawberry Shakes", 4.99, var24 ,varStrawberry, "a1c181", 3, "   ", chkStrawberry)

lblspace = Label(f2Bottom, text="\n\n",bg="#a1c181")
lblspace.grid(row=10, column=0)

# ===================== Frame 3 Bottom =========================
frameTitle(f3, "\nBeer\t                         \n","b5838d", 6)

txtHanuman = menu(f3, "Hanuman   ", 1.49, var19, varHanuman, "b5838d",7,"   ", chkHanuman)
txtAngkor = menu(f3, "Angkor   ", 0.75, var20, varAngkor, "b5838d",8,"   ", chkAngkor)
txtAnchor = menu(f3, "Anchor   ", 0.99, var21, varAnchor, "b5838d",9,"   ", chkAnchor)

lblspace = Label(f3, text="\n\n\n",bg="#b5838d")
lblspace.grid(row=10, column=0)

def checkout():

    newWindow = Toplevel(window)
    newWindow.title("Checkout")
    newWindow.geometry("1425x825+0+0")

    Tops2 = Frame(newWindow, width = 1350, height= 100, bd=12, relief="raised",bg="lightblue")
    Tops2.pack(side=TOP)
    checkout_label = Label(Tops2, font=("Tahoma", 50, "bold"), text="\t     Payment Method\t\t", bg="lightblue")
    checkout_label.pack()

    BottomMainFrame = Frame(newWindow, width = 1425, height= 725, bd=12, relief="raised")
    BottomMainFrame.pack(side=BOTTOM)

    f2Tops = Frame(newWindow, width = 1425, height= 425, bd=5, relief="raised",bg="white")
    f2Tops.pack(side=TOP)

    payment_var = IntVar()
    payment_var.set(1)

    # Payment method radio buttons
    radio_cash = Radiobutton(BottomMainFrame, text="Cash", variable=payment_var, value=1, font=("Arial", 14))
    radio_cash.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    radio_card = Radiobutton(BottomMainFrame, text="Credit Card", variable=payment_var, value=2, font=("Arial", 14))
    radio_card.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    radio_QR = Radiobutton(BottomMainFrame, text="QR", variable=payment_var, value=3, font=("Arial", 14))
    radio_QR.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    # Proceed to Payment button
    proceed_button = Button(BottomMainFrame, text="Proceed to Payment", command=lambda: process_payment(payment_var.get(), f2Tops))
    proceed_button.grid(row=3, column=0, pady=20)

    total_cost_label = Label(BottomMainFrame, text=f"Total Cost: ${costofmeal():.2f}", font=("Arial", 16, "bold"))
    total_cost_label.grid(row=4, column=0, pady=10)

    paid_button = Button(newWindow, text="Paid", command=lambda: [window.destroy(), newWindow.destroy()], font=("Arial", 18, "bold"))
    paid_button.place(relx=0.95, rely=0.95, anchor="se")

def process_payment(payment_method, frame):
    # Destroy existing widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    if payment_method == 3:
        img_path = "C:/Users/User/Desktop/Fall Semester/COSC 121 ComSciA/Python_Coding/FinalProject/2.jpg"
        original_img = PIL.Image.open(img_path)
        # resized_img = original_img.resize((450, 450))  

        img = ImageTk.PhotoImage(original_img)

        process_payment.img_reference = img

        label = Label(frame, image=img)
        label.pack()
    elif payment_method == 2:
        # Credit card
        credit_card_img_path = "C:/Users/User/Desktop/Fall Semester/COSC 121 ComSciA/Python_Coding/FinalProject/3.png"
        credit_card_img = PIL.Image.open(credit_card_img_path)
        resized_credit_card_img = credit_card_img.resize((450, 450))

        credit_card_img = ImageTk.PhotoImage(resized_credit_card_img)

        process_payment.img_reference = credit_card_img

        credit_card_label = Label(frame, image=credit_card_img)
        credit_card_label.pack()
    else:
        # Cash
        Label(frame, text="Enter the amount paid by the customer:", font=("Arial", 16)).pack()

        amount_paid_entry = Entry(frame, font=("Arial", 16))
        amount_paid_entry.pack()

        def calculate_change():
            try:
                amount_paid = float(amount_paid_entry.get())
                total_cost = costofmeal()
                change = amount_paid - total_cost

                Label(frame, text=f"Total Cost: ${total_cost:.2f}", font=("Arial", 16)).pack()
                Label(frame, text=f"Amount Paid: ${amount_paid:.2f}", font=("Arial", 16)).pack()
                Label(frame, text=f"Change: ${change:.2f}", font=("Arial", 16)).pack()

            except ValueError:
                Label(frame, text="Please enter a valid amount.", font=("Arial", 16)).pack()

        calculate_button = Button(frame, text="Calculate Change", command=calculate_change, font=("Arial", 16))
        calculate_button.pack()



    
    

checkOutBtn = Button(f3, padx=16, pady=1, bd=4, fg="black", font=("arial",16,"bold"), width=6, text="Check Out", command=checkout).grid(row=11, column=0, sticky="w", padx=(10, 0))
resetBtn = Button(f3, padx=16, pady=1, bd=4, fg="black", font=("arial",16,"bold"), width=6, text="Reset",command=reset).grid(row=11, column=0, sticky="e", padx=(0, 10))


txtFries.configure(state=DISABLED)
txtHamburger.config(state=DISABLED)





window.mainloop()