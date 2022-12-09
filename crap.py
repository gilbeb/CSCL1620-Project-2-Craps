#https://www.google.com/search?q=how+to+code+craps++with+gui+in+python&rlz=1C1VDKB_enUS1017US1018&sxsrf=ALiCzsYNlHP-soXsIYmEoFkZf8Y60hF_Yg%3A1670022516710&ei=dIWKY6b-KsKtptQPxqWMMA&ved=0ahUKEwimiIDXhtz7AhXClokEHcYSAwYQ4dUDCBE&uact=5&oq=how+to+code+craps++with+gui+in+python&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEMgUIABCiBDoKCAAQRxDWBBCwAzoECCMQJzoFCAAQhgM6BwgjELACECc6CAghEMMEEKABOgoIIRDDBBAKEKABSgQIQRgASgQIRhgAUPwEWMIPYMAZaAFwAXgAgAFjiAGBB5IBAjEwmAEAoAEByAEIwAEB&sclient=gws-wiz-serp#fpstate=ive&vld=cid:e17e0575,vid:nDV7a9_SATg
from tkinter import *
import random
import csv


def dice_roll(number, bet):
    if number == 4 or number == 10:
        return bet * 3
    elif number == 5 or number == 9:
        return bet * 1.5
    elif number == 6 or number ==8:
        return bet * 6 / 5
    elif number == 2 or number == 12:
        return bet * 30
    elif number == 3 or number == 11:
        return bet * 17
    elif number == 7:
        return bet * 2

def number(dice):
    if dice == '\u2680':
        return int(1)
    elif dice == '\u2681':
        return int(2)
    elif dice == '\u2682':
        return int(3)
    elif dice == '\u2683':
        return int(4)
    elif dice == '\u2684':
        return int(5)
    elif dice == '\u2685':
        return int(6)

class Crap:
    def __init__(self, root):

        self.root = root
        self.l1 = Label(root, font=("Helvetica", 260))

        self.label_message = Label(root)
        self.label_message.pack()
        self.label_message.config(text=f'Welcome to Craps. If you roll a 7 first you win.\nIf you roll a different number then you must keep rolling till you roll that number again.\nIf you roll a 7 before you re-roll your number you lose')

        self.frame_bet = Frame(root)
        self.label_bet = Label(self.frame_bet, text='Please enter bet', foreground='blue')
        self.entry_bet = Entry(self.frame_bet)
        self.label_bet.pack()
        self.entry_bet.pack()
        self.frame_bet.pack()

        self.b0 = Button(root,text="Submit Bet", foreground='blue', command=self.bet)
        self.b0.place(x=300, y=0)
        self.b0.pack()

        self.label_message = Label(self.root)
        self.label_message.pack()

        self.b1 = Button(root, text="Roll the Dice!", foreground='blue', command=self.roll)
        self.b1.place(x=300, y=0)
        self.b1.pack()

        self.label_2message = Label(self.root)
        self.label_2message.pack()


    def roll(self):
        x = 0
        bet_file = []
        with open('bet.csv', 'r') as checking:
            reading = csv.reader(checking)
            for row in reading:
                for num in row:
                    bet_file.append(num)
        bet = ''.join([str(elem) for elem in bet_file])

        dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        dice_1 = random.choice(dice)
        dice_2 = random.choice(dice)
        total = number(dice_1) + number(dice_2)

        self.l1.config(text=f'{dice_1}{dice_2}')

        self.l1.pack()
        self.label_message = Label(self.root)
        self.label_message.pack()


        with open('dice_count.csv', 'r') as checking:
            reading = csv.reader(checking)
            for row in reading:
                if '0' in row:
                    global first_number
                    first_number = total
                    x = 1
                    self.label_message.config(text=f'Your number is {first_number}')
        with open('dice_count.csv', 'w') as csvfile:
            content = csv.writer(csvfile)
            content.writerow(str(total))

        if first_number == 7 and first_number == total:
            self.label_2message.config(text=f'Congrats you won ${dice_roll(first_number, float(bet))}', foreground='green')
            self.b1.destroy()
        if first_number == total and x == 0:
            self.label_2message.config(text=f'Congrats you won ${dice_roll(first_number, float(bet))}', foreground='green')
            self.b1.destroy()
        elif total == 7 and x == 0:
            self.label_2message.config(text=f'Sorry 7 has rolled before your number you lose.', foreground='red')
            self.b1.destroy()

    def bet(self):
        bet = self.entry_bet.get()
        try:
            float(bet)
            with open('bet.csv', 'w') as csvfile:
                content = csv.writer(csvfile)
                content.writerow(str(bet))
                self.label_message.config(text=f'Your bet is ${bet}.\nYou may roll the dice now')

        except:
            self.label_message.config(text=f'Please input a valid number.')
        self.entry_bet.delete(0, END)






