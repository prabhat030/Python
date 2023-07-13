import webbrowser as wb
from tkinter import * 

obj=Tk(className=" Python")

e=Entry(obj,font=("Segoe Print",24))
e.place(x=500,y=275)

def navigate():
    query=e.get()
    wb.open("https://www.youtube.com/results?search_query="+query)
    print("Searched text: ",query)
    print("Navigating to YouTube... ")

b=Button(obj,text="Search",
        command=navigate,
        font=("Comic Sans MS",18))
b.place(x=550,y=400)

b1=Button(obj,text="Close",
         command=obj.destroy,
         font=("Comic Sans MS",18))
b1.place(x=700,y=400)
obj.mainloop()