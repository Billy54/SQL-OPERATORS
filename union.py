#Bill Gewrgoulas
#cse52954
united = ''
left = ''
right = ''
fileR = ''
fileS = ''

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

def union():
    global united
    
    leftR = handleR()
    rightS = handleS()
    
    while leftR and rightS:

        if leftR == rightS:
            united.write(rightS[0] + '   ' + rightS[1] + '\n')
            rightS = handleS()
            leftR = handleR()
        elif leftR > rightS:
            united.write(rightS[0] + '   ' + rightS[1] + '\n')
            rightS = handleS()
        elif leftR < rightS:
            united.write(leftR[0] + '   ' + leftR[1] + '\n')
            leftR = handleR()
 
    #hendle remaining rows , if any
    while leftR:
        united.write(leftR[0] + '   ' + leftR[1] + '\n')
        leftR = handleR()
    while rightS:
        united.write(rightS[0] + '   ' + rightS[1] + '\n')
        rightS = handleS()

##################main##################
try:
    fileR = open('R_sortedor.tsv', 'r')
    fileS = open('S_sortedor.tsv', 'r')
    united = open('RunionS.tsv' , 'w')
except:
    print('files could not be opened')
    exit(1)

#init
left = readR()
right = readS()

union()

fileR.close()
fileS.close()
united.close()


