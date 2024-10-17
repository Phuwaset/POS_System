import tkinter as tk
from tkinter import ttk, messagebox
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageTk

# ฟังก์ชันสำหรับสร้างบาร์โค้ด
def generate_barcode():
    data = entry_data.get()  # รับข้อมูลจากกล่อง input
    barcode_type = combo_type.get()  # รับประเภทบาร์โค้ดจากตัวเลือก
    if not data:
        messagebox.showerror("Error", "กรุณาใส่ข้อมูลบาร์โค้ด")
        return
    if not barcode_type:
        messagebox.showerror("Error", "กรุณาเลือกประเภทบาร์โค้ด")
        return

    try:
        # สร้างบาร์โค้ดตามประเภทที่เลือก
        barcode_class = barcode.get_barcode_class(barcode_type)
        bar = barcode_class(data, writer=ImageWriter())  # สร้างบาร์โค้ดด้วย ImageWriter
        filename = f"{data}_{barcode_type}"
        bar.save(filename)  # บันทึกเป็นไฟล์ภาพ PNG
        
        # แสดงบาร์โค้ดที่สร้างขึ้น
        img = Image.open(f"{filename}.png")
        img = img.resize((250, 100))  # ปรับขนาดภาพ
        img = ImageTk.PhotoImage(img)
        lbl_image.config(image=img)
        lbl_image.image = img

        messagebox.showinfo("Success", f"บาร์โค้ดถูกบันทึกเป็นไฟล์: {filename}.png")

    except Exception as e:
        messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {e}")

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Barcode Generator")
root.geometry("400x400")

# กล่องใส่ข้อมูล
label_data = tk.Label(root, text="ข้อมูลบาร์โค้ด:")
label_data.pack(pady=10)
entry_data = tk.Entry(root, width=30)
entry_data.pack()

# กล่องเลือกประเภทบาร์โค้ด
label_type = tk.Label(root, text="ประเภทบาร์โค้ด:")
label_type.pack(pady=10)
barcode_types = ['ean13', 'ean8', 'upc', 'code39', 'code128']  # ประเภทบาร์โค้ดที่รองรับ
combo_type = ttk.Combobox(root, values=barcode_types)
combo_type.pack()

# ปุ่มสร้างบาร์โค้ด
btn_generate = tk.Button(root, text="สร้างบาร์โค้ด", command=generate_barcode)
btn_generate.pack(pady=20)

# ป้ายสำหรับแสดงภาพบาร์โค้ด
lbl_image = tk.Label(root)
lbl_image.pack(pady=10)

root.mainloop()
