password = '123456'
i = 3

while i>0:
    pwd = input('輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        i = i-1
        print("密碼錯誤")
        if i >0:
            print("還有", i ,"次機會")
        if i ==0:
            print("你甚麼時候產生了你沒輸入錯密碼的錯覺")
