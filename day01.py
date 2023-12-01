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
            elif item[x] == 'o' and item[x+1] == 'n' and item[x+2] == 'e':
                first_digit = 1
                break 
            elif item[x] == 't' and item[x+1] == 'w' and item[x+2] == 'o':
                first_digit = 2
                #print('did it!')
                break
            elif item[x] == 't' and item[x+1] == 'h' and item[x+2] == 'r' and item[x+3] == 'e' and item[x+4] == 'e':
                first_digit = 3
                break 
            elif item[x] == 'f' and item[x+1] == 'o' and item[x+2] == 'u' and item[x+3] == 'r':
                first_digit = 4
                break 
            elif item[x] == 'f' and item[x+1] == 'i' and item[x+2] == 'v' and item[x+3] == 'e':
                first_digit = 5
                break 
            elif item[x] == 's' and item[x+1] == 'i' and item[x+2] == 'x':
                first_digit = 6
                break 
            elif item[x] == 's' and item[x+1] == 'e' and item[x+2] == 'v' and item[x+3] == 'e' and item[x+4] == 'n':
                first_digit = 7
                break
            elif item[x] == 'e' and item[x+1] == 'i' and item[x+2] == 'g' and item[x+3] == 'h' and item[x+4] == 't':
                first_digit = 8
                break
            elif item[x] == 'n' and item[x+1] == 'i' and item[x+2] == 'n' and item[x+3] == 'e':
                first_digit = 9
                break 
            elif item[x] == 'z' and item[x+1] == 'e' and item[x+2] == 'r' and item[x+3] == 'o':
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
            elif x+2 <= len(item) and item[x] == 'o' and item[x+1] == 'n' and item[x+2] == 'e':
                last_digit = 1
            elif x+2 <= len(item) and item[x] == 't' and item[x+1] == 'w' and item[x+2] == 'o':
                last_digit = 2
            elif x+4 <= len(item) and item[x] == 't' and item[x+1] == 'h' and item[x+2] == 'r' and item[x+3] == 'e' and item[x+4] == 'e':
                last_digit = 3
            elif x+3 <= len(item) and item[x] == 'f' and item[x+1] == 'o' and item[x+2] == 'u' and item[x+3] == 'r':
                last_digit = 4
            elif x+3 <= len(item) and item[x] == 'f' and item[x+1] == 'i' and item[x+2] == 'v' and item[x+3] == 'e':
                last_digit = 5
            elif x+2 <= len(item) and item[x] == 's' and item[x+1] == 'i' and item[x+2] == 'x':
                last_digit = 6
            elif x+4 <= len(item) and item[x] == 's' and item[x+1] == 'e' and item[x+2] == 'v' and item[x+3] == 'e' and item[x+4] == 'n':
                last_digit = 7
            elif x+4 <= len(item) and item[x] == 'e' and item[x+1] == 'i' and item[x+2] == 'g' and item[x+3] == 'h' and item[x+4] == 't':
                last_digit = 8
            elif x+2 <= len(item) and item[x] == 'n' and item[x+1] == 'i' and item[x+2] == 'n' and item[x+3] == 'e':
                last_digit = 9
            elif x+3 <= len(item) and item[x] == 'z' and item[x+1] == 'e' and item[x+2] == 'r' and item[x+3] == 'o':
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
