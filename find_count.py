def find_freq(nums, target):
    """Find the number of `target`s in `nums`
    """
    # find the first occurance
    # find target-1 (number before target)
    first_index = None
    prev_index = find_occu(nums, target - 1)
    # look for target after it
    for i in range(prev_index, len(nums)):
        if nums[i] == target:
            first_index = i
            break
    
    # find the last occurance
    # find target+1 (number after target)
    last_index = None
    next_index = find_occu(nums, target + 1)
    # look for target before it
    for i in range(next_index, 0, -1):
        if nums[i] == target:
            last_index = i
            break

    if first_index == None or last_index == None:
        return None

    return last_index - first_index + 1

def find_occu(nums, target):
    """Find the index of `target` in `nums` using binary search
    """
    start = 0
    end = len(nums)-1
    # until there is only item left
    while end-start > 0:
        mid = (start+end)//2
        # adjust scope or return
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
    # if there is only one item left
    # it is target or very close to it
    return start

if __name__ == '__main__':
    print('yes')
    test_list = [1,2,2,3,4,5,5,6,7,8,8,8,8,8,8,8,8,8,10,11,12,12,13,13,13,13,14,15]
    assert find_freq(test_list, 9) == None
    assert find_freq(test_list, 8) == 9
    assert find_freq(test_list, 7) == 1