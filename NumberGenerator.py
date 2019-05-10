# 주민번호 생성기/분석기

## 기능.
# -주민번호를 생성하거나, 분석할수있다.

### 해야할 것.
# - 생성버튼을 만든다.
# - 버튼을 누르면, 6자리의 숫자, 7자리의 숫자를 만들고, 문자화 한다.
# - 그 사이에 "-"를 넣는다.
# - 그후 출력한다.

# - 분석버튼을 만든다.
# - 주민번호를 입력받는다.
# - 버튼을 누르면, 앞의 6자리의 숫자로 생년월일을 뽑아낸다.
# - 그후에 7자리의 맨 앞자리로 성별을 알아낸다.
# - 생년월일과 성별을 출력한다.

# - 만들어보기(가리기 기능)
# - 주민번호의 뒷자리 6개를 문자열 *로 변환시킨다.
# - 생성 이후에 변환시킬수 있도록 할것.

import random

def yoon(y):
    return y % 4 == 0
## 윤년 (1년이 366일인 해) 계산.
## 년의 단위수가 3자리 이상일경우 100의 약수 400의 약수 등 다른 조건이있으나
## 주민번호에선 해당년도의 뒷자리 2자리밖에 나오지않으므로 4의 약수로만 계산함.
## 만들고나서 람다식으로도 만들수도 있겠다 싶었는데 if 조건에는 람다가 안들어가는것 같음. 내가 못넣는건가


def product_front():
    months = [4,6,9,11]
## 일수가 30일까지 있는 달.

    yy = str(random.randrange(0,100)).zfill(2)
    mm = str(random.randrange(1,13)).zfill(2)
## 년과 월을 만든다.

    if int(mm) == 2 and yoon(int(yy)) == True:
        dd = str(random.randrange(1,30))
    elif int(mm) == 2:
        dd = str(random.randrange(1,29))
    elif months.count(int(mm)) == True:
        dd = str(random.randrange(1,31))
    else:
        dd = str(random.randrange(1,32))
    dd = dd.zfill(2)
## 윤년을 계산, 윤년일경우이며 2월일경우 1~29일까지
## 윤년이 아니지만 2월일경우 1~28일까지
## 윤년이 아니면서 4,6,9,11월일경우 1~30일까지
## 세가지 모두 아닐경우 1~31일까지.
## 년 월 일 모두 1자리수일땐 0을 붙여 2자릿수로 만들어준다.
    return yy + mm + dd
## 앞 6자리 완성


def product_back():
    sex = str(random.randrange(1,5)) # 주민번호 첫자리
    loc = str(random.randrange(0,97)).zfill(2) # 주민번호 2~3번째 자리 (장소)
    while int(loc) == 44:
        loc = "96"             ## 44는 이젠 부여되지 않으므로 제외함.
                               ## 이전에 44를 부여받은 사람은
                               ## 96으로 바뀌었다고함.
    cen = str(random.randrange(0,100)).zfill(2) ## 주민센터 고유번호. 모르므로 그냥 난수.
    
    order_list = [1,1,1,1,1,1,1,2,2,random.randrange(3,10)]
    order = str(random.choice(order_list)) ## 주민센터에 출생신고된 순서.
    
    ## 보통은 1이지만, 쌍둥이이거나, 같은동에서 출산이 여러번 일어난 경우
    ## 2가 나오고, 그 이상이 나올때도 있지만 흔하진않으므로 만듬.
    
    front = product_front()
    cnt,temp = 0,0
    for i in range(2,8):
        temp += int(front[cnt]) * i
        cnt += 1
    temp += (int(sex)*8)+(int(loc[0])*9)+(int(loc[1])*2)+(int(cen[0])*3)+(int(cen[1])*4)+(int(order)*5)
    last = str(((temp % 11) - 11)%10)
    return sex+loc+cen+order+last

    ## 7번째 자리는 주민번호 앞자리와 뒷자리의 6번째 자릿수의 숫자를 
    ##  [{ 11 - {(2(Y1)+3(Y2)+4(M1)+5(M2)+6(D1)+7(D2)+8(sex)+9(loc[0])+2(loc[1])+3(cen[0])+4(cen[1])+5(order)) % 11} } % 10 ]
    ## 해당 공식에 따라 계산된 수라는 것을 구글링해서 찾아냈다.
    ## 생년월일을 2~7까지 자릿수마다 각각 곱하고, 뒷자리 6자리를 8,9,2,3,4,5 순으로 곱한뒤
    ## 11로 나누어 그 나머지에서 11을 뺀 수의 1번째 자리가 주민번호 뒷자리의 마지막자리 수다.

def product():
    return product_front()+"-"+product_back()

## 주민번호 생성기.
## 생성만 했고 분석은 다음에하자. 2019-04-21

from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.title("주민번호 생성기")
window.geometry("350x150+835+450")
window.resizable(False,False)

def change_text():
    entry.delete(0,14)
    number = product()
    label2.configure(text="        생성됨\n        "+number)
    entry.insert(0,number)

def analysis():
    number = entry.get()
    anal_result = ""
    year,month,day,age,sex,loc = "","","","","",""
    
    if len(number) < 14:
        label3.configure(text="오류: 주민번호 없음")
    
    if int(number[0:2]) <= 20:
        year = "20" + number[0:2]
    else: year = "19" + number[0:2]
    month = number[2:4]
    day = number[4:6]
    
    age = str((list(time.localtime())[0] - int(year)) + 1)
    
    if int(number[7:8])%2 == 1:
        sex = "남성"
    else: sex = "여성"
        
    if int(number[8:10]) <= 8: loc = "서울"
    elif int(number[8:10]) <= 12: loc = "부산"
    elif int(number[8:10]) <= 15: loc = "인천"
    elif int(number[8:10]) <= 25: loc = "경기도"
    elif int(number[8:10]) <= 34: loc = "강원도"
    elif int(number[8:10]) <= 39: loc = "충청북도"
    elif int(number[8:10]) == 40: loc = "대전"
    elif int(number[8:10]) <= 43 or int(number[8:10]) >=45 and int(number[8:10]) <= 47: loc = "충청남도"
    elif int(number[8:10]) == 96: loc = "세종시"
    elif int(number[8:10]) <= 54: loc = "전라북도"
    elif int(number[8:10]) <= 56: loc = "광주"
    elif int(number[8:10]) <= 66: loc = "부산"
    elif int(number[8:10]) <= 70: loc = "대구"
    elif int(number[8:10]) <= 81: loc = "경상북도"
    elif int(number[8:10]) <= 84 or int(number[8:10]) >=86 and int(number[8:10]) <= 91: loc = "경상남도"
    elif int(number[8:10]) == 85: loc = "울산"
    elif int(number[8:10]) <= 95: loc = "제주"
    anal_result= "나이 : "+age+"    생일 : "+year+"년 "+month+"월 "+day+"일\n","성별 : "+sex+"    출생지 : "+loc
    label3.configure(text=anal_result)

def clicked1():
    messagebox.showinfo("도움말",
                 '''주민번호 생성/분석기.
- 생성을 누르면 주민번호를 생성해 자동으로
  분석기 칸에 넣어줌.

- 분석을 누르면 입력되어있는 주민번호를 분석하여
  나이, 생일, 성별, 출생신고지 출력.

- 생성을 누르지않은채로 분석을 눌러도 가능.''')

label = Label(window, text="주민번호 생성/분석\n")
label.grid(row=0,column=0)

label2 = Label(window, text="")
label2.grid(row=0,column=1)

label3 = Label(window, text="")
label3.grid(row=1,column=1)

entry = Entry(window)
entry.grid(row=1,column=0)

button = Button(window, text="생성",font="Consolas", command=change_text)
button.grid(row=3, column=0)

button2 = Button(window, text="분석",font="Consolas", command=analysis)
button2.grid(row=3,column=1)

button3 = Button(window, text="도움말",font="Consolas",command=clicked1)
button3.grid(row=2,column=1)
window.mainloop()