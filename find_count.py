def find_freq(nums, target):
    """Find the number of `target`s in `nums`
    """
    # find the first occurance
    first_index = None
    start = 0
    end = len(nums)-1
    # until there is only item left
    while end > start:
        mid = (start+end)//2
        # adjust scope
        # if lower, increase start
        if nums[mid] < target:
            start = mid + 1
        # if target or higher, decrease end
        elif nums[mid] > target:
            end = mid - 1
        else:
            end = mid
    if nums[start] == target:
        first_index = start
    
    # find the last occurance
    last_index = None
    start = 0
    end = len(nums)-1
    # until there is only item left
    while end > start:
        mid = (start+end)//2
        # adjust scope
        # if higher, decrease end
        if nums[mid] > target:
            end = mid - 1
        # if target or lower, increase start
        elif nums[mid] < target:
            start = mid + 1
        else:
            start  = mid
    if nums[start] == target:
        last_index = start

    if first_index == None or last_index == None:
        return None

    return last_index - first_index + 1


if __name__ == '__main__':
    test_list = [1,2,2,3,4,5,5,6,7,8,8,8,8,8,8,8,8,8,10,11,12,12,13,13,13,13,14,15]
    assert find_freq(test_list, 9) == None
    assert find_freq(test_list, 8) == 9
    assert find_freq(test_list, 7) == 1