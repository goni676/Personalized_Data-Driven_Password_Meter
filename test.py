import math
import PESrank
import testpass
import os
import decimal
import PESrank
import os

def main(password, x):
    rank, explain = PESrank.main(password, os.getcwd(), x)
    return rank
#     n=905*(10**6)
#     ex=0
#     indicators = [1,1,0,0,0,0]
#     info_list=[1]
#     feedback1 = "Your password is "
#     feedback2 = ""
#     feedback3 = ""
#     feedback4 = ""
#     feedback5 = ""
#     if rank<0:
#         rank = 70
#         feedback1 = feedback1 + "strong. "
#         feedback2 = "Although your password is strong, don't reuse it on any accounts you care about. Password reuse is very insecure!."
#         indicators[2] = 1
#         info_list.append(2)
#     else:
#         rank = math.log2(rank)
#         if rank<=30:
#             feedback1 = feedback1 + "weak. "
#             ex=1
#         elif (rank)<=50:
#             feedback1 = feedback1 + "sub-optimal. "
#             ex=1
#         else:
#             feedback1 = feedback1 + "strong. "
#             feedback2 = "Although your password is strong, don't reuse it on any accounts you care about. Password reuse is very insecure!."
#             indicators[2] = 1
#             info_list.append(2)
#     if ex==1:
#         indicators[3] = 1
#         info_list.append(3)
#         feedback3 = "Your password is based on the leaked word: '"+str(explain[0][1])+ "' that was used by " \
#                     +str(int(float(explain[0][2])*n))+ " people. "
#         for lst in explain[1:]:
#             if math.ceil(float(lst[1])*n)>=100:
#                 if lst[0]==1:
#                     feedback3 = feedback3 + "It uses a prefix that was used by "\
#                                 +str(math.ceil(float(lst[1])*n))+ " people. "
#                 if lst[0]==3:
#                     feedback3 = feedback3 + "It uses a suffix that was used by "\
#                                 +str(math.ceil(float(lst[1])*n))+ " people. "
#                 if lst[0]==4:
#                     feedback3 = feedback3 + "It uses a capitaliation pattern that was used by "\
#                                 +str(math.ceil(float(lst[1])*n))+ "people. "
#                 if lst[0]==5:
#                     feedback3 = feedback3+"It uses a l33t pattern that was used by "\
#                                 +str(math.ceil(float(lst[1])*n))+ " people. "
# 
#     indicator, s4 = testpass.contains_mutual_substring(password, username)
#     if (indicator):
#         info_list.append(4)
#         indicators[4] = 1
#         feedback4 = feedback4+"The sequence: '" + s4 + "' appears in both your user name and password. " \
#                                      "It's not recommended to use your account information in your password."
#     result = testpass.find_date(password)
#     if result:
#         info_list.append(5)
#         indicators[5] = 1
#         feedback5 = feedback5+"Your password contains the date pattern: '"+result+"'"
# 
#     return rank, feedback1, feedback2, feedback3, feedback4, feedback5, indicators, info_list
# 
# #
def calc(file_name):
    dict_num = {}
    cnt = 0
    with open(file_name, 'r') as file:
        for line in file:
             if cnt < 5913930:
                cnt = cnt + 1
                line = line.strip()
                if line:
                    index = line.rfind(' ')
                    if index == -1:
                        dict_num[""]= float(line)
                    else:
                        dict_num[line[:index]] = float(line[index + 1:])
    print(cnt)
    return dict_num
#
#
def to_file(numbers, index):
    file_name = str(index)+".txt"

    # Open the file for writing
    with open(file_name, "w") as file:
        # Iterate through the array and write each element to a new line
        for element in numbers:
            file.write(str(element) + "\n")

def compute(origin_dict, tweak_dict):
    product = 0
    cnt = 0
    for key in tweak_dict.keys():
        cnt += 1
        if key in origin_dict.keys():
            if 5913920 > cnt:
                if (tweak_dict[key]<1) and (origin_dict[key]<1):
                    dist_diff = tweak_dict[key] - origin_dict[key]
                    print("dist: ", dist_diff, key)
                    if product:
                        product = product*(1-dist_diff)
                    else:
                        product = 1-dist_diff
    print(product)
    return product


# Initialize counter
counter = 1


# Function to split line into key and value
def split_line(line):
    line = line.rstrip()  # Remove trailing newline
    last_space_idx = line.rfind(' ')  # Find the last space, which separates the key and value
    key = line[:last_space_idx]  # All characters before the last space
    value = decimal.Decimal(line[last_space_idx + 1:])  # All characters after the last space
    return key, value


# Load file a into a_dict

if __name__ == '__main__':
    # a_dict = {}
    # with open('a2.txt', 'r') as a_file:
    #     for line in a_file:
    #         key, value = split_line(line)
    #         a_dict[key] = value
    # 
    # keys_found_in_b = set()
    # 
    # 
    # with open('FRANCE_WO_TRAINING2.txt', 'r') as b_file:
    #     for line in b_file:
    #         key, value = split_line(line)
    # 
    #         # If key is in a_dict
    #         if key in a_dict:
    #             counter *= (1 - (value - a_dict[key]))
    #             a_dict[key] = value
    #             keys_found_in_b.add(key)
    #         else:
    #             counter *= (1 - value)
    #             a_dict[key] = value
    # 
    # # If any keys in a_dict weren't found in b, update them
    # for key in a_dict:
    #     if key not in keys_found_in_b:
    #         a_dict[key] *= counter
    # 
    # # Write the results to a1_combined.txt
    # with open('a2_combined_France.txt', 'w') as out_file:
    #     for key, value in a_dict.items():
    #         out_file.write(f"{key} {value}\n")


    #     for key, value in a_dict.items():
    #         out_file.write(f"{key} {value}\n")
    # y = calc("a1.txt")
    # x = calc("FRANCE_WO_TRAINING1.txt")
    # compute(y, x)
    # # to_file(num2, 2)
    # # to_file(num3, 3)
    # # to_file(num4, 4)
    # # to_file(num5, 5)
    # #
    # # sample1 = ESrank.sample(num1, 1.09, 14)
    # # sample2 = ESrank.sample(num2, 1.09, 14)
    # # P = [num2, num1, num3, num4, num5]
    # # ESrank.main1(P, 5, 1.09, 14)
    # 
    # # print(ESrank.sampleMerge(sample1, sample2, 1.09, 14))
    # # main("12345", "gony")
    def to_num(file_name):
        float_numbers = {}
        with open(file_name, 'r') as file:
            for line in file:
                number_str = line.split()[-1]
                float_numbers(decimal.Decimal(number_str))
        float_numbers.sort(reverse=True)
        print(float_numbers)
        return float_numbers

if __name__ == '__main__':

    with open('FRANCE_WO_TRAINING3.txt', 'r') as file:
        lines = file.readlines()

    # Parse the lines into a list of tuples
    data = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            word = parts[0].strip('"')
            value = float(parts[1])
            data.append((word, value))

    # Sort the list of tuples by the second value in each tuple
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)[0:100]
    p = 0
    for item in sorted_data:
        if p:
            p += item[1]
        else:
            p = item[1]
    print(p)
    # Write the sorted data back to a new file
    with open('output3.txt', 'w') as file:
        cnt = 0
        for item in sorted_data:
            if cnt > 1000000:
                break
            file.write(f'{item[0]} {item[1]}\n')
            cnt += 1