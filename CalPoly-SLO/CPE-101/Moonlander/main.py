def main():
    showWelcome()
    altitude = getAltitude()
    fuel = getFuel()
    
    velocity = 0.00
    acceleration = 0.00
    gravity = 1.62
    time = 0
    fuelRate = 0
    while altitude > 0:
        if time == 0:
            print ''
            print 'LM state at retrorocket cutoff'
        if fuel > 0:
            displayLMState(time,altitude,velocity,fuel,fuelRate)
            fuelRate = getFuelRate(fuel)
            fuel = updateFuel(fuel, fuelRate)
        else: 
            fuelRate = 0
            print 'OUT OF FUEL - Elapsed Time:  {0:d} Altitude:  {1:.2f} Velocity:  {2:.2f}'.format(time,altitude,velocity)
        acceleration = updateAcceleration(gravity,fuelRate)
        altitude = updateAltitude(altitude,velocity,acceleration)
        velocity = updateVelocity(velocity,acceleration)
        time += 1

   
    else:
        print ''
        print 'LM state at landing/impact'
        displayLMState(time,altitude,velocity,fuel,fuelRate)
        displayLMLandingStatus(velocity)



def showWelcome():
    a = 'Welcome aboard the Lunar Module Flight Simulator\n'
    b = "   To begin you must specify the LM's initial altitude"
    c = '   and fuel level.  To simulate the actual LM use'
    d = '   values of 1300 meters and 500 liters, respectively.\n'
    e = '   Good luck and may the force be with you!\n'

    print a; print b; print c; print d; print e
   

def getFuel():
    fuel = 0
    while fuel <= 0: 
        fuel = int(raw_input("Enter the initial amount of fuel on board the LM (in liters): "))
        if fuel <= 0:
            print 'ERROR: Amount of fuel must be positive, please try again '
	    continue
	else: 
	    return fuel 

def getAltitude():
    alt = 0
    while alt < 1 or alt > 9999: 
        alt = int(raw_input("Enter the initial altitude of the LM (in meters): "))
        if alt < 1 or alt > 9999:
            print 'ERROR: Altitude must be between 1 and 9999, inclusive, please try again '
	    continue
        else: 
	    return float(alt)
   

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    print 'Elapsed Time:    {0:d} s'.format(elapsedTime)   
    print '        Fuel:    {0:d} l'.format(fuelAmount)
    print '        Rate:    {0:d} l/s'.format(fuelRate)
    print '    Altitude:    {0:.2f} m'.format(altitude)
    print '    Velocity:    {0:.2f} m/s'.format(velocity)
    print ''

def getFuelRate(currentFuel):
    fuelRate = -1
    while fuelRate < 0 or fuelRate > 9: 
        fuelRate = int(raw_input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
        if fuelRate < 0 or fuelRate > 9:
            print 'ERROR: Fuel rate must be between 0 and 9, inclusive '
	    continue
        elif currentFuel < fuelRate: 
            return currentFuel
        else:
            return fuelRate

def updateAcceleration(gravity, fuelRate):
    return gravity * ((fuelRate / 5.0) - 1) 


def updateAltitude(altitude, velocity, acceleration):
    if (altitude + velocity + (acceleration / 2.0)) < 0 : 
	return 0
    else:    
	return altitude/1.0 + velocity/1.0 + (acceleration / 2.0)


def updateVelocity(velocity, acceleration):
    return velocity + acceleration


def updateFuel(fuel, fuelRate):
    if (fuel - fuelRate) < 0 : 
	return 0
    else:
	return fuel - fuelRate


def displayLMLandingStatus(velocity):
    if velocity > -1 and velocity < 0:
        print 'Status at landing - The eagle has landed!'
    elif velocity < -1 and velocity > -10:
        print 'Status at landing - Enjoy your oxygen while it lasts!'
    elif velocity > 0:
        print 'Wow, this wasn''t supposed to happen. How''d you manage to land with a positive velocity?'
    else:
        print 'Status at landing - Ouch - that hurt!'
    

if __name__ == "__main__":
    main()
