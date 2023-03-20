
def match_indices(string):
  
    if '0' in string:
        return False
    # 2
    if string[1] != '2' and string[3] != '2' and string[4] != '2' and string[5] != '2' and string[7] != '2' and string[5] != '1' and string[7] != '1' and string[4] != '3' and string[5] != '3' and string[1] != '4' and string[8] != '4' and string[2] != '5' and string[8] != '5' and string[5] != '1' and string[2] != '6' and string[8] != '7' and string[9] != '7' and string[0] != '1' and string[1] != '8'and string[8] != '8' and  string[4] != '9':
            flag = True    
    
            
    else:
        flag = False
        
    return flag
    
input_string = "4375563546"
result = match_indices(input_string)
print(result)

    
# indices = [i for i, x in enumerate(numb) if x == "2"]
# print(indices)
stringsss = """

"""

# Splitting the string on newline character
list_of_strings = stringsss.split('\n')
list_of_strings = list(filter(None, list_of_strings))


for ele in list_of_strings:
    total = 0
    for i in ele:
        str_number = str(''.join(filter(str.isdigit,ele)))
        if i == "":
            continue
        if i.isdigit():
            total  += int(i)
            
    print(str_number , ":::::::"  , total  , "::::" ,match_indices(str_number)) 
# Printing the final list

print(list_of_strings)



def reduce_digits(s):
    result = []
    for i in range(len(s)-1):
        # sum up adjacent pairs of digits
        sum_digit = int(s[i]) + int(s[i+1])
        # reduce the sum to a single digit
        if sum_digit > 9:
            sum_digit = sum(map(int, str(sum_digit)))
        result.append(sum_digit)
        a = ''.join(map(str, result))
    return a
    
    
input_str = ''
res = []
for i in range(len(input_str)-1): 
    output_str = reduce_digits(input_str)
    res.append(output_str)
    input_str = output_str
print(res)  # prints '654693233'
