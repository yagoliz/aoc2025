def part_1(content: str) -> str:
    joltage = 0
    for line in content.splitlines():
        maxL = 0
        posL = 0
        for i in range(len(line) - 1):
            if int(line[i]) > maxL:
                maxL = int(line[i])
                posL = i

        maxR = 0
        for i in range(posL + 1, len(line)):
            if int(line[i]) > maxR:
                maxR = int(line[i])

        joltage += maxL * 10 + maxR

    return str(joltage)


def find_best_number(numbers: str) -> tuple[int, int]:
    if len(numbers) == 0:
        raise RuntimeError("Empty number list provided")

    maxL = -1
    posL = 0
    for i, char in enumerate(numbers):
        if int(char) > maxL:
            maxL = int(char)
            posL = i

        if maxL == 9:  # Early stopping
            break

    return (maxL, posL)


def part_2(content: str) -> str:
    joltage = 0
    for line in content.splitlines():
        N = len(line)
        line_joltage = 0
        pos = 0
        for i in range(12, 0, -1):
            best_num, new_pos = find_best_number(line[pos : N - i + 1])
            line_joltage = line_joltage * 10 + best_num
            pos += new_pos + 1

        joltage += line_joltage

    return str(joltage)
