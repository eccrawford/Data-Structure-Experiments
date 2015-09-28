'''

Quadratic Probing vs. Doubling Hashing.
Experiments with the rate of comparisons when attempting to insert values
into a hashtable.

Note that this program requires an external text file to run. This code
has been uploaded for viewing purposes only.

'''

import math

def stringConvert(string):
    n = 37
    num = 0

    for char in string:
        num = num*n + ord(char)

    return num

def sumDigits(k): #hash function 1
    num = 0
    while k:
        num += k % 10
        k /= 10
    return num

def midSquare(k, n): #hash function 2
    num = k*k
    x = num / n
    a = x % n
    return a

def multMethod(k, n): #hash function 3
    v = (math.sqrt(5) - 1)/2
    a = (v*k)%1
    num = int(round(math.floor(n*a)))
    return num

def clearHashTable(table): # simple function that clears the contents of a hashtable for re-experimentation
    return ["" if x != "" else x for x in table]

##########################################

c = [1,0.5, 0.2]
lis = []
f = open('top_secret_agent_aliases_2015.txt', 'r')
aliases = f.readlines()
for line in range(len(aliases)): # generates an initial list of all the aliases, so the hashtable can pull them easily
    lis.append(aliases[line].rstrip('\n'))

################### ACTUAL EXPERIMENT ##################
print "Part 1: Quadratic Probing\n"
n=2477
print "Table size:", n;
hashTable = []
for i in range(n):
    hashTable.append("") #creates an initially empty hashTable
for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis: # changes the aliases into keys
        index = 0
        num = stringConvert(word)
        v = midSquare(num, n) #uses the midSquare hash function in quadratic probing
        a = v
        while ((index < n) and hashTable[a] != None):
            index+=1
            collisions +=1
            a = int(round((v + elem*index + elem*(index**2))))%n
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;

n=2351
print "\nTable size:", n;
hashTable = []
for i in range(n):
    hashTable.append("")
for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis: # changes the aliases into keys
        index = 0
        num = stringConvert(word)
        v = midSquare(num, n)
        a = v
        while ((index < n) and hashTable[a] != None):
            index+=1
            collisions +=1
            a = int(round((v + elem*index + elem*(index**2))))%n
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;

n=2099
print "\nTable size:", n;
hashTable = []
for i in range(n):
    hashTable.append("")
for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis: # changes the aliases into keys
        index = 0
        num = stringConvert(word)
        v = midSquare(num, n)
        a = v
        while ((index < n) and hashTable[a] != None):
            index+=1
            collisions +=1
            a = int(round((v + elem*index + elem*(index**2))))%n
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;
    
##########################################
################### ACTUAL EXPERIMENT ##################


# Double Hash 1 combines the sumDigits hash function and the midSquare hash function
print "\nPart 2: Double Hashing"
n=2477
hashTable = []
for i in range(n):
    hashTable.append("")
print "\nDouble Hash Function 1, table size", n;    
for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis:
        index = 0
        num = stringConvert(word)
        dblHash1 = sumDigits(num)
        a = dblHash1
        while ((index < n) and hashTable[a] != None):
            index += 1
            collisions += 1
            a = int(round((elem*dblHash1 + index*midSquare(num, n)) % n))
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;
    
n=2351
hashTable = []
for i in range(n):
    hashTable.append("")
print "\nDouble Hash Function 1, table size", n;    
for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis:
        index = 0
        num = stringConvert(word)
        dblHash1 = sumDigits(num)
        a = dblHash1
        while ((index < n) and hashTable[a] != None):
            index += 1
            collisions += 1
            a = int(round((elem*dblHash1 + index*midSquare(num, n)) % n))
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;


# Double Hash Function 2 combines the midSquare hash function and the multiplication method
n=2477
hashTable = []
for i in range(n):
    hashTable.append("")    
print "\nDouble Hash Function 2, table size", n;   
for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis:
        index = 0
        num = stringConvert(word)
        dblHash2 = midSquare(num, n) % n
        a = dblHash2
        while ((index < n) and hashTable[a] != None):
            index += 1
            collisions += 1
            a = int(round((elem*dblHash2) + index*multMethod(num, n)) % n)
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;

n=2351
hashTable = []
for i in range(n):
    hashTable.append("")    
print "\nDouble Hash Function 2, table size", n;   
for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis:
        index = 0
        num = stringConvert(word)
        dblHash2 = midSquare(num, n) % n
        a = dblHash2
        while ((index < n) and hashTable[a] != None):
            index += 1
            collisions += 1
            a = int(round((elem*dblHash2) + index*multMethod(num, n)) % n)
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;


# Double hash function three combines the multiplication method and the sumDigits hash function    
n=2477
hashTable = []
for i in range(n):
    hashTable.append("")
print "\nDouble Hash Function 3, table size", n;

for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis:
        index = 0
        num = stringConvert(word)
        dblHash3 = sumDigits(num)
        a = dblHash3
        while ((index < n) and hashTable[a] != None):
            index += 1
            collisions += 1
            a = int(round((elem*dblHash3) + index*multMethod(num, n)) % n)
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;
    
n=2351
hashTable = []
for i in range(n):
    hashTable.append("")
print "\nDouble Hash Function 3, table size", n;

for elem in c:
    collisions = 0
    hashTable = clearHashTable(hashTable)
    for word in lis:
        index = 0
        num = stringConvert(word)
        dblHash3 = sumDigits(num)
        a = dblHash3
        while ((index < n) and hashTable[a] != None):
            index += 1
            collisions += 1
            a = int(round((elem*dblHash3) + index*multMethod(num, n)) % n)
            if hashTable[a] == "":
                hashTable[a] = word
                break
    print "for c1 = c2 =", elem, "the average number of insertion attempts was", collisions/2000.00;
