import tkinter as tk
from tkinter import messagebox
from pytube.exceptions import PytubeError

# creates the window using Tk() fucntion
window = tk.Tk()

# creates title for the window
window.title('YouTube Video Downloader - by Youssef')
window.iconbitmap('C:\\Users\\Dell\\Documents\\icons\\yt icon.ico')

# # dimensions and position of the window
window.geometry('550x140')
# makes the window resizable
window.resizable(height=True, width=True)

# invitation to input
invit = tk.Label(window, text = "input the URL here -->>>", pady=10)
invit.grid(row=0, column=0)

# entry field where input a link
link_field = tk.Entry(window,  width=60)
link_field.insert(0,'----youtube.com/----')
link_field.grid(row=0, column=1, columnspan = 2)

# create the empty widget, will be filed later with config
link_field2 = tk.Label(window, text="", pady=10)
link_field2.grid(row=2, columnspan=3)

# hide msg in the URL entry field 
def hide_text(event):
    link_field.delete(0,tk.END)
# associate event to function
link_field.bind("<1>",hide_text)


def dwld(chosenpath):
    try:
        from pytube import YouTube
        vid = YouTube(link_field.get())
        str = vid.streams.filter(resolution='480p').first()
        str.download(output_path=chosenpath)
        title = vid.title
        link_field.delete(0,tk.END)
        link_field.insert(0,'(download another----youtube.com/---- video)')
        link_field2.config(text=f'{title} \n has been downloaded to \n {chosenpath}')
    except PytubeError as e :
        messagebox.showerror("something went wrong, my friend ! \N{confused face}",
                              f"Either invalid URL or no internet connection. Check this error : {e}")    

def pick_path():
    link_field2.config(text="downloading now, wait a moment.....")
    from tkinter import filedialog
    drct =  filedialog.askdirectory()
    #print(drct)
    dwld(drct)

    
dwld_button = tk.Button(window, text='download it', command=pick_path, bg='red', fg="white")
dwld_button.grid(row=1,columnspan=3)

def closeit(event=None):
    window.destroy()
window.bind("<Control-w>",closeit)

# # runs the window infinitely
window.mainloop()
