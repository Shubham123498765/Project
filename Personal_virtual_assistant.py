from tkinter import *
from tkinter.messagebox import *
import wolframalpha
  
def show_answer():                   #Answer function

    app_id = "6HH4YA-KLRHRL6JVW"     #API Key

    client = wolframalpha.Client(app_id)  #Verification of API key

    question = ques.get()            #Input from user
    
    res = client.query(question)     #Respone from the website
    
    ans = next(res.results).text     #Storing the result
    answer.insert(0, ans)            #Display the result


main = Tk()
main.geometry("500x90")                     #Dimension of the window  
main.title("Personal Virtual Assistant")    #Title Bar
Label(main, text = "Enter Your Question ").grid(row=0)  #Label of question textfield
Label(main, text = "The  Answer  is       ").grid(row=2)  #Lable of answer textfield


ques = Entry(main)       #Takes input         
answer = Entry(main)     #Gives output


ques.grid(row=0, column=4,ipadx=200)    #Question text field   
answer.grid(row=2, column=4,ipadx=200)  #Answer text field


def delete_text():                     #Delete function
    ques.delete(0, "end")              #Clears the question textfield
    answer.delete(0, "end")            #Clears the answer textfield

Button(main, text="Delete", command=delete_text).grid(row=4, column=3, sticky=W, pady=4)  #Delete button
Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)   #Quit button
Button(main, text='Answer', command=show_answer).grid(row=4, column=4, sticky=W, pady=4)    #Answer button

mainloop()              # Executes tkinter 