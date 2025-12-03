def part_1(content: str):

    password = 0
    dial = 50
    for line in content.splitlines():
        rotation = line[0]
        number = int(line[1:])

        if rotation == 'L':
            dial = (dial - number) % 100
        elif rotation == 'R':
            dial = (dial + number) % 100

        if dial == 0:
            password += 1

    return password


def part_2(content: str):
    
    password = 0
    dial = 50
    for line in content.splitlines():
        rotation = line[0]
        number = int(line[1:])

        password += number // 100

        number %= 100

        if rotation == 'L':
            number *= -1

        old_dial = dial
        dial += number
        if dial == 0:
            if old_dial != 0:
                password += 1
        elif dial < 0:
            if old_dial != 0:
                password += 1
            dial += 100
        elif dial > 99:
            password += 1
            dial -= 100

    return password