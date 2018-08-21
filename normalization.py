def minmax():
    omin = float(input("Enter old min "));
    omax = float(input("Enter old max "));
    nmin = float(input("Enter new min "));
    nmax = float(input("Enter new max "));
    v = float(input("Enter value to be normalized "));
    newv = (((v-omin)/(omax-omin))*(nmax-nmin))+nmin;
    print("Normalized value is "+str(newv));

def zscore():
    v = float(input("Enter value to be normalized "));
    m = float(input("Enter mean "));
    s = float(input("Enter standard deviation "));
    newv = (v-m)/s;
    print("Normalized value is " + str(newv));

def dec():
    v = float(input("Enter value to be normalized "));
    temp=len(str(v));
    temp=temp-2;
    div=1;
    while(temp>0):
        div=div*10;
        temp=temp-1;
    newv=v/div;
    print("Normalized value is " + str(newv));

ch = int(input("Enter choice for Normalization \n 1.Min Max  2.Z-score  3.Decimal Scaling"));

if(ch==1):
    minmax();
elif(ch==2):
    zscore();
elif(ch==3):
    dec();
else:
    print("Choice invalid. Terminated.");