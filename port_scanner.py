import sys
import socket
from datetime import datetime

#Define target
def main():
    if len(sys.argv) == 2:
        print("sys.argv[1] = " + str(sys.argv[1]))
        target = socket.gethostbyname(sys.argv[1])
        print("target: " + target)

    else:
        pythonPath = "C:/Python310/python.exe"
        workingDir = "C:/Users/ametah.admin/Desktop/PORTSWIGGER COURSE/Python"
        print("Invalid amount of arguments.")
        print("Syntax: %s '%s' scanner.py <ip>" % (pythonPath, workingDir) )
        sys.exit()

    #pretty banner
    print("-" * 50)
    print("Scanning target %s" % target)
    print("Time started: "+str(datetime.now()))
    print("-" * 50)

    try:
        for port in range(50,85):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port)) #returns error indicator
            print("Checking port {}" .format(port))
            if result == 0:
                print("Port {} is open" .format(port))
            s.close()
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()
            
if __name__ == "__main__":
    main()
