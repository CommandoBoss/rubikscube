<<<<<<< HEAD
import collections



class cube:
    def __init__(self, x,  y, z):
        self.x = x
        self.y = y
        self.z = z
        self.faces = ["W", "R", "G", "Y", "O" , "B",]
        self.FB = ["W", "Y"]
        self.RL = ["G", "B"]
        self.DU = ["R", "O"]

    # def rotate(self, face, prime):
    #     if face == "r":
    #         tempa = self.FB
    #         tempb = self.UD
            
    #         self.FB = tempb
    #         self.UD = tempa
            
    #         if prime:
    #             self.FB = self.FB.reverse()
    #             self.UD = self.UD.reverse()
    #     elif face == ""
        
    def rotate(self, face, prime = False):
        if face == "l" or face == "d" or face == "b":
            c = -1
        else:
            c = 1
            
        if face == "r" or face == "l":
            a = [2,5]
        elif face == "u" or face == "d":
            a = [1,4]
        elif face == "f" or face == "b":
            a = [0,3]
                
        temp = []
        for x in range(6):
            if x in a:
                continue
            
            temp.append(self.faces[x])
            
        a_list = collections.deque(temp)
        a_list.rotate(c)
        temp = list(a_list)
        
        for x in range(6):
            if x in a:
                continue
            self.faces[x] = temp.pop(0)
            
    def show(self):
        print("  " + self.faces[1])
        print(self.faces[5] + " " + self.faces[0] + " " + self.faces[2] + " " + self.faces[3])
        print("  " + self.faces[4])
        
    def arr(self):
        print(self.faces)
        
            
Cube = cube(0, 0, 0)
Cube.show()
Cube.arr()

Cube.rotate("r")
Cube.show()
Cube.arr()
=======
import collections
from itertools import permutations
from itertools import product

class block:
    def __init__(self, x,  y, z):
        self.x = x
        self.y = y
        self.z = z
        self.faces = ["W", "R", "G", "Y", "O" , "B"]
        self.FB = ["W", "Y"]
        self.RL = ["G", "B"]
        self.DU = ["R", "O"]


        
    def rotate(self, face, prime = False):
        if face == "l" or face == "d" or face == "b":
            c = -1
        else:
            c = 1
            
        if face == "r" or face == "l":
            a = [2,5]
        elif face == "u" or face == "d":
            a = [1,4]
        elif face == "f" or face == "b":
            a = [0,3]
                
        temp = []
        for x in range(6):
            if x in a:
                continue
            
            temp.append(self.faces[x])
            
        a_list = collections.deque(temp)
        a_list.rotate(c)
        temp = list(a_list)
        
        for x in range(6):
            if x in a:
                continue
            self.faces[x] = temp.pop(0)
            
    def show(self):
        print("  " + self.faces[1])
        print(self.faces[5] + " " + self.faces[0] + " " + self.faces[2] + " " + self.faces[3])
        print("  " + self.faces[4])
        
    def arr(self):
        print(self.faces)

    def getf(self, face):
        return self.faces[face]

    def coords(self):
        return self.x, self.y, self.z
        
class cube:
    def __init__(self):
        self.blocks = []
        for combo in product(range(3), repeat=3):
            temp = block(combo[0], combo[1], combo[2])
            self.blocks.append(temp)

    def getFace(self, face):
        if face == "r":
            n = 0
            a = 2
        elif face == "l":
            n = 0
            a = 0
        elif face == "u":
            n = 1
            a = 2
        elif face == "d":
            n = 1
            a = 0
        elif face == "f":
            n = 2
            a = 0
        elif face == "b":
            n = 2
            a = 2

        temp = []

        for x in self.blocks:
            if x.coords()[n] == a:
                temp.append(x)

        return temp
    
    def turn(self, face):
        temp = self.getFace(face)
        for x in temp:
            x.rotate(face)

    def out(self):
        for x in self.blocks:
            print(x.faces)
                
    def getCube(self, a, b, c):
        for i in self.blocks:
            if i.x == a and i.y == b and i.z == c:
                return i

    #def display(self):






#up
Cube = cube()
temp = (Cube.getCube(2,2,0))
print(temp.faces)
#Cube.turn("r")
#Cube.out()
# Cube.show()
# Cube.arr()

# Cube.rotate("r")
# Cube.show()
# Cube.arr()
>>>>>>> e881abf2be87eb144b6a5c9239a6823d8ac70c6f
