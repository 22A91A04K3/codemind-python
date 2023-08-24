a= int(input())
if a<=10000:
    d=0.80*a
    h=0.20*a
elif a<=20000:
    d=0.90*a
    h=0.25*a
elif a>=20000:
    d=0.95*a
    h=0.30*a
gs=a+d+h
print(f"{gs:.2f}")