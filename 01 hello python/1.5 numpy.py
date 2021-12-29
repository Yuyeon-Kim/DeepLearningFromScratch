# 211228 넘파이 예제 코드 실습

# 1.5.1 넘파이 가져오기
import numpy as np

# 1.5.2 넘파이 배열 생성하기
x = np.array([1.0, 2.0, 3.0])
print(x)
# [1. 2. 3.]
type(x)
# <class 'numpy.ndarray'>

# 1.5.3 넘파이의 산술 연산
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y)# 원소별 덧셈
# [3., 6., 9.]
print(x - y)
# [-1., -2., -3.])
print(x * y)# 원소별 곱셈
# [ 2.,  8., 18.]
print(x / y)
# [0.5, 0.5, 0.5]
print(x / 2.0)
# [0.5, 1. , 1.5]

# 1.5.4 넘파이의 N차원 배열
A = np.array([[1, 2], [3, 4]])
print(A)
# [[1 2]
#  [3 4]]
A.shape
# (2, 2)
A.dtype
# dtype('int32')

B = np.array([[3, 0], [0, 6]])
A + B
# array([[ 4,  2],
#        [ 3, 10]])
A * B
# array([[ 3,  0],
#        [ 0, 24]])
A * 10
# array([[10, 20],
    #    [30, 40]])

# 1.5.5 브로드캐스트
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
A * B
# array([[10, 40],
#        [30, 80]])

# 1.5.6 원소 접근
# 원소 인덱스로 접근
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
# [[51 55]
#  [14 19]
#  [ 0  4]]
X[0] # 0행
# array([51, 55])
X[0][1] # (0,1) 위치의 원소
# 55

# for문으로 접근
for row in X:
     print(row)
# [51 55]
# [14 19]
# [0 4]

# 인덱스 배열로 접근
X = X.flatten() # X를 1차원 배열로 변환(평탄화)
print(X)
# [51 55 14 19  0  4]
X[np.array([0, 2, 4])] # 인덱스가 0, 2, 4인 원소 얻기
# array([51, 14,  0])

# 특정 조건 만족하는 원소만 얻기
X > 15
# array([ True,  True, False,  True, False, False])
X[X>15]
# array([51, 55, 19])