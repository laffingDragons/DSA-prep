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
        if not a[i] == val:
            a[x] = a[i];  #the order is inverse
            x = x+1;
    print(a, x)    #only retrun X
    return x;

removeValue(4);

#reverse a string array
def reverseString(str = "Hello"):
    a = list(str); # convert a string to array
    n = len(a);
    for i in range(n//2):
        a[i], a[n-1-i] = a[n-1-i], a[i]; # swap 2 value in array a[i], a[n-1-i]
    print("".join(a)); #convert array to string
    return "".join(a);

reverseString("Hello");

#Best time to buy and sell a stock
price = [7, 1, 5, 3, 6, 4, 8, 10, 9];
# price = [ 5, 4, 2, 1];

def findMaxProfit():
    min = price[0];
    maxProfit = 0;
    for i in range(len(price)):
        if maxProfit < (price[i] - min):
            maxProfit = price[i] - min;
        if min > price[i]:
            min = price[i]
    print(maxProfit);

findMaxProfit()

#merge 2 sorted non decreasing array 
num1 = [ 1,5,6,0,0,0]
num2 = [1,2,4]

def mergeSortedArrayMethod1(n1=num1, n2=num2):
    print("Merge 2 sorted non decreasing array : Method 1")
    
    n1Copy = [1,5,6];
    p1 = 0;
    p2 = 0;
    
    for i in range(len(n1Copy)+len(n2)):
        # handling the corner cases right 
        if(p2 >= len(n2) or (p1 < len(n1Copy) and (n1Copy[p1] < n2[p2]))):
            num1[i] = n1Copy[p1];
            p1 = p1+1;
        else:  
            num1[i] = n2[p2];
            p2 = p2+1;
    print(num1);
    
num3 = [ 1,5,6,0,0,0]

def mergeSortedArrayMethod2():
    print("Merge 2 sorted non decreasing array : Method 2")
    p1 = len(num2) -1
    p2 = len(num2) -1
    
    for i in range(len(num2)+len(num2)-1,0, -1):
        
        print(p1, p2, i)
        
        if(p2 < 0): break;
        
        if(p1 >= 0 and ((num3[p1] > num2[p2]))):
            num3[i] = num3[p1];
            p1 -= 1
        else:
            num3[i] = num2[p2];
            p2 -= 1
    print(num3)
 
mergeSortedArrayMethod1()
mergeSortedArrayMethod2()


#Move all the 0's in the array to last

arrWithZero = [1, 0, 3, 0, 12]

def moveAlltheZero():
    print("Move all the 0's in the array to last : ")
    x=0;
    for i in range(len(arrWithZero)):
        if not arrWithZero[i] == 0:
            arrWithZero[x] = arrWithZero[i];
            x += 1;
    for i in range(x, len(arrWithZero)):
        arrWithZero[i] = 0;
    print(arrWithZero);       
            
    
moveAlltheZero()

#Give the max count of conseccutive 1's
arrWithOneAndZero = [1, 0, 1,1,1, 0, 1, 0, 0, 1, 1, 1, 1,1]

def countConsectiveOne():
    print("Give the max count of conseccutive 1's : ");
    curr = 0;
    maxCount = 0;
    
    for i in range(len(arrWithOneAndZero)):
        if arrWithOneAndZero[i] == 1:
            curr += 1;
        else:
            maxCount = max(curr, maxCount);
            curr = 0;
    
    print(max(curr, maxCount));
    
    
countConsectiveOne()

#find a missing no from an array
missingNumArray = [1, 0, 3, 4, 6, 5];

def findMissingNumber(n = len(missingNumArray)):
    print("Find a missing no from an array :-")
    # By using the sumasition formula 
    totalSum = n*(n+1)/2;
    partialSum = 0
    
    for i in range(n):
        partialSum += missingNumArray[i];
    
    print(int(totalSum - partialSum));
    
findMissingNumber()


#Find the missing number from an array of duplicates
arrayOfDuplicates = [ 1, 2, 2, 3, 1, 4, 5 , 4, 5, 3, 6];

def findMissingDuplicateMethod1(n = len(arrayOfDuplicates)):
    print("Find the missing number from an array of duplicates : Method 1")
    hash = {}
    
    for i in range(n):
        if arrayOfDuplicates[i] not in hash:
            hash[arrayOfDuplicates[i]] = 1
        else:
            hash[arrayOfDuplicates[i]] += 1;
    
    for i in range(len(hash)):
        if hash[i+1] == 1:
            print(i+1)
            break;



def findMissingDuplicateMethod2(n = len(arrayOfDuplicates)):
    print("Find the missing number from an array of duplicates using XOR: Method 2 ")
    xor = 0;
    
    for i in range(n):
        xor ^= arrayOfDuplicates[i];
    print(xor);


findMissingDuplicateMethod1()
findMissingDuplicateMethod2()
