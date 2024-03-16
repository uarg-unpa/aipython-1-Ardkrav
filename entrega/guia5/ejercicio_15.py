flores= ['rosas', 'orquídea','lirio','tulipan', 'margarita', 'dalia', 'hortensia']

#a
#print(flores[2:5])
for i in range(2,5):
    print(flores[i])
print()

#b
#print(flores[1::2])
for i in range(1,len(flores),2):
    print(flores[i])

print()

#c
#print(flores[::3])
for i in range(0,len(flores),3):
    print(flores[i])