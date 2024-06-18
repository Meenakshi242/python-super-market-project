import smtplib
import random
import datetime

def main():
    menu = {}
    with open("menu.txt", "r") as file:
        for line in file:
            item, price = line.split(',')
            menu[item] = float(price)

    print("*** A TO Z SUPER MARKET ***")
    print("***** Welcome sir/madam, here is our menu *****")
    for item, price in menu.items():
        print(f"{item}: Rs.{price}")

    order = {}
    total_cost=0
    discount_rate = 10
    gst_rate = 12

    while True:
        item = input("Enter the item you want to order (or 'yes' to finish): ").lower()
        if item == 'yes':
            break
        
        if item not in menu:
            print("Sorry, that item is not available.")
            continue
            
        quantity = int(input(f"Add quantity of {item}: "))
      
        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity

        print("\n--- Bill Summary ---")
        for item, quantity in order.items():
            print(f"{item}: {quantity}")
        
        total_cost = sum(menu[item] * order[item] for item in order)
        
        if total_cost >= 1000:
            discount_amount = (discount_rate / 100) * total_cost
            offer_price = total_cost - discount_amount
            print(f"You ordered above Rs.1000, so your discounted price is Rs.{offer_price}")
        else:
            discount_amount = 0
        
        gst_amount = (total_cost - discount_amount) * (gst_rate / 100)
        
        total_cost = total_cost - discount_amount + gst_amount
        
    
        f=open("bill.txt", "w") 
        x = datetime.datetime.now()
        present_day = x.strftime("%A")
        current_month = x.strftime("%B")

        f.write(f"Date: {x}\n")
        f.write(f"Day: {present_day}\n")
        f.write(f"Month: {current_month}\n")
        f.write("\nBILL SUMMARY:\n")
        
        f.write(f"\nDiscount ({discount_rate}%): Rs.{discount_amount:.2f}\n")
        f.write(f"GST ({gst_rate}%): Rs.{gst_amount:.2f}\n")
        f.write(f"Total cost (including GST): Rs.{total_cost:.2f}")
        
        print("Bill generated successfully")
        print(f"Discount ({discount_rate}%): Rs.{discount_amount:.2f}")
        print(f"GST ({gst_rate}%): Rs.{gst_amount:.2f}")
        print(f"Total cost (including GST): Rs.{total_cost:.2f}")
        
        try:
            receiver_mail=["meenuraguraman@gmail.com"]
            for i in receiver_mail:
                total_bill=total_cost
                print(i,total_bill)
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login("meena2003dummy@gmail.com","uskm amoh chsp aguv")
                message=(f"your total bill is {total_bill}")
                s.sendmail=("meena2003dummy@gmail.com",i,message)
                s.quit()
                print("mail send successfully")
        except:
            print("mail not sent")

    print("Thank you for visiting!")

if __name__ == "__main__":
    main()
