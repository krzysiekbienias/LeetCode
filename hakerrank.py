#You are given the year, and you have to write a function to check if the year is leap or not.

def is_leap(year):
    leap = False

    if (year % 4 == 0) and (year % 100 != 0 or year%400==0):
        leap= True
    return leap


# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):



    arr.sort()

    miniMaxSum(arr)


#Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale
# from  to  for three categories: problem clarity, originality, and difficulty.
#We define the rating for Alice's challenge to be the triplet a=(a[0],a[1],a[2]) ,b=(b[0],b[1],b[2])
# Your task is to find their comparison points by comparing a[i] with b[i] for i=0,1,2
def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for i in range(len(a)):

        if a[i] > b[i]:
            a_points += 1
        if a[i] < b[i]:
            b_points += 1

    return [a_points, b_points]


#Given a square matrix, calculate the absolute difference between the sums of its diagonals.


ans_is_leap=is_leap(year=2100)

a=[5,6,7]
b=[3,6,10]
triplas_compare=compareTriplets(a,b)

print("The End")