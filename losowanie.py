import random
import time

class Lottery:
    def __init__(self):
        self.available_numbers = list(range(1, 50))
        self.selected_numbers = []


    def SelectionEvent():
        while len(selection.selected_numbers) < 6:
            selected_number = -1
            while selected_number < 1 or selected_number > 49:
                try:
                    selected_number = int(input("Please select a number from 1 to 49\n"))
                    if selected_number not in selection.available_numbers and selected_number not in selection.selected_numbers:
                        print("Selected number is out of range. Please choose an integer from 1 to 49")
                    elif selected_number in selection.selected_numbers:
                        print("You have already chosen this number. Please type another number.")
                    else:
                        selection.selected_numbers.append(selected_number)
                        selection.available_numbers.remove(selected_number)
                except ValueError:
                    print("Incorrect input. Please enter an integer.")
                # DEBUGGING LINES
                '''print(selected_number)
                print(type(selected_number))
                print(selection.selected_numbers)
                print(selection.available_numbers)'''
        return selection.selected_numbers
    def DrawEvent():
        print("Welcome to the Lotto Draw! Today is the day for you to become a millionaire!")
        time.sleep(1.5)
        print("The system is going to select 6 out of 49 numbers. Good luck!")
        while len(draw.selected_numbers) < 6:
            time.sleep(1.5)
            drawn_number = random.choice(draw.available_numbers)
            print(drawn_number)
            draw.available_numbers.remove(drawn_number)
            draw.selected_numbers.append(drawn_number)
            print(f"Drawn number is " + str(drawn_number))
        time.sleep(1.5)
        draw.selected_numbers.sort()
        print("Drawn numbers are: " + ", ".join(map(str, draw.selected_numbers)))
        return draw.selected_numbers
    def CompareNumbers():
        win_counter = 0
        for i in selection.selected_numbers:
            if i in draw.selected_numbers:
                win_counter += 1
        if win_counter == 0:
            print('You did not guess any of the drawn numbers. Try your luck again!')
        elif win_counter == 1:
            print(f'You guessed ' + str(win_counter) + ' number.')
        else:
            print(f'You guessed ' + str(win_counter) + ' numbers.')
#instance of the Lottery class calling lists for SelectionEvent function
selection = Lottery()
#instance of the Lottery class calling lists for DrawEvent function
draw = Lottery()

Lottery.SelectionEvent()
Lottery.DrawEvent()
Lottery.CompareNumbers()

'''def SelectionEvent():
    selection = Lottery()
    while len(selection.selected_numbers) < 6:
        selected_number = -1
        while selected_number >= 1 or selected_number <= 49:
            try:
                selected_number = int(input("Please select a number from 1 to 49\n"))
            except ValueError:
                print("Incorrect input. Please enter an integer.")
        print(selected_number)
        print(type(selected_number))
        if selected_number not in selection.available_numbers and selected_number not in selection.selected_numbers:
            print("Selected number is out of range. Please choose an integer from 1 to 49")
        elif selected_number in selection.selected_numbers:
            print("You have already chosen this number. Please type another number.")
        else:
            selection.selected_numbers.append(selected_number)
            selection.available_numbers.remove(selected_number)
        print(selection.selected_numbers)
        print(selection.available_numbers)
    print("dziala normalnie waldusiu")'''

"""This is old code containing only draw function, without lottery class and with unnecessary counter "draw_counter"
def draw():
    NumbersRange.available_numbers = list(range(1, 50))
    drawn_numbers = []
    draw_counter = 0
    print(available_numbers)


    while draw_counter < 6:
        time.sleep(1.5)
        drawn_number = random.choice(available_numbers)
        print(drawn_number)
        #print(available_numbers)
        available_numbers.remove(drawn_number)
        drawn_numbers.append(drawn_number)
        print(f"Drawn number is " + str(drawn_number))
        #print(available_numbers)
        draw_counter = draw_counter + 1

    time.sleep(1.5)
    drawn_numbers.sort()
    #str(drawn_numbers)
    #print(drawn_numbers)
    print("Drawn numbers are: " + ", ".join(map(str, drawn_numbers)))

draw()"""

