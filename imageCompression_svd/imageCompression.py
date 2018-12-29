from PIL import Image
import numpy as np
import sys
#data must be a 2d array n is the number of eigenvalues taken
def compressData(data,n):
    u, s, vh = np.linalg.svd(data, full_matrices=True)
    datanew = np.zeros((len(data),len(data[0])))
    for i in range(n):
        e = s[i]
        for j in range (len(datanew)):
            datanew[j]+=e*u[j][i]*vh[i]
    for i in datanew:
        i+=0.5
    datanew = datanew.astype('uint8')
    return datanew

if len(sys.argv)<3:
    print("usage:python3 imageCompression.py -filename -n")
    exit()
n = int(sys.argv[2])
if n < 0 or n > 256:
    print("invalid n or n is too big")
    exit()
filename = sys.argv[1]
im = Image.open(filename)
a = np.asarray(im)
if n>min(len(a),len(a[0])):
    print("n must be less than or equal to the min of height and width")
l = np.moveaxis(a, -1, 0)
lnew = l.copy()
for i in range(len(lnew)):
       lnew[i] = compressData(lnew[i],n)
anew = np.stack(lnew,axis=-1)

imnew = Image.fromarray(anew)
imnew.show()
imnew.save(filename+"_compressed.png")
original = len(a)*len(a[0])*1.0
compressed = (len(a)*n+len(a[0])*n+n)*1.0
ratio = compressed/original
print("ratio:"+str(ratio))