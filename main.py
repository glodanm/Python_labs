from laba1 import Helicopter


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