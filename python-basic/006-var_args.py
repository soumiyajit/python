"""

Accept variable args in Python and print the same 

"""

def test_varargs(*args):
    for count,item in enumerate(args):
        print '{0}.{1}'.format(count,item)
        


test_varargs("Soumiyajit","Das","Chowdhury")