
class Animal:
    
    sound = "animal sound"
    increase_age_in_months = 1
    increase_required_food_in_kgs = 1
    
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: 10")
        else:
            self._age_in_months = age_in_months
        self._breed = breed
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._required_food_in_kgs = required_food_in_kgs
   
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    def grow(self):
        self._age_in_months+=self.increase_age_in_months
        self._required_food_in_kgs+=self.increase_required_food_in_kgs
    
    @classmethod 
    def make_sound(cls): 
        print(cls.sound)
        
        
class Land_animals:
    @classmethod
    def breathe(cls):
        print("Breathe in air")
    hunted_animal= "Deer"
    no_hunted_animal = 'deers'
    

class Water_animals:
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")
    hunted_animal= "GoldFish"
    no_hunted_animal = 'GoldFish'
    
        
class Hunting_animal:
    hunted_animal= "animal"
    no_hunted_animal = 'animal'
    def hunt(self,zoo):
        if self.hunted_animal in zoo.animal_list:
            zoo.animal_list.remove(self.hunted_animal)
        else:
            print('No {} to hunt'.format(self.no_hunted_animal))    
    
    
    
        
    
class Deer(Animal,Land_animals):
    sound = "Buck Buck"
    increase_age_in_months = 1
    increase_required_food_in_kgs = 2
    pass

class Lion(Animal,Land_animals,Hunting_animal):
    sound = "Roar Roar"
    increase_age_in_months = 1
    increase_required_food_in_kgs = 4
    
class Shark(Animal,Water_animals,Hunting_animal):
    sound = "Shark Sound"
    increase_age_in_months = 1
    increase_required_food_in_kgs = 8
    
class GoldFish(Animal,Water_animals):
    sound = "Hum Hum"
    increase_age_in_months = 1
    increase_required_food_in_kgs = 0.2
    

class Snake(Animal,Land_animals,Hunting_animal):
    sound = "Hiss Hiss"
    increase_age_in_months = 1
    increase_required_food_in_kgs = 0.5
    

class Zoo:
    total_animal_list = []
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self._animal_list = []
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    
    @property
    def animal_list(self):
        return self._animal_list 
    
    
    
    def add_food_to_reserve(self,food_quantity):
        self._reserved_food_in_kgs += food_quantity 
        
    
    def feed(self,animal):
        food = animal.required_food_in_kgs
        if self._reserved_food_in_kgs >0:
            animal.grow()
            self._reserved_food_in_kgs-=food

    def add_animal(self,animal):
        self._animal_list.append(type(animal).__name__)
        self.total_animal_list.append(type(animal).__name__)
        
    def count_animals(self):
        return len(self._animal_list)

    
    @classmethod
    def count_animals_in_all_zoos(cls):
        return(len(cls.total_animal_list))
        
        
    @staticmethod    
    def count_animals_in_given_zoos(zoo):
        total_no_animals = 0
        for i in zoo:
            total_no_animals +=i.count_animals()     
        return(total_no_animals)
        
        
        
        

        
        
        
        
        
        