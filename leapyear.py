year = eval(input("請輸入一個西元年年分"))

if year%4==0 and year%100!=0 or year%400==0 :
    print("閏年")
else:
    print("不是閏年")