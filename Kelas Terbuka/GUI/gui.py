import tkinter

# membuat windows tampilannya
main_windows = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_windows, text = "Aku Ditekan ^_^")
    label2.pack()

label = tkinter.Label(main_windows, text="halo, saya adalah \nGUI sederhana dengan \nmenggunakan python")
tombol = tkinter.Button(main_windows, text="tekan aku", command = event_tekan)

label.pack()
tombol.pack()
# agar windows loop terus, dan hanya berhenti jika diclose
main_windows.mainloop()