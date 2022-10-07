class C2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
        
    def __str__(self):
            
        return f"{self.icap}i + {self.jcap}j "
    
class C3dvec(C2dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k
        
    def __str__(self):   
        return f"{self.icap}i + {self.jcap}j - {self.kcap}k"

vec2D=C2dvec(1,2)
vec3D=C3dvec(3,4,5)
print(vec2D)
print(vec3D)

        
        