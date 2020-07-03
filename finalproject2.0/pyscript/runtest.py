import os
import re
import listdir
import sandbox

javadic = listdir.javadic
junitdic = listdir.junitdic
projectpath = listdir.projectpath

junitPrefix = "java -cp /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.252.b09-2.el8_1.x86_64/lib/junit413.jar:/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.252.b09-2.el8_1.x86_64/lib/hamcrest-core-13.jar:. org.junit.runner.JUnitCore";
filePrefix = "com.junit."

for k,v in junitdic.items():
    allfiles = ""
    v = [filePrefix+re.sub(".java","",x) for x in v]
    for filename in v:
        allfiles = allfiles + " "+filename
    junitdic[k]=allfiles

def run():
    os.system("rm -rf "+projectpath+"/testcontainer/com/*") #reset testconainer/com folder

    for k,v in junitdic.items():
        address1 = projectpath+"/compileresult/"+k+"/com/java/ "
        address3 = projectpath+"/testcontainer/com"
        os.system("cp -r "+ address1+address3)

        for stid in junitdic.keys():
            address2 = projectpath+"/compileresult/"+stid+"/com/junit/ "
            os.system("cp -r "+ address2+address3)
            os.chdir(projectpath+"/testcontainer/")
            #print(projectpath+"/testcontainer/")
            cl = junitPrefix + junitdic[stid]
            sandbox.container(cl)
            #os.system(junitPrefix + junitdic[stid])
           
            #print(junitPrefix + junitdic[stid])
            os.system("rm -rf "+projectpath+"/testcontainer/com/junit")
            print("\n\n\n"+k+"&&"+stid+"test already!\n\n\n")
        os.system("rm -rf "+projectpath+"/testcontainer/com/*")
run()

'''
def run():
    for k,v in junitdic.items():
        os.chdir(projectpath+"/compileresult/"+k)
        os.system(junitPrefix+v)
        print(junitPrefix+v)
        print(k+" is done!!!!!!!!!!!!\n\t")

print(junitdic)
run()
'''

'''
{'s1': ' com.junit.calculatetest com.junit.calculatetest2', 's2': ' com.junit.calculatetest', 's3': ' com.junit.calculatetest com.junit.calculatetest2 com.junit.calculatetest3'}
'''

'''
{'s1': ['com.trustie.test.calculatetest2', 'com.trustie.test.calculatetest'], 's2': ['com.trustie.test.calculatetest'], 's3': ['com.trustie.test.calculatetest', 'com.trustie.test.calculatetest2', 'com.trustie.test.calculatetest3']}
'''

