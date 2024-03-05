class Property:
    def __init__(self, area, rooms_amount, price, address):
        self.area = area
        self.rooms = rooms_amount
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms_amount, house_cost, house_address, plot_size):
        super().__init__(area, rooms_amount, house_cost, house_address)
        self.plot = plot_size

    def __str__(self):
        return (f"House:\n\tArea: {self.area}\n\tAmount of Rooms: {self.rooms}\n\t"
                f"House Price: {self.price}\n\tHouse Address: {self.address}\n\t"
                f"Plot Size: {self.plot}")


class Flat(Property):
    def __init__(self, area, rooms_amount, flat_cost, flat_address, floor):
        super().__init__(area, rooms_amount, flat_cost, flat_address)
        self.floor = floor

    def __str__(self):
        return (f"Flat:\n\tArea: {self.area}\n\tAmount of Rooms: {self.rooms}\n\t"
                f"Flat Price: {self.price}\n\tFlat Address: {self.address}\n\t"
                f"Flat Floor: {self.floor}")


house = House("Village", 3, 450000,
              "Zakopane, Ul. Pracowicza 19", "75 m^2")
flat = Flat("City", 6, 300000,
            "Katowice, Ul. Studencka 45", 2)

print(f"{house}\n")
print(flat)

