
import pandas as pd

df = pd.read_csv('초등학교.csv', encoding='euc-kr')
df.to_excel('전체.xlsx', index=False)

# df['학교명'].to_excel('학교명.xlsx', index=False)
# print(df)


# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_excel('실습.xlsx')
# print(df.head(1))
# print('\n')
# print(df.tail(1))
# print('\n')
# print(df.info())
# print('\n')
# print(df['이름'])
# print('\n')
# print(df[['이름','나이']])
# print('\n')
# print(df[0:2])
# print('\n')
# print(df['이름'][0:2])
# print('\n')
# print(df.loc[2])
# print('\n')
# print(df.loc[0:2]['이름'])
# print('\n')
# print(df.iloc[0,0])
# print('\n')
# print(df["성적"] >=2)
# print('\n')
# print(df[df['성적'] >=2])
# print('\n')
# df1 =df[(df['성적'] >=2) & (df['성적'] >= 3)]
# print(df1)
# print('\n')
# print('\n')
# print('\n')
# print('\n')

# # df1 = df.query("성적 >= 2")
# # print(df1)

# # df1 = df[(df["국어"] >= 80) & (df["수학"] >= 85)]
# # print(df1)

# df1 = df.query("국어 >= 80 and 수학 >= 85")
# print(df1)

# df.sort_values(by=["이름"], ascending= False, inplace=True)
# # //acending 은 디폴트는 오름 차순
# # 정렬을 실제 그 값으로 바꿔라 inplace
# df.reset_index(drop=True, inplace=True)
# print(df)


# print(df.index)
# print(list(df.index))
# print(df.columns)
# print(df.size)

# print(df.describe())

# print(df["반"].value_counts())
# print(df["수학"].sum())
# print(df["수학"].mean())
# # print(df.groupby("반").mean())
# print(df.isna().sum())

# print(df.fillna({"확인여부":"미확인"}))
# print(df.fillna(0))
# print(df)

# df.dropna
# # 샥제 할거다 NA를
# df.dropna(subset=["국어"]) 
# # 샥제 할거다 무엇을

# df["총점"] = df["국어"] + df["수학"]
# print(df)
# # 새로운 컬럼으로 생성

# # print(df.drop("반", axis=0))

# print(df.replace(81, 88))
# print(df.replace({81:88, 90:1}))
# # print(df.replace({"수학":{81:88}, 90:1}))


# # 데이터 프레임 생성 후 데이터프레임의 정보출력
# # 대표 국적별이 영화를 편수를 집계
# # 대표국적이 영국인 데이터 출력
# # 대표국적별 최상위 순위를 출력

# df = pd.read_excel('data3.xlsx')

# plt.plot(df['kor'],'k--',marker='o')
# # k검정 b 파랑 r 빨강 g(녹색)
# # 선스타일 기호 -실선 --파선 :점선 -.파선점선 합친거
# # 마커기호 .점 ^ 삼각형 v역삼각형 s 정사각형 *별표 +더하기

# plt.show()
# # 1번 그림

# plt.plot(df['math'], 'b-', marker='^', label='수학')
# plt.legend
# plt.show()
# # 2번 그림

# x = [1,3,1,4,2,6]
# y = [5,4,2,9,9,6]
# plt.scatter(x,y)
# # 점을 찍어서 산점도를 할꺼냐라는데
# # 점으로 나타내는애임
# plt.show()
# # 3번 그림
# x= ['A','B','C']
# y = [5,4,2]
# plt.bar(x,y)
# plt.show()
# # 4번 그림


# plt.scatter(df['kor'],df['kor'], c='r', marker='o', label='국어')
# plt.scatter(df['math'],df['math'], c='b', marker='o', label='수학')
# plt.legend
# plt.show()
# # 5번 그림

# x = [1,1,2,3,2,2,4,1]
# plt.hist(x, bins = 4, color = "red", align= "left")
# plt.show()
# # 6번 그림
# # x에 대해서 몇개의 값으로 나눌것이냐 

# x= ['A', 'B', 'C']
# y= [90,80,100]
# plt.bar(x,y)
# plt.title('Test Graph')
# plt.xlabel('Group')
# plt.ylabel('Score')
# plt.show()
# # 7번 그림

# x= [1,2,3,4,5]
# y= [2,3,8,4,1]
# fig, axs = plt.subplots(2,3, figsize=(50,50))
# # figsize는 창 사이즈여
# # 앞에 flg언페킹이라고 함 두개로 저장되고 있으니까 앞에는 타이틀이 저장될겨
# # 앞은 행에 개수 뒤는 열의 개수
# axs[0,0].plot(x,y)
# axs[0,1].scatter(x,y)
# axs[1,0].bar(x,y)
# axs[1,1].barh(x,y)
# # 이거는 바를 수평으로 저장할거임
# axs[0,2].hist(x, bins = 4, color = "blue", align= "left")
# axs[1, 2].boxplot(y)
# fig.suptitle('Sub Graph')
# plt.show()
# # 8번 그림


# # seaborm 엑셀을 더 전문적으로 분석할 수 있는 라이브러리





# 3단원 연습하기
# import pandas as pd

# df = pd.read_excel('실습.xlsx')

# print(df)
# print("---------")
# print(df.iloc[2,3])
# print("---------")
# print(df.loc[2]['이름'])
# print("---------")
# print(df.loc[0:2]['나이'])
# print("---------")
# print(df['이름'][0:2])
# # 부터 -1까지
# print("--ㅇㅇㅇㅇ-----")
# print(df.head(2))
# print("---------")
# print(df.tail(2))
# print("---------")
# # print(df[['이름'],['나이']])
# # 대괄호를 조심하자
# print(df[['나이','이름']][1:3])
# print("---------")
# print(df.iloc[1,3])
# print("---------")
# # df = pd.DataFrame(['조영무',23,11],['애송',24,22])
# # print(df)
# # 겉 괄호를 안하면 이건 데이터 프레임이 아니다.
# df = pd.DataFrame([['조영무',23,11],['애송',24,22]])
# print(df)
# print("---------")
# # 딕션어리로 할 때는 {} 박고 시작해라 모두를 감싸 줄 것.
# df = pd.DataFrame({'이름' : ['조영무','애송'],'나이' : [23,24]})
# print(df)

# print("---------")
# df = pd.read_excel('실습.xlsx')
# print(df)
# print("---------")
# print(df["성적"]>= 85)
# print("-----참거짓 말고 하려면 df[df[]]----")
# print(df[df["성적"] > 2])
# print("---------")
# df1 =df[(df['성적'] >=2) & (df['성적'] >= 1)]
# print(df[(df['성적'] > 1) & (df['성적'] >=2)])
# print("----df[  (   df[] >1  )     (   df[]   > 1)      ]----")
# df1 = df.query("성적 >= 2")
# print(df1)
# df1 = df.query("국어 >= 80 and 수학 >= 85")
# print(df1)
# print("----정렬 방법은 두가지 인것임-----")
# df.sort_values(by=["이름"], ascending= False, inplace=True)
# print(df)
# # 행 번호도 바꿀때는 아래거
# df.reset_index(drop=True, inplace=True)
# print(df)
# print("---정령 하나 더 추가 뭔가 정력 관련 필기가 있어야할듯------")
# print("---------")
# print(df.index)
# # 인덱스 정보만 나오는 중
# print("---------")
# print(list(df.index))
# # 인덱스 값들 0번 1 번 2번 출력 해줌
# print("---------")
# print(df.columns)
# print("---------")
# print(df.size)
# print("---------")

# print(df.describe())
# # //기본 통계 값
# print("<----기본 통계 값---->")
# print(df.isna())
# print("<----공백인 데이터---->")
# print(df.isna().sum())
# print("<----없는 값 반환---->")
# # // 없는값 반환
# print(df.fillna({"확인여부":"미확인"}))
# print("<----특정  nan컬럼 인 컬럼---->")
# print(df.fillna(0))
# print("<----특정 행 nan자동 채움---->")

# df.dropna
# print(df)
# # 샥제 할거다 NA를
# print("<----NA를 삭제할 것 이다.---->")
# df.dropna(subset=["국어"]) 
# print(df)
# print("<----무엇을 삭제할 것이다.---->")
# # 샥제 할거다 무엇을

# df["총점"] = df["국어"] + df["수학"]
# print(df)
# print("<----새로운 컬럼 생성---->")
# # 새로운 컬럼으로 생성


# print(df.replace(81, 88))
# print("<----무엇을 무엇으로 바꿀거다---->")
# print(df.replace({81:88, 90:1}))
# print("<----2개이상 일때는 이렇게---->")
# print(df.replace({"수학":{81:88, 90:1}}))
# print("<----특정 열에서 만 바꿀때---->")






# # 1단원 연습하기
# import numpy as np

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr[0,3])
# # 부터 까지 임
# print("----ㅇㅇ-----")
# print(arr[arr > 5])
# print("----------")
# print(arr[1:])
# print(arr.flatten())
# print("----------")
# print(arr.transpose())
# print("----------")
# arr = np.random.randint(15 , size = 3)
# # 공식 확인
# print(arr)
# print("----------")
# print(arr.min())
# print("----------")
# print(arr.var())
# print("----------")
# print(arr.std())
# print("----------")
# # arr를 새로 선언 할때는 함수에 arr를 삽입 / 아니면 그냥 arr를 메서드 호출 하기
# arr = np.var(arr)
# print(arr)
# print("----------")
# arr = np.std(arr)
# print(arr)
# print("----------")
# print("----------")




# # 2단원 공부
# print("----------")
# import pandas as pd

# x = pd.Series([1,2,3], index = ['a','b','c'])
# y = pd.Series([4,5,6], index = ['a','d','e'])
# print(x)
# print("----------")
# print(x / y)
# print("----------")
# print(x[['a','c']])
# print("----------")
# print(x[[0]])
# print("----------")
# print(y.index)
# print("----------")
# print(x.info())
# print("----------")
# print(y.values)
# print("----------")
# a = [1,2,3,4,5,5,5,5,5,5]
# x = pd.Series(a)
# print(x.unique())
# print("----------")
# print(pd.unique(x))
# print("----------")
# print("----------")
# print("----------")
# print("----------")
# print("----------")
# print("----------")







