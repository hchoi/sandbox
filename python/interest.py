principal = 1000
rate = 0.05
numyears = 5
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    # print year, principal   
    # print "%3d %0.2f" % ( year, principal )   
    print "{0:3d} {1:0.2f}".format( year, principal )   
    year += 1
