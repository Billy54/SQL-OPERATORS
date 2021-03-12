
inter = ''
fileR = ''
fileS = ''

left = ''
right = ''

def readR():
    global fileR 
    return fileR.readline().split()

def readS():
    global fileS 
    return fileS.readline().split()

def handleS():
    global  right
    
    temp = right
    right = readS()
    while temp == right:
        temp = right
        right = readS()
        if not right: break
    return temp

def handleR():
    global  left

    temp = left
    left = readR()
    while temp == left:
        temp = left
        left = readR()
        if not left: break
    return temp

def intersection():
    global inter
    
    leftR = handleR()
    rightS = handleS()

    while leftR and rightS:
    
        if leftR == rightS:
            inter.write(rightS[0] + '   ' + rightS[1] + '\n')
            rightS = handleS()
            leftR = handleR()
        elif leftR > rightS:
            rightS = handleS()
        elif leftR < rightS:
            leftR = handleR()

##################main##################
try:
    fileR = open('R_sortedor.tsv', 'r')
    fileS = open('S_sortedor.tsv', 'r')
    inter = open('RintersectionS.tsv' , 'w')
except:
    print('files could not be opened')
    exit(1)

#init
left = readR()
right = readS()

intersection()

fileR.close()
fileS.close()
inter.close()