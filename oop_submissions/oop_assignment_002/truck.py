'''
class Truck:
    
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        self._color = color 
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._is_engine_started = False
        self._car_current_speed = 0
        self._max_cargo_weight = max_cargo_weight
        self._total_load = 0
        
        if self._max_speed <0:
            raise ValueError('Invalid value for max_speed')
        
                
        if self._acceleration <0:
            raise ValueError('Invalid value for acceleration')
            
            
        if self._tyre_friction<0:
            raise ValueError('Invalid value for tyre_friction')
        
        if self.max_cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')
        

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
    
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
       
       
       
       
       
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
        if self._is_engine_started == True:
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")
            
    def stop_engine(self):
        self._is_engine_started = False
'''

from car import Car
class Truck(Car):
    sound = "Honk Honk"
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._total_load =0
        self._current_load =0
        if max_cargo_weight >0:
            self._max_cargo_weight = max_cargo_weight
        else:
            raise ValueError("Invalid Value for cargo_weight")
    
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    

    def load(self,current_load):
        if current_load>0:
            if self._car_current_speed > 0:
                print("Cannot load cargo during motion")
            else:
                if self._total_load+current_load >=self._max_cargo_weight:
                    print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
                else:
                    self._total_load+=current_load
        else:
            raise ValueError("Invalid value for cargo_weight")
        
        
        
        
    
    def unload(self,current_load):
        if current_load > 0:
            if self._car_current_speed > 0:
                print("Cannot unload cargo during motion")        
            else:
                self._total_load-= current_load
        else:
            raise ValueError("Invalid value for cargo_weight")
        
       
    
    
    
    

