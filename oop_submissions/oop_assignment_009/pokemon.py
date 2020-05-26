class Pokemen:
    sound = "s"
    attack_method = ''
    attack_level = 10
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
    
    def __str__(self):
        return ("{} - Level {}".format(self.name,self.level))
    
    def attack(self):
        print('{} attack with {} damage'.format(self.attack_method,self.level*self.attack_level))

class Land:
    running = "run"
    @classmethod    
    def run(cls):
        print(cls.running)
        
class Water:
    swimming = "swim"
    @classmethod    
    def swim(cls):
        print(cls.swimming)


class Flying:
    flying = "fly"
    @classmethod
    def fly(cls):
        print(cls.flying)
        
class Pikachu(Pokemen,Land):
    sound = 'Pika Pika'
    running = 'Pikachu running...'
    attack_level = 10
    attack_method = "Electric"
    
class Squirtle(Pokemen,Land,Water):
    sound = 'Squirtle...Squirtle'
    running = 'Squirtle running...'
    swimming = 'Squirtle swimming...'
    attack_level = 9
    attack_method = "Water"
    
class Pidgey (Pokemen,Flying):
    sound = 'Pidgey...Pidgey'
    flying = 'Pidgey flying...'
    attack_level = 5
    attack_method = "Air"
    
class Swanna(Pokemen,Water,Flying):
    sound = 'Swanna...Swanna'
    flying = 'Swanna flying...'
    swimming = 'Swanna swimming...'
    attack_level = 9
    attack_method = "Water"
    def attack(self):
        super().attack()
        self.attack_level ,self.attack_method = 5 , "Air"
        super().attack()
    
class Zapdos(Pokemen,Flying):
    sound = 'Zap...Zap'
    flying = 'Zapdos flying...'
    attack_level = 10
    attack_method = "Electric"
    def attack(self):
        super().attack()
        self.attack_level , self.attack_method = 5,"Air"
        super().attack()
    
class Island:
    total_island_list =[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.total_island_list.append(self)
        
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
        return cls.total_island_list
        
class  Trainer:
    def __init__(self,name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = self._experience * 10
        self._food_in_bag = 0
        self._current_island = 'You are not on any island'
        self.total_catched_pokemon=[]
    
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
        return self._experience*10
        
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

    def catch(self,pokemon):
        if self.experience >=pokemon.level*100:
            print("You caught {}".format(pokemon.name))
            self._experience+=pokemon.level*20
            self.total_catched_pokemon.append(pokemon)
            pokemon.masters = self
        else:
            print('You need more experience to catch {}'.format(pokemon.name))
    def get_my_pokemon(self):
        return self.total_catched_pokemon
        
    def __str__(self):
        return self._name
        
'''        
my_zapdos = Zapdos(name="Ryan")
my_zapdos.attack()
'''    
    