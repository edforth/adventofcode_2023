def part1(inputfile):
    answer = 0
    with open(inputfile,'r') as f:
        lines = f.read().split("\n")
    print(lines)
    for item in lines:
        print(item)
    return str(answer)

def part2(inputfile):
    answer = 0
    with open(inputfile,'r') as f:
        lines = f.read().split("\n")
    #print(lines)
    for item in lines:
        #print(item)
    return answer

print("Part 1 test case 1 answer = ", part1('day00input-testcase1.txt'))
print("Part 1 answer = ", part1('day00input.txt'))
#Did I get it first try? What did I change?
print("Part 2 test case 1 answer = ", part2('day00input-part2-testcase1.txt'))
print("Part 2 answer = ", part2('day00input.txt'))
#Did I get it first try? What did I change?
