import tkinter as tk 
import random

#creates main window
root = tk.Tk()

#initiate variables: score and count(to count how many questions have been answered)
count=0
score=0
#generates two random numbers between 1 and 10
def generate_numbers():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a, b 

def generate_operator():
    operators = "*/+-"
    selected_operator = random.choice(operators)
    return selected_operator

def process_input(a, b, question, entry, submit_button, close_button, operator):
    #declare score as global variable
    global score
    #initialize input from entry textbox to a variable 
    input = entry.get()
    if operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    elif operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b


    #score increases by 1 if correct 
    if float(input) == result: 
        score +=1
    
    question.destroy()
    entry.destroy()
    submit_button.destroy()
    close_button.destroy()
    loop_questions()

def close_window():
    root.destroy()

#Display user's score as -/10
def print_results(score):
    Title = tk.Label(root, text=f"Your score is {score}/10")
    #formatting my label 
    Title.pack(padx= 30, pady=30)

#Question and answer cycle to loop 10 times
def loop_questions():
    global count
    if count < 10:

        count+=1
        #generate random numbers for a and b
        a, b =generate_numbers()

        #generate random operator 
        operator=generate_operator()

        #display question
        question=tk.Label(root, text=f"{a}{operator}{b}=")
        question.pack(padx=10, pady=10)

        #get input from user 
        entry = tk.Entry(root, width=10)
        entry.pack()

        #Submit button that calls input processing function when clicked, 
        #taking the user input and two numbers being added as parameters
        submit_button=tk.Button(root, text="Submit", command=lambda: process_input(a , b, question, entry, submit_button, close_button, operator))
        submit_button.pack()
        close_button = tk.Button(root, text="Close", command=close_window)
        close_button.pack()
        
    else: 
        print_results(score)

def main():
    global count
    global score
    global root
    #create main window and set window size
    root.geometry("400x300")
    #Titles
    root.title("Quick Math Test")
    label1=tk.Label(root, text="Quick Math Test", font=("comic sans", 18))
    label1.pack(padx=10, pady=10)
    loop_questions()

    root.mainloop()

if __name__ == "__main__":
    main()





