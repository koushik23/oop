import math
from car import Car
class RaceCar(Car):
    
    sound="Peep Peep\nBeep Beep"
    
    
    def accelerate(self):
        super().accelerate()
        if self.nitro >0 and self._is_engine_started == True:
            additional_acceleration=math.ceil(self._acceleration*0.3)
            self._car_current_speed +=additional_acceleration
            self.nitro-=10
        if self._car_current_speed > self._max_speed:
            self._car_current_speed = self._max_speed
        
    def apply_brakes(self):
        if self._car_current_speed >=self._max_speed//2 :
            self.nitro+=10
        super().apply_brakes()
        
        
        
        
        
        
"""
racecar = RaceCar(color="Red", max_speed=250, acceleration=50, tyre_friction=30)  
racecar.start_engine()  
racecar.accelerate()  
racecar.accelerate()  
racecar.accelerate()   
print(racecar.current_speed)
  
racecar.apply_brakes()
print(racecar.current_speed)

print(racecar.nitro)  
 
racecar.accelerate()  
print(racecar.current_speed)

print(racecar.nitro)

racecar.apply_brakes()
print(racecar.nitro)
racecar.accelerate()
print(racecar.nitro)
racecar.sound_horn()  # Prints

racecar1 = RaceCar(color="Red", max_speed=250, acceleration=50, tyre_friction=30)
racecar1.start_engine()  
racecar1.accelerate()  
racecar1.accelerate()  
racecar1.accelerate()   
print(racecar1.current_speed)
  
racecar1.apply_brakes()
print(racecar1.current_speed)

print(racecar1.nitro)  
 
racecar1.accelerate()  
"""