#250201073

world_list = [[[("Sophia", (150,495), "Doll"), ("Ethan", (150,495), "Train"),
("Liam", (150,495), "Stuffed Toy")], [("Zoe", (220,400), "Doll"), ("Emma",
(220,400), "Doll")], [("Emily", (300,465), "Doll"), ("William", (300,465), "Stuffed Toy")]], [[("Olivia", (490,380), "Train"), ("Jack", (490,380), "Stuffed Toy")],
[("Hannah", (590,400), "Doll"), ("Benjamin", (590,400), "Train"), ("Michael",
(590,400), "Stuffed Toy")], [("Sarah", (530,490), "Stuffed Toy")]], [("Owen",
(310,690), "Train")], [("Max", (610,620), "Stuffed Toy")]]


class Santa:

    def __init__ (self,list_of_children,rem_distance,santa_coordinate):
        self.list_of_children = list_of_children
        self.rem_distance  = rem_distance
        self.santa_coordinate = santa_coordinate
    def get_list_of_children(self):
        return self.list_of_children
    def get_rem_distance(self):
        return self.rem_distance
    def get_santa_coordinate(self):
        return self.santa_coordinate
    def set_rem_distance(self,coordinates):
        
        
        
        
    

    
    
    
    
    '''def collect_wishes(self, world_list):
        x = 1
        for i in world_list:
            for j in i:
                child_name = 'child' + str(x)
                child_name = world_list[i][j]
                x = x + 1
                print(child_name)
     '''           

class Item:
    Item_list = ['Stuffed Toy', 'Doll', 'Train']
    def __init__ (self, toy):
        self.toy = toy
    def get_toy(self):
        return self.toy
    def set_toy(self,toy):
        if toy in self.Item_list:
            self.toy = toy
    def calculate_capacity(self):
        if self.toy is 'Stuffed Toy':
            volume =+ 7
        elif self.toy is 'Doll':
            volume =+ 3
        elif self.toy is 'Train':
            volume =+ 5
        return volume
    

class Sleigh:
    def __init__ (self,volume,current_items):
        self.volume = volume
        self.current_items = current_items
    def get_volume(self):
        return self.volume
    def get_current_items(self):
        return self.current_items
    def set_volume(self,volume):
        if 0 <= volume <= 15:
            self.volume = volume
    def holding_items(self):
        
class Child:
    def __init__ (self,world_list):
        #self.child_names = child_names
        #self.child_wishes = child_wishes
        #self.child_coordinates = child_coordinates
        self.world_list = world_list
    '''def get_child_names(self):
        return self.child_names
    def get_child_wishes(self):
        return self.child_name_wishes
    def get_child_coordinates(self):
        return self.child_coordinates'''
    def set_child_names(self,world_list):
        names = []
        for i in world_list:
            for j in i:
                names.append(self.world_list[i][j][0])
        return names
    def set_child_coordinates(self,world_list):
        coordinates = []
        for i in world_list:
            for j in i:
                coordinates.append(self.world_list[i][j][1])
        return coordinates
    def set_child_wishes(self,world_list):
        wishes = []
        for i in world_list:
            for j in i:
                wishes.append(self.world_list[i][j][2])
        return wishes
                
child1 = ("Sophia", (150,495), "Doll")
child2 = ("Ethan", (150,495), "Train")
child3 = ("Liam", (150,495), "Stuffed Toy")
child4 = ("Zoe", (220,400), "Doll")
child5 = ("Emma",(220,400), "Doll")
child6 = ("Emily", (300,465), "Doll")
child7 = ("William", (300,465), "Stuffed Toy")
child8 = ("Olivia", (490,380), "Train")
child9 = ("Jack", (490,380), "Stuffed Toy")
child10 = ("Hannah", (590,400), "Doll")
child11= ("Benjamin", (590,400), "Train")
child12 = ("Michael",(590,400), "Stuffed Toy")
child13 = ("Sarah", (530,490), "Stuffed Toy")
child14 =("Owen",(310,690), "Train")
child15 = ("Max", (610,620), "Stuffed Toy")

children_list = [child1,child2,child3,child4,child5,child6,child7,child8,child9,child10,child11,child12,child13,child14,child15]


print('Welcome to Santa Claus’ Workshop!')      
print('Remaining Distance 8.000 kilometers.')
Santa_workshop = (0,0)
    def remaining_children(List):
        print(('-')*37)
        print(' name    | distance | wish     ')
        print(('-')*37)
        for i in range(len(List)):
            print('|',List[i][0],'|',List[i][1],'|',List[i][2],'|')
    
    def removing_children(List,child):
        for i in List:
            if child is List[i][0]:
                List.remove(i)
    #def santa_sleigh()
    '''def travel(total_distance,world_list,child):
        for i in List:
            if child is List[i][0]:
                List[1][2]-'''
                
    while True:
        print('Here are the children left that needs their Christmas presents and their distance from Santa:')
        remaining_children(children_list)
        next_child = input('Where should Santa go next?')
        next_child = next_child.title()
        print('Checking Cargo!')
        print('Santa is going to ',next_child)
        print('Remaining Distance: ', )
        
                
        


