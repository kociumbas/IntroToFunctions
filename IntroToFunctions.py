accessMode = "w"


def giveInfo(p_infoInFile):
    return

def giveFileName(p_fileName):
    return

giveFileName=(input("Give the filename with extention: "))
giveInfo=(input("Write data for the file: "))


myFile=open(giveFileName, accessMode)
myFile.write(giveInfo)
myFile.close()