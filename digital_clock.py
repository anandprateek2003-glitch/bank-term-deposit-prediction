import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    clock.config(text=current_time)
    clock.after(1000, update_time)

root = tk.Tk()
root.title('Digital Clock')

clock = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
clock.pack(anchor='center')

update_time()
root.mainloop()