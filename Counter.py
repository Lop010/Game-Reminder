from tkinter import *
root = Tk()
root.geometry("150x100")
root.title("Counter")


count = 0
# - Button Function - #
def buttonfunction():
  global count
  count += 1


# - Button - #
Button(text="Count", command=buttonfunction) .grid(column=2, row=2, pady=10)

# - Label - #
Label(text=(count)) .grid(column=2, row=0, pady=10)

root.mainloop()