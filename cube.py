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