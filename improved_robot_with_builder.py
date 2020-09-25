from abc import ABC, abstractmethod  # For Builder classes

class Robot:

  # Like keywords code, we prefer creating the init in that way except implementing robot name types None. 
  # We also added "army".
  def __init__(self, army = "", bipedal = "", 
          quadripedal = "", wheeled = "", flying = "", 
          traversal = [], detection_systems = []):

    self.army = army
    self.bipedal = bipedal
    self.quadripedal = quadripedal
    self.wheeled = wheeled
    self.flying = flying
    self.traversal = traversal
    self.detection_systems = detection_systems
 
  def __str__(self):
    
    # https://realpython.com/python-f-strings/
    # For creating the string, we used that way.

    string = f"{self.army}{self.bipedal}{self.quadripedal}{self.wheeled}{self.flying} ROBOT. \n"

    if self.traversal:
      string += "Traversal modules installed:\n"

    for module in self.traversal:
      string += "- " + str(module) + "\n"

    if self.detection_systems:
      string += "Detection systems installed:\n"

    for system in self.detection_systems:
      string += "- " + str(system) + "\n"

    return string
   
#---------------------------------------------------------------------------

# Concrete classes for components
# We did our concrete classes like two separate classes.
# And, we put our robot subcomponents into the them as attributes.

class Traversal:

  def __init__(self):
    self.two_pedals = "two legs"
    self.four_pedals = "four legs"
    self.arms = "two arms"
    self.wings = "wings"
    self.two_wheels = "two wheels"
    self.four_wheels = "four wheels"
    self.blades = "blades"
    self.magnifying_glass = "magnifying glasses"
    self.weapons = "weapons"

class DetectionSystem:
  def __init__(self):
    self.camera = "cameras"
    self.infrared = "infrareds"
    self.sensor = "sensors"

#----------------------------------------------------------------------------

class RobotBuilder(ABC):
    
  # We collected __init__, reset, and get_product methods into the RobotBuilder because of the advantages of abstract class.
  def __init__(self):
    self.product = Robot()

  def reset(self):
    self.product = Robot()

  def get_product(self):
        return self.product
  
  # For Builder Pattern, we use getter and setter here.
  @abstractmethod
  def getTraversal(self):
    pass
  
  def setTraversal(self):
    pass
  
  @abstractmethod
  def build_detection_system(self):
    pass

class AndroidBuilder(RobotBuilder):

  # For Builder Pattern, we use getter and setter here.
  def getTraversal(self):
    self.product.bipedal = "BIPEDAL"
  
  def setTraversal(self):
    self.product.traversal.append(traversal_object.two_pedals)
    self.product.traversal.append(traversal_object.arms)
  
  def build_detection_system(self):
    self.product.detection_systems.append(detect_sys_object.camera)

class AutonomousCarBuilder(RobotBuilder):

  # For Builder Pattern, we use getter and setter here.
  def getTraversal(self):
    self.product.wheeled = "WHEELED"
  
  def setTraversal(self):
    self.product.traversal.clear()
    self.product.traversal.append(traversal_object.four_wheels)

  def build_detection_system(self):
    self.product.detection_systems.clear()
    self.product.detection_systems.append(detect_sys_object.infrared)

# We created ArmyAndroidBuilder for a new robot.
class ArmyAndroidBuilder(RobotBuilder):

  # For Builder Pattern, we use getter and setter here.
  def getTraversal(self):
    self.product.army = "MILITARY"
  
  def setTraversal(self):
    self.product.traversal.clear()
    self.product.traversal.append(traversal_object.weapons)
    self.product.traversal.append(traversal_object.blades)
    self.product.traversal.append(traversal_object.magnifying_glass)

  def build_detection_system(self):
    self.product.detection_systems.clear()
    self.product.detection_systems.append(detect_sys_object.sensor)
    self.product.detection_systems.append(detect_sys_object.camera)

#-------------------------------------------------------------------------

class Director:

  # We again collected the same calls into a method.
  def make_robot(self, builder):
        builder.getTraversal()
        builder.setTraversal()
        builder.build_detection_system()
        return builder.get_product()
        
director = Director()

# Creating object for concrete Traversal Class to use its attributes
traversal_object = Traversal()

# Creating object for concrete Detection System Class to use its attributes
detect_sys_object = DetectionSystem()

print()

builder = AndroidBuilder()
print(director.make_robot(builder))

builder = AutonomousCarBuilder()
print(director.make_robot(builder))

builder = ArmyAndroidBuilder()
print(director.make_robot(builder))
