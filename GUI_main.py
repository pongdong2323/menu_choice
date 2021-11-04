from tkinter import *
import random

def food():
    menu = ["짜장면", "짬뽕", "라면", "김밥", "돈까스"]
    a = random.randint(0, 4)
    
    label1.config(text="{}".format(menu[a]))

    global photo2
    photo_jja = PhotoImage(file=r"D:\DK\rob_py\picture\jja.png")
    photo_jjam = PhotoImage(file=r"D:\DK\rob_py\picture\jjam.png")
    photo_ra = PhotoImage(file=r"D:\DK\rob_py\picture\ra.png")
    photo_gim = PhotoImage(file=r"D:\DK\rob_py\picture\gim.png")
    photo_don = PhotoImage(file=r"D:\DK\rob_py\picture\don.png")
    photo2 = [photo_jja, photo_jjam, photo_ra, photo_gim, photo_don]
    label2.config(image=photo2[a])

root = Tk()
root.title("오늘 머 먹지")
root.geometry("540x380")

label1 = Label(root, text = "추천메뉴")
label1.pack()

photo = PhotoImage(file= r"D:\DK\rob_py\picture\doldol.png")
label2 = Label(root, image=photo)
label2.pack()

btn1 = Button(root, text="추천메뉴",command=food)
btn1.pack()

root.mainloop()

