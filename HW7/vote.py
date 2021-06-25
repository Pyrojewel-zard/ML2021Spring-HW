import pandas as pd
from scipy import stats
 
file1 = pd.read_csv('./result (16).csv')
file2 = pd.read_csv('./result (17).csv')

print(file1[0])
# ans = []
# for i in range(len(file1['ID'])):
#   nums = []
#   nums.append(file1['ID'][i])
#   nums.append(file2['ID'][i])
#   ans.append(stats.mode(nums)[0][0])
# print(len(ans))

# with open('result_final.csv', 'w') as f:
#     f.write('ID,Answer\n')
#     for i, y in enumerate(ans):
#         f.write('{},{}\n'.format(i, y))