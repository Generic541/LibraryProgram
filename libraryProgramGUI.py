#' -*- coding:utf8 -*-

from Tkinter import *

class studentListViewer(Frame):
    def __init__(self, master):

        # StudentList Listbox Packing
        studentList = Listbox(master)
        studentList.grid(row=0, column=0)

        # Entry packing
        InputBox = Entry(master)
        InputBox.grid(row=1, column=0)

        # Button packing - Student Creation Button
        studentCreateBtn = Button(master, text="학생 정보 만들기")
        studentCreateBtn.grid(row=1, column=1)

        # Button packing - Student deletion Button
        studentDeleteBtn = Button(master, text="학생 정보 지우기")
        studentDeleteBtn.grid(row=1, column=2)

        # Button packing - Student info search Button
        studentSearchBtn = Button(master, text="학생 정보 찾기")
        studentSearchBtn.grid(row=1, column=3)

        # Button packing - student book rent delay date modification Button
        studentBookModBtn = Button(master, text="연체 일수 조정하기")
        studentBookModBtn.grid(row=1, column=4)


# Program main func
def main():
    
    # Represents GUI size as "Horizontal*Vertical+(X padding)+(Y padding)"
    root = Tk()
    root.geometry('500x400')
    libraryProgram = studentListViewer(root)
    root.mainloop()

if __name__ == '__main__':
    main()
