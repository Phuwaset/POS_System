from tkinter import *
from tkinter.ttk import Progressbar
#ttk.Progressbar: ใช้สำหรับสร้างโปรเกรสบาร์ที่แสดงการโหลด

import sys
sys.path.append('C:\\Users\\phuwa\\Downloads\\CoffeeShopManagentSystem-main\\CoffeeShopManagentSystem-main')
import CoffeeManagementSystem.AccountSystem
import os

root = Tk()
# root.resizable(0, 0)
image = PhotoImage(file='images\\coffeeShop-ico.png')

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)

#root.wm_attributes('-alpha', 0.9)
root.wm_attributes('-topmost', True)
root.config(background='#fd6a36') #กำหนดสีพื้นหลังของหน้าต่างเป็นสีส้ม (#fd6a36).

welcome_label = Label(text='WELCOME To The SHOP', bg='#fd6a36',  font=("yu gothic ui", 15, "bold"), fg='black')
welcome_label.place(x=80, y=25)

bg_label = Label(root, image=image, bg='#fd6a36')
bg_label.place(x=130, y=65)
# welcome_label: สร้างข้อความต้อนรับที่แสดงคำว่า "WELCOME To The SHOP" พร้อมตั้งค่าแบบอักษรและสีพื้นหลัง/ตัวอักษร.
# bg_label: แสดงรูปภาพที่กำหนดจากไฟล์ coffeeShop-ico.png.

progress_label = Label(root, text="Please Wait...", font=('yu gothic ui', 13, 'bold'), fg='black', bg='#fd6a36')
progress_label.place(x=190, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=390)

exit_btn = Button(text='x', bg='#fd6a36', command=lambda: exit_window(), bd=0, font=("yu gothic ui", 16, "bold"),
                  activebackground='#fd6a36', fg='white')
exit_btn.place(x=490, y=0)


def exit_window():
    sys.exit(root.destroy())


def top():
    root.withdraw()
    os.system("python AccountSystem.py")
    root.destroy()
    
# เมื่อโปรแกรมโหลดเสร็จแล้ว จะทำการเรียกโปรแกรม AccountSystem.py โดยใช้ os.system และซ่อนหน้าต่างปัจจุบันด้วย root.withdraw().

i = 0

def load():
    global i
    if i <= 10:
        txt = 'Please Wait...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()

#ฟังก์ชัน load() ใช้สำหรับทำให้โปรเกรสบาร์เพิ่มขึ้นทีละ 10% ทุก 1 วินาที เมื่อถึง 100% จะเรียกฟังก์ชัน top() เพื่อรันโปรแกรมถัดไป.

# ฟังก์ชันสำหรับ logout ด้วยการกดปุ่ม Q
def logout(event=None):
    exit_window()


# ผูกปุ่ม Q ให้เรียกฟังก์ชัน logout เมื่อกด
root.bind('<KeyPress-q>', logout)

# ลองแสดงผลหน้าต่างแบบปกติเพื่อตรวจสอบว่าเกิดจากการใช้ overrideredirect หรือไม่
root.overrideredirect(False)

load()

root.mainloop()