
1) Given a subset of daily sales and sellers, find the subset that identifies those with the highest daily sales average.

FB:
####Given an list A of objects and another list B which is  identical to A except that one element is removed, find that removed element.
The answer of course is to sum all the numbers in A, sum all the numbers in B, subtract the sum of B from the sum of A, and that gives you the number.



There is a table that tracks every time a user turns a feature on or off, with columns user_id, action ("on" or "off), date, and time.

How many users turned the feature on today?
How many users have ever turned the feature on?
In a table that tracks the status of every user every day, how would you add today's data to it?  


####1. Find the intersection of two arrays of integers.
arr1 = [1,2,3,4,5,6]
arr2 = [3,6,8,9,10,11,2]
arr3 = []
for i in arr1:
  for b in arr2:
    if i == b:
      arr3.append(i)
OR BETTER:
[value for value in arr1 if value in arr2]
OR BETTER:
list(set(arr1) & set(arr2))

BEST:
set(arr1).intersection(arr2)

####2. Find the nth prime number

# generate nth prime number:
def nth_prime_number(n):
    if n==1:
        return 2
    count = 1
    num = 1
    while(count < n):
        num +=2 #optimization: a prime number has to be odd: start at 1 so only check odd numbers
        if is_prime(num):
            count +=1
    return num


def is_prime(num):
    factor = 2
#     optimization: only check up to square root of number
    while (factor * factor <= num):
        if num % factor == 0:
             return False
        factor +=1
    return True


####3. Use a binary search to find the index of a given value within an array of integers.
# Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):

    # Check base case
    if r >= l:
        <!-- int() will only return integers so 1,2,3. No decimals -->
        mid = int(l + (r - l)/2)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        # Element is not present in the array
        return -1

<!-- Now iterative: -->
# Iterative Binary Search Function
# It returns location of x in given array arr if present,
# else returns -1
def binarySearch(arr, l, r, x):

    while l <= r:
        <!-- int() will only return integers so 1,2,3 -->
        mid = int()l + (r - l)/2);

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1



####4. An SQL exercise to extract various specific items of a table.
