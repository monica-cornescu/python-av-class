class Vehicle():
  def __init__(self, wheels, max_weight):
    self.wheels = wheels
    self.speed = 0
    self._packages = [] 
    self.max_weight = max_weight

  def accelerate(self, amount):
    self.speed += amount

  def add_package(self, packages):
    if not isinstance(packages, list):
      packages = [packages]

    if self.max_weight < self._sum_package_weight(packages) + self.get_total_weight():
        raise Exception("Max weigt exceeded!!!")

    self._packages.extend(packages)
    
    

  def remove_package(self, package):
    self._packages.remove(package)

  def get_package_count(self):
    return len(self._packages)

  def get_total_weight(self):
    return self._sum_package_weight(self._packages)

  # TODO we can do better
  def _sum_package_weight(self, packages):
    ret = 0
    for package in packages:
      ret += package.weight
    return ret

  def get_total_volume(self):
    ret = 0
    for package in self._packages:
      ret += package.volume
    return ret

  # TODO 
  def get_packages(self):
    return self._packages

  


class Car(Vehicle):
  pass
