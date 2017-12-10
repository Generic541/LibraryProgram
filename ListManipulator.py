# -*- coding: utf8 -*-

'''
    도서관 연체자 기록 프로그램
    Python 2.7.13에서 작동합니다.
    저작권 보호를 받지 않습니다.
    제작자 : 장현우(TC_G)

    ListManipulator 모듈은 다음과 같은 메소드를 제공합니다.
    이하 메소드들은 정적 메소드(@staticmethod)로, 인스턴스를 생성할 필요가 없습니다.

    1) createStudent(name, grade, classNum, studentID, delayAmount):
       매개변수로 넘겨받은 값들을 이용해 student 클래스의 인스턴스를 생성합니다.
       또한 그 인스턴스의 주소를 반환합니다.

    2) searchStudent(studentID):
        매개변수로 넘겨받은 studentID 값을 이용해 해당 값을 가진 인스턴스를 찾습니다.

    3) deleteStudent(studentID):
        매개변수로 넘겨받은 studentID 값을 이용해 해당 값을 가진 인스턴스를 먼저 찾습니다.
        그 후 해당 인스턴스를 studentList 리스트에서 제거합니다.

    4) setDelayAmount(studentID, newValue):
        매개변수로 넘겨받은 studentID 값을 이용해 해당 값을 가진 인스턴스를 먼저 찾습니다.
        그 후 해당 인스턴스의 '연체 일수' 값을 newValue 로 변경합니다.
'''

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
