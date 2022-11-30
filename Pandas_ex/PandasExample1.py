import pandas as pd

df3 = pd.read_excel('김병진 성별 추가.xlsx', engine='openpyxl', sheet_name='3월')
df11 = pd.read_excel('김병진 성별 추가.xlsx', engine='openpyxl', sheet_name='수능')
df3 = df3.replace('확를과통계')
df11 = df11.replace('확를과통계')
#print(df11)
#print(df11.columns)
#print()

final_df = pd.ExcelWriter('준희센빠이.xlsx', engine='xlsxwriter')

one_sample_t_test_df = pd.DataFrame()
two_sample_t_test_df = pd.DataFrame()
anova_test_df = pd.DataFrame()
chi_square_test_df = pd.DataFrame()
regression_test_df = pd.DataFrame()



# one_sample_t_test
#print(df11[(df11['선택 과목']=='화법과작문')]['등급'])
talkdf = list(df11[(df11['선택 과목']=='화법과작문')]['등급'])
langdf = list(df11[(df11['선택 과목']=='언어와매체')]['등급'])
probdf = list(df11[(df11['선택 과목.1']=='확률과통계')]['등급.1'])
calcdf = list(df11[(df11['선택 과목.1']=='미적분')]['등급.1'])
geomdf = list(df11[(df11['선택 과목.1']=='기하')]['등급.1'])
engdf = list(df11['등급.2'])
hisdf = list(df11['등급.3'])

name_list = ['화법과작문', '언어와매체', '확률과통계', '미적분', '기하', '영어', '한국사']
subject_list = [talkdf, langdf, probdf, calcdf, geomdf, engdf, hisdf]
for i in range(len(name_list)):
    one_sample_t_test_df[name_list[i]] = pd.Series(subject_list[i])
#print(one_sample_t_test_df)
print(df11[(df11['등급']==1) & (df11['등급.1']==1)])

# two_sample_t_test


# anova_test
#print(df11['선택\n과목'].unique())
#print()
#print(df11['선택\n과목.1'].unique())


# chi_squre_test
sexdf = list(df11['성별'])
mathdf = list(df11['선택 과목.1'])
for i in range(len(mathdf)):
    if mathdf[i] == '미적분':
        mathdf[i] = 1
    if mathdf[i] == '기하':
        mathdf[i] = 2
    if mathdf[i] == '확률과통계':
        mathdf[i] = 3
name_list = ['성별', '수학선택과목']
input_list = [sexdf, mathdf]
for i in range(len(name_list)):
    chi_square_test_df[name_list[i]] = pd.Series(input_list[i])
#print(chi_square_test_df)


# regression_test