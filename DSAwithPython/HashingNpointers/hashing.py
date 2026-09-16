def countFreq(l):
    d = dict()
    for element in l:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1

    return d           




ourList = ["a", "b","c" , "d" , "a" , "d" , "c" , "b" , "a"]

result = countFreq(ourList)

for ele in result:
    print (ele ,":", result[ele])