list=['Malayalam','Racecar','PHP']
list[0]=list[0].upper()
result=[]
for i in list:
    i_str=str(i)
    reserved_str=''.join(reversed(i_str))
    if i_str== reserved_str:
        result.append(i)
print("Palindrome words are",result)