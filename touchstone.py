# This function takes in the device type, service type, damage type
# and warranty status to find the cost of the repair estimate
# after processing the data it will return the total cost
def getEstimate(deviceType, serviceType, damageType, warrantyStatus):
  total = 0

  # If the damage is accidental it will run this loop and provide cost based
  # on the device type. Phone/Tablet have the same cost
  if damageType == "accidental":
    if deviceType == "computer":
      total = 299
    elif deviceType == "smartwatch":
      total = 99
    else:
      total = 199

  #If the damage type is a hardware failure it will check if the device is
  # in or out of warranty and provide the cost based on this. Out of warranty
  # is $100 for any device, in warranty is $0
  if damageType == "hardware failure":
    if warrantyStatus == "oow":
      total = 100
    else:
      total = 0

  # If the damage type is a software failure it will check if the device is
  # in or out of warranty and provide the cost based on this. Out of warranty
  # is $50 for any device, in warranty is $0
  if damageType == "software failure":
    if warrantyStatus == "oow":
      total = 50
    else:
      total = 0

  #Free repairs(in warranty), do not have a mail-in cost. Other repair do
  # as such any repair over $0 that is mail-in gets $10 added to total
  if (serviceType == "mail-in" and total > 0):
    total += 10

  #Once the total is calculated it is returned
  return total


# This function will provide the URL relevant for the
def getLink(serviceType):
  if (serviceType == "mail-in"):
    return "www.xyzservice.py/mail-in"
  else:
    return "www.xyzservice.py/store-appointment"


# This function is to get the device type
# The while check will make sure the device type is one of the 4 valid types.
# Once a valid type is provided it will return the value
def getDevice():

  #list of the valid device types
  validTypes = ["phone", "smartwatch", "tablet", "computer"]

  print(
    "We provide service for the following type of devices \n (Phone, Tablet, Smartwatch, Computer)\n"
  )
  dType = input("Please enter your device Type: ").lower()

  #Check to make sure the entered value is a valid device type
  while dType not in validTypes:
    print("\nAttention: That is not a valid device type.\n")
    dType = input("Please enter your device Type: ").lower()

  return dType


# This function is to get the warranty starus
# The while check will make sure the device type is one of the 2 valid types.
# Once a valid type is provided it will return the value
def getWarranty():

  wStatus = input(
    "Is your device in warranty? Please enter Yes or No: ").lower()
  print(wStatus)

  #Check to make sure the entered value is a valid device type
  while wStatus not in ("yes", "no"):
    print("\nAttention: That is not a valid answer\n")
    wStatus = input(
      "Is your device in warranty? Please enter Yes or No: ").lower()

  if (wStatus == "yes"):
    wStatus = "in-warranty"
  else:
    wStatus = "out-of-warranty"

  return wStatus


# This function is to get the damage type
# The while check will make sure the device type is one of the 4 valid types.
# Once a valid type is provided it will return the value
def getDamage():

  #list of the valid device types

  print("We provide service for the following type of damage or failures \n ")
  print("1. Accidental")
  print("2. Hardware Failure")
  print("3. Software Failure\n")
  dmgType = input(
    "Please enter the number choice matching your damage or failure type: ")

  # Check to make sure the entered value is a valid number selection type
  # Due to input type accepting strings we have to make sure it matches as a string
  while dmgType not in ("1", "2", "3"):
    print("\nAttention: That is not a valid damage or failure type.\n")
    dmgType = input(
      "Please enter the number choice matching your damage or failure type: ")

  # Return the relevant damage type according to the choice made 
  if(dmgType == "3"):
    return "software failure"
  elif (dmgType == "2"):
    return "hardware failure"
  else:
    return "accidental"


# Main Section of the program

deviceType = ""
warrantyStatus = ""
damageType = ""
repairType = ""
serviceTotal = 0
serviceURL = ""
continueVar = False

deviceType = getDevice()
warrantyStatus = getWarranty()
damageType = getDamage()

print(deviceType)
print(warrantyStatus)
print(damageType)
