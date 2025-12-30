from tkinter import *
from tkinter import messagebox
import pyperclip
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():
    pass_gen_textbox.delete(0,END)

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password="".join(password_list)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #     password += char
    pass_gen_textbox.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_name=web_textbox.get()
    email_name=email_textbox.get()
    password_name=pass_gen_textbox.get()
    if len(web_name)==0 or len(password_name)==0:
        print(messagebox.showinfo(title="Oops!",message="please dont leave any fields empty"))
    else:
        is_ok=messagebox.askokcancel(title=web_name,message=f"These are the fields entered\n"
                                                              f"Email:{email_name}\n password:{password_name}\n")
        if is_ok:
            with open(file="data.txt",mode="a") as f:
                f.write(f"{web_name} | {email_name} | {password_name}\n")
                #f.write("\n"+web_name+"|"+email_name+"|"+password_name)
        web_textbox.delete(0, END)
        pass_gen_textbox.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#image into the loop
canvas=Canvas(width=200,height=200,highlightthickness=0)
lock_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

#website,email,password labels
website_label=Label(text="Website :")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username :")
email_label.grid(column=0,row=2)

pass_gen_label=Label(text="Password Generator :")
pass_gen_label.grid(column=0,row=3)

#generator button,add button

pass_gen_button=Button(text="Generate Password",command=gen_pass)
pass_gen_button.grid(column=2,row=3)

add_button=Button(width=42,text="ADD",command=save)
add_button.grid(column=1,row=4,columnspan=2)


#textbox for web,email,pass_gen
web_textbox=Entry(width=50)
web_textbox.grid(column=1,row=1,columnspan=2)
web_textbox.focus()

email_textbox=Entry(width=50)
email_textbox.grid(column=1,row=2,columnspan=2)
email_textbox.insert(0,"mamidalasivabalaji@gmail.com")

pass_gen_textbox=Entry(width=30)
pass_gen_textbox.grid(column=1,row=3)









window.mainloop()

