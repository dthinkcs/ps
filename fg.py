
# copy the function you have this is just for my convenniece
def finalGrade(scoresList):
    weights = [0.05, 0.05, 0.40, 0.50]
    grade = 0
    for i in range(len(scoresList)):
        grade += float(scoresList[i]) * weights[i]
    return grade

import csv
def main():
    with open('something.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        file = open('something.txt')
        for row in spamreader:
            student = file.readline().strip()
            scores = row
            print(student, finalGrade(scores))
            


if __name__ == "__main__":
    main()
