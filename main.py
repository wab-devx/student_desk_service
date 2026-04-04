import os
from src.app import app
from src.reports import class_report

def display_menu() :
    print("\n==== Student Service Desk & Registrary ====")
    print("1) Add student")
    print("2) Uptade student")
    print("3) Delete student")
    print("4) Find student by ID")
    print("5) Search by name")
    print("6) Print class report")
    print("7) Create service ticket")
    print("8) List tickets (filter by status)")
    print("9) Resolve ticket")
    print("0) Exit\n")

def clear_screen() :
    if os.name == "nt" :
        os.system("cls")
    else :
        os.system("clear")

def main_menu() :
    while True :
        display_menu()
        ch = input("Choice : ")
        if ch == "1" :
            clear_screen()
            app.add_student()
        elif ch == "2" :
            clear_screen()
            app.update_student()
        elif ch == "3" :
            clear_screen()
            app.delete_student()
        elif ch == "4" :
            clear_screen()
            app.find_by_id()
        elif ch == "5" :
            clear_screen()
            app.search_by_name()
        elif ch == "6" :
            clear_screen()
            class_report()
        elif ch == "7" :
            clear_screen()
            app.create_service_ticket()
        elif ch == "8" :
            clear_screen()
            app.list_tickets()
        elif ch == "9" :
            clear_screen()
            app.resolve_ticket()
        elif ch == "0" :
            print("\nSee you later !")
            break 
        else :
            print("\nInvalid choice ! Please try again")
            continue
        
main_menu()
