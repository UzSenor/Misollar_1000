# 38-misol. Shaxmat doskasining ikkita turli (x1, y1) va (x2, y2) kordinatalari berilgan (1-8 oraliqda yotuvchi butun sonlar).
# Jumlani rostlikka tekshiring. Fil bir yurishda bir maydondan boshqasiga o'ta oladi.
x1 = int(input("x1 (1-8) = "))
y1 = int(input("y1 (1-8) = "))
x2 = int(input("x2 (1-8) = "))
y2 = int(input("y2 (1-8) = "))
print(abs(x1-x2)==1 or abs(y1-y2)==1)