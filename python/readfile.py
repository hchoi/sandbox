f = open("readfile.py")
line = f.readline()
while line:
    print line,    # end with , for escaping linefeed
    # print (line,end='') # Python3
    line = f.readline()
f.close() 
