from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        response = simpledialog.askinteger("Guess", "What is your guess?")
        # 5. If the guess is correct
        if response == random_num:
            # 6. Win. Use 'sys.exit(0)' to end the program
            sys.exit(0)
        # 7. if the guess is high
        elif response > random_num:
            # 8. Tell them it's too high
            messagebox.showinfo(message="Your guess is too high")
        # 9. Else if the guess is low
        elif response < random_num:
            # 10. Tell them it's too low
            messagebox.showinfo(message="Your guess is too low")
    #11. Outside of the loop, tell the user they lost
    messagebox.showinfo(message="You lost!")
    window.mainloop()
