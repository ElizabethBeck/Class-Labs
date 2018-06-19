a = [ "Euclid", "Archimedes", "Newton","Descartes", "Fermat", "Turing", "Euler", "Einstein", "Boole", "Fibonacci", "Nash"]
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U','u']
print(vowels)
if a[0][0] in vowels:  # is E in Euclid (==a[0][0]) in the list of vowels ???
    print('YES')
else:
    print('NO')

j = 0
#for k  in a:
    #print('11..', k, len(k), k[j])
maxlen = 0
minlen = 0 
for k in a:
    if len(a[j]) > maxlen:
        maxlen = len(a[j])
        t = a[j]
    elif len(a[j]) < maxlen:
        minlen = len(a[j])
        u = a[j]
    j = j+1
print('1', t, "is the longest name at: ", len(t), "letters." )
print('2', u, "is the shortest name at: ", len(u), "letters")
print ('1', a)
print ('2', a[2])
print ('3', a[len(a)-1])
print ('4', a[2][0])
print ('5', a[2][1])
s = a[2] + a[3]
print('6', s)
print('7',len(a))
print('8',a[0], " ", len(a[0]))
print('9',a[0][0] +  a[1][0])
x = len(a[0]) - 1
y = len(a[1]) - 1
print('10', a[0][x]+ a[1][y])
