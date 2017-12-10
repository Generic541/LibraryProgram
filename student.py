# -*- coding: utf8 -*-

'''
    도서관 연체자 기록 프로그램
    Python 2.7.13에서 작동합니다.
    저작권 보호를 받지 않습니다.
    제작자 : 장현우(TC_G)

    student 모듈은 다음과 같은 메소드를 제공합니다.

    1) getName(self) : student 인스턴스의 '이름' 값을 반환합니다.
    2) getGrade(self) : student 인스턴스의 '학년' 값을 반환합니다.
    3) getClassNum(self) : student 인스턴스의 '반' 값을 반환합니다.
    4) getDelayAmount(self) : student 인스턴스의 '연체 일수' 값을 반환합니다.
    5) getStudentID(self) : student 인스턴스의 '학생증 번호' 값을 반환합니다.
    6) setName(self, newValue) : student 인스턴스의 '이름' 값을 newValue 값으로 설정합니다.
    7) setGrade(self, newValue) : student 인스턴스의 '학년' 값을 newValue 값으로 설정합니다.
    8) setClassNum(self, newValue) : student 인스턴스의 '반' 값을 newValue 값으로 설정합니다.
    9) setDelayAmount(self, newValue) : student 인스턴스의 '연체 일수' 값을 newValue 값으로 설정합니다.
    10) setStudentID(self, newValue) : student 인스턴스의 '학생증 번호' 값을 newValue 값으로 설정합니다.

    student 모듈에 대한 인스턴스는 다음과 같은 값을 넘겨야 합니다.
    - 학생 이름(name)
    - 학년(grade)
    - 반(classNum)
    - 학생증 번호(studentID)
    - 연체 일수(delayAmount)
'''


class student:
    
        def __init__(self, name, grade, classNum, studentID, delayAmount):
                self.name = name
                self.grade = grade
                self.classNum = classNum
                self.delayAmount = delayAmount
                self.studentID = studentID

        def getName(self):
                return self.name

        def setName(self, newValue):
                self.name = newValue
                return self.name

        def getGrade(self):
                return self.grade

        def setGrade(self, newValue):
                self.grade = newValue
                return self.grade

        def getClassNum(self):
                return self.classNum

        def setClassNum(self, newValue):
                self.classNum = newValue
                return self.classNum

        def getDelayAmount(self):
                return self.delayAmount

        def setDelayAmount(self, newValue):
                self.delayAmount = newValue
                return self.delayAmount

        def getStudentID(self):
                return self.studentID
