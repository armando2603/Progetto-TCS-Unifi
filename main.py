__author__ = "Giuseppe serna"

f_gram = open('grammar.txt', 'r')
prod = f_gram.read().splitlines()
print(prod, end='\n \n')
terminals = []
variables = []
prodT = {}
prodV = {}
var = []

for p in prod:
    s = p.split("->")
    var.append(s[0])
    s = s[1]
    s = s.split("|")
    for i in s:
        if len(i) == 1:
            terminals.append(i)
            prodT[i] = []
        else:
            variables.append(i)
            prodV[i] = []
k = 0
for p in prod:

    s = p.split("->")
    s = s[1]
    s = s.split("|")
    for i in s:
        if len(i) == 1:
            terminals.append(i)
            prodT[i].append(k)
        else:
            variables.append(i)
            prodV[i].append(k)
    k +=1
#Creo i dizionari terminals e variables


x=input('inserisci una stringa : ')

print('');
#inizializzo la matrice len(x) x len(x)
m = [[[False for y in range(len(prod))] for k in range(len(x))] for j in range(len(x))]

for s in range(len(x)):
    if x[s] in terminals:
        for i in prodT[x[s]]:
            m[0][s][i] = True

#eseguo i passi rimanenti

for l in range(1,len(x)):
    for s in range(len(x)-l):
        for p in range(1, l+1):
            for i in range(len(prod)):
                for j in range(len(prod)):
                    if m[p-1][s][i] and m[l-p][p+s][j]:
                        if var[i]+var[j] in variables:
                            a = prodV[var[i]+var[j]]
                            for f in a:
                                m[l][s][f] = True

if m [len(x)-1][0][0] == True:
    print('La stringa inserita appartiene alla gramatica')
else:
    print('La stringa inserita non appartiene alla grammatica')
    print('');

#disegno la tavola
for i in range(len(x)-1, -1, -1):
    for k in range(len(x)):
        z = ''
        for j in range(len(prod)):
            if m[i][k][j] == True:
                z = z+var[j]
            if j == len(prod)-1:
                if len(z) == 0:
                    space = ''
                    for k in range(len(prod)):
                        space = space + ' '
                    print('-'+space , end='')
                else:
                    space = ''
                    for k in range(len(prod)-len(z)+1):
                        space = space + ' '
                    print(z+space , end ='')
    print('')
for i in range(len(x)):
    space = ''
    for k in range(len(prod)):
        space=space+' '
    print(str(x[i]), end=space)

print('\n');





