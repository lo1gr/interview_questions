import sys
# to run them navigate to this folder using the terminal command:
# cd folder
# then python3 interview_test.py < data1.txt
# if want to feed first exercise, data2.txt if want to feed second etc.

# order statistic:
# Goal is to find the k order statistic in an array:
# input type:
# 5
# 1 2 5 6 7 8 9 99
# output: 7
# k = int(input())
# a = list(map(int, input().rstrip().split()))
#
# a.sort()
# print(a[k-1])
#
# #
# # Recommender system:
# # input:
# # Bob:Rock,Blues,Jazz
# # Alice:Rock,Jazz,Blues
# # John:Jazz,Blues,Rock
# #
# # Look for users with lower amount of inversions compared with the base users
# # Input:
# # This is the active user, aka the first line
# # Output:
# # This is an array for the reference users:
#
# queries = []
# # if know how many end users:
# # for _ in range(2):
# #     queries.append(list(map(str, input().rstrip().split())))
# while True:
#     try:
#         queries.append(list(map(str, input().rstrip().replace(':',',').split(','))))
#     except(EOFError):
#         break
#
# active = queries[0]
#
# # get array of number [1,2,3,4] whatever length-1 of the preferences is
# # eg bob likes 3 stuff. len will be 4 (bob + 3 stuff) but range stops at -1
# num = list(range(1,len(queries[0])))
# dct = dict(zip(queries[0][1:], num))
#
# # remove the active user since we have the mapping already:
# queries = queries[1:]
# # extract the username
# untouched = [el[0] for el in queries]
#
# for i in range(0,len(queries)):
#     queries[i][1:] = list(map(dct.get, queries[i][1:]))
#
# # now lets calculate the minimum swaps:
# def countSwaps(a):
#     numSwaps = 0
#     while True:
#         SwapsFlag = False
#         for i in range(len(a)-1):
#             if a[i] > a[i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]
#                 numSwaps += 1
#                 SwapsFlag = True
#         if not SwapsFlag:
#             break
#     return numSwaps

# print(queries)
# let's count the number of swaps now:
# arr_swaps = []
# for i in range(len(queries)):
#     arr_swaps.append(countSwaps(queries[i][1:]))
#
# # make a dict with key: untouched and value: arr_swaps
# dict2 = dict(zip(untouched, arr_swaps))
#
# # sort dict per value:
# import operator
#
# # sort item per value
# output_sorted = sorted(dict2.items(), key= operator.itemgetter(1))
#
# # output the names, having been already sorted
# for i in output_sorted:
#     print(i[0], end=' ')
#
#
#
# Normalize levels:
# array of values, take the max, and modify the values in the array so that they are:
# value*100/max
#
# queries = []
# while True:
#     try:
#         queries.append(list(map(int, input().rstrip().split(','))))
#     except(EOFError):
#         break
#
# def normalize_me(arr,max):
#     return [x*100/max for x in arr]
#
# normalized = []
# for arr in queries:
#     maximum = max(arr)
#     print(maximum)
#     normalized.append([x*100//maximum for x in arr])
#
# print(normalized)
#
#
#
#
#
#




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



# import sys
# from statistics import mean
#
# arr = []
# for line in sys.stdin:
#     arr.append(line.rstrip())
#
#
# # date is leftmost 10 elements of array of array
# # print(len('2009-03-02'))
# dates = [el.split('|')[0] for el in arr]
# prices = [float(el.split('|')[1]) for el in arr]
#
#
#
# for i in range(50,len(dates)):
#     count = 0
#     # The prices of the day of also influence in the DMA
#     # reasonable assumption: weekends do not matter, only look at trading days
#     DMA_9 = mean(prices[i-8:i+1])
#     DMA_50 = mean(prices[i-49:i+1])
#     if DMA_9 > DMA_50:
#         count+=1
#         print(dates[i])
#
# if count==0:
#     print('NULL')


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
