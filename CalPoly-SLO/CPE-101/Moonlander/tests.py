import moonlander
assert moonlander.updateAcceleration(4, 5) == 0
assert moonlander.updateAcceleration(4, 10) == 4.0
assert moonlander.updateAcceleration(4, 0) == -4

assert moonlander.updateAltitude(100, -100, -10) == 0 
assert moonlander.updateAltitude(100, 0, -10) == 95.0
assert moonlander.updateAltitude(5, -5, 0) == 0 

assert moonlander.updateVelocity(100, -100) == 0 
assert moonlander.updateVelocity(100, -105) == -5
assert moonlander.updateVelocity(5, 0) == 5.0 

assert moonlander.updateFuel(100, 100) == 0 
assert moonlander.updateFuel(100, 105) == 0 
assert moonlander.updateFuel(5, 0) == 5 
