from EgyagyasSzoba import SingleRoom
from KetagyasSzoba import DoubleRoom
from Lakosztaly import Suite
from Szalloda import Hotel


class BookingSystem:
    def __init__(self):
        self.hotel = Hotel()

    def load_data(self):
        self.hotel.add_room(SingleRoom("101", "25000")) # Single + Price
        self.hotel.add_room(SingleRoom("102", "25000")) # Single + Price
        self.hotel.add_room(DoubleRoom("201", "55000")) # Double + Price
        self.hotel.add_room(DoubleRoom("202", "55000")) # Double + Price
        self.hotel.add_room(Suite("501", "100000"))     # Suite + Price

    def user_interact(self):
        while True:
            print("1. Foglalás")            # (Alap)
            print("2. Szaba Lista")         # (Alap)
            print("3. Ár Lista")            # (Alap)
            print("4. Kilépés")             # (Alap)
            print("5. Lemondás")            # (Új)
            print("6. Véglegesítés")        # (Új)

            user_choice = input("Válasz a fenti opciók közül: ")

            if user_choice == "1":
                room_number = input("Add meg a szobaszámát amit le szeretnél foglalni: ")
                self.hotel.book_room_by_number(room_number)
                print(f"A {room_number} szoba sikeresen lefoglalva")

            elif user_choice == "2":
                print("Elérhető szobák:", self.hotel.check_availability())

            elif user_choice == "3":
                print("Szoba árak:", self.hotel.get_room_prices())

            elif user_choice == "4":
                break





booking_system = BookingSystem()
booking_system.load_data()
booking_system.user_interact()