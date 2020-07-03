import os
import re
import listdir

javadic = listdir.javadic
junitdic = listdir.junitdic
projectpath = listdir.projectpath

junitPrefix = "java org.junit.runner.JUnitCore";
filePrefix = "com.junit."

for k,v in junitdic.items():
    allfiles = ""
    v = [filePrefix+re.sub(".java","",x) for x in v]
    for filename in v:
        allfiles = allfiles + " "+filename
    junitdic[k]=allfiles

def run():
    for k,v in junitdic.items():
        os.chdir(projectpath+"/compileresult/"+k)
        os.system(junitPrefix+v)
#        print(junitPrefix+v)
        print(k+" is done!!!!!!!!!!!!\n\t")
print(junitdic)
run()


'''
{'s1': ['com.trustie.test.calculatetest2', 'com.trustie.test.calculatetest'], 's2': ['com.trustie.test.calculatetest'], 's3': ['com.trustie.test.calculatetest', 'com.trustie.test.calculatetest2', 'com.trustie.test.calculatetest3']}
'''
