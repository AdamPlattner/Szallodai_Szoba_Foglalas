from EgyagyasSzoba import SingleRoom
from KetagyasSzoba import DoubleRoom
from Lakosztaly import Suite
from Szalloda import Hotel
from Foglalas import Reservation


#Hotel létrehozása
hotel = Hotel()

#Hotelszobák létrehozása
hotel.add_room(SingleRoom("101", "25000"))  # Single + Price
hotel.add_room(SingleRoom("102", "25000"))  # Single + Price
hotel.add_room(DoubleRoom("201", "55000"))  # Double + Price
hotel.add_room(DoubleRoom("202", "55000"))  # Double + Price
hotel.add_room(Suite("501", "100000"))      # Suite + Price

hotel.add_room(SingleRoom("103", "25000"))  # Single + Price
hotel.add_room(SingleRoom("104", "25000"))  # Single + Price
hotel.add_room(SingleRoom("105", "25000"))  # Single + Price

hotel.add_room(DoubleRoom("203", "55000"))  # Double + Price
hotel.add_room(SingleRoom("204", "25000"))  # Single + Price
hotel.add_room(SingleRoom("205", "25000"))  # Single + Price


#Szobafoglalás létrehozása
hotel.book_room_by_number("102")
hotel.book_room_by_number("104")
hotel.book_room_by_number("203")
hotel.book_room_by_number("201")
hotel.book_room_by_number("205")

while True:
    print("")
    print("1. Foglalás")            # (Alap)
    print("2. Szaba Lista")         # (Alap)
    print("3. Ár Lista")            # (Alap)
    print("4. Lemondás")            # (Új)
    print("5. Véglegesítés")        # (Új) Mentett_foglalás.txt fáljba
    print("6. Kilépés")             # (Alap)

    user_choice = input("Válasz a fenti opciók közül: ")

    if user_choice == "1":
        room_number = input("Add meg a szobaszámát amit le szeretnél foglalni: ")
        hotel.book_room_by_number(room_number)

    elif user_choice == "2":
        print("Összes szaba:   ",hotel.listAllRooms())
        print("Elérhető szobák:", hotel.check_availability())

    elif user_choice == "3":
        print("Szoba árak:", hotel.get_room_prices())

    elif user_choice == "4":
        room_number = input("Add meg a szobaszámát amit le szeretnél mondani: ")
        hotel.book_unroom_by_number(room_number)

    elif user_choice == "5":
        hotel.saveToFile()

    elif user_choice == "6":
        break

