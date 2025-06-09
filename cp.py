import cv2
from tkinter import *
from tkinter import filedialog, Label
import threading

clicked_color = ""

def select_img():
    global img_path, img
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg, *.png, *.jpeg")])
    if img_path:
        img = cv2.imread(img_path)
        threading.Thread(target=show_image).start()

def show_image():
    global img
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", click_event)
    while True:
        img_copy = img.copy()
        if clicked_color:
            cv2.rectangle(img_copy, (0,0), (250,40), (0,0,0), -1)
            cv2.putText(img_copy, clicked_color,(10,30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255),2)
        cv2.imshow("Image",img_copy)
        if cv2.waitKey(1) and 0xFF == 27:
             cv2.destroyWindow("Image")
             break

def click_event(event, x, y, flags, param):
    global clicked_color
    if event == cv2.EVENT_LBUTTONDOWN:
        b,g,r = img[y,x]
        clicked_color = f"RGB: ({r},{g},{b})"
        label_var.set(clicked_color)

root = Tk()
root.title("Color Picker App")
root.geometry("300x150")

label_var = StringVar()
label = Label(root, textvariable=label_var, font=("Helvetica",16))
label.pack(pady=10)

bt = Button(root, text="Select Image", command=select_img, font = ("Helvetica",14))
bt.pack()

info_label = Label(root, text="Click on the image to get RGB(press ESC to stop)", font=("Helvetica",10))
info_label.pack(pady=5)

root.mainloop()
        
