class Package():

  def __init__(self, weight, volume):

      self.weight = weight

      self.volume = volume



  def __repr__(self):

    return f"package weight {self.weight} volume {self.volume}"