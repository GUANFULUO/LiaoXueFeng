    '''   1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1'''
#杨辉三角难点在于在函数中表达与上一行的对应关系。
def triangles1():
    ls = [1]
    while True:
        yield ls
        ls.append(0)#方法1的思路在于在上一行末尾加上一个0，巧妙地利用了1+0=1,0+1=1,以及切片ls[-1]
                    #这样所有的数字都可以用相同的公式递推得到
        ls = [ls[i-1] + ls[i] for i in range(len(ls))]
def triangles2():
    ls = [1]
    while True:
        yield ls
        ls = [1]+ [ls[i] + ls[i+1] for i in range(len(ls)-1)] + [1]
#第二种方法的思路是从上一行的本身来构造新的一行，利用了range(0)相当于不进行循环这一特点，佩服佩服。