nums = []

num = 1

while num !=0:
	num+=1
	print(num)
	nums.append(num)
	if num == 1000:
		break
file = open("numeros.txt","w")

file.write(str(nums))
file.close()