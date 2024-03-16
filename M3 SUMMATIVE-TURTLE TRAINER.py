import turtle
import	tkinter	as	tk
from	tkinter	import	ttk
from	tkinter.messagebox	import	showinfo

intro	=	tk.Tk()
intro.geometry("400x400")
intro.title('Turtle trainer')
# Create intro tab

note = ttk.Notebook(intro)
note.pack(padx=10, pady=10, anchor= tk.W)
frame1	=	ttk.Frame(note)
frame2	=	ttk.Frame(note)
frame3	=	ttk.Frame(note)
frame4	=	ttk.Frame(note)
note.add(frame1, text ="Introduction")
note.add(frame2, text ="Shapes")
note.add(frame3, text ="Pen and Colors")
note.add(frame4, text ="Text")
#create notebook
def wrong_answer():
    msg = f"Sorry but that's wrong, try again."
    showinfo(title='Information', message=msg)
#Message for wrong answer

#shape training------------------------------------------------------------------------------------
def turtle_shapes():
    btnqS1o1.config(state="enabled")
    btnqS1o2.config(state="enabled")
    btnqS1o3.config(state="enabled")
    btnqS1o4.config(state="enabled")
    screen = turtle.Screen()
    turtle.title("Shapes training")
    t = turtle.Turtle()
    turtle.mainloop()
#create turtle window
def right_S1():
    btnqS2o1.config(state = "enabled")
    turtle.shape("turtle")
    msg = """Correct!
    
The method turtle.shape( ) changes the turtle head
depending on the input in the parenthesis.
    """
    showinfo(title='Information', message=msg)
#correct answer for specific questions
def right_S2():
    btnqS3o1.config(state="enabled")
    btnqS3o2.config(state="enabled")
    btnqS3o3.config(state="enabled")
    btnqS3o4.config(state="enabled")
    ans= txtS2.get()
    if ans == "turtle.rt(90)":
        for i in range(4):
            turtle.fd(200)
            turtle.rt(90)
        msg = """Correct!
    
    The method turtle.rt( ) makes the turtle turn
    right from where it is currently facing, by the
    given value as the angle. 90 would make it turn 
    completely right which if done 4 times makes a square.
        """
        showinfo(title='Information', message=msg)
    else:
        msg = f"Sorry but that's wrong, try again."
        showinfo(title='Information', message=msg)
def right_S3():
    btnqS4o1.config(state="enabled")
    btnqS4o2.config(state="enabled")
    btnqS4o3.config(state="enabled")
    btnqS4o4.config(state="enabled")
    turtle.penup()
    turtle.goto(150,-150)
    style = ('Courier', 30, 'italic')
    turtle.write("Quadrant 4",font=style,align="center")
    msg = """Correct!

Following the cartesian plane the area where 
the square is created is in quadrant 4, where
x is positive and y is negative.
        """
    showinfo(title='Information', message=msg)
def right_S4():
    btnqS5o1.config(state="enabled")
    btnqS5o2.config(state="enabled")
    turtle.home()
    turtle.clear()
    turtle.pendown()
    turtle.dot(90)
    msg = """Correct!

The method turtle.dot(size,color) is one
that creates a perfect circle for you that is 
filled-in with the color of your choice.
        """
    showinfo(title='Information', message=msg)

def right_S5():
    name = txtName.get()
    file = open("Log.txt", "a")
    file.write(f"{name.upper()} Shapes progress             : Complete\n")
    file.close()
    turtle.clear()
    msg = """Correct!

The method turtle.dot(size,color) is one
that creates a perfect circle for you that is 
filled-in with the color of your choice.
        """
    showinfo(title='Information', message=msg)
    msgF = """
    You have completed the shapes portion of the
    trainer. You may now close the turtle window
    and switch to a different tab of your choosing.
            """
    showinfo(title='Information', message=msgF)



#shape training------------------------------------------------------------------------------------

#color training------------------------------------------------------------------------------------
def turtle_colors():
    btnqC1o1.config(state="enabled")
    screen = turtle.Screen()
    turtle.title("Pen and Colors training")
    t = turtle.Turtle()
    turtle.mainloop()
def right_C1():
    btnqC2o1.config(state="enabled")
    btnqC2o2.config(state="enabled")
    btnqC2o3.config(state="enabled")
    btnqC2o4.config(state="enabled")
    selected_items = Cq1options.curselection()  # Get	the	indices	of	selected	items
    selected_text = [Cq1options.get(i) for i in selected_items]  # Get	the	selected	item(s)
    x =f"{''.join(selected_text)}"
    if x == "BackgroundTurtle":
        msg = """Correct!

        In turtle graphics you can change the colors 
        of the background and turtle. However, you can
        recolor much more than that!
                """
        showinfo(title='Information', message=msg)
    else:
        msg = f"Sorry but that's wrong, try again."
        showinfo(title='Information', message=msg)

def right_C2():
    btnqC3o1.config(state="enabled")
    turtle.shapesize(3,3,3)
    turtle.fillcolor("red")
    msg = """Correct!

The method turtle.fillcolor( ) will change the inner
color of a turtle. You can either input the name of
the color or the hex code equivalent of the color.
            """
    showinfo(title='Information', message=msg)
def right_C3():
    btnqC4o1.config(state="enabled")
    btnqC4o2.config(state="enabled")
    x = txtC31.get()
    y = txtC32.get()
    if x == "turtle.begin_fill()" and y == "turtle.end_fill()":
        turtle.begin_fill()
        turtle.fd(100)
        turtle.lt(120)
        turtle.fd(100)
        turtle.lt(120)
        turtle.fd(100)
        turtle.end_fill()
        msg = """Correct!

        The method turtle.begin_fill() tells the program
        that you are making a closed shape that will be filled
        in, and turtle.end_fill() indicates that you are done
        with the shape.
                    """
        showinfo(title='Information', message=msg)
    else:
        msg = f"Sorry but that's wrong, try again."
        showinfo(title='Information', message=msg)
def right_C4():
    btnqC5o1.config(state="enabled")
    msg = """Correct!

The color of the outside of a filled shape is determined
by your pen's color, which is configured using the method
turtle.pencolor or by changing the color of both pen and fill
using turtle.color.
                """
    showinfo(title='Information', message=msg)
def right_C5():
    name = txtName.get()

    ans = txtC5.get()
    if ans == "turtle.stamp()":
        file = open("Log.txt", "a")
        file.write(f"{name.upper()} Pen and color progress             : Complete\n")
        file.close()
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.stamp()
        turtle.fd(100)
        turtle.stamp()
        turtle.fd(100)
        msg = """Correct!

        The method turtle.stamp() leaves behind an imprint
        on the window, where your turtle was when it was
        called.
               """
        showinfo(title='Information', message=msg)
        msgF = """
            You have completed the pen and colors portion 
            of the trainer. You may now close the turtle window
            and switch to a different tab of your choosing.
                    """
        showinfo(title='Information', message=msgF)
    else:
        msg = f"Sorry but that's wrong, try again."
        showinfo(title='Information', message=msg)

#color training------------------------------------------------------------------------------------
#text training------------------------------------------------------------------------------------
def turtle_text():
    btnqT1o1.config(state="enabled")
    btnqT1o2.config(state="enabled")
    btnqT1o3.config(state="enabled")
    btnqT1o4.config(state="enabled")
    screen = turtle.Screen()
    turtle.title("Text training")
    t = turtle.Turtle()
    turtle.mainloop()
def right_T1():
    btnqT2o1.config(state="enabled")
    turtle.write("Hello, this is writing", align = "center",font=("Arial",16,"normal"))
    msg = """Correct!

The method turtle.write() will display a given message,
with the content being the first parameter and other
configuration options available in the parameters.
          """
    showinfo(title='Information', message=msg)
def right_T2():
    btnqT3o1.config(state="enabled")
    ans = txtT2.get()
    if ans == "t.write(message,font=(family,size,style)" or ans == "t.write(message,font=(family, size, style)":
        msg = """Correct!

        When assigning a font, it will take a font family, size
        and style. Which is then used for that particular message.
                       """
        showinfo(title='Information', message=msg)
    else:
        msg = f"Sorry but that's wrong, try again."
        showinfo(title='Information', message=msg)
def right_T3():
    btnqT4o1.config(state="enabled")
    btnqT4o2.config(state="enabled")
    selected_items = Tq3options.curselection()  # Get	the	indices	of	selected	items
    selected_text = [Tq3options.get(i) for i in selected_items]  # Get	the	selected	item(s)
    x =f"{''.join(selected_text)}"
    if x == "BoldItalic":
        turtle.clear()
        turtle.penup()
        turtle.goto(200,200)
        turtle.write("Hello", align="center", font=("Arial", 20, "bold"))
        turtle.goto(200, 90)
        turtle.write("This is styles", align="center", font=("Arial", 20, "italic"))
        msg = """Correct!

        Examples of font or formatting styles are bold
        and italicization. Which are used to highlight text.
                """
        showinfo(title='Information', message=msg)
    else:
        msg = f"Sorry but that's wrong, try again."
        showinfo(title='Information', message=msg)
def right_T4():
    btnqT5o1.config(state="enabled")
    btnqT5o2.config(state="enabled")
    btnqT5o3.config(state="enabled")
    btnqT5o4.config(state="enabled")
    msg = """Correct!

    A simple program can be created that displays text
    on-click. However, it is not done by just a method.
    It can be done by created a function that uses the
    turtle.write() method as one of it's parts.  
            """
    showinfo(title='Information', message=msg)
def right_T5():
    name = txtName.get()
    file = open("Log.txt", "a")
    file.write(f"{name.upper()} Text progress             : Complete")
    file.close()
    turtle.clear()
    turtle.write(
"""
    Hello, this is Arial.
A font family for your text.
    """, align="center", font=("Arial", 20, "bold"))
    msg = """Correct!

       As shown before, the first argument of a font is
       the font family. From the Choices, Arial is the
       only one that is a font family.  
                """
    showinfo(title='Information', message=msg)
    msgF = """
                You have completed the text portion of the trainer. 
                You may now close the turtle window and switch to a
                different tab of your choosing.
                        """
    showinfo(title='Information', message=msgF)


logs = {}
def cred():
    btnqS1o1.config(state="enabled")
    btnqS1o2.config(state="enabled")
    btnqS1o3.config(state="enabled")
    btnqS1o4.config(state="enabled")
    btnqC1o1.config(state="enabled")
    btnqT1o1.config(state="enabled")
    btnqT1o2.config(state="enabled")
    btnqT1o3.config(state="enabled")
    btnqT1o4.config(state="enabled")
    global logs
    name = txtName.get()
    if name == "":
        msg = "Please input a name"
        showinfo(title='Information', message=msg)
    else:
        age = txtAge.get()
        course = boxCourse.get()
        Yl = txtYL.get()
        x = [f"====TURTLE TRAINER LOG | {name.upper()}====",
    f"{name.upper()} Age                      : {age}",
    f"{name.upper()} Course                : {course}",
    f"{name.upper()} Year level             : {Yl}"]
        logs = {name.title():x}
        file = open("Log.txt", "a")
        for i in x:
            file.write(i+"\n")
        file.close()
        txtName.configure(state="disabled")
        txtAge.configure(state= "disabled")
        boxCourse.configure(state="disabled")
        txtYL.configure(state="disabled")
        btnSub.config(state="disabled")
def stop():
    btnqS1o1.config(state="disabled")
    btnqS1o2.config(state="disabled")
    btnqS1o3.config(state="disabled")
    btnqS1o4.config(state="disabled")
    btnqS2o1.config(state="disabled")
    btnqS3o1.config(state="disabled")
    btnqS3o2.config(state="disabled")
    btnqS3o3.config(state="disabled")
    btnqS3o4.config(state="disabled")
    btnqS4o1.config(state="disabled")
    btnqS4o2.config(state="disabled")
    btnqS4o3.config(state="disabled")
    btnqS4o4.config(state="disabled")
    btnqS5o1.config(state="disabled")
    btnqS5o2.config(state="disabled")

    btnqC1o1.config(state="disabled")
    btnqC2o1.config(state="disabled")
    btnqC2o2.config(state="disabled")
    btnqC2o3.config(state="disabled")
    btnqC2o4.config(state="disabled")
    btnqC3o1.config(state="disabled")
    btnqC4o1.config(state="disabled")
    btnqC4o2.config(state="disabled")
    btnqC5o1.config(state="disabled")


    btnqT1o1.config(state="disabled")
    btnqT1o2.config(state="disabled")
    btnqT1o3.config(state="disabled")
    btnqT1o4.config(state="disabled")
    txtName.configure(state="enabled")
    txtAge.configure(state="enabled")
    boxCourse.configure(state="enabled")
    txtYL.configure(state="enabled")
    btnSub.config(state="enabled")
def log():
    x= list()
    name = txtLog.get()
    file = open("Log.txt", "r")
    log = file.readlines()
    file.close()
    for i in log:
        if name.upper() in i:
            x.append(i)
    y = "\n".join(x)
    msg = y
    showinfo(title='Information', message=msg)
def delete():
    global logs
    delete = txtDel.get()
    nameDel = delete.upper()
    file = open("Log.txt", "r")
    log = file.readlines()
    file.close()
    file = open("Log.txt", "w")
    for line in log:
        if nameDel not in line:
            file.write(line)
    file.close()



#text training------------------------------------------------------------------------------------

lblIntro = ttk.Label(frame1,	text="""
Hello and welcome to the Turtle trainer!

Here you will learn more about turtle graphics. As you can see above, 
there are tabs on different topics about turtle graphics. You may start
by filling in the boxes with your information, most importantly your name.
Afterwards, press START LOG to do an attempt at the quizzes. End your 
attempt by choosing the STOP LOG option. Press OPEN to see previous attempts
and DELETE to remove logs of certain attempts. Once you have started the log
you can answer by opening any of the tabs above named with the topics.
""")
lblIntro.pack(padx=10, pady=10, anchor= tk.W)

fName = ttk.Frame(frame1)
fName.pack(padx=10, pady=5, anchor= tk.W,)
lblName	= ttk.Label(fName, text="Enter name        : ")
lblName.pack(side=tk.LEFT)
txtName	= ttk.Entry(fName)
txtName.pack(side=tk.LEFT)
txtName.focus()
fAge = ttk.Frame(frame1)
fAge.pack(padx=10, pady=5, anchor= tk.W)
lblAge	= ttk.Label(fAge, text="Enter age           : ")
lblAge.pack(side=tk.LEFT)
txtAge	= ttk.Entry(fAge)
txtAge.pack(side=tk.LEFT)
txtAge.focus()
fCourse = ttk.Frame(frame1)
fCourse.pack(padx=10, pady=5, anchor= tk.W)
lblCourse	= ttk.Label(fCourse, text="Enter course      : ")
lblCourse.pack(side=tk.LEFT)
n = tk.StringVar()
boxCourse = ttk.Combobox(fCourse,width= 17,textvariable= n )
boxCourse['values'] = (' ATYB',
                       ' CAS',
                       ' CCIS',
                       ' CEA',
                       ' CHS',)
boxCourse.pack(side=tk.LEFT)
boxCourse.current()
fYL = ttk.Frame(frame1)
fYL.pack(padx=10, pady=5, anchor= tk.W)
lblYL	= ttk.Label(fYL, text="Enter year level : ")
lblYL.pack(side=tk.LEFT)
txtYL	= ttk.Entry(fYL)
txtYL.pack(side=tk.LEFT)
txtYL.focus()
btnSub = ttk.Button(frame1, text="START LOG", command=cred)
btnSub.pack(padx=10, pady=5, anchor= tk.W)
btnEnd = ttk.Button(frame1, text="END LOG", command=stop)
btnEnd.pack(padx=10, pady=5, anchor= tk.W)
lblLog = ttk.Label(frame1, text="View log of user:")
lblLog.pack(padx=10, pady=10, anchor= tk.W)
txtLog = ttk.Entry(frame1)
txtLog.pack(padx=10, pady=10, anchor= tk.W)
btnLog = ttk.Button(frame1, text = "OPEN", command=log)
btnLog.pack(padx=10, pady=10, anchor= tk.W)
lblDel = ttk.Label(frame1, text="""
Would like to delete a log?
Enter name.""")
lblDel.pack(padx=10, pady=10, anchor= tk.W)
txtDel = ttk.Entry(frame1)
txtDel.pack(padx=10, pady=10, anchor= tk.W)
btnDel = ttk.Button(frame1, text = "DELETE", command=delete)
btnDel.pack(padx=10, pady=10, anchor= tk.W)
#Intro
#Shapes-------------------------------------------------------------------------------------------------------------
lblShapes = ttk.Label(frame2, text="Click here to start.")
lblShapes.pack(padx=10, pady=5, anchor= tk.W)
btnSshapes = ttk.Button(frame2, text = "Start training", command=turtle_shapes)
btnSshapes.pack(padx=10, pady=5, anchor= tk.W)

questionS1 = ttk.LabelFrame(frame2, text="1) If I wanted to set the courser to a turtle shape what would I code in?")
questionS1.pack(padx=10, pady=5, anchor=tk.W)
btnqS1o1 = ttk.Button(questionS1, text="turtle.shape('turtle')",command=right_S1, state = "disabled")
btnqS1o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqS1o2 = ttk.Button(questionS1, text="turtle.shapeTurtle",command=wrong_answer, state = "disabled")
btnqS1o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")
btnqS1o3 = ttk.Button(questionS1, text="turtle.shape = Turtle",command=wrong_answer, state = "disabled")
btnqS1o3.grid(row=1,column=0,padx=10, pady=5, sticky="W")
btnqS1o4 = ttk.Button(questionS1, text="shape.Turtle(Turtle)",command=wrong_answer, state = "disabled")
btnqS1o4.grid(row=1,column=1,padx=10, pady=5, sticky="W")

questionS2 = ttk.LabelFrame(frame2, text=
"""
2) If I wanted to make a square I would use the code below:
    for i in range(5):
        turtle.fd(200)
        ????
But as you can see it's missing a line. This line would make the turtle turn right, what should it be?
""")
questionS2.pack(padx=10, pady=5, anchor=tk.W)
txtS2 = ttk.Entry(questionS2)
txtS2.pack(side=tk.LEFT)
btnqS2o1 = ttk.Button(questionS2, text="Submit",command=right_S2, state = "disabled")
btnqS2o1.pack(padx=10, pady=5, anchor=tk.W)

questionS3 = ttk.LabelFrame(frame2, text=
"""
3) Using the cartesian coordinate system at what quadrant is the square situated in?
""")
questionS3.pack(padx=10, pady=5, anchor=tk.W)
btnqS3o1 = ttk.Button(questionS3, text="Quadrant 1",command=wrong_answer, state = "disabled")
btnqS3o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqS3o2 = ttk.Button(questionS3, text="Quadrant 2",command=wrong_answer, state = "disabled")
btnqS3o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")
btnqS3o3 = ttk.Button(questionS3, text="Quadrant 3",command=wrong_answer, state = "disabled")
btnqS3o3.grid(row=1,column=0,padx=10, pady=5, sticky="W")
btnqS3o4 = ttk.Button(questionS3, text="Quadrant 4",command=right_S3, state = "disabled")
btnqS3o4.grid(row=1,column=1,padx=10, pady=5, sticky="W")

questionS4 = ttk.LabelFrame(frame2, text=
"""
4) We will reset the turtle. Now, there exists a method that will create a filled-in
circle for us. What is the method?
""")
questionS4.pack(padx=10, pady=5, anchor=tk.W)
btnqS4o1 = ttk.Button(questionS4, text="turtle.makecircle( )",command=wrong_answer, state = "disabled")
btnqS4o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqS4o2 = ttk.Button(questionS4, text="makecircle.turtle( )",command=wrong_answer, state = "disabled")
btnqS4o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")
btnqS4o3 = ttk.Button(questionS4, text="turtle.dot( )",command=right_S4, state = "disabled")
btnqS4o3.grid(row=1,column=0,padx=10, pady=5, sticky="W")
btnqS4o4 = ttk.Button(questionS4, text="turtle.circle( )",command=wrong_answer, state = "disabled")
btnqS4o4.grid(row=1,column=1,padx=10, pady=5, sticky="W")

questionS5 = ttk.LabelFrame(frame2, text=
"""
5) From what we can see from teh previous questions there are multiple ways to create
shapes in turtle graphics. Coding every step, using loops to automate the steps, and 
methods that create simple shapes.
""")
questionS5.pack(padx=10, pady=5, anchor=tk.W)
btnqS5o1 = ttk.Button(questionS5, text="True",command=right_S5, state = "disabled")
btnqS5o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqS5o2 = ttk.Button(questionS5, text="False",command=wrong_answer, state = "disabled")
btnqS5o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")

#Shapes-------------------------------------------------------------------------------------------------------------

#Colors-------------------------------------------------------------------------------------------------------------
lblColors = ttk.Label(frame3, text="Click here to start.")
lblColors.pack(padx=10, pady=5, anchor= tk.W)
btnSColors = ttk.Button(frame3, text = "Start training", command=turtle_colors)
btnSColors.pack(padx=10, pady=5, anchor= tk.W)

questionC1 = ttk.LabelFrame(frame3, text=
"""1) Which of the options below can a programmer change the color of?
(choose all that apply)
""")
questionC1.pack(padx=10, pady=5, anchor=tk.W)
Cq1options = tk.Listbox(questionC1,selectmode=tk.MULTIPLE)
Cq1options.config(width=0,height=0)
Cq1options.pack(padx=10,pady=1, anchor=tk.W)
options = ["Background","Turtle","Window","Desktop"]
for i in options:
    Cq1options.insert(tk.END, i)
btnqC1o1 = ttk.Button(questionC1, text="Submit",command=right_C1, state = "disabled")
btnqC1o1.pack(padx=10, pady=5, anchor=tk.W)

questionC2 = ttk.LabelFrame(frame3, text=
"""
2) In turtle graphics you can change the color of the turtle and pen.
If you write down this code : "t.fillcolor("#FF0000")", what will
bethe effects? (I = inner, O = outer)
""")
questionC2.pack(padx=10, pady=5, anchor=tk.W)
btnqC2o1 = ttk.Button(questionC2, text="I is yellow",command=wrong_answer, state = "disabled")
btnqC2o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqC2o2 = ttk.Button(questionC2, text="I is red",command=right_C2, state = "disabled")
btnqC2o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")
btnqC2o3 = ttk.Button(questionC2, text="O is blue",command=wrong_answer, state = "disabled")
btnqC2o3.grid(row=1,column=0,padx=10, pady=5, sticky="W")
btnqC2o4 = ttk.Button(questionC2, text="O is green",command=wrong_answer, state = "disabled")
btnqC2o4.grid(row=1,column=1,padx=10, pady=5, sticky="W")

questionC3 = ttk.LabelFrame(frame3, text=
"""
3) In turtle graphics you can fill in shapes that you draw.
To do this you need to methods at the start and end of your
shape code. What are these methods?
""")
questionC3.pack(padx=10, pady=5, anchor=tk.W)
txtC31 = ttk.Entry(questionC3)
txtC31.pack(padx=10, pady=5,side=tk.LEFT)
txtC32 = ttk.Entry(questionC3)
txtC32.pack(padx=10, pady=5,side=tk.LEFT)
btnqC3o1 = ttk.Button(questionC3, text="Submit",command=right_C3, state = "disabled")
btnqC3o1.pack(padx=10, pady=5, anchor=tk.W)

questionC4 = ttk.LabelFrame(frame3, text=
"""
4) When filling in an object you draw, the color of the outside
is determined like this t.begin_fill(color,->pen color).
""")
questionC4.pack(padx=10, pady=5, anchor=tk.W)
btnqC4o1 = ttk.Button(questionC4, text="True",command=wrong_answer, state = "disabled")
btnqC4o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqC4o2 = ttk.Button(questionC4, text="False",command=right_C4, state = "disabled")
btnqC4o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")

questionC5 = ttk.LabelFrame(frame3, text=
"""
5) Say that you like to leave an imprint of your turtle while 
it is moving across the window. What method would you use?
""")
questionC5.pack(padx=10, pady=5, anchor=tk.W)
txtC5 = ttk.Entry(questionC5)
txtC5.pack(padx=10, pady=5,side=tk.LEFT)
btnqC5o1 = ttk.Button(questionC5, text="Submit",command=right_C5, state = "disabled")
btnqC5o1.pack(padx=10, pady=5, anchor=tk.W)

#Colors-------------------------------------------------------------------------------------------------------------
#Text-------------------------------------------------------------------------------------------------------------
lblText = ttk.Label(frame4, text="Click here to start.")
lblText.pack(padx=10, pady=5, anchor= tk.W)
btnSTtext = ttk.Button(frame4, text = "Start training", command=turtle_text, state = "disabled")
btnSTtext.pack(padx=10, pady=5, anchor= tk.W)

questionT1 = ttk.LabelFrame(frame4, text=
"""1) There is a method that displays text on the turtle window
which can be configured for your wants. Which one is it?
""")
questionT1.pack(padx=10, pady=5, anchor=tk.W)
btnqT1o1 = ttk.Button(questionT1, text="turtle.text()",command=wrong_answer, state = "disabled")
btnqT1o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqT1o2 = ttk.Button(questionT1, text="turtle.talk()",command=wrong_answer, state = "disabled")
btnqT1o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")
btnqT1o3 = ttk.Button(questionT1, text="turtle.write()",command=right_T1, state = "disabled")
btnqT1o3.grid(row=1,column=0,padx=10, pady=5, sticky="W")
btnqT1o4 = ttk.Button(questionT1, text="turtle.message()",command=wrong_answer, state = "disabled")
btnqT1o4.grid(row=1,column=1,padx=10, pady=5, sticky="W")

questionT2 = ttk.LabelFrame(frame4, text=
"""
2) When specifying a font for text there are usually 3 parts
that are given. 
(write in this format: t.write(message,font=(__,__,__)
""")
questionT2.pack(padx=10, pady=5, anchor=tk.W)
txtT2 = ttk.Entry(questionT2)
txtT2.pack(padx=10, pady=5,side=tk.LEFT)
btnqT2o1 = ttk.Button(questionT2, text="Submit",command=right_T2, state = "disabled")
btnqT2o1.pack(padx=10, pady=5, anchor=tk.W)

questionT3 = ttk.LabelFrame(frame4, text=
"""
3) Select all answers that are font styles.
""")
questionT3.pack(padx=10, pady=5, anchor=tk.W)
Tq3options = tk.Listbox(questionT3,selectmode=tk.MULTIPLE)
Tq3options.config(width=0,height=0)
Tq3options.pack(padx=10,pady=1, anchor=tk.W)
optionsT3 = ["Bold","Center","Italic","Arial"]
for i in optionsT3:
    Tq3options.insert(tk.END, i)
btnqT3o1 = ttk.Button(questionT3, text="Submit",command=right_T3, state = "disabled")
btnqT3o1.pack(padx=10, pady=5, anchor=tk.W)

questionT4 = ttk.LabelFrame(frame4, text=
"""
4) Using python turtle, a program can be created that displays
text on-click using only a method.
""")
questionT4.pack(padx=10, pady=5, anchor=tk.W)
questionT4.pack(padx=10, pady=5, anchor=tk.W)
btnqT4o1 = ttk.Button(questionT4, text="True",command=wrong_answer, state = "disabled")
btnqT4o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqT4o2 = ttk.Button(questionT4, text="False",command=right_T4, state = "disabled")
btnqT4o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")

questionT5 = ttk.LabelFrame(frame4, text=
"""
5) Here is a code that will a message: t.write(message,font=(__,16,"bold").
Now it will make a message with a font size of 16, and it will be bold.
Which of the options below is a valid input for the blank space?
""")
questionT5.pack(padx=10, pady=5, anchor=tk.W)
btnqT5o1 = ttk.Button(questionT5, text="Arial",command=right_T5, state = "disabled")
btnqT5o1.grid(row=0,column=0,padx=10, pady=5, sticky="W")
btnqT5o2 = ttk.Button(questionT5, text="Black",command=wrong_answer, state = "disabled")
btnqT5o2.grid(row=0,column=1,padx=10, pady=5, sticky="W")
btnqT5o3 = ttk.Button(questionT5, text="Italicize",command=wrong_answer, state = "disabled")
btnqT5o3.grid(row=1,column=0,padx=10, pady=5, sticky="W")
btnqT5o4 = ttk.Button(questionT5, text="Center",command=wrong_answer, state = "disabled")
btnqT5o4.grid(row=1,column=1,padx=10, pady=5, sticky="W")
#Text-------------------------------------------------------------------------------------------------------------
intro.mainloop()