import tkinter
import pytube

root = tkinter.Tk()
root.geometry("700x700")

frame = tkinter.Frame(root).pack()

root.title("YT Download Video Tool")

mainLabel = tkinter.Label(frame, text = "Paste your yt video link").pack()

link = tkinter.StringVar()
linkVideoEntry = tkinter.Entry(frame, width=40, textvariable=link).pack()

def download():
    url = pytube.YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text = 'done')

downloadButton = tkinter.Button(frame, text= "Download", command=download).pack()

root.mainloop()
