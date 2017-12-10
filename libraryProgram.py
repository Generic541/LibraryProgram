# -*- coding: utf8 -*-
# 도서관 연체자 기록 프로그램

# 이하는 상태 코드
INVAILD_NUMBER_GIVEN = -1
CRITICAL_FAILURE = -99

# 학생
class student:
        '''
                name        = 이름
                grade       = 학년
                classNum    = 반
                delayAmount = 연체 일수
        '''
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

# 명단 관리 클래스
# 학생들을 '어떻게 찾아낼 것인지' 기준점 같은게 있어야 함
# '학생 ID' 를 이용해서 탐색하면 됨
class ListManipulator:

        # 학생 리스트
        global StudentList
        StudentList = []

        # 토큰
        STUDENT_ID              = 100
        STUDENT_NAME            = 101
        STUDENT_GRADE           = 102
        STUDENT_CLASS_NUMBER = 103
        STUDENT_DELAY_AMOUNT = 104

        @staticmethod
        def createStudent(name, grade, classNum, studentID, delayAmount):
                # if classNum.isalpha() == False or grade.isalpha() == False or delayAmount.isalpha() == False:
                        #print StudentList
                        #return False

                instance = student(name, grade, classNum, studentID, delayAmount)
                StudentList.append(instance)
                print StudentList

        @staticmethod
        def searchStudent(studentID):
                for studentData in StudentList:
                        if studentData.getStudentID() == studentID:
                                return studentData
                return False

        # 반환형이 리스트임에 주의
        @staticmethod
        def getStudentData(token):

                dataBuffer = []
                if token == ListManipulator.STUDENT_ID:
                        for studentData in StudentList:
                                print studentData
                                dataBuffer.append(studentData)
                                return dataBuffer
                                # return lambda x: x.append(studentData.getStudentID())
                elif token == ListManipulator.STUDENT_GRADE:
                        for studentData in StudentList:
                                print studentData
                                dataBuffer.append(studentData)
                                return dataBuffer
                                # return lambda x: x.append(studentData.getGrade())
                elif token == ListManipulator.STUDENT_NAME:
                        for studentData in StudentList:
                                print studentData
                                dataBuffer.append(studentData)
                                return dataBuffer
                                # return lambda x: x.append(studentData.getName())
                elif token == ListManipulator.STUDENT_DELAY_AMOUNT:
                        for studentData in StudentList:
                                print studentData
                                dataBuffer.append(studentData)
                                return dataBuffer
                                # return lambda x: x.append(studentData.getDelayAmount())
                elif token == ListManipulator.STUDENT_CLASS_NUMBER:
                        for studentData in StudentList:
                                print studentData
                                dataBuffer.append(studentData)
                                return dataBuffer
                                # return lambda x: x.append(studentData.getClassNum())

        # 탐색이 먼저 선행된 후에 삭제해야 함. 인스턴스째로 날리면 됨
        # 일반적인 방식으로는 안될 가능성 큼(리스트가 인스턴스를 담고 있어 수정이 힘듬)
        # 파일에서 정보를 불러오는 형식으로 짜는것도 나쁘진 않을듯?
        @staticmethod
        def deleteStudent(studentID):

                idx = 0
                if ListManipulator.searchStudent(studentID) is not False:
                        instance = ListManipulator.searchStudent(studentID)

        # 몇번째 정보인지를 알아내야 함
                ID = ListManipulator.getStudentData(ListManipulator.STUDENT_ID)
                print ListManipulator.getStudentData(ListManipulator.STUDENT_ID)
                
                for i in ID:
                        if instance.getStudentID == i:
                                 # 만약 값이 없다면 여기에서 예외처리
                                idx = getStudentData(ListManipulator.STUDENT_ID).index(ID)

                del StudentList[idx]

                # 데이터 정리
                for i in range(idx, len(StudentList)-2):
                        if StudentList[i] == None: return
                        StudentList[i] = StudentList[i+1]

                return True

        @staticmethod
        def setDelayAmount(studentID, newValue):

                # 안쓰이는 코드. 개선 필요함
                if newValue <= 0:
                        return INVAILD_NUMBER_GIVEN

                if ListManipulator.searchStudent(studentID) is not False:
                        instance = ListManipulator.searchStudent(studentID)
                        print type(instance)
                        if isinstance(instance, student) is True:
                                instance.setDelayAmount(newValue)
                                return
                return False

class commandHandler:

        global Manipulator
        Manipulator = ListManipulator()

        @staticmethod
        def createStudent():
                if Manipulator.createStudent(str(raw_input("이름? : ")),
                        str(raw_input("학년? : ")), 
                        str(raw_input("반? : ")), 
                        str(raw_input("학생증 번호? : ")), 
                        str(raw_input("연체 일수? : "))) == False:
                        print("학생 정보 생성에 실패하였습니다. 정확한 정보를 입력해주세요.")

        @staticmethod
        def deleteStudent():
                try:
                        Manipulator.deleteStudent(raw_input("학생증 번호? : "))
                except(ValueError):
                        print("그 학생증 번호를 가진 학생이 없습니다.")
                except(TypeError):
                        print("현재 학생 데이터가 전혀 없습니다. 데이터를 삭제할 수 없습니다.")
                except(Exception):
                        print("알 수 없는 오류가 발생했습니다.")

        @staticmethod
        def searchStudent():
                try:
                        temp = Manipulator.searchStudent(raw_input("학생증 번호? : "))
                        print "그 학생 이름은 " + str(temp.getName()) + "입니다."
                        print "현재 " + str(temp.getGrade()) + "학년이고, " + str(temp.getClassNum()) + "반이며 " + str(temp.getDelayAmount()) + "일간 연체한 상태이며 " + "학생증 일련번호는 " + str(temp.getStudentID()) + "입니다."
                except(AttributeError):
                        print("그 학생증 번호를 가진 학생이 없습니다.")
                        print

        @staticmethod
        def setDelayAmount():
                if Manipulator.setDelayAmount(raw_input("학생증 번호? : "), 
                                        raw_input("연체 일수는 뭘로 바꾸시겠습니까? : ")) == False:
                        print "그 학생증 번호를 가진 학생이 없습니다."
                        return
                print "성공적으로 변경이 완료되었습니다."


        @staticmethod
        def showAllList():
                pass

command = commandHandler()

while(True):
        print('장흥고등학교 도서관 연체자 기록 프로그램 v 0.1')
        print('1 : 학생 정보 만들기')
        print('2 : 학생 정보 지우기')
        print('3 : 학생 연체 일수 조정하기')
        print('4 : 학생 정보 찾기')
        print('5 : 학생 정보 목록 보기')

        my_input = int(raw_input("> "))
        if my_input == 1:
                print command
                command.createStudent()
        elif my_input == 2:
                print command
                command.deleteStudent()
        elif my_input == 3:
                print command
                command.setDelayAmount()
        elif my_input == 4:
                print command
                command.searchStudent()
        elif my_input == 5:
                print command
                
