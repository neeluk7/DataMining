n = int(input("Enter n "));

val=[0];

for i in range(1,n+1):
    temp1 = (float(input("Enter expected"+str(i))));
    temp2 = (float(input("Enter observed"+str(i))));
    val.append(((temp2-temp1)*(temp2-temp1))/temp1);

del val[0];
#print(exp);
#print(sqdiff);

cr = float(input("Enter critical value "));

chisq = sum(val);

print("chi square value is "+str(chisq));
if(chisq>cr):
    print("Values are dependent as chi square is large.");
else:
    print("Values are independent.");

