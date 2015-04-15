
print "<HTML>"
print "<pre>"
for x in range(0, 11):
    if x % 2 == 0:
        print "<font face=verdana color=\'#00FFFF\'>%5d%5d </font>" %(x,x**2)
    else:
        print"<font face=verdana color=\'blue\' >%5d%5d </font>" %(x,x**2)
print "</pre>"
print "</HTML>"
