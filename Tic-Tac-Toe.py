from tkinter import *
import random
import tkinter.messagebox
trainflag=0
tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
pb = StringVar()
p1 = StringVar()
p2 = StringVar()

tracker=[1,2,3,4,5,6,7,8,9]
state = [0,0,0,0,0,0,0,0,0]

bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def reset():
    global tracker,state,bclick,flag
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "
    tracker=[1,2,3,4,5,6,7,8,9]
    state = [0,0,0,0,0,0,0,0,0]
    bclick=True
    flag=0

def btnClick(i,buttons):
    global tracker,state
    global bclick, flag, player2_name, player1_name, pb, pa
    if buttons["text"] == " " and bclick == True:
        #print("a")
        tracker.remove(i)
        state[i-1]=1
        buttons["text"] = "X"
        bclick = False
        pb = "O Wins!"
        pa = "X Wins!"
        #checkForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        tracker.remove(i)
        state[i-1]=2
        buttons["text"] = "O"
        bclick = True
        #checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        #disableButton()
        #tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        #reset()
        return 2

    elif(flag == 8):
        #tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        #reset()
        return 0

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        #disableButton()
        #tkinter.messagebox.showinfo("Tic-Tac-Toe", pb)
        #reset()
        return 1
    else:
        return -1

    
def randomplayer():
    if(len(tracker)==0):
        return 0
    return random.choice(tracker)

def clickbutton(k):
    if(k==1):
        btnClick(1,button1)
    elif(k==2):
        btnClick(2,button2)
    elif(k==3):
        btnClick(3,button3)
    elif(k==4):
        btnClick(4,button4)
    elif(k==5):
        btnClick(5,button5)
    elif(k==6):
        btnClick(6,button6)
    elif(k==7):
        btnClick(7,button7)
    elif(k==8):
        btnClick(8,button8)
    elif(k==9):
        btnClick(9,button9)

def sstate():
    global state
    return "".join([str(i) for i in state])

svf=dict()

def train1():
    global svf,state,tracker,flag
    for i in range(25000):
        reset()
        print(i,"========================================================================================")
        while(True):
            if(sstate() not in svf.keys()):
                svf[sstate()]=[0,0,0,0,0,0,0,0,0]
            print(sstate(),"------",svf[sstate()])
            
            prevstate=sstate()
            
            k=randomplayer()
            clickbutton(k)
            
            if(sstate() not in svf.keys()):
                svf[sstate()]=[0,0,0,0,0,0,0,0,0]
            print(sstate(),"====",svf[sstate()])
            if(checkForWin()==-1):
                svf[prevstate][k-1]=(1-0.6)*svf[prevstate][k-1] + 0.6*(-2+0.7*max(svf[sstate()]))
            elif(checkForWin()==0):
                svf[prevstate][k-1]=(1-0.6)*svf[prevstate][k-1] + 0.6*(5+0.7*max(svf[sstate()]))
                reset()
                break
            elif(checkForWin()==1):
                svf[prevstate][k-1]=(1-0.6)*svf[prevstate][k-1] + 0.6*(-10+0.7*max(svf[sstate()]))
                reset()
                break
            elif(checkForWin()==2):
                svf[prevstate][k-1]=(1-0.6)*svf[prevstate][k-1] + 0.6*(10+0.7*max(svf[sstate()]))
                reset()
                break
            
            prevstate=sstate()
            
            k=randomplayer()
            if(k==0):
                reset()
                break
            clickbutton(k)
            
            if(sstate() not in svf.keys()):
                svf[sstate()]=[0,0,0,0,0,0,0,0,0]
            
            if(checkForWin()==-1):
                svf[prevstate][k-1]=(1-0.6)*svf[prevstate][k-1] + 0.6*(-2+0.7*max(svf[sstate()]))
            elif(checkForWin()==0):
                svf[prevstate][k-1]=(1-0.6)*svf[prevstate][k-1] + 0.6*(5+0.7*max(svf[sstate()]))
                reset()
                break
            elif(checkForWin()==1):
                svf[prevstate][k-1]=(1-0.6)*svf[prevstate][k-1] + 0.6*(-10+0.7*max(svf[sstate()]))
                reset()
                break
            elif(checkForWin()==2):
                svf[prevstate][k-1]=(1-0.6)*svf[prevstate][k-1] + 0.6*(10+0.7*max(svf[sstate()]))
                reset()
                break

                
    trainflag=1
    tracker=[1,2,3,4,5,6,7,8,9]
    state = [0,0,0,0,0,0,0,0,0]
    print("finished")
    print(len(svf))
    

def play1():
    global svf,tracker,state,bclick,flag
    print(sstate())
    print(svf[sstate()])
    print(tracker)
    max=-10000
    for h in tracker:
        if(svf[sstate()][h-1]>max):
            max=svf[sstate()][h-1]
            o=h
    clickbutton(o)
        
    
    
buttons = StringVar()

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(1,button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(2,button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(3,button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(4,button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(5,button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(6,button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(7,button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(8,button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(9,button9))
button9.grid(row=5, column=2)

rst = Button(tk, text='RESET', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: reset())
rst.grid(row=6, column=1)

play = Button(tk, text='PLAY', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play1())
play.grid(row=0, column=0)

train = Button(tk, text='TRAIN', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: train1())
train.grid(row=0, column=2)


tk.mainloop()
