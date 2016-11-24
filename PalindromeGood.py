#Solution 3, best

string = raw_input()

found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

n = len(string)
record={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
for i in range(0,n):
    record[string[i]] = record[string[i]]+1
odd = 0
found = True

for ch in record:
    if record[ch] % 2 <> 0:
        odd = odd + 1
    if odd >=2:
        found = False
        break     

if not found:
    print("NO")
else:
    print("YES")
