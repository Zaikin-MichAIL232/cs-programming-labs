user_input = input()
original_list = list(map(int, user_input.split()))
corrected_list=original_list.copy()
for i in range(len(corrected_list)):
    if corrected_list[i]<0:
        corrected_list[i]=0
print(corrected_list,original_list)
