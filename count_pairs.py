def count_pairs(numbers=None, target=0):
    numbers = numbers or []
    seen = set()
    result = 0

    for number in range(len(numbers)):
        for num in range(number + 1, len(numbers)):
            pair = tuple(sorted((numbers[number], numbers[num])))
            if numbers[number] + numbers[num] == target and pair not in seen:
                result += 1
                seen.add(pair)
    return result


print(count_pairs([1, 3, 2, 2, 3, 4], 5))
print(count_pairs([1, 1, 1, 1], 2))
print(count_pairs([1, 2, 3, 4, 5], 7))
