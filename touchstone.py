# This function takes in the device type, service type, damage type
# and warranty status to find the cost of the repair estimate
# after processing the data it will return the total cost
def getEstimate(deviceType, serviceType, damageType, warrantyStatus):
  total = 0

  # If the damage is accidental it will run this loop and provide cost based
  # on the device type. Phone/Tablet have the same cost
  if damageType == "Accidental":
    if deviceType == "Computer/Laptop":
      total += 299
    elif deviceType == "Smartwatch":
      total += 99
    else:
      total += 199

  #If the damage type is a hardware failure it will check if the device is
  # in or out of warranty and provide the cost based on this. Out of warranty
  # is $100 for any device, in warranty is $0
  if damageType == "Hardware failure":
    if warrantyStatus == "Out of warranty":
      total += 100

  # If the damage type is a software failure it will check if the device is
  # in or out of warranty and provide the cost based on this. Out of warranty
  # is $50 for any device, in warranty is $0
  if damageType == "Software failure":
    if warrantyStatus == "Out of warranty":
      total += 50

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

    #Assigns the value based on the selected menu item 
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

    #Check to make sure the entered value is a valid device type
    while wStatus not in ("yes", "no"):
        print("\nAttention: That is not a valid answer\n")
        wStatus = input("Is your device in warranty? Please enter Yes or No: ").lower()

    #Assigns the value depending on in or out of warranty
    if (wStatus == "yes"):
        wStatus = "In warranty"
    else:
        wStatus = "Out of warranty"

    return wStatus


# This function is to get the damage type
# The while check will make sure the device type is one of the 4 valid types.
# Once a valid type is provided it will return the value
def getDamage():

    #list of the damage types using a numerical menu
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
    print("\nWe provide mail-in and store apponntment service options\n")
    print("1. Mail-in")
    print("2. Store appointment")
    serType = input("\nPlease enter the number choice matching the type requested: ")

    #Checks that there was a valid choice of 1 or 2 
    while serType not in ("1", "2"):
        print("\nAttention: That is not a valid selection.\n")
        serType = input("Please enter the number choice matching the service type requested: ")

    if(serType == "1"):
        return "Mail-in"
    else:
        return "Store appointment"

  


# Main Section of the program

#Sets up the variables with default values 
deviceType = ""
warrantyStatus = ""
damageType = ""
repairType = ""
serviceTotal = 0
serviceURL = ""
continueVar = True

#Hello menu to be shown on initialization 
print("\nWelcome to XYZ Service's Program:")
print("---------------------------------")

#The while loop will run once, if the customer doesn't provide yes to conitnue it will close out the program 
while continueVar:
    print("Please input the information requested to get a service estimate.\n")
    deviceType = getDevice()
    warrantyStatus = getWarranty()
    damageType = getDamage()
    repairType = getService()
    serviceURL = getLink(repairType)
    serviceTotal = getEstimate(deviceType, repairType, damageType, warrantyStatus)
    serviceTotal = format(serviceTotal, ".2f")

    print("\n\nService Estimate:")
    print("---------------------")
    print("Device type: " + deviceType)
    print("Warranty Status: " + warrantyStatus)
    print("Damage/Failure Type: " + damageType)
    print("Repair Type: " + repairType)
    print("Repair Quote(Subject to evaluation by repair tech) : $" + serviceTotal)
    print("To set up service please use the following URL:  (" + serviceURL + ")")
    
    #Check if the customer would like to process another service request
    choice = input("\nWould you like to get an estimate for another device? \n "
                   + " if so, enter Yes (other inputs will close out program): ").lower()
    
    if(choice != "yes"):
       continueVar = False
    
#Goodbye message for once the program is closes 
print("\nThanks for using the XYZ Service program, have a great day!\n")


