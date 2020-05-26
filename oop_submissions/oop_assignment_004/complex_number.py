
import math
class ComplexNumber:
    def __init__(self,real=0,img=0):
        
        
        if type(real) is str and type(img) is str :  
            raise ValueError("Invalid value for real and imaginary part")
        elif type(img) is str:    
            raise ValueError("Invalid value for imaginary part")
        elif type(real) is str :
            raise ValueError("Invalid value for real part")
        else:
            self.real_part = real
            self.imaginary_part = img
            
    def __str__(self):
        return "{}{:+}i".format(self.real_part,self.imaginary_part)
        
    
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
    
    
    def __add__(self,other):
        return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
    
    def __sub__(self,other):
        return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
        
    
    def __mul__(self,other):
        return ComplexNumber(self.real_part*other.real_part-self.imaginary_part*other.imaginary_part,self.imaginary_part*other.real_part+self.real_part*other.imaginary_part)
    
    
    def __truediv__(self,other):
        sr, si, oR, oi = self.real_part, self.imaginary_part,other.real_part, other.imaginary_part
        r = float(oR**2 + oi**2)
        other.imaginary_part = -other.imaginary_part
        # print((sr*oR+si*oi)/r, (si*oR-sr*oi)/r)
        #return ComplexNumber((sr*oR+si*oi)/r, (si*oR-sr*oi)/r)
        
        real = self*other
        #print(real)
        return ComplexNumber(real.real_part/r,real.imaginary_part/r)
        
        
        
        
        
        
     
        
    def __abs__(self):
        return round(math.sqrt(self.real_part**2 + self.imaginary_part**2),3)
        
        
        
    def __eq__(self, other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part    
        
"""        
a= ComplexNumber(1,2)
b=ComplexNumber(3,4)
d= a*b
c= a/b
print(c)
print(d)
"""