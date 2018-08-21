import math;
import statistics;
def euc(x,y,a,b):
    return math.sqrt(((x-a)*(x-a))+((y-b)*(y-b)));

def kmeans():
    n = int(input("Enter number of data points "));
    k = int(input("Enter number of clusters to be formed "));

    x = [0];
    y = [0];

    for i in range(1, n + 1):
        x.append(float(input("Enter x" + str(i))));
        y.append(float(input("Enter y" + str(i))));

    del x[0];
    del y[0];

    clu = [1];
    cnx = [x[0]];
    cny = [y[0]];
    for i in range(1, k):
        clu.append(i + 1);
        cnx.append(x[i]);
        cny.append(y[i]);

    for i in range(k, n):
        mindist = 10000;
        clu.append(0);
        for j in range(0, k):
            t = euc(x[i], y[i], cnx[j], cny[j]);
            if (t < mindist):
                mindist = t;
                clu[i] = clu[j];
        cnx[clu[i] - 1] = (cnx[clu[i] - 1] + x[i]) / 2;
        cny[clu[i] - 1] = (cny[clu[i] - 1] + y[i]) / 2;
    print("Points in the order as entered in input have been assigned following cluster numbers");
    print(clu);

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

def correlation():
    n = input("Enter n ");
    n = int(n);
    x = [0];
    y = [0];
    for i in range(1, n + 1):
        x.append(float((input("Enter x" + str(i)))));
        y.append(float((input("Enter y" + str(i)))));
    del x[0];
    del y[0];
    cov = covariance(x, y, n);
    sx = statistics.stdev(x);
    sy = statistics.stdev(y);
    cor = cov / (sx * sy);
    print(cor);
    if (cor > 0):
        print("Positively related.");
    else:
        print("Negatively related.");

ch = int(input("Enter choice 1-K means 2-Correlation"));
if(ch==1):
    kmeans();
elif(ch==2):
    correlation();
else:
    print("Invalid choice. Terminated.");