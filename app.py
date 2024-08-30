numbers = [3, 5, -4, 8, 11, 1, -1, 6]
target_num = 10


def two_number_sum(nums, target):
    for i in range(len(nums) - 1):
        x = nums[i]
        for j in range(i + 1, len(nums)):
            y = nums[j]
            added_numbers = x + y
            if target == added_numbers:
                return [x, y]
    return []


def two_num_sum(num, target):
    table = {}
    for num in numbers:
        y = target_num - num
        if y in table:
            return [y, num]
        else:
            table[num] = True

    return []


def is_valid_subsequence(sequence, sub_sequence):
    sub_idx = 0
    for item in sequence:
        if item == sub_sequence[sub_idx]:
            sub_idx += 1
            if sub_idx == len(sub_sequence):
                return True

    return False


output = []


def sorted_square_array(lst_of_nums):
    for value in lst_of_nums:
        output.append(value ** 2)
    output.sort()
    return output


seq = [5, 6, 7, 8]
sub_seq = [5, 5, 7, 8]
listing = [3, 5, 2, 9, 5, 1, 7]
result = two_number_sum(numbers, target_num)
is_valid = is_valid_subsequence(seq, sub_seq)
squares_list = sorted_square_array(listing)
print(squares_list)