# def twosum(nums, targate):
#     count=0
#     for i in range(len(nums)):
#         for j in range(len(nums)-1):
#             if nums[i]+nums[j]==targate:
#                 # count +=1
#                 return [i,j]

def twosum(nums, targate):
    pair = {}
    for i in range(0,len(nums)):
        compliments = targate-nums[i]#
        if compliments in pair:
            return [pair[compliments], i]
        pair[nums[i]]=i

nums = [12,3,14,7,4,18]
targate = 32 
print(twosum(nums, targate))