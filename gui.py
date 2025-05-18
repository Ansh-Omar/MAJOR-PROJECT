from tkinter import *
def GUI():
    from PIL import Image , ImageTk
    import action 
    import spech_to_text 
    import pymysql as ms
    myobj = ms.connect(host = "localhost", user = "root", password="",database="Project1")
    mysqlc = myobj.cursor()

    def User_send():
        send = entry1.get()
        bot = action.Action(send)
        print(bot)
        text.insert(END, "Me --> "+send+"\n")
        if bot != None:
            text.insert(END, "Bot <-- "+ str(bot)+"\n")
        if bot == "ok sir":
              root1.destroy()
        try:
            ins="insert into data(ME,BOT) values(%s,%s)"
            # TO input single data at a time
            tu=(send,bot)
            mysqlc.execute(ins,tu)
            myobj.commit();
            print("Data inserted")
        except:
            print("Data error...")           

    def ask():   
        ask_val= spech_to_text.spech_to_text()
        bot_val = action.Action(ask_val)
        print(bot_val)
        text.insert(END, "Me --> "+ask_val+"\n")
        if bot_val != None:
           text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
        if bot_val == "ok sir":
            root1.destroy()
        try:
            ins="insert into data(ME,BOT) values(%s,%s)"
            # TO input single data at a time
            tu=(ask_val,bot_val)
            mysqlc.execute(ins,tu)
            myobj.commit();
            print("Data inserted")
        except:
            print("Data error...")        

    def delete_text():
        text.delete("1.0", "end")
        try:
            mysqlc.execute("TRUNCATE TABLE data")
            myobj.commit()
        except ms.MySQLError as err:
            print(f"Error: {err}")


    root1 = Tk()
    root1.geometry("550x675")
    root1.title("AI Assistant")
    root1.resizable(False,False)
    root1.config(bg="#6F8FAF")

    


    # Main Frame
    Main_frame = LabelFrame(root1 , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
    Main_frame.config(bg="#FFFFFF") # #6F8FAF
    Main_frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)

    # Text Lable 
    Text_lable = Label(Main_frame, text = "AI Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg="#FFFFFF", fg="#333333") # bg = "#356696"
    Text_lable.grid(row=0 ,  column=0 , padx=70 , pady= 10)


    # Image 
    '''try:
        image_path = r"D:/Python code/Desktop AI Assistant/assistant.png"
        img = Image.open(image_path)
        Display_Image = ImageTk.PhotoImage(img)
        Image_Lable = Label(Main_frame, image= Display_Image)
        Image_Lable.image = Display_Image
        Image_Lable.grid(row = 1 ,  column=0 , pady=20)
    except Exception as e:
        print("Image Load Karne Me Error:", e)'''


    # Add a text widget

    text=Text(root1 , font= ('Courier 10 bold') , bg = "#000000", fg="#FFFFFF") # bg = "#356696"
    text.grid(row = 1,  column= 0)
    text.place(x= 100, y= 150, width= 375, height= 300) 

    def on_entry_click(event):
        # Clear the placeholder text when the entry is clicked
        if entry1.get() == "Ask anything...":
            entry1.delete(0,END)
            entry1.config(fg='black')

    # Add a entry widget
    entry1 = Entry(root1, justify = CENTER, bg="#FFFFFF", fg="#333333")
    entry1.insert(0,"Ask anything...")
    entry1.bind("<FocusIn>", on_entry_click)
    entry1.place(x=100 , y = 500 , width= 350, height= 30)

    # Add a text button1
    button1 =  Button(root1,  text="ASK" , bg="#4CAF50", fg="#FFFFFF" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
    button1.place(x= 70, y= 575) # bg="#356696"

    # Add a text button2
    button2 =  Button(root1,  text="Send" , bg="#2196F3", fg="#FFFFFF" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
    button2.place(x= 400, y= 575) # bg="#356696"

    # Add a text button3
    button3 = Button(root1, text="Delete", bg="#F44336", fg="#FFFFFF" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
    button3.place(x= 225, y= 575) # bg="#356696"
    root1.mainloop()

# GUI()