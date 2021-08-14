import pylab as plt
import numpy as np

lll_known=np.asarray([117.327, 108.172])
bbb_known = np.asarray([-0.074, -42.985])
distance_known= np.asarray([218.6, 11.41])

lll_cand=np.asarray([117.327, 108.172])
bbb_cand = np.asarray([-10.074, -4.985])
distance_cand= np.asarray([218.6, 11.41])

l_axis_name ='latitude l (deg)'
b_axis_name = 'longitude b (deg)'

for i in range(len(lll_known)):
    if lll_known[i]>180:
        lll_known[i] -= 360


for i in range(len(lll_cand)):
    if lll_cand[i]>180:
        lll_cand[i] -= 360


fig = plt.figure(figsize=(12,9))


ax = fig.add_subplot(111, projection="mollweide")
ax.set_xlabel("Galactic Longitude")
ax.set_ylabel("Galactic Latitude")
ax.set_title("Galactic Location and DM of Pulsars and Candidates")
ax.grid(True)

sc = ax.scatter(np.array(lll_known)*np.pi/180., np.array(bbb_known)*np.pi/180., c=distance_known, marker= ".", label= "Known Pulsars")
sc = ax.scatter(np.array(lll_cand)*np.pi/180., np.array(bbb_cand)*np.pi/180., c=distance_cand, marker= "*", label = "Candidates")

#plt.colorbar(sc)
cbar = plt.colorbar(sc)
cbar.set_label('Distance')
plt.legend(loc='upper right', fontsize="9")

plt.show()
