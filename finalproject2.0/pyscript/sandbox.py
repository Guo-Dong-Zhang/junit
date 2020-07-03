import os

def container(_command):
    prefix = "docker run -v /finalproject/testcontainer:/home -w /home centos_nginx_java_python "
    command = prefix+_command
    os.system(command)
    print("\n\n\n\ndocker run!!!\n\n\n\n")
