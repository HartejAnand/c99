def getText():
    fileName= input("enter file name: ")
    fn=open(fileName)
    counted=0
    for line in fn:
        words=line.split(" ")
        counted=counted+len(words)

    print(counted)
    print("⬆ total words")

getText()