print ("BUDGET TRACKER")

print ("Vitajte v programe Budget Tracker pre sledovanie Vašich financií.")

main_menu = ("1.Príjmy\n2.Výdavky\n3.Zostatok\n4.Koniec")
choice_menu = (" ")
all_income = 0
all_cost = 0

while choice_menu != "4":

    print ("MENU")
    print (main_menu)
    choice_menu = input("Pre pokračovanie zadajte poradové číslo kategórie z menu: ")



    if choice_menu == "1":


        print ("Vaše príjmy:")

    
    
        income_Q = input ("Chcete zadať ďalšiu prijatú sumu? áno/nie\n")

        while income_Q != "nie":
            add_income = (float(input("Zadajte sumu: ")))
            all_income = all_income + add_income
            print (f"Vaše príjmy spolu predstavujú {all_income} eur.")
            income_Q = input ("Chcete zadať ďalšiu prijatú sumu? áno/nie\n")

        print (f"V poriadku. Výška Vašich príjmov je {all_income} eur.")



    elif choice_menu == "2":


        print ("Vaše výdavky")

    

        cost_Q = input ("Chcete zadať nejaké nové výdavky? áno/nie\n")

        while cost_Q != "nie":
            add_cost = (float(input("Zadajte sumu: ")))
            all_cost = all_cost + add_cost
            print (f"Vaše výdavky spolu predstavujú {all_cost} eur.")
            cost_Q = input ("Chcete zadať nejaké nové výdavky? áno/nie\n")
        
        print (f"V poriadku. Výška Vašich výdavkov je {all_cost} eur.")
        print ("Pre ďalšie operácie sa vráťte, prosím, do menu.")




    elif choice_menu == "3":

        remaining = 0
        remaining = all_income - all_cost
        print (f"Váš zostatok je {remaining} eur")



    elif choice_menu == "4":

        print ("Koniec")


