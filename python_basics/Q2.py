def exp_i(i):
    return complex(0,1)**i
for i in range(1,30):
    print(f"i**{i} = {exp_i(i)}")