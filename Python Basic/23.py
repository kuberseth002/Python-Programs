# number divisble by another number
my_list = [12, 65, 54, 39, 102, 339, 221,]

result=list(filter(lambda x:(x%13==0 ),my_list))
print(result)