import statistics;
def covariance(x, y, n):
    xm = int(round(sum(x)/len(x)));
    ym = int(round(sum(y)/len(y)));
    mul = [0];
    for i in range(0, n):
        dx = x[int(i)]-xm;
        dy = y[int(i)]-ym;
        mul.append(dx*dy);
    cov = (sum(mul))/(n-1);
    return cov;

def correlation(x, y, cov):
    sx = statistics.stdev(x);
    sy = statistics.stdev(y);
    cor = cov/(sx*sy);
    print(cor);
    if(cor>0):
        print("Positively related.");
    else:
        print("Negatively related.");

n = input("Enter n ");
n = int(n);
x=[0];
y=[0];
for i in range(1, n+1):
    x.append(float((input("Enter x"+str(i)))));
    y.append(float((input("Enter y"+str(i)))));
del x[0];
del y[0];
print(x);
print(y);
choice = input("Press 1 for Covariance. Press 2 for Correlation. ");
choice=int(choice);
cov = covariance(x, y, n);
if(choice==1):
    print(cov);
    if (cov > 0):
        print("Positively related.");
    else:
        print("Negatively related.");
if(choice==2):
    correlation(x, y, cov);
if(choice!=1 and choice!=2):
    print("Invalid choice. Terminated.");