class Vehicle():
  def __init__(self, wheels, max_weight, max_volume):
    self.wheels = wheels
    self.speed = 0
    self._packages = [] 
    self.max_weight = max_weight
    self.max_volume = max_volume

  def accelerate(self, amount):
    self.speed += amount

  def add_packages(self, packages):
    if not isinstance(packages, list):
      packages = [packages]

    for p in packages:
      if self.max_weight >= p.weight + self.get_total_weight() and self.max_volume >= p.volume + self.get_total_volume():
          self._packages.append(p)

    
  # remove only one package
  def remove_package(self, packages):
    if not isinstance(packages, list):
      packages = [packages]
    for p in packages:
      if p in self._packages:
        self._packages.remove(p)

  def get_package_count(self):
    return len(self._packages)

  def get_total_weight(self):
    return self._sum_packages_weight(self._packages)

  def get_total_volume(self):
    return self._sum_packages_volume(self._packages)

  # TODO we can do better
  def _sum_packages_weight(self, packages):
    ret = 0
    return sum([p.weight for p in packages])

  def _sum_packages_volume(self, packages):
    ret = 0
    return sum([p.volume for p in packages])

  # TODO 
  def get_packages(self):
    return self._packages

# return the packages which did not fit


class Car(Vehicle):
  pass

