
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


#### Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

#### For example, the length of your array of zeros . Your list of queries is as follows:
#### https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#### a b k
#### 1 5 3
#### 4 8 7
#### 6 9 1
#### index->	 1 2 3  4  5 6 7 8 9 10
####	[0,0,0, 0, 0,0,0,0,0, 0]
####	[3,3,3, 3, 3,0,0,0,0, 0]
####	[3,3,3,10,10,7,7,7,0, 0]
####	[3,3,3,10,10,8,8,8,1, 0]
####largest value is 10



        #!/bin/python3

        import math
        import os
        import random
        import re
        import sys

        # Complete the arrayManipulation function below.
        def arrayManipulation(n, queries):
                # Big O (N)
                res = [0] * (n+1) # we only really need one terminal row, since we're applying each pass to all rows below
                return res, queries


                # loop through all the queries and apply the increments/decrements for each
                # Big O (M) (size of queires)
                for row in range(len(queries)):
                        a = queries[row][0]
                        b = queries[row][1]
                        k = queries[row][2]

                        res[a-1] += k # increment the starting position
                        # this is where a loop would increment everything else between a & b by k
                        # but instead of taking b-a steps, we take a constant 2 steps, saving huge on time
                        res[b] -= k # decrement the position AFTER the ending position
                # now loop through res one time - Big O (N) (size of res)
                sm = 0 # running sum
                mx = 0 # maximum value found so far
                # loop2 that checks the overlap:

                for i in range(len(res)):
                    # only sum the positive values
                        sm += res[i]
                        if sm > mx:
                                mx = sm

                # total run time is Big O (2*N + M) >> Big O(N)
                return mx


        if __name__ == '__main__':
            fptr = open(os.environ['OUTPUT_PATH'], 'w')

            nm = input().split()

            n = int(nm[0])

            m = int(nm[1])

            queries = []

            for _ in range(m):
                queries.append(list(map(int, input().rstrip().split())))

            result = arrayManipulation(n, queries)

            fptr.write(str(result) + '\n')

            fptr.close()




#### Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.
#### Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
####For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is No.
####input format:
####The first line contains two space-separated integers, m and n, the numbers of words in the magazine and the note..
####The second line contains m space-separated strings, each magazine[i].
####The third line contains n space-separated strings, each note[i].


input:
6 5
two times three is not four
two times two is four
output:
No

<!-- because two only appears once in the magazine -->



            #!/bin/python3

            import math
            import os
            import random
            import re
            import sys
            from collections import Counter

            # Complete the checkMagazine function below.
            def checkMagazine(magazine, note):
                if (Counter(note) - Counter(magazine)) == {}:
                    return "Yes"
                return "No"

            if __name__ == '__main__':
                mn = input().split()

                m = int(mn[0])

                n = int(mn[1])

                magazine = input().rstrip().split()

                note = input().rstrip().split()

                print(checkMagazine(magazine, note))


#### Given two strings, determine if they share a common substring. A substring may be as small as one character.
#### For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
<!-- input: 2
hello
world
hi
world -->
<!-- output:
YES
NO -->

                # Complete the twoStrings function below.
                def twoStrings(s1, s2):
                    return 'YES' if set(list(s1)) & set(list(s2)) != set() else 'NO'

#### Sherlock and Anagrams
#### Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of #### substrings of the string that are anagrams of each other.

#### For example s=mom, the list of all anagrammatic pairs is  [m,m], [mo,om] at positions  (0,2) (0,1) (1,2) respectively.
def sherlockAndAnagrams(s):
    count = []
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a'] * b[j],2))) for j     in b]))
    return sum(count)



#### counting triplets:
<!-- https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen -->




        from collections import Counter

        def countTriplets(arr, r):
            r2 = Counter()
            r3 = Counter()
            count = 0

            for v in arr:
                if v in r3:
                    count += r3[v]

                if v in r2:
                    r3[v*r] += r2[v]

                r2[v*r] += 1

            return count



#### You are given  queries. Each query is of the form two integers described below:
- 1 x : Insert x in your data structure.
- 2 y : Delete one occurence of y from your data structure, if present.
- 3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
<!-- https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen -->
<!-- works but run time error for some: -->
def freqQuery(queries):
    output = []
    three_out = []
    for operation in queries:
        if operation[0] == 1:
            output.append(operation[1])
        elif operation[0] == 2:
            output.remove(operation[1])
        else:
            if operation[1] in Counter(output).values():
                three_out.append(1)
            else:
                three_out.append(0)
    return three_out

    def freqQuery(queries):
        # freq is count of all elements added with operation 1 & 2
        freq = Counter()
        cnt = Counter()
        result = []
        for action, value in queries:
            if action == 1:
                cnt[ freq[value] ] -= 1
                freq[value] += 1
                cnt[ freq[value] ] += 1
                # return freq, cnt
            elif action == 2:
                if freq[value] > 0:
                    cnt[ freq[value] ] -= 1
                    freq[value] -= 1
                    cnt[ freq[value] ] += 1
                    return freq, cnt
            else:
                result.append(1 if cnt[value] > 0 else 0)
        return result



####SORTING:
#### Bubble sort algorithm:
#### compare the current index with the following, if it is higher, then swap elements
<!-- https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting -->
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numSwaps = 0
    while True:
        SwapsFlag = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                numSwaps += 1
                SwapsFlag = True
        if not SwapsFlag:
            break
    print('Array is sorted in', numSwaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

#### Mark and Toys


# Complete the maximumToys function below.
#Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if prices = [1,2,3,4] and Mark has k=7 to spend, he can buy items [1,2,3] for 6, or [3,4] for 7 units of currency. He would choose the first group of  items.
<!-- https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting -->
def maximumToys(prices, k):
    # first get a sorted array
    prices.sort()
    count = 0
    for i in prices:
        if (i <= k):
            count += 1
            # spent money so decrease pot by what was spent
            k -= i
        else:
            break
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#### Sorting: Comparator
<!-- https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting -->
Declare a Checker class that implements the comparator method as described. It should sort first descending by score, then if 2 have the
same score, ascending by name. The code stub reads the input, creates a list of Player objects, uses your method to sort the data, and prints it out properly.

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score=score

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        if a.name < b.name:
            return -1
        else:
            return 1

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)

@TODO: this one!
#### Fraudulent activity notifications
<!-- https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting -->



#### Merge Sort: Counting Inversions basically just like the bubble sort count But
#### we want faster execution time
<!--
Sample input:
2  
5  
1 1 1 2 2  
5  
2 1 3 1 2
Sample output:
0  
4   
-->
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    res = [0] * len(arr)

    return merge(arr, res, 0, len(arr)-1)


def merge(arr, res, left, right):
    if left >= right:
        return 0

    inversions = 0

    left_end = (left + right) // 2
    right_start = left_end + 1

    inversions += merge(arr, res, left, left_end)
    inversions += merge(arr, res, right_start, right)
    inversions += mergeHalf(arr, res, left, right)
    return inversions


def mergeHalf(arr, res, left, right):
    if left >= right:
        return 0

    inversions = 0

    left_end = mid = (left + right) // 2
    right_start = right_beg = left_end + 1
    left_beg = index = left

    while left <= left_end and right_start <= right:
        pt1 = arr[left]
        pt2 = arr[right_start]

        if pt1 <= pt2:
            res[index] = pt1
            index += 1
            left += 1
        else:
            res[index] = pt2
            index += 1
            inversions += mid - left + 1
            right_start += 1

    while left <= left_end:
        res[index] = arr[left]
        left += 1
        index += 1

    while right_start <= right:
        res[index] = arr[right_start]
        right_start += 1
        index += 1


    arr[left_beg:left_end + 1] = res[left_beg:left_end + 1]
    arr[right_beg:right + 1] = res[right_beg: right + 1]

    return inversions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()




####STRING MANIPULATION:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
# input is two strings
# output: single integer denoting the number of characters you must delete to make the two strings anagrams of each other. Anagrams is when they contain the same letters, in a different order or not.
<!-- eg:
input:
cde
abc
output:
4
we have to delete d, e, a and b to make the words anagrams-->

from string import ascii_lowercase

def makeAnagram(a, b):
    count = 0
    for letter in ascii_lowercase:
        ia = a.count(letter)
        ib = b.count(letter)
        # add to the count var the difference between the count of a specific letter
        #
        count += abs(ia - ib)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

#Alternating characters
<!-- https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen -->
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
# Output: For each query, print the minimum number of deletions required on a new line.


<!--
Input:
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Output:
3
4
0
0
4
 -->

def alternatingCharacters(s):
    deletions = 0
    for i in range(len(s)):
        try:
            if s[i] == s[i+1]:
                deletions+=1
        except IndexError:
            break
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

# Special String Again
s = mnoopoo substrings are {m, n, o, o, p, o, o, non, ono, opo, oo}
output must be number of words that can be formed:
<!--
input:
4
aaaa
output:
10: a,a,a,a, aa,aa,aa,aaa,aaa,aaaa -->
<!-- https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen -->


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.

def triangular_number(n):
    return (n**2+n)/2

# 1) len(s) -> count all char of the word;
# 2) exp1 -> count all words that follow this rule: a_a also aaaa_aaaa;
# 3) exp2 -> count all repeated char of the word and with triangular number all combinations of these repeated chars. Example of this step is: aaaa has the combination of:
# 'aa'+'aa'+'aa'+'aaa'+'aaa'+'aaaa' = 6 (realize 6 is the same T3 of triangular number sequence).
def substrCount(n, s):
    count = len(s)

    exp1 = r'(([a-z])\2*)(?!\1)(?=[a-z]\1)'
    m = re.finditer(exp1,s)
    count += sum([len(x.group(0)) for x in m])

    exp2 = r'([a-z])\1+'
    m = re.finditer(exp2,s)
    count += sum([triangular_number(len(x.group(0))-1) for x in m])

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


# Common child
A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD different from ABDC.

<!--
input:
SHINCHAN
NOHARAAA
output:
3
 -->

 #!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the commonChild function below.
def commonChild(s1, s2):
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for _ in range(n + 1)]

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    return lcs[n - 1][m - 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()


# Greedy Algorithm

# Minimum Absolute Difference in an Array
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
# two solutions, more or less the same:
# want to find minimum absolute difference between all elements in array
<!-- https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms -->
<!--
input:
5
1 -3 71 68 17
output:
3
-->

def minimumAbsoluteDifference(arr):
    arr.sort()
    minus = math.inf
    print(arr)
    for i in range(1,len(arr)):
        diff = abs(arr[i-1]-arr[i])
        print(diff)
        if diff < minus:
            minus = diff
            print('min: ' + str(min))
    return minus



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



def minimumAbsoluteDifference(arr):

    arr.sort()

    return min([abs(arr[counter+1] - arr[counter]) for counter in range(len(arr)-1)]



# Luck Balance
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers,  and :

 First number is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by the second item; if she loses it, her luck balance will increase by the first item.
 The second number enotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.
If Lena loses no more than  important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.
<!-- https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms -->

<!-- input:
6 3
5 1
2 1
1 1
8 1
10 0
5 0
output:
29
There are 6 contests. Of these contests, 4 are important and she cannot lose more than 3 of them. Lena maximizes her luck if she wins the 3rd important contest (where L[i]=1) and loses all of the other five contests for a total luck balance of 5+2+8+10+5-1 = 29. -->

2 solutions

def luckBalance(k, contests):
    # sort from greatest luck to least luck, so that can add them in importance
    contests.sort(reverse=True)
    luck = 0

    for contest in contests:
    # meaning if it is nonimportant to miss
        if contest[1] == 0:
            luck += contest[0]
    # it is important to miss, check if we can miss it
        elif k > 0:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]

    return luck



    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    # Complete the luckBalance function below.
    def luckBalance(k, contests):
        # k is the number of important contests she can lose
        # if it is unimportant, then can just lose it and get the luck value
        # fail the most number of important ones, with the highest luck value

        count = sum([el[0] for el in contests if el[1] == 0])

        # fail k contests, but the ones with the most points
        contests_win = [el[0] for el in contests if el[1] == 1]

        # sorted sorts a list based on the first element
        contests_win = sorted(contests_win, reverse = True)
        # or t.sort(key=lambda x: x[0])reverse

        count = count + sum(contests_win[:k]) - sum(contests_win[k:len(contests_win)])

        return count

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        contests = []

        for _ in range(n):
            contests.append(list(map(int, input().rstrip().split())))

        result = luckBalance(k, contests)

        fptr.write(str(result) + '\n')

        fptr.close()

# Water count:
<!-- https://leetcode.com/problems/container-with-most-water/solution/ -->
We have to maximize the Area that can be formed between the vertical lines using the shorter line as length and the distance between the lines as the width of the rectangle forming the area.

Approach1: Brute force:
class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0

        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                max_area = max(max_area,min(height[i],height[j]) * (j-i))
        return max_area

Approach2: two pointer approach
class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        l = 0
        r = len(height)-1

        while(l<r):
            max_area = max(max_area,min(height[r],height[l]) * (r-l))

            if (height[l] < height[r]):
                l+=1
            else:
                r-=1
        return max_area

Idea:
when have two pointers at the two ends,
can only increase the area covered by moving the pointers if we increase the height
of the pointers. Hence the lower of the two pointers will be changed for the next one
and the area will be compared to the previous one.


#Best time to buy a stock
<!-- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ -->

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Approach1 (Brute Force):
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_return = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if i < j:
                    max_return = max(max_return, j-i)

        return max_return

Approach2 (one pass):
IDEA: The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = math.inf
        max_profit = 0

        for i in range(len(prices)):
                if prices[i] < minprice:
                    minprice = prices[i]
                elif (prices[i] - minprice > max_profit):
                    max_profit = prices[i] - minprice

        return max_profit

#Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

        You may assume no duplicates in the array.
<!-- https://leetcode.com/problems/search-insert-position/submissions/ -->
        class Solution:
            def searchInsert(self, nums: List[int], target: int) -> int:
                i=0
                index=0
                if target in nums:
                    return nums.index(target)
                else:
                    while i <len(nums):
                        if target > nums[i]:
                            index=i+1
                        i+=1
                return index









-- Challenges that I had: --
ROLE = 061152

import sys
# order statistic:

k = int(input())
a = list(map(int, input().rstrip().split()))

a.sort()
print(a[k-1])


# Recommender system:
# input:
# Bob:Rock,Blues,Jazz
# Alice:Rock,Jazz,Blues
# John:Jazz,Blues,Rock
# Look for users with lower amount of inversions compared with the base users
# This is the active user, aka the first line

# This is an array for the reference users:

queries = []
# if know how many end users:
# for _ in range(2):
#     queries.append(list(map(str, input().rstrip().split())))
while True:
    try:
        queries.append(list(map(str, input().rstrip().replace(':',',').split(','))))
    except(EOFError):
        break

active = queries[0]

num = list(range(1,len(queries[0])))

dct = dict(zip(queries[0][1:], num))

# remove the active user since we have the mapping already:
queries = queries[1:]
# extract the username
untouched = [el[0] for el in queries]

for i in range(0,len(queries)):
    queries[i][1:] = list(map(dct.get, queries[i][1:]))

# now lets calculate the minimum swaps:
def countSwaps(a):
    numSwaps = 0
    while True:
        SwapsFlag = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                numSwaps += 1
                SwapsFlag = True
        if not SwapsFlag:
            break
    return numSwaps

# print(queries)
# let's count the number of swaps now:
arr_swaps = []
for i in range(len(queries)):
    arr_swaps.append(countSwaps(queries[i][1:]))

# make a dict with key: untouched and value: arr_swaps
dict2 = dict(zip(untouched, arr_swaps))
# sort dict per value:
import operator

# sort item per value
output_sorted = sorted(dict2.items(), key= operator.itemgetter(1))

# output the names, having been already sorted
for i in output_sorted:
    print(i[0], end=' ')



# Normalize levels:
# array of values, take the max, and modify the values in the array so that they are:
# value*100/max

queries = []
while True:
    try:
        queries.append(list(map(int, input().rstrip().split(','))))
    except(EOFError):
        break

def normalize_me(arr,max):
    return [x*100/max for x in arr]

normalized = []
for arr in queries:
    maximum = max(arr)
    print(maximum)
    normalized.append([x*100//maximum for x in arr])

print(normalized)




# Stock Trader - Bullish Cross
# Programming challenge description:
# A classic stock trading pattern happens when a 9-Day Moving Average (9-DMA) crosses the 50-Day Moving Average (50-DMA). This can be indicative of a bullish or a bearish setup, depending on the direction.
#
# When the 9-DMA crosses above the 50-DMA from below, it is Bullish. When the 9-DMA cross below the 50-DMA from above, it is Bearish.
#
# Write a program that reads in a series of dates and prices, calculates the 9-DMA and 50-DMA, then returns the dates of any bullish signals that occurred.
#
# NOTE: The Moving Average cannot be calculated for a given day if there is not enough historical data to cover the period in question. For example, a series of prices that begin on January 1 cannot have a 9-DMA calculated before January 9 since 9 days of historical prices do not exist until January 9.
#
# Input:
# A series of Date|Price pairs in non-localized format. Dates will follow ISO 8601 format YYYY-MM-DD. Prices will be a two-decimal value with no currency indications.
#
# For example:
#
# 2016-01-01|22.05
# 2016-01-02|22.45
# 2016-01-03|23.57
# Output:
# A date in ISO 8601 format where a Golden Cross occurred. If no Golden Cross happened, return the string NULL



import sys
from statistics import mean

arr = []
for line in sys.stdin:
  arr.append(line.rstrip())


date is leftmost 10 elements of array of array
print(len('2009-03-02'))
dates = [el.split('|')[0] for el in arr]
prices = [float(el.split('|')[1]) for el in arr]



for i in range(50,len(dates)):
    count = 0
    # The prices of the day of also influence in the DMA
    # reasonable assumption: weekends do not matter, only look at trading days
    DMA_9 = mean(prices[i-8:i+1])
    DMA_50 = mean(prices[i-49:i+1])
    if DMA_9 > DMA_50:
        count+=1
        print(dates[i])

if count==0:
    print('NULL')



# Median of Medians
# Input:
# 3
# 1 2 5 4 6 3 7 8
# Output:
# 4
# 1. Divide the list into sublists with k elements. Last sublist may contain fewer than k elements
# 2. Sort each sublist, get its median and append it to another list containing medians of sublists
# 3. If the medians list has a length more than k, compute its median recursively, proceeding with step1
# 4. If the medians list has k elements or fewer, sort it and determine its median. Return it as a pivot
# If an array is of odd length, the median is the middle element after the array has been sorted.
# If an array is of even legnth, there are two middle elements after it has been sorted. In this case,
# we will define the median as the left (first) of these 2 middle elements.

k = int(input())
arr = list(map(int, input().split()))

def get_median(arr):
    arr.sort()
    median = "ODD"
    size = len(arr)
    # case if even
    if size%2 == 0:
        median = arr[int((size/2)-1)]
    else:
        # int(2.9) will return 2 because int() truncates
        median = arr[int(size/2)]
    return median

def median_of_medians(arr, k):
    # 1. divide list into sublists of k elements
    chunks = [arr[i * k:(i + 1) * k] for i in range((len(arr) + k - 1) // k )]
    # 2. Append medians of sublists together
    medians = list(map(get_median,chunks))
    # 3. if medians list has length > k, compute its median recursively, proceeding with step1
    if len(medians) > k:
        median_of_medians(medians, k)
# If the medians list has k elements or fewer, sort it and determine its median.
# Return it as a pivot
    else:
        print(get_median(medians))

median_of_medians(arr,k)





Leetcode:
<!-- https://leetcode.com/problems/integer-to-roman/submissions/ -->

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Input: 3
Output: "III"

Input: 4
Output: "IV"

class Solution:
    def intToRoman(self, num: int) -> str:
        coding = zip([1000,900,500,400,100,90,50,40,10,9,5,4,1],
        ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        )
        result = []
        for n, r in coding:
            while num>=n:
                result.append(r)
                num -=n
        return ''.join(result)
