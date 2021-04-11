#Bill Gewrgoulas
# cs52954 Uoi

diff = ''
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

def difference():
    global inter
    
    leftR = handleR()
    rightS = handleS()

    while leftR and rightS:
        
        if leftR == rightS:
            rightS = handleS()
            leftR = handleR()
        elif leftR > rightS:
            rightS = handleS()
        elif leftR < rightS:
            diff.write(leftR[0] + '   ' + leftR[1] + '\n')
            leftR = handleR()

    #handle remaining rows , if any
    while leftR:
        diff.write(leftR[0] + '   ' + leftR[1] + '\n')
        leftR = handleR()


##################main##################
try:
    fileR = open('R_sorted.tsv', 'r')
    fileS = open('S_sorted.tsv', 'r')
    diff = open('RdifferenceS.tsv' , 'w')
except:
    print('files could not be opened')
    exit(1)

#init
left = readR()
right = readS()

difference()

fileR.close()
fileS.close()
diff.close()
