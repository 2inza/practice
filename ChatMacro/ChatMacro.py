# 기능
# 어차피 나만 쓸것이므로 인터페이스는 깔끔히 구성할필요까진 없다
# 칸에 넣은 텍스트를 변수에 저장 후 롤 채팅에 내보내기
# 활성화/비활성화를 특정 키로 조작할수 있도록

import keyboard as kb
import tkinter as tk
import tkinter.messagebox as tkmsg
import time

wd = tk.Tk()
wd.title("LoLChatOnlyMacro by Minersya - 미네르샤")
wd.geometry("450x260+500+300")
wd.resizable(False, False)

title = tk.Label(wd, text="빈 칸에 문자를 적어넣고 저장\n그 다음 빈 칸 왼쪽의 키를 롤에서 누르셈")
title.grid(row=0, column=1)

first = tk.Label(wd, text="F1 ")
second = tk.Label(wd, text="F2 ")
third = tk.Label(wd, text="F3 ")
fourth = tk.Label(wd, text="F4 ")
fifth = tk.Label(wd, text="F5 ")
sixth = tk.Label(wd, text="F6 ")
seventh = tk.Label(wd, text="F7 ")
eighth = tk.Label(wd, text="F8 ")
ninth = tk.Label(wd, text="F9 ")
labelList = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]
for i, x in enumerate(labelList):
    i += 1
    x.grid(row=i, column=0)

firstEntry = tk.Entry(wd, width=50)
secondEntry = tk.Entry(wd, width=50)
thirdEntry = tk.Entry(wd, width=50)
fourthEntry = tk.Entry(wd, width=50)
fifthEntry = tk.Entry(wd, width=50)
sixthEntry = tk.Entry(wd, width=50)
seventhEntry = tk.Entry(wd, width=50)
eighthEntry = tk.Entry(wd, width=50)
ninthEntry = tk.Entry(wd, width=50)
entryList = [firstEntry, secondEntry, thirdEntry, fourthEntry, fifthEntry,
             sixthEntry, seventhEntry, eighthEntry, ninthEntry]
entryVariableList = ['', '', '', '', '', '', '', '', '']
for i, z in enumerate(entryList):
    i += 1
    z.grid(row=i, column=1)


def save():
    f = open("prevData.txt", 'w')
    for o, a in enumerate(entryList):
        entryVariableList[o] = a.get()
        f.write(a.get() + '}')
    f.close()


def test():
    while True:
        if kb.is_pressed('ctrl') and kb.is_pressed('`'):
            break
        elif kb.is_pressed('f1'):
            kb.press('\n')
            kb.write(entryVariableList[0])
            time.sleep(0.05)
            kb.press('\n')
        elif kb.is_pressed('f2'):
            kb.press('\n')
            kb.write(entryVariableList[1])
            time.sleep(0.05)
            kb.press('\n')
        elif kb.is_pressed('f3'):
            kb.write(entryVariableList[2])
            time.sleep(0.05)
            kb.press('\n')
        elif kb.is_pressed('f4'):
            kb.write(entryVariableList[3])
            time.sleep(0.05)
            kb.press('\n')
        elif kb.is_pressed('f5'):
            kb.write(entryVariableList[4])
            time.sleep(0.05)
            kb.press('\n')
        elif kb.is_pressed('f6'):
            kb.write(entryVariableList[5])
            time.sleep(0.05)
            kb.press('\n')
        elif kb.is_pressed('f7'):
            kb.write(entryVariableList[6])
            time.sleep(0.05)
            kb.press('\n')
        elif kb.is_pressed('f8'):
            kb.write(entryVariableList[7])
            time.sleep(0.05)
            kb.press('\n')
        elif kb.is_pressed('f9'):
            kb.write(entryVariableList[8])
            time.sleep(0.05)
            kb.press('\n')
        else:
            pass


def deleting():
    for e in entryList:
        e.delete(0, 999)


def delete_all():
    confirm = tkmsg.askokcancel('ㄹㅇ?', "모두 지우려면 확인, 아니면 취소")
    if confirm:
        deleting()
    else:
        pass


def load():
    f = open("prevData.txt", 'r')
    data = f.read()
    divided = data.split('}')
    deleting()
    for i, q in enumerate(entryList):
        q.insert(0, divided[i])
    f.close()
    save()


testButton = tk.Button(wd, text='시작, 종료 시 Ctrl + `', command=test, width=50)
testButton.grid(row=10, column=1)

saveButton = tk.Button(wd, text='저장', command=save)
saveButton.place(x=390, y=36, width=50, height=90)
loadButton = tk.Button(wd, text='불러오기', command=load)
loadButton.place(x=390, y=131, width=50, height=90)
deleteButton = tk.Button(wd, text='모두삭제', command=delete_all)
deleteButton.place(x=390, y=226, width=50, height=25)


def verifying_data():
    verified = True
    try:
        f = open("prevData.txt", 'r')
        data = f.read()
        if len(data) < 9:
            verified = False
        f.close()
    except:
        f = open("prevData.txt", 'w')
        f.write('}}}}}}}}}')
        tkmsg.showwarning('warning', "프로그램과 같은 폴더에 있는 prevData.txt는 이전에 사용했던 문장들을 저장한 파일입니다.\n"
                                     "따라서 삭제하시거나 내용을 수정하시면 작동이 안될 가능성이 있습니다.\n"
                                     "최대한 디버깅을 했으나 혹시 문제가 일어날 수 있으니 건들지 말아주세요.")
        f.close()
    if not verified:
        tkmsg.showwarning('warning', "프로그램과 같이있는 prevData.txt 파일을 건들지 말아주세요.")
        f = open("prevData.txt", 'w')
        f.seek(0)
        f.truncate()
        f.write('}}}}}}}}}')
        f.close()
        verified = True


verifying_data()
load()
save()
wd.mainloop()



