def two_sum_multiply(nums, target):
	nums_visited = set()

	for num in nums:
		second_num = target - num
		if second_num in nums_visited:
			ans = num * second_num
			return ans
		else:
			if num not in nums_visited:
				nums_visited.add(num)
			continue


	return -1

# print(two_sum_multiply([1721,979,366,299,675,1456], 2020))

list_of_nums = []
f = open('input.txt', 'r')
for num in f:
	list_of_nums.append(int(num.strip()))

# print(list_of_nums)	

print(two_sum_multiply(list_of_nums, 2020))