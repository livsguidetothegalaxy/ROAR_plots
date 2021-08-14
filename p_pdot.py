import matplotlib.pyplot as plt
import numpy as np

p_x_known = np.asarray([0.1153635682680, 0.69374767047, 0.3158731909,  1.240699038946, 0.00353632915276244 ])
p_dot_y_known = np.log10(np.asarray([5.96703E-15,2.097E-15, 3.6039E-13, 5.6446E-16, 9.85103E-20]))

p_x_cand = np.asarray([1.1153635682680, 1.69374767047, 1.3158731909,  0.240699038946, 1.00353632915276244 ])
p_dot_y_cand = np.log10(np.asarray([5.96703E-15,2.097E-15, 3.6039E-13, 5.6446E-16, 9.85103E-20]))


fig, ax = plt.subplots(1,1)
import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter
ax.get_xaxis().set_major_formatter(FormatStrFormatter("%.4f"))
ax.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())

fig.suptitle('Period Derivative vs Pulsar Period (pdot vs p)')
plt.xlabel('period (s)', fontsize =14)
plt.ylabel('log_10(Pdot)', fontsize=14)
  


otherspulsars, = plt.plot(p_x_known , p_dot_y_known, 'o', color = '#003D30', markersize = 4, label = "Known Pulsars")
candidates, = plt.plot(p_x_cand , p_dot_y_cand, '*', color = '#009175', markersize = 6, label = "Candidates")
xscale = ax.set_xscale('log')
plt.legend(loc='upper left', fontsize="9")
