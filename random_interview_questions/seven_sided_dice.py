from random import randint

# Given a dice which rolls from 1 to 5, simulate a uniform 7 sided dice!


def dice5():
    return randint(1, 5)


def convert5to7():

    # For constant re-roll purposes
    while True:

        # Roll the dice twice
        roll_1 = dice5()
        roll_2 = dice5()

        # Convert the combination to the range 1 to 25
        # range of 0-20 and range of 1-5
        num = ((roll_1-1) * 5) + (roll_2)

        # print 'The converted range number was:',num
        # this number is arbitrary
        if num > 21:
            # re-roll if we are out of range
            continue

        return num % 7 + 1


print(convert5to7())
