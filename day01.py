def part1(inputfile):
    answer = 0
    with open(inputfile,'r') as f:
        lines = f.read().split("\n")
    for item in lines:
        first_digit = 0 
        for character in item:
            if character.isdigit():
                first_digit = character
                break
        last_digit = 0 
        for character in item:
            if character.isdigit():
                last_digit = character
        answer = answer + int(str(first_digit) + str(last_digit))
    return str(answer)

def part2(inputfile):
    answer = 0
    with open(inputfile,'r') as f:
        lines = f.read().split("\n")
    #print(lines)
    for item in lines:
        #print(item)
        first_digit = 0
        for x in range(len(item)):
            #print(item[x])
            #print(item[x] + item[x+1] + item[x+2]) 
            if item[x].isdigit():
                first_digit = item[x]
                #print('is digit!')
                break
            elif x+2 <= len(item) and item[x:x+3] == 'one':
                first_digit = 1
                break 
            elif x+2 <= len(item) and item[x:x+3] == 'two':
                first_digit = 2
                #print('did it!')
                break
            elif x+4 <= len(item) and item[x:x+5] == 'three':
                first_digit = 3
                break 
            elif x+3 <= len(item) and item[x:x+4] == 'four':
                first_digit = 4
                break 
            elif x+3 <= len(item) and item[x:x+4] == 'five':
                first_digit = 5
                break 
            elif x+2 <= len(item) and item[x:x+3] == 'six':
                first_digit = 6
                break 
            elif x+4 <= len(item) and item[x:x+5] == 'seven':
                first_digit = 7
                break
            elif x+4 <= len(item) and item[x:x+5] == 'eight':
                first_digit = 8
                break
            elif x+2 <= len(item) and item[x:x+4] == 'nine':
                first_digit = 9
                break 
            elif x+3 <= len(item) and item[x:x+4] == 'zero':
                first_digit = 0
                break 
        #print('first_digit = ' + str(first_digit))
        last_digit = 0 
        for x in range(len(item)):
            #print(item[x])
            #print(item[x] + item[x+1] + item[x+2]) 
            if item[x].isdigit():
                last_digit = item[x]
                #print('is digit!')
            elif x+2 <= len(item) and item[x:x+3] == 'one':
                last_digit = 1
            elif x+2 <= len(item) and item[x:x+3] == 'two':
                last_digit = 2
            elif x+4 <= len(item) and item[x:x+5] == 'three':
                last_digit = 3
            elif x+3 <= len(item) and item[x:x+4] == 'four':
                last_digit = 4
            elif x+3 <= len(item) and item[x:x+4] == 'five':
                last_digit = 5
            elif x+2 <= len(item) and item[x:x+3] == 'six':
                last_digit = 6
            elif x+4 <= len(item) and item[x:x+5] == 'seven':
                last_digit = 7
            elif x+4 <= len(item) and item[x:x+5] == 'eight':
                last_digit = 8
            elif x+2 <= len(item) and item[x:x+4] == 'nine':
                last_digit = 9
            elif x+3 <= len(item) and item[x:x+4] == 'zero':
                last_digit = 0
        #print('last_digit = ' + str(last_digit))


        answer = answer + int(str(first_digit) + str(last_digit))
    
    #print(lines)
    return answer

print("Part 1 test case 1 answer = ", part1('day01input-testcase1.txt'))
print("Part 1 answer = ", part1('day01input.txt'))
#Correct on first attempt!   54877
print("Part 2 test case 1 answer = ", part2('day01input-part2-testcase1.txt'))
print("Part 2 answer = ", part2('day01input.txt'))
#Correct on first attempt!   54100
