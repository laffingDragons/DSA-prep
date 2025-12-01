# Write a recursion function to count till 0
from gettext import find


def countTillZero(n = 10):
    if(n < 0 ): return;
    print(n);
    n -= 1;
    countTillZero(n);
countTillZero(10);

#Write a recursion funtion to count till n from 1
def countTilln(n = 1, x = 10):
    if(x < n): return;
    print(n);
    n += 1;
    countTilln(n);

countTilln(1,10)

#write a recursion function to find the sum on all the number in array
nums = [1, 3, 4, 6, 7, 8, 10];

def findSum(n):
    if(n < 0) : return 0;
    return nums[n] + findSum(n-1)
    

print(f"The sum of all the element : ", findSum(len(nums)-1))

def sumOfOdd(n):
    isOdd = not (nums[n] % 2 == 0);
    if n < 0 : 
        if isOdd : 
            return nums[n]
        else:
            return 0
    if isOdd:
        return nums[n] + sumOfOdd(n-1)
    else:
        return sumOfOdd(n-1)
    # return nums[n] + sumOfOdd(n - 1) if nums[n] % 2 else sumOfOdd(n - 1)

    
print(f"The sum of all the Odd elements : ", sumOfOdd(len(nums)-1))

# find the factorial of a number
def findFactorial(n):
    if n == 1 : return 1;
    return n * findFactorial(n-1);

print("The factorial is :", findFactorial(4));

#find if the number is power of 2
def findPowerOfTwo(n):
    if n == 1: return True;
    if n < 1 : return False;
    return findPowerOfTwo(n/2);

print("The is factorial:", findPowerOfTwo(16));

#find the fibonacci number at the index n
def fib(n):
    if n <= 1: return n;
    return fib(n-1) + fib(n-2)

print("The fibonacci number at the index 5 is:", fib(8));
