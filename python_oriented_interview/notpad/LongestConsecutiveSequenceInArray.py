class LongestConsecutiveSequenceInArray:
    arr = [100, 4, 200, 1, 3, 2]
    num_set=set(arr)
    longest=0
    longest_arr=[]
    for num in arr:
        if num-1 not in num_set:
            current=num
            current_arr=[current]
            
            while current+1 in num_set:
                current+=num
                current_arr.append(current)
                
            if len(current_arr)>longest:
                longest=len(current_arr)
                longest_arr = current_arr
    print(longest)
    print(longest_arr)
	