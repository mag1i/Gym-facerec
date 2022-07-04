from tkinter import Label, ttk

import cv2
import numpy
videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False

videoCaptureObject.release()
cv2.destroyAllWindows()

Payment = Label(frame1, text="Last activity", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(
    x=50, y=240)
self.cmd_quest = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
self.cmd_quest['values'] = (
"Select", "Aerobic", "weightlifting ", "musculation", "sona", "Aerobic sona", "musculation sona",
"Racewalking, jogging, or running.", "losing weight activity", "Bicycling")
self.cmd_quest.place(x=50, y=270, width=250)
self.cmd_quest.current(0)

self.Pay = Label(frame1, text="Duration", font=("Lato", 15, "bold"), bg="#0b0205", fg="white").place(x=370,
                                                                                                    y=240)
self.cmdquest = ttk.Combobox(frame1, font=("Lato", 13), state='readonly', justify=CENTER)
self.cmdquest['values'] = ("Select", "weekly", "monthly", "yearly")
self.cmdquest.place(x=370, y=270, width=250)
self.cmdquest.current(0)

