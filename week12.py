# prime number (소수)
# 1보다 큰 자연수 중 1과 자기 자신 외에는 나누어 떨어 지지 않는 수

is_prime = True
number = int(input("Input number : "))

if number <= 1:
    is_prime = False

for i in range(2, number+1):  # 1부터 입력한 수까지 반복
    if number % i == 0:  # 입력한 수를 1부터 입력된 수까지 나누어 떨어지는지 조건문으로 체크
        is_prime = False  # 약수 발견 시 is_prime 변경
    print(i, end=' ')

if is_prime:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number! (divisors : {counts})")