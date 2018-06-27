# open raw data source file (IPs)
import numpy as np
from sklearn.cluster import MeanShift# as ms
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

infile = "/root/OSINT/Plot/datasets/ThreatQIPs.csv"
outfile = "/root/OSINT/Plot/datasets/ThreatQSplitIPs.csv"

with open(outfile, "a") as out:
    with open(infile) as f:
        content = f.readlines()
        # change IP to 3 chunks for 1-16,17-24,25-32 bits
        for ip in content:
            #print ip
            binip = ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
            splitbin = binip[0:16]
            f1 = int(splitbin,2) # feature one is decimal of /24 network
            f2 = int(ip.split('.')[2]) # feature three is octet 3
            f3 = int(ip.split('.')[3])  # feature three is octet 4
            out.write("%i,%i,%i\n" % (f1,f2,f3))
            #print f1,f2,f3
            #np.append([f1,f2,f3],axis=0)
    f.close()
out.close()

# True

    #print np


