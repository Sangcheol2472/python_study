# =========================
# 피보나치 수열
# -> 1부터 n까지의 피보나치 수열을 리스트 혈태로 생성하시오.
# 1, 1, 2, 3, 5, 8, 13, ...
# f(1) = 1
# f(X) = f(x2) + f(x1)
# =========================

# %%
# n 입력받기
n = int(input('숫자를 입력하세요: '))

fibo = []

for i in range(0, n):
    k = None
    
    if i < 2:
        k = 1
        
    else:
        k = fibo[i-1] + fibo[i-2]

    fibo.append(k)

print(fibo)
