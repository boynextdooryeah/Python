a,b=0,1
while b<1000:
    if a+b<1000:
        print(b,end=',')
    if a+b>1000:
        print(b)
    a,b = b,a+b

#todo  list   列表推导式
#todo [表达式 for 变量 in 列表 (if 条件)]
#todo [out_exp_res for out_exp in input_list (if condition)]

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
#           out_exp_res：列表生成元素表达式，可以是有返回值的函数。
#                       for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
#                                          if condition：条件语句，可以过滤列表中不符合条件的值。
print('\n',new_names)

multiples = [i for i in range(30) if i%3==0]
print(multiples)

#todo  dict   字典推导式
#todo { key_expr: value_expr for value in collection (if condition) }
#todo       依旧 key : value
listdemo = ['Google','Ru-noob', 'Taobao']
new_dict = {key:len(key) for key in listdemo}

print(new_dict)

#todo  set   集合推导式
#todo { expression for item in Sequence (if conditional) }
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

#todo  tuple 元组推导式
#todo (expression for item in Sequence (if conditional) )
d = (x for x in range(1,10))
print(d)         #<generator object <genexpr> at 0x7faf6ee20a50>   返回的是生成器对象
print(tuple(d))  # 使用 tuple() 函数，可以直接将生成器对象转换成元组