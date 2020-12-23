from tkinter import *
# window=Tk()
#
# photo=PhotoImage(file="cat.gif")
# label1=Label(window,image=photo)
# label1.grid()
#
#
# label1.pack()
# window.mainloop()

from tkinter import *
tk = Tk()
tk.title("cat")
canvas = Canvas(tk, width = 800, height=800)
canvas.pack()
canvas.grid(row=2, column=3)

image = PhotoImage(file = 'cat_for_jy.gif')
canvas.create_image(20,20, anchor =NW, image= image)
tk.mainloop()



# class MyFrame(Frame):
#     def __init__(self, master):
#         img = PhotoImage(file='cat.gif')
#         lbl = Label(image=img)
#         lbl.pack()
#         lbl.grid()
#         lbl.image = img  # 레퍼런스 추가
#         lbl.place(x=0, y=0)
#
#
# def main():
#     root = Tk()
#     root.title('이미지 보기')
#     root.geometry('600x400+10+10')
#     myframe = MyFrame(root)
#     root.mainloop()
#
# main()


# from tkinter import *
# from PIL import ImageTk, Image
# root = Tk()
#
# canv = Canvas(root, width=700, height=500 )
# canv.grid(row=2, column=3)
#
# img = ImageTk.PhotoImage(Image.open("real_cat.jpg"))  # PIL solution
# canv.create_image(20, 20, anchor=NW, image=img)
#
# mainloop()

import  tkinter
print(tkinter.TkVersion)