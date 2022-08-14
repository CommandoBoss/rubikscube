import collections
import enum

facenames = {
    'f': 0,
    'u': 1,
    'r': 2,
    'b': 3,
    'd': 4,
    'l': 5
}
rotation_names = {
    'f': (0,3),
    'b': (0,3),
    'u': (1,4),
    'd': (1,4),
    'r': (2,5),
    'l': (2,5)
}
facefilter = {        #sorting for faces (face, value) ex: all blocks on 'f' face have z (2) value of 0
    'f': (2, 0),
    'u': (1, 0),
    'r': (0, 2),
    'b': (2, 2),
    'd': (1, 2),
    'l': (0, 0)
}

facesort = {        
    'f': (2, False, 0, False),
    'u': (0, False, 2, True),
    'r': (2, False, 1, False),
    'b': (0, True, 1, False),
    'd': (0, False, 2, False),
    'l': (2, True, 1, False)
    }


class block:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.faces = ['w', 'r', 'g', 'y', 'o' , 'b',]
        #              f    u    r    b    d     l

    def getpos(self):
        return (self.x, self.y, self.z)



    def X(self):
        return self.X
        
    def Y(self):
        return self.y

    def Z(self):
        return self.z

    def getfaces(self):
        return self.faces
    
    def getface(self, face):
        return self.faces[facenames[face]]

    def rotate(self, face, clockwise = True, count = 1):
        self.faces = rotate_list(self.faces, rotation_names[face], clockwise, count)

    def __str__(self):
        return f'  {self.faces[3]}  \n  {self.faces[1]}  \n{self.faces[5]} {self.faces[0]} {self.faces[2]}\n  {self.faces[4]} '



class cube:
    def __init__(self):
        self.blocks = []
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.blocks.append(block(x,y,z))
    
    def getface(self, face) -> list[block]:            #returns all blocks on a given face
        chunk, value = facefilter[face]
        temp = []
        for x in self.blocks:
            if x.getpos()[chunk] == value:
                temp.append(x)
        return temp

    def getblock(self, x, y, z):
        for v in self.blocks:
            if v.getpos() == (x,y,z):
                return v

    def setblock(self, x, y, z, new):
        for i, v in enumerate(self.blocks):
            if v.getpos() == (x,y,z):
                self.blocks[i] = new

    def rotate(self, face: list[block], clockwise = True, count = 1):
        primes = {
            'f': False,
            'u': True,
            'r': False,
            'b': True,
            'd': False,
            'l': True
        }
        tempspin = clockwise
        if primes[face] is True:
            tempspin = not clockwise

        temp = self.getface(face)
        sort_a, ascending_a, sort_b, ascending_b = facesort[face]
        temp = sorted(temp, key =  lambda a: a.getpos()[sort_a], reverse= ascending_a)
        temp = sorted(temp, key = lambda a: a.getpos()[sort_b], reverse= ascending_b)

        for x in range(len(temp)):
            temp[x].rotate(face, tempspin, count)
        
        print(len(temp))

        temp = spin(temp, clockwise)

        for v in temp:
            self.setblock(v.X(), v.Y(), v.Z(), v)








def rotate_list(List: list, keep: list, clockwise = True, count = 1):     #rotates 'List' keeping indexes in 'keep' static, completes 'count' # of rotations
    if clockwise is False:         #makes rotation count negative for counter-clockwise rotation
        count = count * -1
    
    temp = []
    for i, v in enumerate(List):
        if i not in keep:
            temp.append(v)          # create a temporary list (temp) excluding the values we dont want rotated
            List[i] = 0             # mark the spots of rotated items with a 0 to be replaced later


    a_list = collections.deque(temp)    
    a_list.rotate(count)
    temp = list(a_list)             #use collections to rotate the list set the 'temp' variable back to it

    for i,v in enumerate(List):     #adds the rotated items back into the original list
        if v == 0:
            List[i] = temp.pop(0)

    return List

def spin(List, clockwise = True):
    temp = [
        List[6],
        List[3],
        List[0],
        List[7],
        List[4],
        List[1],
        List[8],
        List[5],
        List[2]
    ]
    return temp


x = ['a', 'b', 'c', 'd', 'e', 'f']

rubik = cube()


x = rubik.getblock(0, 0, 0)

print(x)

rubik.rotate('b')
print('\n')
x = rubik.getblock(0, 0, 2)
print(x)

# rubik.rotate('u')
# print('\n')
# x = rubik.getblock(0, 0, 0)
# print(x)
