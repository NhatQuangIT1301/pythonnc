import tkinter as tk
from tkinter import ttk, Menu, scrolledtext, messagebox

class TinhLuong:
    def __init__(self, root):
        self.root = root
        self.root.title("Tinh luong")
        self.root.resizable(False,False)

        # Kích thước cửa sổ
        window_width = 350
        window_height = 600

        # Lấy kích thước màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Tính toán tọa độ x và y để đặt cửa sổ ở trung tâm
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        # Đặt kích thước và vị trí cửa sổ
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        #menu bar
        menu_bar = Menu(win)
        win.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=exit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.ThongTinSanPham)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        tabControl = ttk.Notebook(self.root)
        tabControl.pack(expand=1, fill="both")

        self.NhanVien(tabControl)
        self.QuanLy(tabControl)

    def NhanVien(self, tabControl):
        #tab Nhan Vien
        tabNhanVien = ttk.Frame(tabControl)
        tabControl.add(tabNhanVien, text="Nhan Vien")

        #frame Nhan Vien
        frame_NhanVien = ttk.LabelFrame(tabNhanVien, text="Tinh Luong Nhan Vien")
        frame_NhanVien.grid(column=0, row=0, padx=25, pady=15)
        
        #label Tinh
        lbl_lcb = ttk.Label(frame_NhanVien, text="Luong Co Ban: ")
        lbl_lcb.grid(column=0, row=0, padx=10, pady=10, sticky="W")

        lbl_snlv = ttk.Label(frame_NhanVien, text="So Gio Lam Viec: ")
        lbl_snlv.grid(column=0, row=1, padx=10, pady=10, sticky="W")

        lbl_trocap = ttk.Label(frame_NhanVien, text="Tro Cap: ")
        lbl_trocap.grid(column=0, row=2, padx=10, pady=10, sticky="W")
        
        #textbox
        self.lcb = tk.DoubleVar()
        txt_lcb = ttk.Entry(frame_NhanVien, width=25, textvariable=self.lcb)
        txt_lcb.grid(column=1, row=0, padx=10, pady=10)
        txt_lcb.focus()

        self.sglv = tk.DoubleVar()
        txt_sglv = ttk.Entry(frame_NhanVien, width=25, textvariable=self.sglv)
        txt_sglv.grid(column=1, row=1, padx=10, pady=10)

        self.trocap = tk.DoubleVar()
        txt_trocap = ttk.Entry(frame_NhanVien, width=25, textvariable=self.trocap)
        txt_trocap.grid(column=1, row=2, padx=10, pady=10)

        #btn Tinh
        btn_Tinh = ttk.Button(frame_NhanVien, text="Enter", command=self.LuongNhanVien)
        btn_Tinh.grid(column=1, row=3, pady=10)

        #frame Tinh Luong Nhan Vien
        frame_LuongNhanVien = ttk.LabelFrame(tabNhanVien, text="Ket Qua")
        frame_LuongNhanVien.grid(column=0, row=1, padx=20, pady=5)

        #label luong
        lbl_luong = ttk.Label(frame_LuongNhanVien, text="Luong:")
        lbl_luong.grid(column=0, row=0, padx=10, pady=2, sticky="W")

        #btn Clear
        btn_Clear = ttk.Button(frame_LuongNhanVien, text="Clear", command=self.Clear_LuongNhanVien)
        btn_Clear.grid(column=1, row=0, sticky="E", padx=12)

        #scrolledtext
        scr_w = 31
        scr_h = 15
        self.scroll_NhanVien = scrolledtext.ScrolledText(frame_LuongNhanVien, width = scr_w, height = scr_h, wrap = tk.WORD)
        self.scroll_NhanVien.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

    def QuanLy(self, tabControl):
        #tab Quan Ly
        tabQuanLy = ttk.Frame(tabControl)
        tabControl.add(tabQuanLy, text="Quan Ly")
        
        #frame Nhan Vien
        frame_QuanLy = ttk.LabelFrame(tabQuanLy, text="Tinh Luong Quan Ly")
        frame_QuanLy.grid(column=0, row=0, padx=30, pady=15)
        
        #label Tinh
        lbl_lcb = ttk.Label(frame_QuanLy, text="Luong Co Ban")
        lbl_lcb.grid(column=0, row=0, padx=10, pady=10, sticky="W")

        lbl_snlv = ttk.Label(frame_QuanLy, text="He So Chuc Vu")
        lbl_snlv.grid(column=0, row=1, padx=10, pady=10, sticky="W")

        lbl_trocap = ttk.Label(frame_QuanLy, text="Thuong")
        lbl_trocap.grid(column=0, row=2, padx=10, pady=10, sticky="W")
        
        #textbox
        self.lcb_quanly = tk.DoubleVar()
        txt_lcb = ttk.Entry(frame_QuanLy, width=25, textvariable=self.lcb_quanly)
        txt_lcb.grid(column=1, row=0, padx=10, pady=10)
        txt_lcb.focus()

        self.hscv = tk.DoubleVar()
        txt_hscv = ttk.Entry(frame_QuanLy, width=25, textvariable=self.hscv)
        txt_hscv.grid(column=1, row=1, padx=10, pady=10)

        self.thuong = tk.DoubleVar()
        txt_thuong = ttk.Entry(frame_QuanLy, width=25, textvariable=self.thuong)
        txt_thuong.grid(column=1, row=2, padx=10, pady=10)

        #btn Tinh
        btn_Tinh = ttk.Button(frame_QuanLy, text="Enter", command=self.LuongQuanLy)
        btn_Tinh.grid(column=1, row=3, pady=10)

        #frame Tinh Luong Nhan Vien
        frame_LuongQuanLy = ttk.LabelFrame(tabQuanLy, text="Ket Qua")
        frame_LuongQuanLy.grid(column=0, row=1, padx=30, pady=5)

        #label luong
        lbl_luong = ttk.Label(frame_LuongQuanLy, text="Luong:")
        lbl_luong.grid(column=0, row=0, padx=10, pady=2, sticky="W")

        #btn Clear
        btn_Clear = ttk.Button(frame_LuongQuanLy, text="Clear", command=self.Clear_LuongQuanLy)
        btn_Clear.grid(column=1, row=0, sticky="E", padx=12)

        #scrolledtext
        scr_w = 30
        scr_h = 15
        self.scroll_QuanLy = scrolledtext.ScrolledText(frame_LuongQuanLy, width = scr_w, height = scr_h, wrap = tk.WORD)
        self.scroll_QuanLy.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

    def LuongNhanVien(self):
        try:
            lcb = self.lcb.get()
            sglv = self.sglv.get()
            trocap = self.trocap.get()
            self.scroll_NhanVien.insert(tk.INSERT, str(int(lcb + sglv * 200000 + trocap)) + "\n")
        except Exception as ex:
            messagebox.showerror("Input Error", "Lỗi dữ liệu đầu vào!\nVui lòng xem và nhập lại")
        
    def LuongQuanLy(self):
        try:
            lcb = self.lcb_quanly.get()
            hscv = self.hscv.get()
            thuong = self.thuong.get()
            self.scroll_QuanLy.insert(tk.INSERT, str(int(lcb * hscv + thuong)) + "\n")
        except Exception as ex:
            messagebox.showerror("Input Error", "Lỗi dữ liệu đầu vào!\nVui lòng xem và nhập lại")

    def ThongTinSanPham(self):
        messagebox.showinfo("Thong Tin San Pham", "Cach tinh luong:\n  Nhan vien: \n     luong = luong co ban + so gio lam viec * 200.000 + tro cap\n  Quan ly: \n     luong = luong co ban * he so chuc vu + thuong")

    def Clear_LuongNhanVien(self):
        self.scroll_NhanVien.delete(1.0, tk.END)

    def Clear_LuongQuanLy(self):
        self.scroll_QuanLy.delete(1.0, tk.END)

if __name__ == "__main__":
    win = tk.Tk()
    TinhLuong(win)
    win.mainloop()