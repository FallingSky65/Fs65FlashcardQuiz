import sys, os, pandas

def howToUse():
    ...

def main(argv):
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


    
if __name__ == "__main__":
    main(sys.argv)