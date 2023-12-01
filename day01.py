def part1(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().split("\n\n")
    #print(lines)
    return str(answer)

def part2(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().split("\n\n")
    #print(lines)
    return answer

print("Part 1 test case 1 answer = ", part1('day01input-testcase1.txt'))
print("Part 1 answer = ", part1('day01input.txt'))
#Correct on first attempt!   67016
print("Part 2 test case 1 answer = ", part2('day01input-testcase1.txt'))
print("Part 2 answer = ", part2('day01input.txt'))
