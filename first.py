a = "#"
b = "#"
c = "#"
d = "#"
e = "#"
f = "#"
g = "#"
h = "#"
i = "#"

xwin = 0
while(xwin == 0):
    print ""+a,""+b,""+c,"| a b c\n"+d,""+e,""+f,"| d e f\n"+g,""+h,""+i,"| g h i"
    xchoice = raw_input("Place your x: ")
    xplace = 0
    while(xplace == 0):
        if(xchoice == 'a'):
            if(a == 'o'):
                print "invalid choice"
            elif (a == 'x'):
                print "invalid choice"
            else:
                a = 'x'
                xplace = 1
        elif(xchoice == 'b'):
            if(b == 'o'):
                print "invalid choice"
            elif(b == 'x'):
                print "invalid choice"
            else:
                b = 'x'
                xplace = 1
        elif(xchoice == 'c'):
            if(c == 'o'):
                print "invalid choice"
            elif(c == 'x'):
                print "invalid choice"
            else:
                c = 'x'
                xplace = 1
        elif(xchoice == 'd'):
            if(d == o):
                print "invalid choice"
            elif(d == x):  
                print "invalid choice"
            else:
                d = x
                xplace = 1
        elif(xchoice == 'e'):
            if(e == o):
                print "invalid choice"
            elif(e == x):
                print "invalid choice"
            else:
                e = x
                xplace = 1
        elif(xchoice == 'f'):
            if(f == o):
                print "invalid choice"
            elif(f == x):
                print "invalid choice"
            else:
                f = x
                xplace = 1
        elif(xchoice == 'g'):
            if(g == o):
                print "invalid choice"
            elif(g == x):
                print "invalid choice"
            else:
                g = x
                xplace = 1
        elif(xchoice == 'h'):
            if(h == o):
                print "invalid choice"
            elif(h == x):
                print "invalid choice"
            else:
                h = x
        elif(xchoice == 'i'):
            if(i == o):
                print "invalid choice"
            elif(i == x):
                print "invalid choice"
            else:
                i = x
                xplace = 1
        else:
            print"invalid choice"
    owin = 0
    print ""+a,""+b,""+c,"| a b c\n"+d,""+e,""+f,"| d e f\n"+g,""+h,""+i,"| g h i"
    ochoice = raw_input("Place your o: ") 
    oplace = 0
    while(oplace == 0):
        if(ochoice == 'a'):
            if(a == 'x'):
                print "invalid choice"
            elif(a == 'o'):
                print "invalid choice"
            else:
                a = 'o'
                oplace = 1
        elif(ochoice == 'b'):
            if(b == 'x'):
                print "invalid choice"
            elif(b == 'o'):
                print "invalid choice"
            else:
                b = 'o'
                oplace = 1
        elif(ochoice == 'c'):
            if(c == x):
                print "invalid choice"
            elif(c == x):
                print "invalid choice"
            else:
                c = o
                oplace = 1
        elif(ochoice == 'd'):
            if(d == x):
                print "invalid choice"
            elif(d == x):
                print "invalid choice"
            else:
                d = o
                oplace = 1
        elif(ochoice == 'e'):
            if(e == x):
                print "invalid choice"
            elif(e == x):
                print "invalid choice"
            else:
                e = o
                oplace = 1
        elif(ochoice == 'f'):
            if(f == x):
                print "invalid choice"
            elif(f == x):
                print "invalid choice"
            else:
                f = o
                oplace = 1
        elif(ochoice == 'g'):
            if(g == x):
                print "invalid choice"
            elif(g == x):
                print "invalid choice"
            else:
                g = o
                oplace = 1
        elif(ochoice == 'h'):
            if(h == x):
                print "invalid choice"
            elif(h == x):
                print "invalid choice"
            else:
                h = o
                oplace = 1
        elif(ochoice == 'i'):
            if(i == x):
                print "invalid choice"
            elif(i == x):
                print "invalid choice"
            else:
                i = o
                oplace = 1
        else:
            print"invalid choice"
    if ((a and b and c) or (d and e and f) or (g and h and i) or (a and d and g) or b,e,h or c,f,i or a,e,i or c,e,g is 'x'):
        xwin = 1
        print "x wins" 
    if (a,b,c or d,e,f or g,h,i or a,d,g or b,e,h or c,f,i or a,e,i or c,e,g is 'o'):
        owin = 1
        print "o wins" 