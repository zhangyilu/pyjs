x = 1
y = 2 * 3
if x == 1 :
  x = 2
endif
while x == 2 :
  x = x + 1
  x = x + 1
endwhile
print ( x )

#函数一定要有返回值

def pow ( x , n ) :
    s = 1
    while n > 0 :
        s = s * x
        n = n - 1
    endwhile
    return s
    
print ( pow ( 2 , 3 ) )

##全局变量 & 局部变量
x = 1
y = 2
def fa ( x ) :
    print ( x )
    print ( y )
    return 1
fa ( 4 )

#传递表达式 & 返回表达式
x = 1
y = 2
def fb ( x , y ) :
    if x == 5 :
       print ( x + y )
    endif
    return x * y
a = fb ( 2 * x , 2 * y )
print ( a )

#函数出现在表达式，参数，返回值中
def fs ( x ) :
    return x + 1
def fp ( ) :
    return 10
def fq ( x ) :
    return x + fp ( )
print ( fq ( fs ( fp ( ) * 2 ) ) )
print ( fp ( ) * 2 )
print ( fq ( 1 ) )

#递归
def fc ( x ) :
    if x <= 10 :
        x = fc ( x + 1 )
    endif
    return x
b = fc ( 9 )
print ( b )