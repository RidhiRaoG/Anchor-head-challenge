from random import randint
denominator = 0
numerator = 0
for i in range(10000):
    location = 4
    distance = 0
    reached = 0
    fall = 0
    list =[]
    while distance < 17:
        n = randint(0,1)
        distance += 1
        list.append(distance)
        if n == 0:
            list.append('Left')
            location -= 1
            list.append(location)
        if n == 1:
            list.append('Right')
            location += 1
            list.append(location)
        if location < 1 or location > 9 and distance < 17:
            location = 4
            distance = 0
            list.append("FALL")
            fall += 1
    reached += 1
    print(reached/(reached+fall), "is the probability of success.")
    #print(list)
    #print(list.count("FALL"))
    numerator += reached
    denominator += (reached+fall)
average = numerator/denominator
print (average, "TOTAL")