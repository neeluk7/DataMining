# 5 9 12 13 15 25 50 70 72 92 204 232
# 4 8 9 15 21 21 24 25 26 28 29 34

import math;

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0

print("Enter data record values");
lst = [int(x) for x in input().split()];
binsize = input("Enter bin size");
binsize = int(binsize);
# print(lst);
lst.sort();
# print(lst);
# print(type(binsize));
meanCopy = [lst[x:x + binsize] for x in range(0, len(lst), binsize)];
print("Smoothing by mean for all bins as follows:");
for l in meanCopy:
    mean = int(round(sum(l) / len(l)));
    # print(mean);
    for (i, item) in enumerate(l):
        l[i] = mean;
    print(l);

medianCopy = [lst[x:x + binsize] for x in range(0, len(lst), binsize)];
# print(medianCopy);
print("Smoothing by median for all bins as follows:");
for l in medianCopy:
    m = int(median(l));
    for (i, item) in enumerate(l):
        l[i] = m;
    print(l);

print("Smoothing by boundary for all bins as follows:");
boundaryCopy = [lst[x:x + binsize] for x in range(0, len(lst), binsize)];
for l in boundaryCopy:
    lower = l[0];
    upper = l[len(l) - 1];
    for (i, item) in enumerate(l):
        if (i != 0 and i != len(l) - 1):
            if ((l[i] - lower) < (upper - l[i])):
                l[i] = lower;
            else:
                l[i] = upper;
    print(l);