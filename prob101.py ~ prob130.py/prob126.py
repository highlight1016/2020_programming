a = input("우편번호: ")
우편번호 = a[:3]
if a in ["010", "011", "012"]:
    print("강북구")
elif a in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
