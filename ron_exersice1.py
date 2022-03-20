#1
# for i in range(5):
#     print("i love python")

#2
# numbers = []
# for i in range(11):
#     numbers.append(i)
# print(numbers)

#3
# numbers = []
# for i in range(10):
#     num = int(input("enter number :"))
#     numbers.append(num)
# print(sorted(numbers))

#4
# module3 = 0
# count = 0
# numbers = []
# bigger10 = 0
# lower10 = 0
# for i in range(11):
#     num = int(input("enter number : "))
#     numbers.append(num)
#     count += num
# dividedby11 = []
# for i in numbers:
#     x=i/11
#     dividedby11.append(x)
#     if i > 10:
#         bigger10 +=1
#     if i < 10:
#         lower10 +=1
#     if i%2==0:
#         print("thos numbers are even :",i)
#     if i%3==0:
#         module3+=1
# print("how much bigger then 10:", bigger10,"how much lower then 10 :",lower10)
# print("numbers divided by 11 :",dividedby11)
# print("this is the sum of the numbers :",count)
# print(module3)

#5
# nums = []
# for i in range(3):
#     nums.append(int(input("enter number:")))
# nums.insert(0,3)
# nums.insert(1,int(input("enter number :")))
# nums.insert(2,nums[0]+nums[1])
# nums.insert(3,nums[0]*nums[1]*nums[2])
# print(nums)
# print(sorted(nums,reverse=True))

#6
# grades1 = []
# grades2 = []
# Overlapping_grades = 0
# for i in range(10):
#  grades1.append(int(input("enter grades1:")))
#  grades2.append(int(input("enter grades2: ")))
# for i in grades1:
#     for j in grades2:
#         if i == j:
#             Overlapping_grades +=1
#
# animal = input("choose animal")
# print(len(animal))
# print("GRADE 1 : ",grades1, "\n ","GRADE2 ",grades2)
# print("Overlapping grades :", Overlapping_grades)


#7
# sum_lane = 0
# shvil_israel = []
# for i in range(20):
#     part = input("what is the name of the part : ?")
#     lane = int(input("how much kilometer the lane : "))
#     shvil_israel.append(part)
#     sum_lane+=lane
# print("those are the roads :",shvil_israel,"\n the total lane of the aroad is : ",sum_lane)


#8
# total = []
# customer = []
# boxes = []
# bigger_then20 = 0
# box = 35
# order = 10
# y=0
# x=0
# for i in range(2):
#     name = input("what is your name :")
#     amount_box = int(input("how many boxes you need : "))
#     customer.append(name)
#     boxes.append(amount_box)
# for i in boxes:
#     if i > 20:
#         bigger_then20 += 1
#     if i < 4:
#         x = box * i+order
#         total.append(x)
#     else:
#        y =box*i
#        total.append(y)
# print("name of customer : ",customer,"\n the total price is : ",total)
# print("the orders that bigger then 20 :",bigger_then20)


#9
# kids = [ ]
# last_name = []
# total_kids = 0
# for i in range(2):
#     last_name.append(input("what is your last name?: "))
#     kids.append(int(input("how many kids you got?:")))
# for i in kids:
#     total_kids += i
#     if i > 3:
#         print("discount")
# print(last_name,"\n",kids)
# print("this is the total kids :",total_kids)

# 10
# name = []
# born = []
# blood_type = []
# type_0 = 0
# for i in range(2):
#     name.append(input("what is your name ? : "))
#     born.append(int(input("what is year of born ? : ")))
#     blood_type.append(input("what is your blood type ? : "))
# for i in blood_type:
#     if i == "o":
#         type_0+=1
# print(name ,"\n",born,"\n",blood_type,"\n","with type o -",type_0)












