import tkinter as tk
import tkinter.font as font
from motion import noise
from noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion 
 
window = tk.Tk()
window.title("Smart cctv camera")
window.geometry('1080x700') 
 
frame1 = tk.Frame(window) 
 
label_title = tk.Label(frame1,text="Smart cctv ")
label_font = font.Font(size=40, weight='bold',family='times')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2) 
 
icon = Image.open('icons/cctv.jpg')
icon = icon.resize((150,150))  
  
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2) 
 
btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50))
btn1_image = ImageTk.PhotoImage(btn1_image) 
 
btn2_image = Image.open('icons/rectangle.png')
btn2_image = btn2_image.resize((50,50))
btn2_image = ImageTk.PhotoImage(btn2_image) 
 
btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50))
btn3_image = ImageTk.PhotoImage(btn3_image) 
 
btn4_image = Image.open('icons/record.png')
btn4_image = btn4_image.resize((50,50))
btn4_image = ImageTk.PhotoImage(btn4_image) 
 
btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50))
btn5_image = ImageTk.PhotoImage(btn5_image) 
 
 
# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Monitor button', height=100, width=300, fg='black',command = find_motion, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10)) 
 
btn2 = tk.Button(frame1, text='Rectangle button ', height=100, width=300, fg='black', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5)) 
 
btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Noise button ', height=100, width=300, fg='black', command=noise, image=btn3_image, compound='left') 
  
btn3['font'] = btn_font
btn3.grid(row=4, pady=(20,10)) 
 
btn4 = tk.Button(frame1, text='Record button ', height=100, width=300, fg='black', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=4, pady=(20,10), column=3) 
 
btn5 = tk.Button(frame1, text='exit button ',height=90, width=200, fg='red', command=window.quit, image=btn5_image,compound='left')
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=2) 
 
frame1.pack()
window.mainloop() 
