# 公鸡每只5元，母鸡每只3元，小鸡3只一元，现要求用100元钱买100只鸡，问公鸡、母鸡、小鸡各买几只？
# 设公鸡数量为x只，母鸡数量为y只，小鸡数量为z只，可得以下两个方程
# 5x+3y+z/3=100
# x+y+z=100

for x in range(0,100): # x取0到100之间
    for y in range(0,100):
        z=100-x-y
        if z>0 and 5*x+3*y+z/3==100 and x+y+z==100:   # 两个条件‘与’起来
            alist = [f"公鸡{x}只，母鸡{y}只，小鸡{z}只"]
            alist.sort(reverse=True);
            print(alist)
