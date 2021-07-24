def solution(id_list):

    # Initiate unique Id
    unique_id = 0

    # XOR for every id in id list
    for i in id_list:

        # XOR operation
        unique_id ^= i

    return unique_id


# only one guaranteed unique
print(solution([1, 2, 3, 2, 3]))
