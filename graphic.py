import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
coordx = []
fluxx = []
coordy = []
fluxy = []
photo = pyfits.open('v523cas60s-001(1).fit')
scidata = photo[0].data
print(scidata[154][226])#216,236
for i in range(216,237):
    fluxx.append(scidata[154][i])
    coordx.append([i])
for i in range(144,164):
    fluxy.append(scidata[i][226])
    coordy.append([i])


plt.figure()
plt.subplot(1,2,1)
plt.plot(coordx,fluxx)
plt.xlabel("coordinate")
plt.ylabel("flux")
plt.title("grafic X")
plt.subplot(1,2,2)
plt.plot(coordy,fluxy)
plt.xlabel("coordinate")
plt.ylabel("flux")
plt.title("grafic Y")
plt.show()
