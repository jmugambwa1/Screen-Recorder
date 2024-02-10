from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("400x600")  # Window size
root.resizable(False, False)
root.config(bg="black")
root.title("Screen Recorder")

recording_status = StringVar()
recording_status.set("Not Recording")

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file) + ".mp4", 5)
    recording_status.set("Recording...")

def resume_rec():
    rec.resume_recording()
    recording_status.set("Recording...")

def pause_rec():
    rec.pause_recording()
    recording_status.set("Recording Paused")

def stop_rec():
    rec.stop_recording()
    recording_status.set("Recording Stopped")

rec = pyscreenrec.ScreenRecorder()

# Icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# Heading
lb1 = Label(root, text="Screen Recorder", bg="#fff", font="arial 15 bold")
lb1.pack(pady=10)

image1 = PhotoImage(file="screen.png")
Label(root, image=image1).pack(pady=30)

# Entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, font="arial 15")
entry.place(x=50, y=550)
Filename.set("File Name")

# Buttons
start = Button(root, text="Start", font="arial 20", bd=0, relief="groove", command=start_rec)
start.place(x=140, y=210)

image2 = PhotoImage(file="play.png")
play = Button(root, image=image2, bg="#fff", command=resume_rec)
play.place(x=70, y=450)

image3 = PhotoImage(file="pause.png")
pause = Button(root, image=image3, bg="#fff", command=pause_rec)
pause.place(x=170, y=450)

image4 = PhotoImage(file="stop.png")
stop = Button(root, image=image4, bg="#fff", command=stop_rec)
stop.place(x=270, y=450)

# Recording status label
status_label = Label(root, textvariable=recording_status, bg="black", fg="white", font="arial 7")
status_label.pack(pady=5)

root.mainloop()
