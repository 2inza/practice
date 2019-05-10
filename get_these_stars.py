import tkinter 
import tkinter.messagebox

window = tkinter.Tk()
window.title("별먹기겜")
window.geometry("700x500+835+450")
window.resizable(False,False)
label1 = tkinter.Label(window, text="판 크기 입력.")
label1.place(x=0,y=0)
entry = tkinter.Entry(window)
entry.place(x=0,y=20)

def clicked1():
    tkinter.messagebox.showinfo("Error","Error Occured")

def BoardSize():
    width = entry.get()
    height = 0
    if width.isdigit():
            width = int(width)
            if width % 2 == 1:
                height = width
                return height
    else:
        return clicked1()
            

def BoardProduct():
    board = []
    line = ""
    height = BoardSize()
    cnt = 0
    while True:
        if cnt == height:
            break
        for i in range(height):
            line += '□'
            if len(line) == height:
                board.append(line)
                line = ""
            elif (len(line)) == (height//2) and cnt == (height//2):
                line += "◈"
        cnt += 1
    return board


def BoardPrint():
    height = BoardSize()
    board = BoardProduct()
    for i in range(height):
        tkinter.Label(window, text=board[i]).place(x=200,y=0 + (17*i))


button1 = tkinter.Button(window, text="완료", command=BoardPrint)
button1.place(x=0,y=40)



window.mainloop()


## 시행착오
## 테트리스 이전에, 뱀 게임,
## 뱀게임 이전에 캐릭터를 움직여서 별을 먹으면 스코어가 오르는 게임을 구현하려했으나
## 나의 무식함으로 실패
