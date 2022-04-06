num = int(input("Enter numbers count: "))
nums = []

for i in range(0,num):
    nums.append(int(input("Enter a number: ")))

print("Unsorted List: ",nums)

sort = False

while sort == False:
    num_swap = 0
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            tmp = nums[i-1]
            nums[i-1] = nums[i]
            nums[i] = tmp
            num_swap = num_swap + 1
        #input("ss")

    if num_swap == 0:
        sort = True

print("Sorted List: ",nums)
