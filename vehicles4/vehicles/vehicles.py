class Vehicle:
    def __init__(self, wheels, max_weight, max_volume):
        self.wheels = wheels
        self.speed = 0
        self._packages = []
        self.max_weight = max_weight
        self.max_volume = max_volume

        # initialized to -1 (as a marker to indicate value is not calculated)
        self._total_package_weight = -1
        self._total_package_volume = -1

    def accelerate(self, amount):
        self.speed += amount

    def add_packages(self, packages):
        if not isinstance(packages, list):
            packages = [packages]

        for p in packages:
            self.add_package(p)

    def add_package(self, package):
        if self._package_can_be_added(package):
            self._packages.append(package)
            # reset to -1 (should be recalculated if needed)
            self._total_package_weight = -1
            self._total_package_volume = -1

    def _package_can_be_added(self, package):
        return self._adding_package_will_not_exceed_max_weight(package) \
               and self._adding_package_will_not_exceed_max_volume(package)

    def _adding_package_will_not_exceed_max_weight(self, package):
        return self.max_weight >= package.weight + self.get_total_weight()

    def _adding_package_will_not_exceed_max_volume(self, package):
        return self.max_volume >= package.volume + self.get_total_volume()

    # remove only one package
    def remove_packages(self, packages):
        if not isinstance(packages, list):
            packages = [packages]

        for p in packages:
            self.remove_package(p)

    def remove_package(self, package):
        if package in self._packages:
            self._packages.remove(package)
            # reset to -1 (should be recalculated if needed)
            self._total_package_weight = -1
            self._total_package_volume = -1

    def get_package_count(self):
        return len(self._packages)

    def get_total_weight(self):
        if self._total_package_weight == -1:
            self._total_package_weight = self._sum_packages_weight(self._packages)
        return self._total_package_weight

    def get_total_volume(self):
        """returns sum of all package volumes"""
        if self._total_package_volume == -1:
            self._total_package_volume = self._sum_packages_volume(self._packages)
        return self._total_package_volume

    # TODO we can do better
    @staticmethod
    def _sum_packages_weight(packages):
        return sum([p.weight for p in packages])

    @staticmethod
    def _sum_packages_volume(packages):
        return sum([p.volume for p in packages])

    # TODO
    def get_packages(self):
        return self._packages


# return the packages which did not fit


class Car(Vehicle):
    pass
