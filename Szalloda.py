
class Hotel:
    def __init__(self):
        self.room = []
        self.booking = []

    def add_room(self, room):
        self.room.append(room)

    def listAllRooms(self):
        available_room = []
        for room in self.room:
            available_room.append(room.number)
        return available_room

    def check_availability(self):
        available_room = []
        for room in self.room:
            if not room.is_booked:
                available_room.append(room.number)

        return available_room

    def book_room_by_number(self, number):
        for room in self.room:
            if room.number == number:
                    return room.book_room()
        print("\nA megadott szobaszám nem létezik a szállodában.")

    def book_unroom_by_number(self, number):
        for room in self.room:
            if room.number == number:
                    return room.unbook_room()
        print("\nA megadott szobaszám nem létezik a szállodában.")

    def get_room_prices(self):
        return {room.number: room.price for room in self.room}

    def saveToFile(self):
        f = open("demofile3.txt", "w")
        f.write("Az Ön által lefoglalt szobák listája:\n")
        f.write("\n")
        osszes = 0
        for room in self.room:
            if room.is_booked:
                f.write(f"{room.number} --- {room.price}Ft")
                osszes = osszes + int(room.price)
                f.write("\n")
        f.write("\n")
        f.write(f"Szobák ára összessen: {osszes}Ft")
        f.close()


