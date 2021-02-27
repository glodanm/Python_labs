class Helicopter:

    price = "1000 000 USD"
    @staticmethod
    def avg_price():
        return Helicopter.price


    def __init__(self, max_mass=0, name="missing value", max_height=0, color="missing value", height=0, producer="missing value"):
        self.max_mass = max_mass
        self.name = name
        self.max_height = max_height
        self.color = color
        self.height = height
        self.producer = producer

    
    def __del__(self):
        pass
    
    def __str__(self):
        return "Max mass(in kilos): " + str(self.max_mass) + "\nName: " + self.name + "\nMax height(in meters): " + str(self.max_height) + "\nColor: " + self.color + "\nHeight(): " + str(self.height) + "\nProducer: " + self.producer

def main():
    helicopter1 = Helicopter("1000", "Galya", "Red")
    print(helicopter1.__str__())
    print(f"Price: {helicopter1.avg_price()} \n")

    
    helicopter2 = Helicopter("1750", "Potter", "5000", "Brown")
    print(helicopter2.__str__())
    print(f"Price: {helicopter2.avg_price()} \n")

    
    helicopter3 = Helicopter("1400", "Time4Fly", "4750", "White", "Made in USA")
    print(helicopter3.__str__())
    print(f"Price: {helicopter3.avg_price()} \n")

if __name__ == "__main__":
    main()