import random
import time


def draw():
    available_numbers = list(range(1, 50))
    drawn_numbers = []
    draw_counter = 0


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
    '''print(f"Drawn number is: " + str(drawn_numbers))'''
    print("Drawn numbers are: " + ", ".join(map(str, drawn_numbers)))

draw()
