#250201073

# # # # # # # # # # # # # # # # # # # #
# Monsters' World
from random import randint

n = 4
object_number = 4  #1G, 3M
flag = True

while flag:
    obj_cell_list = []
    flag = False
    
    #randomly select cells of objects that should not overlap with each other
    while True:
        cell = randint(0, n**2-1)
        if cell not in obj_cell_list:
            obj_cell_list.append(cell)    #first position for G, others for W 
        if len(obj_cell_list) == object_number:
            break  
   
    #determine whether objects are in proper cells 
    monsters = obj_cell_list[1:object_number]
    gold = obj_cell_list[0]
    if 0 in obj_cell_list: #G and Ms are not in cell 0
        flag = True
    elif (1 in monsters) and (n in monsters): #both cells adjacent to 0 does not include M.
        flag = True
    elif gold==(n-1): #if G is in the second corner
        if (n-2 in monsters) and (2*n-1 in monsters):
            flag = True
    elif gold==(n**2-n): #if G is in the third corner
        if (n**2-2*n in monsters) and (n**2-n+1 in monsters):
            flag = True
    elif gold==(n**2-1): #if G is in the last corner
        if (n**2-n-1 in monsters) and (n**2-2 in monsters):
            flag = True
    elif gold>0 and gold<(n-1): #the upper edge
        if (gold-1 in monsters) and (gold+n in monsters) and (gold+1 in monsters):
            flag = True
    elif gold>(n-1) and gold<(n**2-1): #the right edge
        if (gold-n in monsters) and (gold-1 in monsters) and (gold+n in monsters):
            flag = True
    elif gold>0 and gold<(n**2-n): #the left edge
        if (gold-n in monsters) and (gold+1 in monsters) and (gold+n in monsters):
            flag = True
    elif gold>(n**2-n) and gold<(n**2-1): #the lower edge
        if (gold-1 in monsters) and (gold-n in monsters) and (gold+1 in monsters):
            flag = True

#write the world to the file
f = open("monstersworld.txt", "w")
for i in range(n**2):
    if i==0:
        line = "P"
    elif i in obj_cell_list:
        if i==gold:
            line = "G"
        else:
            line = "M"
    else:
        line = "0" 
        
    if i != (n**2-1):
        f.write(line + "\n")
    else:
        f.write(line) 
f.close()

# INSERT YOUR CODE HERE ...

def read_matrix(fname):
    fin = open(fname, "r")
    mtx = fin.readlines()
    fin.close()
    myMtx = [["S" for x in range(4)] for y in range(4)]
    # print(myMtx)
    next_line = 0
    for i in range(4):
        for j in range(4):
            myMtx[i][j] = mtx[next_line][0]
            if mtx[next_line][0] == '0':
                myMtx[i][j] = 'S'
            next_line += 1
    myMtx[0][0] = 'S'
    # print(myMtx)
    return myMtx

# In[ ]:

myMatrix = read_matrix("monstersworld.txt")

def print_matrix(mtx, x, y, steps):
    print("Number of steps taken so far is " + str(steps) + ".")
    steps += 1 
    mtx[x][y] = 'P'
    for i in mtx:
        print(''.join(i))
    mtx[x][y] = myMatrix[x][y] 
    return mtx, steps

# In[ ]:

row = len(myMatrix)
column = len(myMatrix[0])

for i in range(row):
    for j in range(column):
        if myMatrix[i][j] == 'M':
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if((k == 0 or l == 0) and (k != l) and (k+i >= 0 and k+i < row) and (l+j >= 0 and l+j < column) and (myMatrix[i+k][j+l] != 'M' and myMatrix[i+k][j+l] != 'G') ):
                        myMatrix[i+k][j+l] = 'H'

# print(myMatrix)

# In[ ]:

def check_and_print(x, y, steps):
    if myMatrix[x][y] == 'H':
        print("You just heard a howl. Be careful!")
    if myMatrix[x][y] == 'G':
        print("Yay! You have found the gold.")  
        print("\nGAME OVER")
        print("Score: " + str(int(100/steps)))
        exit()
    if myMatrix[x][y] == 'M':
        print("Oh no! You are eaten by a monster.")
        print("\nGAME OVER")
        print("Score: 0")
        exit()
    if myMatrix[x][y] == 'S':
        print("You are in a safe room. Don’t worry!")           


def traverse(mtx, key, x, y, steps):
    if key == 'd':
        if y+1 >= 4:
            print("You hit the wall. Try another move!")
        else:
            y = y + 1
            check_and_print(x, y, steps)
            mtx, steps = print_matrix(mtx, x, y, steps)
    elif key == 's':
        if x+1 >= 4:
            print("You hit the wall. Try another move!")
        else:
            x = x + 1
            check_and_print(x, y, steps)
            mtx, steps = print_matrix(mtx, x, y, steps)
    elif key == 'a':
        if y-1 < 0:
            print("You hit the wall. Try another move!")
        else:
            y = y - 1
            check_and_print(x, y, steps)
            mtx, steps = print_matrix(mtx, x, y, steps)
    elif key == 'w':
        if x-1 < 0:
            print("You hit the wall. Try another move!")
        else:
            x = x - 1
            check_and_print(x, y, steps)
            mtx, steps = print_matrix(mtx, x, y, steps)
    else:
        print("There is no such direction! Choose right (d), left (a), up (w) or down (s).g")
    print()
    return mtx, x, y, steps

# MAIN FUNCTION 

x = 0
y = 0

# Initial Print
player_matrix = [[myMatrix[0][0], '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?'], ['?', '?', '?', '?']]
check_and_print(0, 0, 0)
print_matrix(player_matrix, 0, 0, 0)
print()

steps_taken = 1
while True:
    key_pressed = input("What is your move?: ")
    player_matrix, x, y, steps_taken = traverse(player_matrix, key_pressed, x, y, steps_taken)