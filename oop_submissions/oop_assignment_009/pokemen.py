class pokemen:
    
    sound = "s"
    running = "r"
    swimming = "ju"
    flying = 10
    def __init__(self,name,level=1):
        if len(name)<=0:
            raise ValueError ("name cannot be empty")
        else:
            self._name = name
        if level<=0:
            raise ValueError ("level should be > 0")
        else:
            self._level = level
        
        self.masters = "No Master"
    
    
    @property
    def name (self):
        return self._name
    @property
    def level(self):
        return self._level
    @property
    def master(self):
        if self.masters!="No Master":
            return self.masters
        else:    
            print(self.masters)
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod    
    def run(cls):
        print(cls.running)
        
    @classmethod    
    def swim(cls):
        print(cls.swimming)
    @classmethod
    def fly(cls):
        print(cls.flying)
        
        
        
    def __str__(self):
        return ("{} - Level {}".format(self.name,self.level))
        
    
    
class Pikachu(pokemen):
    sound = 'Pika Pika'
    running = 'Pikachu running...'
    def attack(self):
        print("Electric attack with {} damage".format(self.level*10))
    
    
    
class Squirtle(pokemen):
    sound = 'Squirtle...Squirtle'
    running = 'Squirtle running...'
    swimming = 'Squirtle swimming...'
    def attack(self):
        print("Water attack with {} damage".format(self.level*9))
    
    
    
class Pidgey (pokemen):
    sound = 'Pidgey...Pidgey'
    flying = 'Pidgey flying...'
    def attack(self):
        print('Air attack with {} damage'.format(self.level*5))
    

class Swanna(pokemen):
    sound = 'Swanna...Swanna'
    flying = 'Swanna flying...'
    swimming = 'Swanna swimming...'
    def attack(self):
        print("Water attack with {} damage".format(self.level*9))
        print("Air attack with {} damage".format(self.level*5))
    
    

class Zapdos(pokemen):
    sound = 'Zap...Zap'
    flying = 'Zapdos flying...'
    def attack(self):
        print("Electric attack with {} damage".format(self.level*10))
        print("Air attack with {} damage".format(self.level*5))
    
            
class Island:
    total_list =[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.total_list.append(self)
        
    @property    
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property    
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property    
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
        
    def add_pokemon(self,poky):
        if self._pokemon_left_to_catch<self._max_no_of_pokemon :
            self._pokemon_left_to_catch +=1
        else:
            print("Island at its max pokemon capacity")
            
    def __str__(self):
        return ("{} - {} pokemon - {} food".format(self.name,self.pokemon_left_to_catch,self.total_food_available_in_kgs))
        
    @classmethod
    def get_all_islands(cls):
        return cls.total_list


class  Trainer:
    a = ''
    
    def __init__(self,name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = self._experience * 10
        self._food_in_bag = 0
        self._current_island = 'You are not on any island'
        self.total=[]
    
    @property    
    def name (self):
        return self._name
    @property    
    def experience(self):
        return self._experience
    @property
    def current_island (self):
        if self._current_island == 'You are not on any island' :  
            print(self._current_island)
        else:    
            return (self._current_island)
    @property
    def food_in_bag(self):
        return self._food_in_bag
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    
    
    
    
    def move_to_island(self,island):
        self._current_island = island
        self.island = island
    def collect_food(self):
        if self._current_island == 'You are not on any island' :
            print('Move to an island to collect food')
        elif self.food_in_bag !=self._max_food_in_bag:
            if self.island._total_food_available_in_kgs>=self._max_food_in_bag:
                self.island._total_food_available_in_kgs-=self._max_food_in_bag
                self._food_in_bag+=self._max_food_in_bag
            elif self.island._total_food_available_in_kgs > 0:
                self._food_in_bag+=self.island._total_food_available_in_kgs
                self.island._total_food_available_in_kgs=0
            if self._food_in_bag>self._max_food_in_bag:
                self._food_in_bag = self.max_food_in_bag
            
    def catch(self,pokemon):
        if pokemon.level ==1 and self.experience >=100:
            print("You caught {}".format(pokemon.name))
            self._experience+=20
            self.total.append(pokemon)
            pokemon.masters = self
        elif pokemon.level>1 and self.experience >=(100+pokemon.level*10):
            print("You caught {}".format(pokemon.name))
            self._experience+=pokemon.level*10
            pokemon.masters = self
            self.total.append(pokemon)
            
        else:
            print('You need more experience to catch {}'.format(pokemon.name))
        
    
    def get_my_pokemon(self):
        return self.total
        
    def __str__(self):
        return self._name



