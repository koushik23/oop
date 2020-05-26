class Car:
    sound = 'Beep Beep'
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self._color = color 
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._is_engine_started = False
        self._car_current_speed = 0
        self.nitro = 0
        #self.sound = 'Beep Beep'
        if self._max_speed <0:
            raise ValueError('Invalid value for max_speed')
        
                
        if self._acceleration <0:
            raise ValueError('Invalid value for acceleration')
                
            
        if self._tyre_friction<0:
            raise ValueError('Invalid value for tyre_friction')
        
    @property
    def color (self):
        return self._color
        
    
    @property
    def max_speed(self):
        return self._max_speed
    
    @property
    def acceleration(self):
        return self._acceleration
    
    
    @property
    def tyre_friction(self):
        return self._tyre_friction
    
    @property
    def current_speed(self):
        return self._car_current_speed
    
    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    
        
    def start_engine(self):
        self._is_engine_started = True
        
    def accelerate(self):
        if self._is_engine_started == True:
            self._car_current_speed+=self._acceleration
            if self._car_current_speed > self._max_speed:
                self._car_current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
            
        
    def apply_brakes(self):
        self._car_current_speed -= self._tyre_friction
        if self._car_current_speed < 0:
            self._car_current_speed = 0
            
    def sound_horn(self):
        if self.is_engine_started == True:
            print(self.sound)
        else:
            print("Start the engine to sound_horn")
            
    def stop_engine(self):
        self._is_engine_started = False

    

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

car.sound_horn()  # Prints

"""