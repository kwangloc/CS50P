def f(*args, **kwargs):
    # print("Positional:", args)
    for arg in args:
        print(arg)

def f_2(**kwargs):
    print("Named:", kwargs)
    # for kwarg in kwargs:
    #     print(kwarg)
        
f(100, 50, 25)
f_2(galleons=100, sickles=50, knuts=25)
