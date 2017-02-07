class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)
class Student(Person):
    def __init__(self,firstName,lastName,IdNum,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNum
        self.scores=scores
    def calculate(self):
        sumAverage=sum(scores)/len(scores)
        if sumAverage<40:
            return 'T'
        elif sumAverage>=40 and sumAverage<55:
            return 'D'
        elif sumAverage>=55 and sumAverage<70:
            return 'P'
        elif sumAverage>=70 and sumAverage<80:
            return 'A'
        elif sumAverage>=80 and sumAverage<90:
            return 'E'
        else:
            return 'O'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())