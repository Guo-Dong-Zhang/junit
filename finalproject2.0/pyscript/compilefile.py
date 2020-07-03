import listdir
import os

'''

example java file tree:
{'s1': ['calculate.java', 'calculate2.java', 'calculate3.java'], 's2': ['calculate.java', 'calculate2.java', 'calculate3.java'], 's3': ['calculate.java', 'calculate2.java']}

example junit file tree:
{'s1': ['calculatetest.java', 'calculatetest2.java'], 's2': ['calculatetest.java'], 's3': ['calculatetest.java', 'calculatetest2.java', 'calculatetest3.java']}

'''

javadic = listdir.javadic
junitdic = listdir.junitdic
projectpath = listdir.projectpath

mkdircommand = "mkdir -p "+projectpath+"/compileresult/"

#every time when start compiling, reset compileresult fold first to clear the history 
os.system("rm -rf "+projectpath+"/compileresult/*")

#make new fold relate to students' id in compileresult fold to save the compile result 
for x in javadic.keys():
    os.system(mkdircommand+x)


def compile(filedic,typeflg):
    commandls = [] #list to save compiling command
    compileprefix = "javac -d "+ projectpath+"/compileresult/"
    for k,v in filedic.items():
        compilecommand = compileprefix +k +" "
        v = [projectpath+typeflg+k+"/"+x for x in v]
        commandls = [compilecommand+filename for filename in v]
        #print(commandls)
        for cl in commandls:
            os.chdir(projectpath+"/compileresult/"+k)
            os.system(cl)

compile(javadic,"/javalist/")
compile(junitdic,"/junitlist/")
