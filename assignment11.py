from tkinter import *
import webbrowser as wb

def form():
    name = entry_name.get()
    contact = entry_contact.get()
    
    source = var_source.get()
    if var_source.get() == 1:
        source = "Youtube Ads"
    elif var_source.get() == 2:
        source = "Instagram Ads"
    elif var_source.get() == 3:
        source = "Facebook Ads"
    elif var_source.get() == 4:
        source = "Google Ads"

    if source == "Youtube Ads":
        wb.open("https://support.google.com/youtube/thread/677314/%F0%9F%94%8D-youtube-faqs-need-help-start-here?hl=en")
    elif source == "Instagram Ads":
        wb.open("https://about.instagram.com/blog/announcements/instagram-community-guidelines-faqs/")
    elif source == "Facebook Ads":
        wb.open("https://www.facebook.com/faqpage/")
    elif source == "Google Ads":
        wb.open("https://one.google.com/faq")


    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}, Contact: {contact}, Source: {source}\n")


window =Tk()
window.title("Enquiry Form")

main_label = Label(window,text='Enquiry Page',font='Fixedsys')
main_label.pack()

label_name =Label(window, text="Name:")
label_name.pack()
entry_name =Entry(window)
entry_name.pack()

label_contact = Label(window, text="Contact:")
label_contact.pack()
entry_contact = Entry(window)
entry_contact.pack()

label_source = Label(window, text="Where did you heard about our App/Website?",font=('Arial',10))
label_source.pack()

var_source = IntVar()

radiobutton_1 = Radiobutton(window, text="Youtube Ads", variable=var_source, value=1)
radiobutton_1.pack()

radiobutton_2 = Radiobutton(window, text="Instagram Ads", variable=var_source, value=2)
radiobutton_2.pack()

radiobutton_3 = Radiobutton(window, text="Facebook Ads", variable=var_source, value=3)
radiobutton_3.pack()

radiobutton_4 = Radiobutton(window, text="Google Ads", variable=var_source, value=4)
radiobutton_4.pack()

button_submit = Button(window, text="Submit", command=form)
button_submit.pack()

window.mainloop()