w, h = 8, 8;
A =[[0 for x in range(w)] for y in range(h)]
A[7][4] = 'K'
print A
print ('\n' .join([''.join(['{:4}'.format(item) for item in row])for row in A]))

class MyClass:

    i = 12345

    def f(self):
        return 'hello world'
        

