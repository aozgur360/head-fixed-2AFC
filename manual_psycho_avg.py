import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy import stats
from scipy.optimize import curve_fit
import scipy as sy

p0_per = [10.63742843, 16.76545473, 12.91226567]
p1_per = [14.06177156, 25.14396553, 16.93995547]
p2_per = [24.74358974, 29.01289663, 15.04740615]
p3_per = [52.04545455, 64.16051335, 14.29202606]
p4_per = [61.1969697, 66.85809298, 52.07168797]
p5_per = [90.68181818, 77.78731594, 81.13277143]
p6_per = [86.17132867, 76.95929374, 78.10080757]
p7_per = [ 86.42406854, 84.4852204, 86.81988088]
        
  
x_axis = range(0,8)
pall_avg = []
all_sem = []
pall_avg.append(statistics.mean(p0_per))
pall_avg.append(statistics.mean(p1_per))
pall_avg.append(statistics.mean(p2_per))
pall_avg.append(statistics.mean(p3_per))
pall_avg.append(statistics.mean(p4_per))
pall_avg.append(statistics.mean(p5_per))
pall_avg.append(statistics.mean(p6_per))
pall_avg.append(statistics.mean(p7_per))
all_sem.append(stats.sem(p0_per))
all_sem.append(stats.sem(p1_per))
all_sem.append(stats.sem(p2_per))
all_sem.append(stats.sem(p3_per))
all_sem.append(stats.sem(p4_per))
all_sem.append(stats.sem(p5_per))
all_sem.append(stats.sem(p6_per))
all_sem.append(stats.sem(p7_per))

#    plt.figure()
x = (np.hstack(x_axis))
y = (np.hstack(pall_avg))
err = (np.hstack(all_sem))
plt.xlabel('Left to Right Light Displays')
plt.ylabel('Percent Lick Right')
plt.axhline(50, color="gray")
plt.errorbar(x,y,err, linestyle='None')
#    f.show()

    #fitted pyschometric curve
d = np.array(x_axis, dtype=float)
p2 = np.array(pall_avg,  dtype=float) # scale to 0..1


LL = pall_avg[0]
RL = 100 - pall_avg[-1]


def pf(x, alpha, beta):
    print(beta)
    return LL + (100 - LL - RL) / (1 + np.exp( -(x-alpha)/beta ))
    
#    g = plt.figure(2)    
#    plt.figure()
par0 = sy.array([0., 1.]) # use some good starting values, reasonable default is [0., 1.]
par, mcov = curve_fit(pf, d, p2, par0)
#    print(par)
#    print("Left Lapse Rate:", LL)
#    print("Right Lapse Rate:", RL)
average_lapse = (LL + RL)/2
print("average_lapse rate:", average_lapse)

plt.xlabel('Left to Right Light Displays')
plt.ylabel('Percent Lick Right')
plt.axhline(50, color="gray")
plt.plot(d, p2, 'o', mfc = 'None')
plt.plot(d, pf(d, par[0], par[1]))
#    g.show()

pall_avg.clear()
all_sem.clear()

#plt.savefig(r'Z:\Ali O\Behavioral Training\behavioral figures\allctr_musc_psycho' + '.pdf', bbox_inches='tight')
#plt.savefig(r'Z:\Ali O\Behavioral Training\behavioral figures\allctr_musc_psycho' + '.eps', format='eps', dpi=1200)
