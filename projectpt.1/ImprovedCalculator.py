from tkinter import *
expression = ""


def num_press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def compute():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except ZeroDivisionError:
        equation.set(" Cannot Divide by Zero")
        expression = ""
    except:
        equation.set(" An Error Has Occurred")
        expression = ""


def clear_text():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    window = Tk()
    window.configure(background="white")
    window.title("CalculatorPlus By Nicholas Dill")
    window.geometry("420x230")
    equation = StringVar()
    expression_field = Entry(window, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=80)

    button_one = Button(window, text=' 1 ', fg='white', bg='black', command=lambda: num_press(1), height=1, width=7)
    button_one.grid(row=4, column=0)

    button_two = Button(window, text=' 2 ', fg='white', bg='black', command=lambda: num_press(2), height=1, width=7)
    button_two.grid(row=4, column=1)

    button_three = Button(window, text=' 3 ', fg='white', bg='black', command=lambda: num_press(3), height=1, width=7)
    button_three.grid(row=4, column=2)

    button_four = Button(window, text=' 4 ', fg='white', bg='black', command=lambda: num_press(4), height=1, width=7)
    button_four.grid(row=3, column=0)

    button_five = Button(window, text=' 5 ', fg='white', bg='black', command=lambda: num_press(5), height=1, width=7)
    button_five.grid(row=3, column=1)

    button_six = Button(window, text=' 6 ', fg='white', bg='black', command=lambda: num_press(6), height=1, width=7)
    button_six.grid(row=3, column=2)

    button_seven = Button(window, text=' 7 ', fg='white', bg='black', command=lambda: num_press(7), height=1, width=7)
    button_seven.grid(row=2, column=0)

    button_eight = Button(window, text=' 8 ', fg='white', bg='black', command=lambda: num_press(8), height=1, width=7)
    button_eight.grid(row=2, column=1)

    button_nine = Button(window, text=' 9 ', fg='white', bg='black', command=lambda: num_press(9), height=1, width=7)
    button_nine.grid(row=2, column=2)

    button_zero = Button(window, text=' 0 ', fg='white', bg='black', command=lambda: num_press(0), height=1, width=7)
    button_zero.grid(row=5, column=1)

    add = Button(window, text=' + ', fg='white', bg='black', command=lambda: num_press("+"), height=1, width=7)
    add.grid(row=5, column=3)

    subtract = Button(window, text=' - ', fg='white', bg='black', command=lambda: num_press("-"), height=1, width=7)
    subtract.grid(row=4, column=3)

    multiply = Button(window, text=' * ', fg='white', bg='black', command=lambda: num_press("*"), height=1, width=7)
    multiply.grid(row=3, column=3)

    divide = Button(window, text=' / ', fg='white', bg='black', command=lambda: num_press("/"), height=1, width=7)
    divide.grid(row=2, column=3)

    equal = Button(window, text=' = ', fg='white', bg='orange', command=compute, height=1, width=7)
    equal.grid(row=6, column=3)

    clear = Button(window, text='Clear', fg='white', bg='red', command=clear_text, height=1, width=7)
    clear.grid(row=6, column=0)

    decimal = Button(window, text='.', fg='white', bg='black', command=lambda: num_press("."), height=1, width=7)
    decimal.grid(row=5, column=2)

    percent = Button(window, text=' % ', fg='white', bg='black', command=lambda: num_press("%"), height=1, width=7)
    percent.grid(row=5, column=0)

    window.mainloop()
