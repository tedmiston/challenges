"""
Zipped! - https://www.hackerrank.com/challenges/zipped
"""


def main():
    n, x = input().split()
    n = int(n)  # student count
    x = int(x)  # subject count
    grades = [[float(i) for i in input().split()] for i in range(x)]

    grades_by_student = zip(*grades)
    average_by_student = [sum(i) / len(i) for i in list(grades_by_student)]
    average_by_student = [round(i, 1) for i in average_by_student]

    for i in average_by_student:
        print(i)

if __name__ == '__main__':
    main()
