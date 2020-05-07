import math

#instructions
print('Kindly Follow Instructions ')
print('Entry should be `1 Grammar`')
print('`#` is read as Epsilon')

#read Grammar , split the grammar into independent rules and store in nested list
str1 = input('Enter Grammar : ')
lst = str1.split('->')
lst[1] = lst[1].split('|')

char = input('Enter the String : ')

#pre-intializations
final = []
new = []
count = 0
concat = ''

#function to compute the string from given grammar
def first(lst) :
    concat = ''
    #for each rule in list do 
    for i in lst[1] :
        k=0
        #for each character in rule
        for j in i :
            if char[k] == j :  #if character is equal to corresponding character in given string
                concat=concat+j   #conatenate the character and continue
                concat2=concat    #copy of concat for further use

            elif j.isupper() :   #if character is upper case 
                for j in lst[1]:          #replace the it with possible rules
                    concat=concat+j
                    concat = concat+i[k+1:]
                    if len(concat) < len(char)+2 :
                        final.append(concat)     #append the strings in a new list
                        concat = concat2

            elif j == '#' :                 #if character is # then remove # from string as a substitute for Epsilon 
                concat=concat+i[k+1:]
                if len(concat) < len(char)+2 :
                        final.append(concat)
                        concat = concat2

            k=k+1    #increment char count
        concat = ''
    #print(final)
    return final

#function to compute strings after first string is generated
def second(lst, lst2) :
    concat = ''
    concat2 = ''
    #for each string in revised list
    for i in lst2[1] :
        k=0
        #for each character in string
        for j in i :
            if i == '':   #if empty skip 
                break
            elif k==len(char) :   #if the length of string is equal the length of given string 
                if j.isupper():   #if j is upper case then replace it with rules  and append it into list
                    for j in lst[1]:            
                        concat=concat+j
                        if len(concat) <= len(char)+3 and len(concat) > 3 :
                            final.append(concat)
                            concat = concat2
                    break
                elif j == '#' :  #if # then remove it 
                    concat=concat+i[k+1:]
                    if len(concat) < len(char)+2 :
                            final.append(concat)
                            concat = concat2
                            break
            elif char[k] == j :    #if character is equal to corresponding character in given string 
                concat=concat+char[k]  #concate and continue
                concat2=concat
            elif j.isupper() :
                for j in lst[1]:                
                    concat=concat+j
                    if len(concat) <= len(char)+3 and len(concat) > 3 :
                        final.append(concat)
                        concat = concat2
                break
            elif j == '#' :
                concat=concat+i[k+1:]
                if len(concat) < len(char)+2 :
                        final.append(concat)
                        concat = concat2
                        break
            k = k+1
        concat = ''
    #print(final)
    return final

#function to keep the possible matching string and discard the rest of them
def filter(final, count) :
    #if more than twice a string is generated then grammar is ambiguous
    for x in final :
        if char == x :
            count = count+1
            if count == 2 :
                print('Ambiguous')
                exit()

    rev = []
    new = ['X']
    rep = ''
    #for each generated string do 
    for x in final : 
        z = 0 
        l = 0
        rep = ''
        for y in x :
            #if the length of generated is string is less than equal to given string compare
            if len(x) <= len(char)+1 :
                if z == len(char) :
                    if y.isupper() :   #if upper case, the string has possible substitute append it to revised list
                        rev.append(x)
                    elif y == '#':    #if # append it to revised list
                        rev.append(x)

                elif char[z] == y :   #if corresponding char is found then continue
                    rep = rep + char[z]
                    
                elif y.isupper() :   #if upper case, string has possible substitute append it to revised list
                    rev.append(x)
                    break

                elif y == '#' :    #if # append it to revised list
                    rev.append(x)
                    break

                z = z + 1  #increment character in string 

    new.append(rev)
    #print(new)
    return new

#perform functions for 4 or n times
final = first(lst)
c = 1
while c < 6 :
    new = filter(final ,count)
    final = second(lst,new)
    c = c + 1
new = filter(final ,count)
#count of string is not more than 2 then grammar is unambiguous
if count == 1 or count == 0 :
        print('Unambiguous')
    
