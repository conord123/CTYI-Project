import os
os.system('cls')

a = "#"
b = "#"
c = "#"
d = "#"
e = "#"
f = "#"
g = "#"
h = "#"
i = "#"

owin = 0
xwin = 0
while(xwin == 0 and owin == 0):
    xplace = 0
    while(xplace == 0):
        os.system('clear')
        print ""+a,""+b,""+c,"| a b c\n"+d,""+e,""+f,"| d e f\n"+g,""+h,""+i,"| g h i"
        xchoice = raw_input("Place your x: ")
        if(xchoice == 'a'):
            if(a == 'o' or a == 'x'):
                print "invalid choice"
            else:
                a = 'x'
                xplace = 1
        elif(xchoice == 'b'):
            if(b == 'o' or b == 'x'):
                print "invalid choice"
            else:
                b = 'x'
                xplace = 1
        elif(xchoice == 'c'):
            if(c == 'o' or c == 'x'):
                print "invalid choice"
            else:
                c = 'x'
                xplace = 1
        elif(xchoice == 'd'):
            if(d == 'o' or d == 'x'):
                print "invalid choice"
            else:
                d = 'x'
                xplace = 1
        elif(xchoice == 'e'):
            if(e == 'o' or e == 'x'):
                print "invalid choice"
            else:
                e = 'x'
                xplace = 1
        elif(xchoice == 'f'):
            if(f == 'o' or f == 'x'):
                print "invalid choice"
            else:
                f = 'x'
                xplace = 1
        elif(xchoice == 'g'):
            if(g == 'o' or g == 'x'):
                print "invalid choice"
            else:
                g = 'x'
                xplace = 1
        elif(xchoice == 'h'):
            if(h == 'o' or h == 'x'):
                print "invalid choice"
            else:
                h = 'x'
                xplace = 1
        elif(xchoice == 'i'):
            if(i == 'o' or i == 'x'):
                print "invalid choice"
            else:
                i = 'x'
                xplace = 1
        else:
            print"invalid choice"
        
    if ((a=='x' and b=='x' and c=='x') or (d=='x' and e=='x' and f=='x') or (g=='x' and h=='x' and i=='x') or (a=='x' and d=='x' and g=='x') or (b=='x' and e=='x' and h=='x') or (c=='x' and f=='x' and i=='x') or (a=='x' and e=='x' and i=='x') or (c=='x' and e=='x' and g=='x')):
        xwin = 1
        os.system('clear')
        print ""+a,""+b,""+c,"| a b c\n"+d,""+e,""+f,"| d e f\n"+g,""+h,""+i,"| g h i"
        print "x wins"
        break
    oplace = 0
    while(oplace == 0):
        os.system('clear')
        print ""+a,""+b,""+c,"| a b c\n"+d,""+e,""+f,"| d e f\n"+g,""+h,""+i,"| g h i"
        ochoice = raw_input("Place your o: ")
        if(ochoice == 'a'):
            if(a == 'x' or a == 'o'):
                print "invalid choice"
            else:
                a = 'o'
                oplace = 1
        elif(ochoice == 'b'):
            if(b == 'x' or b == 'o'):
                print "invalid choice"
            else:
                b = 'o'
                oplace = 1
        elif(ochoice == 'c'):
            if(c == 'x' or c == 'o'):
                print "invalid choice"
            else:
                c = 'o'
                oplace = 1
        elif(ochoice == 'd'):
            if(d == 'x' or d == 'o'):
                print "invalid choice"
            else:
                d = 'o'
                oplace = 1
        elif(ochoice == 'e'):
            if(e == 'x' or e == 'o'):
                print "invalid choice"
            else:
                e = 'o'
                oplace = 1
        elif(ochoice == 'f'):
            if(f == 'x' or f =='o'):
                print "invalid choice"
            else:
                f = 'o'
                oplace = 1
        elif(ochoice == 'g'):
            if(g == 'x' or g == 'o'):
                print "invalid choice"
            else:
                g = 'o'
                oplace = 1
        elif(ochoice == 'h'):
            if(h == 'x' or h == 'o'):
                print "invalid choice"
            else:
                h = 'o'
                oplace = 1
        elif(ochoice == 'i'):
            if(i == 'x' or i == 'o'):
                print "invalid choice"
            else:
                i = 'o'
                oplace = 1
        else:
            print"invalid choice" 
    if ((a=='o' and b=='o' and c=='o') or (d=='o' and e=='o' and f=='o') or (g=='o' and h=='o' and i=='o') or (a=='o' and d=='o' and g=='o') or (b=='o' and e=='o' and h=='o') or (c=='o' and f=='o' and i=='o') or (a=='o' and e=='o' and i=='o') or (c=='o' and e=='o' and g=='o')):
        owin = 1
        os.system('clear')
        print ""+a,""+b,""+c,"| a b c\n"+d,""+e,""+f,"| d e f\n"+g,""+h,""+i,"| g h i"
        print "o wins" 
        break