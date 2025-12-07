
from functools import reduce
from operator import mul, add
import re

def parse_operations(content: str) -> (list[list[int]], list[str]):
    data, ops = [], []
    lines = content.splitlines()
    for line in lines[0:-1]:
        line = re.sub(' +', ' ', line)
        line = line.strip()
        data.append([int(string) for string in line.split(' ')])

    ops = lines[-1]
    ops = re.sub(' +', ' ', ops)
    ops = ops.strip()
    ops = [op for op in ops.split(' ')]

    return data, ops


def part_1(content: str) -> str:
    data, operations = parse_operations(content)

    m, n = len(data), len(data[0])

    total = [0] * n
    for j in range(n):
        if operations[j] == '*':
            op = mul
        else:
            op = add

        total[j] = reduce(op, [data[i][j] for i in range(m)])


    return str(sum(total))


def parse_operations_alt(content: str) -> list[int]:
    lines = content.splitlines()
    numbers = lines[:-1]
    ops = lines[-1]

    nelems = len(re.sub(' +', ' ', ops).strip().split(' '))
    total_sum = [0] * nelems

    height = len(numbers)
    width = len(ops)
    i, idx = 0, 0
    while i < len(ops):
        if ops[i] != ' ':
            if ops[i] == '+':
                op = add
            else:
                op = mul

            k = i+1
            while k < width and ops[k] == ' ':
                k += 1

        group = []
        for number in numbers:
            if k < width:
                group.append(number[i:k-1])
            else:
                group.append(number[i:])

        
        nums = max([len(num) for num in group])
        group_total = [0] * nums
        for j in range(nums):
            for m in range(height):
                if group[m][j] != ' ':
                        group_total[j] = group_total[j] * 10 + int(group[m][j])

        total_sum[idx] = reduce(op, group_total)

        i = k
        idx += 1
            
    return total_sum


def part_2(content: str) -> str:
    total = parse_operations_alt(content)
    return str(sum(total))

