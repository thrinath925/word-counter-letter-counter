def count_dict(mystring):
    d = {}
# count occurances of character
    for w in mystring: 
        d[w] = mystring.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))
        
print("enter your text")
mystring=input()
print("number of alphabet  you have entered::",len(mystring))
print()
print("repated letters")
count_dict(mystring)
print()

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

word_length = len(mystring.split())
print("\nNumber of words =",word_length)
print()
print("Reparted Words:")
print()
a=word_count(mystring)
for key in sorted(a):
    print ("%s: %s" % (key, a[key]))

g=input()    
