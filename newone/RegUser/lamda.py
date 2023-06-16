# a  = [x for x in range(1,1001) if x%8 == 0]
# print(a)

# a = [x for x in range(1,1001) if "6" in str(x)]
# print(a)



# string2 = string1.split(" ")
# print(string2)
# lista = [x for x in string1]
# b = ''.join(lista)
# print(b)
#
# list1 = "".join([x for x in string1])
# list2 = "".join([x for x in string1 if x not in ["a","e","i","o","u"]])
# print(list2)
# print(list1)


# lis = ["Pratik", "Ram","amit", "Yash", "Himesh"]
# a = [x for x in lis if len(x) > 4]
# print(a)
# string1 = "Hello  I am Kraken I love to eat humans"
#
# d = {x: len(x) for x in string1.split()}
# # print(d)
#
# l = [x for x in string1.split() if "k" not in x]
# # print(l)
#
# k = [x for x in string1.split() if len(x) < 5]
# # print(k)
#
#
# p = [n for n in range(1,10)]
# print(p)

# lp = [x for x in range(1,1001) if x%7 == 0]
# print(lp)
#
# ku = [x for x in range(1,1001) if "3" in str(x)]
# print(ku)
#
# bankai = "bankai katen kyokotsu karamatsu shinju"
# po = len([x for x in bankai if x == " "])
# print(po)

# d = "Yellow yalks like yelling and yawning and yesterday they yoddled  while eating yuky yams"
# lk= [x for x in d if x in  ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]]
# print(lk)

# nums  = range(1, 1001)
# q8_answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
# print(q8_answer)


# a=["hi", 4, 8.99, "apple" ,('t,b','n')]
# z = [(x, a.index(x)) for x in a]
# print(z)

# a = [1,2,3,4]
# b = [2,3,4,5]
# c = []
# for x in a:
#     for y in b:
#         if x == y:
#             print(x)


# li = [x for x in a for y in b if x == y]
# print(li)


# li = [x for x in stringo.split() if x.isdecimal()]   #iterable.isdecimal() returns the actual digit, remember you are an idiot
# print(li)

# li = [ x for x in range(1, 21) if x%2 == 0 ]
# print(li)
#
# li = range(1,21)
# for x in li:
#     if x%2 == 0:
#         print("even")
#     else:
#         print("odd")

# l1=['even' if i%2==0 else 'odd' for i in range(1,21)]
# print(l1)

# a = [1,2,3,4,5,6,7,8,9]
# b = [2,7,1,12]
# ls = [(x,y) for x in a for y in b if x==y]
# print(ls)



# stringo = "In 1984 there were 13 instances of a protest with over 1000 people attending"
# li = [x for x in stringo.split() if len(x)< 4]
# print(li)

#
li = [(x, y) for x in range(1,101) for y in range(9, 2, -1) if x % y == 0 ]
print(li)

ll = [1, 2, 3, 4, 5, 6]
a = max(ll)
print(a)

# for x in range(1,1001):
#
#     for y in range(9,2,-1):
#         if x%y == 0:
#             print(x,y)
#             break
#

