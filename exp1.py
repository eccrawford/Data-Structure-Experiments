'''
Binary Search vs. Trinary search.
Searching for elements in a list vs. Searching for elements not in a list
'''
from random import *
from time import *
import math

def binSearch(lis, first, last, value):
    if first > last:
        return -1
    else:
        mid = (first+last)//2
        if lis[mid] == value:
            return mid
        elif lis[mid] > value:
            return binSearch(lis, first, mid-1, value)
        else:
            return binSearch(lis,mid+1, last, value)



def triSearch(lis, first, last, value):
    if first > last:
        return -1
    else:
        oneThird = first + (last-first)//3
        twoThird = first + 2*(last-first)//3

        if lis[oneThird] == value:
            return oneThird
        elif lis[oneThird] > value:
            return triSearch(lis, first, oneThird-1, value)
        elif lis[twoThird] == value:
            return twoThird
        elif lis[twoThird] > value:
            return triSearch(lis, oneThird+1, twoThird-1, value)
        else:
            return triSearch(lis, twoThird+1, last, value)


def quickSort(lis): #standard qsort implementation
    small = []
    partitionList=[]
    big=[]
    if len(lis) > 1:
        partition = lis[0]
        for i in lis: 
            if i < partition:
                small.append(i)
            if i == partition:
                partitionList.append(i)
            if i > partition:
                big.append(i)
        return quickSort(small) + partitionList + quickSort(big)
    else:
        return lis

def test1():   
    lengthList=[15625,31250,62500, 250000, 1000000]
    print "---------------EXPERIMENT 1---------------"
    print '\n'
    for i in lengthList: #performs each experiment on every element of the list
        lis=[]
        print "Binary Search: n =",i;
        print "---------------"
        #create and sort the list
        for j in range(i):
            lis.append(randint(0,10*i))
            
        sortedList = quickSort(lis)
        #performs the experiments for binary search using different k values for every n
        k= i//2
        print "k = n/2:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e] #ensures that the target value will definitely be in the list
            binSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');
        
        k = i//5
        print "k = n/5:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]
            binSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');

        k = i//10
        print "k = n/10:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]
            binSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');
        print '\n'
        
        #Trinary Search
        #performs the experiments for trinary search using different k values for every n
        print "Trinary Search: n =",i;
        print "---------------"
        k = i//2
        print "k = n/2:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]
            triSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');

        k = i//5
        print "k = n/5:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]
            triSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');

        k = i//10
        print "k = n/10:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]
            triSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');
        print '\n'
test1()
print "---------------EXPERIMENT 2---------------"
print '\n'
def test2():
    lengthList=[15625,31250,62500, 250000, 1000000]
    for i in lengthList:
        lis=[]
        print "Binary Search: n =", i;
        print "---------------"
        for j in range(i):
            lis.append(randint(0,10*i))
            
        sortedList = quickSort(lis)
        #performs the experiments for binary search using different k values for every n
        k= i//2
        print "k = n/2:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]*(-1)
            #multiplies each target by -1 to ensure it definitely won't be in the list, since the list contains only positve values
            binSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');
    
        
        k = i//5
        print "k = n/5:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]*(-1)
            binSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');

        k = i//10
        print "k = n/10:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]*(-1)
            binSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');
        print '\n'
        
        #Trinary Search
        #performs the experiments for trinary search using different k values for every n
        print "Trinary Search: n =", i;
        print "---------------"
        
        k = i//2
        print "k = n/2:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]*(-1)
            triSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');

        k = i//5
        print "k = n/5:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]*(-1)
            triSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');

        k = i//10
        print "k = n/10:", k;
        start = clock()
        for e in range(0, k):
            target = sortedList[e]*(-1)
            triSearch(sortedList, 0, len(sortedList)-1, target)
        totalTime = (clock() - start)
        c = totalTime/(k*(math.log(i)))
        print "Time for", k, "searches:", totalTime;
        print "The constant multiple is c =", format(c, '.13f');
        print '\n'
test2()
