# This function takes in the device type, service type, damage type
# and warranty status to find the cost of the repair estimate
# after processing the data it will return the total cost
def getEstimate(deviceType, serviceType, damageType, warrantyStatus):
  total = 0

  # If the damage is accidental it will run this loop and provide cost based
  # on the device type. Phone/Tablet have the same cost
  if damageType == "accidental":
    if deviceType == "Computer/Laptop":
      total = 299
    elif deviceType == "Smartwatch":
      total = 99
    else:
      total = 199

  #If the damage type is a hardware failure it will check if the device is
  # in or out of warranty and provide the cost based on this. Out of warranty
  # is $100 for any device, in warranty is $0
  if damageType == "Hardware Failure":
    if warrantyStatus == "Out of warranty":
      total = 100
    else:
      total = 0

  # If the damage type is a software failure it will check if the device is
  # in or out of warranty and provide the cost based on this. Out of warranty
  # is $50 for any device, in warranty is $0
  if damageType == "Software Failure":
    if warrantyStatus == "Out of warranty":
      total = 50
    else:
      total = 0

  #Free repairs(in warranty), do not have a mail-in cost. Other repair do
  # as such any repair over $0 that is mail-in gets $10 added to total
  if (serviceType == "Mail-in" and total > 0):
    total += 10

  #Once the total is calculated it is returned
  return total


# This function will provide the URL relevant for the
def getLink(serviceType):
  if (serviceType == "Mail-in"):
    return "www.xyzservice.py/mail-in"
  else:
    return "www.xyzservice.py/store-appointment"


# This function is to get the device type
# The while check will make sure the device type is one of the 4 valid types.
# Once a valid type is provided it will return the value
def getDevice():

    print("\nWe provide service for the following type of devices:")
    print("1. Phone/Tablet")
    print("2. Smartwatch")
    print("3. Computer/Laptop \n")
    dType = input("\nPlease enter the number that matches your device type: ")

    # Check to make sure the entered value is a valid selection,
    # we are looking for a number but input takes values in as string as such it checks
    # against strings of the numbers 
    while dType not in ("1", "2", "3"):
        print("\nAttention: That is not a valid selection.\n")
        dType = input("Please enter the number that matches your device type: ")


    if(dType == "1"):
        return "Phone/Tablet"
    elif(dType == "2"):
        return "Smartwatch"
    else: 
        return "Computer/Laptop"


# This function is to get the warranty starus
# The while check will make sure the device type is one of the 2 valid types.
# Once a valid type is provided it will return the value
def getWarranty():

    wStatus = input("\nIs your device in warranty? Please enter Yes or No: ").lower()
    print(wStatus)

    #Check to make sure the entered value is a valid device type
    while wStatus not in ("yes", "no"):
        print("\nAttention: That is not a valid answer\n")
        wStatus = input("Is your device in warranty? Please enter Yes or No: ").lower()

    if (wStatus == "yes"):
        wStatus = "In warranty"
    else:
        wStatus = "Out of warranty"

    return wStatus


# This function is to get the damage type
# The while check will make sure the device type is one of the 4 valid types.
# Once a valid type is provided it will return the value
def getDamage():

    #list of the valid device types

    print("\nWe provide service for the following type of damage or failures")
    print("1. Accidental")
    print("2. Hardware Failure")
    print("3. Software Failure\n")
    dmgType = input("\nPlease enter the number choice matching your damage or failure type: ")

    # Check to make sure the entered value is a valid number selection type
    # Due to input type accepting strings we have to make sure it matches as a string
    while dmgType not in ("1", "2", "3"):
        print("\nAttention: That is not a valid selection.\n")
        dmgType = input("Please enter the number choice matching your damage or failure type: ")

    # Return the relevant damage type according to the choice made 
    if(dmgType == "3"):
        return "Software failure"
    elif (dmgType == "2"):
        return "Hardware failure"
    else:
        return "Accidental"

# This function will get the service type (mail-in or store)
def getService():
    print("\nWe provide mail-in and store apponntment service options")
    print("1. Mail-in")
    print("2. Store appointment")
    serType = input("\nPlease enter the number choice matching the type requested: ")

    while serType not in ("1", "2"):
        print("\nAttention: That is not a valid selection.\n")
        serType = input("Please enter the number choice matching the service type requested: ")

    if(serType == "1"):
        return "Mail-in"
    else:
        return "Store appointment"

  


# Main Section of the program

deviceType = ""
warrantyStatus = ""
damageType = ""
repairType = ""
serviceTotal = 0
serviceURL = ""
continueVar = False

while !continueVar:
    deviceType = getDevice()
    warrantyStatus = getWarranty()
    damageType = getDamage()
    repairType = getService()
    serviceURL = getLink(repairType)
    serviceTotal = getEstimate(deviceType, repairType, damageType, warrantyStatus)
      



print(deviceType + "\n")
print(warrantyStatus + "\n")
print(damageType + "\n")
print(repairType + "\n")
print(serviceURL +  "\n")
print(serviceTotal)