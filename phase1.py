#Remove duplicate element from a non decreasing array keeping it in place
duplicateNonDecreasingArr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def removeDuplicateElments():
    a = duplicateNonDecreasingArr;
    n = len(a);
    x = 0;
    
    for i in range(n):
        if a[i]>a[x]:
            x = x+1;
            a[x] = a[i];
    print(a, x+1)    
    return x+1;
removeDuplicateElments();

#Remove a recurring val from an arr
duplicateNonDecreasingArr2 = [0, 0, 0, 0, 1, 2, 2, 3, 3, 4]

def removeValue(val = 3):
    a = duplicateNonDecreasingArr2;
    n = len(duplicateNonDecreasingArr2);
    x = 0;
    for i in range(n):
        print(x)
        if not a[i] == val:
            a[x] = a[i];  #the order is inverse
            x = x+1;
    print(a, x)    #only retrun X
    return x;

removeValue(4);



