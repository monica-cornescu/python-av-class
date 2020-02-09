from vehicles.vehicles import Car
from vehicles.package import Package


def main():

    morgan = Car(wheels=3, max_weight=170, max_volume=1800)

    ferrari = Car(wheels=4, max_weight=100, max_volume=200)

#    print(ferrari.speed, morgan.speed)

#    print(ferrari.wheels, morgan.wheels)

#    print(ferrari.speed)

#    print(ferrari.max_weight)

    p1 = Package(weight=20, volume=50)

    p2 = Package(weight=150, volume=100)

    p3 = Package(weight=10, volume=20)

    morgan.add_packages([p1, p2, p3])

    print(morgan.get_packages())

#    morgan.add_packages(p2)

    print(morgan.get_packages())

    print(f"packet count is: {morgan.get_package_count()}")

    print(f"total weight is: {morgan.get_total_weight()}")

    print(f"total volume is: {morgan.get_total_volume()}")


#   morgan.remove_package([p1, p3])


if __name__ == "__main__":
    main()
