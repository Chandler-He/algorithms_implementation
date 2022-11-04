class Solution():
	def max_sum(self, a):
		n = len(a)
		maxSum = -2*10**5
		#def  max sum is the least num.
		if a == []:
			return 0
		# if the array is none, return 0, won't trigger index out of range.
		for i in range(0, n):
			currSum = 0
			for j in range(i, n):
				currSum = currSum + a[j]
				if(currSum > maxSum):
					maxSum = currSum
		return maxSum
	

	def print_subarray(self, arr):
    		
		if arr == [] or arr == 0:
			return arr
		#judge if the arr is none or 0

		# stores the max sum sublist
		curr_max = -2*10**5

		# stores the maximum sum of sublist ending at the current position
		end_max = 0

		# stores endpoints of maximum sum sublist currently.
		start = 0
		end = 0

		# stores starting index of a non-nrgative sum sequence
		idx = 0

		# traverse the given list
		for i in range(len(arr)):
			
			end_max += arr[i]
            # update the maximum sum of sublist 'ending' at index 'i'
			
			if end_max < arr[i]:
				end_max = arr[i]
				idx = i
				# if the maximum sum becomes less than the current element, start from the current element
			
			elif curr_max < end_max:
				curr_max = end_max
				start = idx
				end = i
              # update result if the current sublist sum is found to be greater
		print(arr[start: end + 1])
		

		
res = Solution()

arr1 = []
arr2 = [1]
arr3 = [1, 2, 3, 4]
arr4 = [-2,-4,-7,-8]
arr5 = [-2, 3, 5, -7]
arr6 = [-2, -3, 4, -1, -2, 1, 5, -3]
arr7 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


print("*"*50)
print("test case 1")
print("the subarray is:")
subarray = res.print_subarray(arr1)
max_sum = res.max_sum(arr1)
print("the max sum is: ", max_sum)

print("*"*50)
print("test case 2")
print("the subarray is:")
subarray = res.print_subarray(arr2)
max_sum = res.max_sum(arr2)
print("the max sum is: ", max_sum)

print("*"*50)
print("test case 3")
print("the subarray is:")
subarray = res.print_subarray(arr3)
max_sum = res.max_sum(arr3)
print("the max sum is: ", max_sum)

print("*"*50)
print("test case 4")
print("the subarray is:")
subarray = res.print_subarray(arr4)
max_sum = res.max_sum(arr4)
print("the max sum is: ", max_sum)

print("*"*50)
print("test case 5")
print("the subarray is:")
subarray = res.print_subarray(arr5)
max_sum = res.max_sum(arr5)
print("the max sum is: ", max_sum)

print("*"*50)
print("test case 6")
print("the subarray is:")
subarray = res.print_subarray(arr6)
max_sum = res.max_sum(arr6)
print("the max sum is: ", max_sum)

print("*"*50)
print("test case 7")
print("the subarray is:")
subarray = res.print_subarray(arr7)
max_sum = res.max_sum(arr7)
print("the max sum is: ", max_sum)
