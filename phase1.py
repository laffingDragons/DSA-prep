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
