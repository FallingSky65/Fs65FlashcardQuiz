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
    
    df = pandas.read_csv(targetFilePath)

    
if __name__ == "__main__":
    main(sys.argv)