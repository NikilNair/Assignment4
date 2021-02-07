def get_avg(arr):
	total = 0
	if len(arr) == 0:
		return 0
	else:
		for i in arr:
			total += i
		return total/len(arr)



# print(f"The average of the [1,2,3,4,5] array is {get_avg([])}")


# x = input("Please enter a series of numbers and the program will calculate the average: Numbers must be seperated by a space: ")
# y = []
# avg = 0
#
# for i in x:
# 	if i != " ":
# 		y.append(int(i))
#
# for i in y:
# 	avg += i
# avg = avg / (len(y))
#
# print(f"The average of this series of numbers is {avg}")
