
r = 0.13
n1=0

caf1 = 130
while caf1 >65:
   caf1 = caf1*(1-r)
   n1+=1

caf2 = 130
for i in range(1,25):
    caf2 = caf2*(1-r)

caf3 = 130
for i in range(1,25):
    caf3 = caf3*(1-r)
    caf3+= 130

print("CAFFEINE VALUES")
print("One cup: less than 65 mg. will reamin after {} hours.".format(n1))
print("One cup: {0:.2f} mg. will remain after 24 hours.".format(caf2))
print("Hourly cups: {0:.2f} mg. will reamin after 24 hours.".format(caf3))