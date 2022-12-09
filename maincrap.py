from crap import *
def main():
    csv_input = '0'
    with open('dice_count.csv', 'w') as csvfile:
        content = csv.writer(csvfile)
        content.writerow(csv_input)
    root = Tk()
    root.resizable(False, False)
    root.title('Craps')
    root.geometry("800x650")
    widgets = Crap(root)
    root.mainloop()



if __name__ == '__main__':
    main()