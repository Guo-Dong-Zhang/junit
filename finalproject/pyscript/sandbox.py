import os
import feedback
from subprocess import Popen, PIPE



def container(_command):
    prefix = "docker run -v /finalproject/testcontainer:/home -w /home centos_nginx_java_python "
    command = prefix+_command
    
    stdout = Popen(command, shell=True, stdout=PIPE).stdout
    result = stdout.read()
    print(feedback.checkresult(result),"from feedback file")
    #os.system(command)
    print("\n\n\n\ndocker run!!!\n\n\n\n")
