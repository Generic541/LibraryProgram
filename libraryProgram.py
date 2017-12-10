# -*- coding: utf8 -*-
# 도서관 연체자 기록 프로그램

import ListManipulator
import student

class libraryProgram:

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

# 인스턴스를 왜 여기서 구현하는거지..?
# 코드 정리가 필요함
program = libraryProgram()

while(True):
        print('장흥고등학교 도서관 연체자 기록 프로그램 v 0.1')
        print('1 : 학생 정보 만들기')
        print('2 : 학생 정보 지우기')
        print('3 : 학생 연체 일수 조정하기')
        print('4 : 학생 정보 찾기')
        print('5 : 학생 정보 목록 보기')

        my_input = int(raw_input("> "))
        if my_input == 1:
                # print command
                program.createStudent()
        elif my_input == 2:
                # print command
                program.deleteStudent()
        elif my_input == 3:
                # print command
                program.setDelayAmount()
        elif my_input == 4:
                # print command
                command.searchStudent()
        elif my_input == 5:
                # print command
                # TODO : 일괄 조회기능 구현
