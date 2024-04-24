import sys, os, pandas
from random import shuffle

def clear():
    os.system("clear") # unix systems
    #os.system("cls") # windows

def howToUse():
    print("To use: 'python main.py __.csv' where __.csv is a path to a csv file with 2 columns")

def quiz(fronts : list, backs : list):
    fronts = fronts.copy()
    backs = backs.copy()
    while len(fronts) > 0:
        print(f"{len(fronts)} flashcard(s) left.\n")

        randomIndices = [i for i in range(len(fronts))]
        shuffle(randomIndices)

        frontsTemp = fronts.copy()
        backsTemp = backs.copy()

        for i in range(len(fronts)):
            print(fronts[randomIndices[i]])
            x = input(">>")
            if x.lower() == backs[randomIndices[i]].lower():
                print("<correct>\n")
                frontsTemp.remove(fronts[randomIndices[i]])
                backsTemp.remove(backs[randomIndices[i]])
            else:
                print("The correct answer is " + backs[randomIndices[i]] + ".")
                print("mark as correct? (y/n)")
                op = input(">>")
                if op.lower() == "y":
                    frontsTemp.remove(fronts[randomIndices[i]])
                    backsTemp.remove(backs[randomIndices[i]])
                print("<ok>\n")

        fronts = frontsTemp
        backs = backsTemp

        clear()

def main(argv : list):
    if len(argv) <= 1:
        howToUse()
        return
    targetFilePath = argv[1]
    if not os.path.isfile(targetFilePath):
        print(f"error: file '{targetFilePath}' does not exist")
        return
    if os.path.splitext(os.path.basename(targetFilePath))[-1] != ".csv":
        print("error: file must be .csv")
        return
    
    df = pandas.read_csv(targetFilePath, header=None)
    if df.shape[1] == 1:
        print("error: csv has only one column")
        return
    df = df[[0,1]]
    print(df.head())
    print("\nWhich column do you want to be hidden? (0,1)")
    choice = input("> ") + '1'
    if choice[0] == '0':
        fronts = df[1].tolist()
        backs = df[0].tolist()
    else:
        fronts = df[0].tolist()
        backs = df[1].tolist()
    #print("fronts =", fronts)
    #print("backs =", backs)
    fronts = [str(s).strip() for s in fronts]
    backs = [str(s).strip() for s in backs]

    clear()
    quiz(fronts, backs)
    while (input("Restart? (y/n): ")+'n').lower()[0] == 'y':
        quiz(fronts, backs)
    print("bye!")
    
if __name__ == "__main__":
    main(sys.argv)