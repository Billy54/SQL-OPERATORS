#Bill Gewrgoulas
#cs52954 Uoi

fileR = ''
group = ''

def readR():
    global fileR 
    return fileR.readline().split()

def output(outTuple):
    global group, out
    group.write(outTuple[0] + '   ' + str(outTuple[1]) + '\n')

def mergeSort(array):
    
    if len(array) <= 1:
        return array
    mid = int(len(array) / 2)
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right)

def merge(left, right):

    temp = []
    lp = rp = 0
    while lp < len(left) and rp < len(right):
        
        if left[lp][0] < right[rp][0]:
            temp.append(left[lp])
            lp += 1
        elif left[lp][0] > right[rp][0]:
            temp.append(right[rp])
            rp += 1
        else:
            right[rp][1] = int(right[rp][1]) + int(left[lp][1]) 
            temp.append(right[rp])                               #comment  out if we only want to remove dupliacates
            left.pop(lp)                                         #pop it out form left so we wont lose the order
            rp += 1
            
    temp.extend(left[lp:])
    temp.extend(right[rp:])

    return temp

#######################main#######################
try:
    fileR = open('R.tsv', 'r')
    group = open('Rgroupby.tsv', 'w')
except:
    print('files could not be opened')
    exit(1)

####read the whole thing####
myList = []
read = readR()
while read:
    myList.append(read)
    read = readR()
fileR.close()

result = mergeSort(myList)
for tuple in result:
    output(tuple)
group.close()
