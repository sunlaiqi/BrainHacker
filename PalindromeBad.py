# Solution 1
string = raw_input()

found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
list_string = list(string)
n = len(list_string)
odd = 0
while n > 0:
    if n == 1:
        odd = odd + 1
        break
    for i in range(1,n):
        if list_string[0] == list_string[i]:
            list_string.pop(i)
            list_string.pop(0)
            break
    if n == len(list_string):
        odd = odd + 1
        list_string.pop(0)
        
    n = len(list_string)

if odd < 2:
    found = True
        
if not found:
    print("NO")
else:
    print("YES")

# Solution 2

string = raw_input()

found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

n = len(string)
record=[]

for i in range(0,n):
    if i not in record:
        item = string[i]
        for m in range(i+1,n):
            if m not in record:
                if item == string[m]:
                    record.append(i)
                    record.append(m)
                    break
                    
if n - len(record) < 2:
    found = True
    
if not found:
    print("NO")
else:
    print("YES")
