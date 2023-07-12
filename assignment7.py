def assign(file="file1.txt"):
    try:
        file=open(file,"+a")
        file.writelines(["Name:Prabhat",
                    "\nRoll_no:05",
                    "\nClass:Third Year"])
        file.seek(0)
        print(file.readlines())
    except IOError:
        print("Exception Handling")

assign()


