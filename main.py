# make 2 vaiables and add them in 3rd variable and print the sum
import array


a= 10;
b= 30;
c = a * b;

print(f"{c}");

# Play with strings 
firstName = "Akkshay"
lastName = "Paatil"

print(f"My name is {firstName} {lastName}")

# Play with arrays 
arr = [1, 4, 70, 6, 60, 30,100];
arrString = ["Shivani", "Akkshay", "Gupta", "Paatil", True, 3, arr]

print(arr[2]+ arr[4])
print(arrString[6][1]);

# Playing with objects
obj = {
    "a": 2,
    "b": "Akkshay",
    "arr": arrString,
    "tempObj": {"c": "tempvalue"}
}

print(obj["tempObj"])        
print(obj["arr"]) 

# Playing with functions   
# dynamic Functions.  
def printHelloWorld(name) :
    print(f"Hello {name}!")

printHelloWorld("Akkshay")
printHelloWorld("Shivani")

def sumAndMultiple(a,b):   
    print(f"Sum of {a} and {b} is {a+b}")
    print(f"Multiple of {a} and {b} is {a*b}")
    
sumAndMultiple(10, 30);


def giveSquare(x):
    return (f"Square of {x} is {x*x}")

print(f"{giveSquare(4)}");


def votingEligibility(age): 
    if(age < 0):
        print("Invalid age")
    elif(age >= 18):
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

votingEligibility(13)
votingEligibility(19)
votingEligibility(-1)


def evenOrOdd (x):
    if(x % 2 == 0):
        print("Its an even number")
    else:
        print("Its a odd number")

evenOrOdd(4)
evenOrOdd(7)


#Playing with loop
# Doing things over and over again.  
# range(intialisation i = 2 , Condition i > 16, change  i++)
for i in range(2,9,2):
    print(f"Hello world! {i}")

print(range(5))

for i in range(2, 0, -1):
    print(f"Hello world! {i}")
    
def greet(x):
    print(f"Hello Akkshay {x}")

for i in range(2):
    greet(i)

# Print elements of arr 
for i in range(len(arr)):
    print(arr[i])

# Print even no to console 
for i in range(len(arr)):
    evenOrOdd(arr[i])
    
# Playing with while loops 

z = 0
while(z < 5):
    print(f"While loop {z}")
    z += 1


# Search an element in an Array and returns the index if not the return -1
#wrong method for python
def searchAnElement(x):
    if(arr.index(x)):
        return arr.index(x)
    else:
        return -1

def searchAnElementWithLoop(x):
    for i in range(len(arr)):
        if(arr[i] == x):
            return i;
    return -1;
        
    
print(searchAnElementWithLoop(10));
# print(searchAnElement(22));

# Count all the negative numbers in an arr.  
negativeArr = [0, -11, -22, 66, -33, 77, -44, -55];

def countNegativeNumbers():
    x=0;
    for i in range(len(negativeArr)):
        if(negativeArr[i] < 0):
            x += 1;
    return x;

print(countNegativeNumbers())
        
# write a function to return largest no in the array
def findTheLargestAndSmallestNo(noArr):
    largestNo = noArr[0];
    smallestNo = noArr[0];
    for i in range(len(noArr)):
        if(largestNo < noArr[i]):
            largestNo = noArr[i];
        if(smallestNo > noArr[i]):
            smallestNo = noArr[i];
    return [largestNo, smallestNo];

print(f"Find the largest and smallest no in the Array : {findTheLargestAndSmallestNo(arr)}");
print(f"Find the largest and smallest no in the Array : {findTheLargestAndSmallestNo(negativeArr)}");

#find the second largest no in the array
def secondLargestNo(noArr):
    if(len(noArr) < 1):
        return "Array should have atleast 2 elements";
    
    firstLargest = -float("inf"); #largest no avaiable
    secondLargest = -float("inf") - 1;
    
    for i in range(len(noArr)):
        if(firstLargest < noArr[i]):
            # very Important to update Second Largest before updating First Largest 
            secondLargest = firstLargest;
            firstLargest = noArr[i];
        # very Important step  
        # is Value  greater than secondLargest, but not equal to firstLargest (this will make sure that duplicates wont affect)
        if(secondLargest < noArr[i] and firstLargest != noArr[i]):
            secondLargest = noArr[i];
    
    return [firstLargest, secondLargest]
    
print(f"Find the 2nd largest : {secondLargestNo(arr)}");

#Play loop within a Loop
def runDoubleLoop():
    for i in range(3):
        # for j in range(i): # for(j=0; j < i; j++)
        for j in range(i + 1): # for(j=0; j <= i; j++)
            print(f" Value of i ={i}, Value of j = {j}")

runDoubleLoop()

def loopingProblem():
    # for(i=5; i>0; i--){
    #     for(j=0; j<i; j++){
    #         console.log(i,j)
    #     }
    # }
    for i in range(5,0, ):
        for j in range(i):
            print(f"Double loop Problem: Value of i,j ={i}, {j}")

loopingProblem();


# Print a star pattern with n row and cols
def basicStarPatern(row = 4, col = 4):
    for i in range(row):
        star = ""
        for j in range(col):
            star += "*"
        print(star)
    
basicStarPatern(4, 5)


def halfPatern(row = 4):
    for i in range(row):
        star = ""
        for j in range(i+1):
            star += "*"
        print(star)
    
halfPatern(9)

def halfNumberPattern(row=5):
    for i in range(row):
        star="";
        for j in range(i+1):
            star = star + str(j+1)
        print(star);

halfNumberPattern(9)

def halfNumberPatternWithRow(row=5):
    for i in range(row):
        star="";
        for j in range(i+1):
            star = star + str(i+1)
        print(star);

halfNumberPatternWithRow(9)


def halfNumberPatternUpsideDown(row=5):
    for i in range(row):
        star="";
        for j in range(row-i):
            star = star + str(j+1)
        print(star);

halfNumberPatternUpsideDown(9)

def invertedUpsideDownStar(row = 5):
    for i in range(row):
        star=""
        # adding empty spaces  
        for j in range(row-i-1):
            star+=" "
        # adding stars  
        for k in range(i+1):
            star+="*"
        print(star)
    
invertedUpsideDownStar(9)  


# My Logic for inverted star pattern  
def inverterHalfStar(row=4):
    for i in range(row):
        star = ""
        
        for j in range(row):
            if j >= i:
                star = star + "*"
            else:
                star = star + " "
        print(f"{star}")

inverterHalfStar(9)

#pattern with switch
def patternWithSwitch(row = 5):
    for i in range(row):
        star = "";
        switch=1;
        for j in range(i+1):
            star += str(switch);
            if(switch==1):
                switch = 0;
            else:
                switch = 1;
        print(star);

patternWithSwitch(9)

def patternWithSwitchAgain(row = 5):
    switch=1;
    for i in range(row):
        star = "";
        for j in range(i+1):
            star += str(switch);
            if(switch==1):
                switch = 0;
            else:
                switch = 1;
        print(star);

patternWithSwitchAgain(9);

# COunt the digits in the number
def countTheDigits(n):
    #if the no is 0
    if(n == 0): 
        return 1
    # if the no is -ve
    n = abs(n)
    
    count=0;
    while n>0 :
        n = int(n/10);
        count += 1;
    return count;

print(countTheDigits(1234567))

#Check wheter the digit are palindrome 
def checkForPalindromeDigit(x):
    if(x<0):
        print("The given is -ve number")
        return
    n = x
    rev = 0;
    while(n>0):
        rem = n % 10;
        rev = (10*rev) + rem;
        n = int(n/10);
    
    print(f"{x} and reverse {rev}")
    if(x == rev):
        print("The number is Palindrome")
    else:
        print("The number is Not a Palindrome")
    # print(f"{x} is {'Palindrome' if str(x) == str(x)[::-1] else 'Not a Palindrome'}")
    

checkForPalindromeDigit(12321)


