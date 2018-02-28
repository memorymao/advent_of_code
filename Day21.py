import numpy as np

def graghToNum(s):  # the map rule for image to number
    return {'#': 1, '.': 0}[s]

def getData():
    inputs = open('./advent2017/input21.txt','r').readlines()
    before = []
    after = []
    for i, n in enumerate(inputs): 
        n = n.split()
        mat = []
        for s in n[0].split('/'): mat.append(list(map(graghToNum,s)))
        before.append(mat)
        mat = []
        for s in n[2].split('/'): mat.append(list(map(graghToNum,s)))
        after.append(mat)
    return before, after

def transform(mat, target):
    def flip(a): return a[::-1] # flip up and down
    def rotate(a) : return list(map(list,zip(*a[::-1]))) # rotate 90 degrees (clockwise)
    for f in range(2):
        for r in range(4):
            if mat == target : return True
            mat = rotate(mat)
        mat = flip(mat)
    return False

def enhance(iteration):
    m = np.array([[0,1,0],[0,0,1],[1,1,1]])
    while iteration >0 :
        # divide the matrix to cells , by  2*2 or 3*3
        divisition = (2 if len(m) %2 ==0 else 3)
        cellnum = len(m)//divisition   # length of cells
        cells = []
        for k in np.vsplit(m, cellnum):  cells.extend(np.hsplit(k, cellnum))
        # enhance the cells with the rules
        for k, cell in enumerate(cells):
            for  i, mat in enumerate(before):
                if transform(mat, cell.tolist()): 
                    cells[k] = after[i]
                    break
        # join the cells into matrix
        m=[]
        for i in range(cellnum): m.append(np.hstack(cells[i*cellnum:i*cellnum+cellnum]))
        m = np.vstack(m[0:cellnum])
        # finish this iteration
        iteration -=1
    return m
            
global after
global before
before, after = getData()
print(np.sum(enhance(18)==1))
