class HakerRank:
    def __init__(self):
        self.m_leap = self.is_leap(year=2100)
        self.m_triplas_compare = self.compareTriplets(a=[5, 6, 7], b=[3, 6, 10])
        self.mgrade = self.gradingStudents(grades=[73, 67, 38, 33])
        self.valey_ans = self.countingValleys(s='UDDDUDUU')
        self.bassketbal_record = self.breakingRecords(scores = [10, 5, 20, 20, 4, 5, 2, 25, 1])

        # You are given the year, and you have to write a function to check if the year is leap or not.
    def is_leap(self, year):
            leap = False

            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                leap = True
            return leap

            # Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
            # Then print the respective minimum and maximum values as a single line of two space-separated long integers.

    def miniMaxSum(self, arr):

            arr.sort()

            miniMaxSum(arr)

        # Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale
        # from  to  for three categories: problem clarity, originality, and difficulty.
        # We define the rating for Alice's challenge to be the triplet a=(a[0],a[1],a[2]) ,b=(b[0],b[1],b[2])
        # Your task is to find their comparison points by comparing a[i] with b[i] for i=0,1,2
    def compareTriplets(self, a, b):
            a_points = 0
            b_points = 0
            for i in range(len(a)):

                if a[i] > b[i]:
                    a_points += 1
                if a[i] < b[i]:
                    b_points += 1

            return [a_points, b_points]

        # HackerLand University has the following grading policy:

    # Every student receives a grade in the inclusive range from 0 to 100.
    # Any  less than 40 is a failing grade.

    # Sam is a professor at the university and likes to round each student's  according to these rules:
    # If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of .
    # If the value of grade is less than 40, no rounding occurs as the result will still be a failing grade.

    def gradingStudents(self, grades):
        adjusted_grades = []

        for i in range(len(grades)):
            if grades[i] < 38:
                adjusted_grades.append(grades[i])
            if (grades[i] >= 38):
                reminder5 = grades[i] % 5
                if reminder5 >= 3:
                    grades[i] += 5 - reminder5
                    adjusted_grades.append(grades[i])
                else:
                    adjusted_grades.append(grades[i])
        return adjusted_grades

    # find the image of point p when we translate it by 180 degrees with respect to p

    # def image_of_point(ll_p,ll_q):
    #   for i in range(len(ll_p))

    # Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
    # During his last hike he took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill, D
    # step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude.
    # We define the following terms:
    # 1.A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending
    # with a step down to sea level.
    # 2.A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending
    # with a step up to sea level.

    def countingValleys(self, s):
        num_of_valeys = 0
        temp = 0
        for i in range(len(s)):
            if s[i] == "U":
                temp += 1
            if s[i] == "D":
                temp -= 1
            if temp < -1:
                num_of_valeys += 1
        return num_of_valeys

    # Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
    # She tabulates the number of times she breaks her season record for most points and least points in a game.
    # Points scored in the first game establish her record for the season, and she begins counting from there.

    def breakingRecords(self, scores):
        broke_min_count = 0
        broke_max_count = 0

        for i in range (len(scores)):
            temp=scores[i]
            if temp>broke_max_count:
                broke_max_count+=1
            if temp<broke_min_count:
                broke_min_count+=1
        return [broke_max_count, broke_min_count]

class Strings():
    def __init__(self):
        self.mint_camelcase=self.camelcase()


#Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:
#It is a concatenation of one or more words consisting of English letters.
#All letters in the first word are lowercase.
#For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
#Given , print the number of words in  on a new line.
#For example, . There are  words in the string.
    def camelcase(s):




###############################----SOLUTIONS----###################################################

haker_rank_obj = HakerRank()

print("The End")
