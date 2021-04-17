import tkinter
import cv2  
import PIL.Image, PIL.ImageTk

# pip install opencv-python
# time => 22:34
# pip install pillow

def play():
    pass


# Width and height of our main screen
SET_WIDTH = 650
SET_HIGHT = 368

# Tkinter GUI starts here
window = tkinter.Tk()
window.title("CodeWithHarry Third Umpire Decision Review Kit")

cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromArray(cv_img))
image_on_canvas = canvas.create_image(0,0, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width=50)
btn.pack()
btn = tkinter.Button(window, text="<< Previous (Slow)", width=50)
btn.pack()
btn = tkinter.Button(window, text="Next (Slow) >>", width=50)
btn.pack()
btn = tkinter.Button(window, text="Next (fast) >>", width=50, command=play)
btn.pack()
btn = tkinter.Button(window, text="Give Out!", width=50)
btn.pack()
btn = tkinter.Button(window, text="Give Not Out!", width=50)
btn.pack()

window.mainloop()