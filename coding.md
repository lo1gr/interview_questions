
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


#### hourglass problem:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # first lets get one position of the hourglass:
    hourglass = []
    count = 0
    for j in range(1,5):
        for i in range(1,5):
            center = arr[j][i]
            summation = center + arr[j-1][i]+ arr[j+1][i]+ arr[j+1][i+1] +arr[j-1][i+1]+             arr[j+1][i-1] + arr[j-1][i-1]
            if count == 0:
                maximum = summation
            count+=1
            if summation > maximum:
                maximum = summation
            # hourglass.append(summation)
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


####A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .
####Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
<!-- sample input:
5 4
1 2 3 4 5 -->
<!-- sample output:
5 1 2 3 4 -->

    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    # input:
    # len(array)  number_rot
    # array

    # Complete the rotLeft function below.
    def rotLeft(a, d):
        # a is array d is number of rotations
        # d is modulo the len of array since it would just loop around same values!
        # d = len(a) % d

        # use slicing
        # take first d elements
        end = a[:d]
        del a[:d]
        a.extend(end)

        return ( " ".join( str(e) for e in a ) )


    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        nd = input().split()

        n = int(nd[0])

        d = int(nd[1])

        a = list(map(int, input().rstrip().split()))

        result = rotLeft(a, d)

        # fptr.write(' '.join(map(str, result)))
        fptr.write(str(result))
        fptr.write('\n')

        fptr.close()


#### New Year Chaos:
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if  and  bribes , the queue will look like this: .

What is minimum number of bribes that took place to get the queue into its current state!

<!-- input:
Input Format

The first line contains an integer , the number of test cases.

Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.
-->

<!-- output:
Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people. -->



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(Q):
    #
    # initialize the number of moves
    moves = 0
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    Q = [P-1 for P in Q]
    #
    # Loop through each person (P) in the queue (Q)
    for i,P in enumerate(Q):
        # i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of
        # its original position
        if P - i > 2:
            return "Too chaotic"
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
    return moves

    # now we know it is clean, have figure out # changes:

    for index, el in enumerate(q):
        diff = index-el
        if diff != 0:
            # then swap with element in position
            count+=1
            q[index], q[index+diff] = q[index+diff], q[diff]
    return count



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
