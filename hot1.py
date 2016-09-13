#-- defining function --#
def hotjar(a):
    b = [1,2,3]
    i = 0;
    while i < (len(a)-2):
        if b == a[i:i+3:1]:
            return True
            break
        i += 1
#-- example of using ---#
a = [0, 4, 5, 34, 34, 1, 2, 3, 5, 6, 7]
if hotjar(a):
    print ('true')
else:
    print ('false')