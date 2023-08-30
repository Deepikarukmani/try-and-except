try and except:
a=100/1
print(a)
try:
    a=100/0
    print(b)
    try:                               #Nested try
        print("efn")
    except:
        print("wfihne")

except NameError:
    print("something WRONG")

except:
    print("something is fishy")

finally:
    print("the end")

raise exception:
if input()=="100":
    raise Exception("no negative numbers")

