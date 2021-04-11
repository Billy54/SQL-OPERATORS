#Bill Gewrgoulas
# cs52954 Uoi

#merge join in case of many to many relation
import heapq 

fileR = ''
fileS = ''
joined = ''

buffer = []
bufferSize = []
heapq.heapify(bufferSize)
heapq.heapify(buffer)

def readR():
    global fileR 
    return fileR.readline().split()

def readS():
    global fileS 
    return fileS.readline().split()

def mergeJoin():
    global buffer, bufferSize , joined

    right = readS()
    left = readR()
   
    while left and right:
        if left[0] == right[0]:
            heapq.heappush(buffer , right)
            joined.write(left[0] + '   ' + left[1] + '   ' + right[1] + '\n')
            right = readS()
            if not right: break
        
        if left[0] < right[0]:
            left = readR()
            if not left: break
            if len(buffer):
                if left[0] == buffer[0][0]:
                    for el in buffer:
                        joined.write(left[0] + '   ' + left[1] + '   ' + el[1] + '\n')
                else:
                    heapq.heappush(bufferSize , -1*len(buffer))
                    buffer.clear()
                
        elif left[0] > right[0]:
            right = readS()
            heapq.heappush(bufferSize , -1*len(buffer))
            buffer.clear()

    #merge the remaining tuples in the buffer , if any|
    left = readR()
    while left and len(buffer):
        if left[0] == buffer[0][0]:
            for el in buffer:
                joined.write(left[0] + '   ' + left[1] + '   ' + el[1] + '\n')
        else:
            break
        left = readR()
    heapq.heappush(bufferSize , -1*len(buffer))
    buffer.clear()
    
######main######
try:
    fileR = open('R_sorted.tsv', 'r')
    fileS = open('S_sorted.tsv', 'r')
    joined = open('RjoinS.tsv' , 'w')
except:
    print('files could not be opened')
    exit(1)

mergeJoin()
print('max buffer size was: %s ' % (-1*heapq.heappop(bufferSize)))
fileR.close()
fileS.close()
joined.close()

