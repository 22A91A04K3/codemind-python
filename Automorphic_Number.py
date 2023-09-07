n=int(input())
sq=n**2
n_string=str(n)
sq_string=str(sq)
if sq_string.endswith(n_string):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")