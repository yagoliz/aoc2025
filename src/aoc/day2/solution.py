def is_invalid(num: str) -> bool:
    n = len(num)

    # Odd lengths cannot be invalid
    if n % 2 != 0:
        return False
    
    # We can compare both sides
    return num[:n//2] == num[n//2:]


def part_1(content: str) -> str:
    count = 0
    for ids in content.split(","):
        left, right = ids.split("-")

        for num in range(int(left), int(right)+1):
            if is_invalid(str(num)):
                count += num

    return str(count)


def is_invalid_seq(num: str) -> bool:
    n = len(num)

    for sublen in range(1, n//2 + 1):
        # If n is not a multiple of n, for sure it's invalid
        if n % sublen != 0:
            continue

        pattern = num[:sublen]
        equal = True
        for start in range(1,n//sublen):
            if pattern != num[start*sublen:sublen*(start+1)]:
                equal = False
                break
        
        if equal:
            return True

    return False


def part_2(content: str) -> str:
    count = 0
    for ids in content.split(","):
        left, right = ids.split("-")

        for num in range(int(left), int(right)+1):
            if is_invalid_seq(str(num)):
                count += num

    return str(count)