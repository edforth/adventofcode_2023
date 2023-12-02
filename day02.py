def part1(inputfile):
    answer = 0
    with open(inputfile,'r') as f:
        lines = f.read().split("\n")
    #print(lines)
    maxredcubes = 12
    maxgreencubes = 13
    maxbluecubes = 14
    sumid = 0
    for item in lines:
        if item == '':
            continue
        possiblegame = 1 
        #print(item)
        input1 = item.split(':')
        input2 = input1[0].split(' ')
        gameid = int(input2[1])
        # UUGHH, each pull is multiple colors, seperated by semicolons, then commas for each color within. 
        #print('gameid = ' + str(gameid))
        pulls = input1[1].split(';')
        for pull in pulls: 
            #if possiblegame == 0:
            # break 
            pullitems = pull.split(',')
            for pullitem in pullitems: 
                input3 = pullitem.strip().split(' ')
                cubeqty = int(input3[0])
                cubecolor = input3[1]
                #print('This pull was for ' + str(cubeqty) + ' ' + str(cubecolor))
                if cubecolor == 'red':
                    if cubeqty > maxredcubes:
                        possiblegame = 0
                elif cubecolor == 'green':
                    if cubeqty > maxgreencubes:
                        possiblegame = 0
                elif cubecolor == 'blue':
                    if cubeqty > maxbluecubes:
                        possiblegame = 0
                else:
                    print('WHAAAAAT?????????')
        if possiblegame == 1:
            sumid = sumid + gameid
        #print(sumid)

    return str(sumid)

def part2(inputfile):
    answer = 0
    with open(inputfile,'r') as f:
        lines = f.read().split("\n")
    #print(lines)

    cubepowersum = 0
    for item in lines:
        minredcubes = 0
        mingreencubes = 0
        minbluecubes = 0
        if item == '':
            continue
        possiblegame = 1 
        #print(item)
        input1 = item.split(':')
        input2 = input1[0].split(' ')
        #print('gameid = ' + str(gameid))
        pulls = input1[1].split(';')
        for pull in pulls: 
            #if possiblegame == 0:
            # break 
            pullitems = pull.split(',')
            for pullitem in pullitems: 
                input3 = pullitem.strip().split(' ')
                cubeqty = int(input3[0])
                cubecolor = input3[1]
                #print('This pull was for ' + str(cubeqty) + ' ' + str(cubecolor))
                if cubecolor == 'red':
                    if minredcubes == 0 or minredcubes < cubeqty:
                        minredcubes = cubeqty
                elif cubecolor == 'green':
                    if mingreencubes == 0 or mingreencubes < cubeqty:
                        mingreencubes = cubeqty
                elif cubecolor == 'blue':
                    if minbluecubes == 0 or minbluecubes < cubeqty:
                        minbluecubes = cubeqty
                else:
                    print('WHAAAAAT?????????')
        cubepower = minredcubes * mingreencubes * minbluecubes
        cubepowersum = cubepowersum + cubepower
        #print(sumid)
    return str(cubepowersum)

print("Part 1 test case 1 answer = ", part1('day02input-testcase1.txt'))
print("Part 1 answer = ", part1('day02input.txt'))
#First try! 2505
print("Part 2 test case 1 answer = ", part2('day02input-testcase1.txt'))
print("Part 2 answer = ", part2('day02input.txt'))
#First Try! 70265
