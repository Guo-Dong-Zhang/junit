import os

projectpath = "/finalproject"
javapath = projectpath+"/javalist"
junitpath = projectpath+"/junitlist"

#global var to save the java file name and junit file name in dic
javadic={}
junitdic={}


#walk through the whole file
def flist(filepath):
    layer = 0
    filedic = {}
    idls = []
    for dirname,subdirlist,filelist in os.walk(filepath):
        if layer == 0:
            idls = subdirlist.copy()
        else:
            filedic[idls[layer-1]] = filelist
        layer = layer+1
    return filedic


javadic= flist(javapath)
junitdic= flist(junitpath)

#print("java doc:",javadic)
#print("junit doc:",junitdic)




