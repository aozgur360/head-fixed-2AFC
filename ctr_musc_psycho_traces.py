import os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy import stats
from scipy.optimize import curve_fit
import scipy as sy

#intended_trials = []
#experimental_trials = []
#c_pos = []
#w_pos = []
#zero_pos = []
#one_pos = []
#two_pos = []
#three_pos = []
#four_pos = []
#five_pos = []
#six_pos = []
#seven_pos = []
#
#
#master_p0 = []
#master_p1 = []
#master_p2 = []
#master_p3 = []
#master_p4 = []
#master_p5 = []
#master_p6 = []
#master_p7 = []
#
#pall_avg = []
#all_sem = []
#
#x_axis = range(0,8)
#
#trials_sep = []
#
#trials_sep = []
#p0_trials = []
#p9_trials = []
#p7_trials =[]

mouse = ['muscAll',]
#filepath = [r"Z:\Ali O\Behavioral Training\Learning Mice Data\stage 3\b"]

#        filepath = dataDir + 'stage ' + str(stage) + '/' + [i]
for i in mouse:
    filepath = 'Z:/Ali O/Behavioral Training/Learning Mice Data/stage 4' + '/' + i
    
    intended_trials = []
    experimental_trials = []
    c_pos = []
    w_pos = []
    zero_pos = []
    one_pos = []
    two_pos = []
    three_pos = []
    four_pos = []
    five_pos = []
    six_pos = []
    seven_pos = []
    
    
    master_p0 = []
    master_p1 = []
    master_p2 = []
    master_p3 = []
    master_p4 = []
    master_p5 = []
    master_p6 = []
    master_p7 = []
    
    pall_avg = []
    all_sem = []
    
    x_axis = range(0,8)
    
    trials_sep = []
    
    trials_sep = []
    p0_trials = []
    p9_trials = []
    p7_trials =[]
    
#    print(filepath)
#        for filename in glob.glob(os.path.join(filepath, '*.txt')):
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
        
#            count_trials = (sum(1 for match in re.finditer(r"\bto_state_2\b", txt))) - 1
        
            trials_sep = (re.split(r'reward_C', txt, flags=re.MULTILINE))
            for trial in trials_sep:
                                        
                if re.search(r'\blight_on_0_1\b', trial):
                    intended_trials.append("zero")
                    if 'to_state_3_2' in trial:
                        experimental_trials.append("W")
                    else: 
                        experimental_trials.append("C")
                if re.search(r'\blight_on_1_1\b', trial):
                    intended_trials.append("one")
                    if 'reward' in trial:
                        experimental_trials.append("C")
                    else: 
                        experimental_trials.append("W")
                if re.search(r'\blight_on_2_1\b', trial):
                    intended_trials.append("two")
                    if 'reward' in trial:
                        experimental_trials.append("C")
                    else: 
                        experimental_trials.append("W")                            
                if re.search(r'\blight_on_3_1\b', trial):
                    intended_trials.append("three")
                    if 'reward' in trial:
                        experimental_trials.append("C")
                    else: 
                        experimental_trials.append("W")
                if re.search(r'\blight_on_4_1\b', trial):
                    intended_trials.append("four")
                    if 'reward' in trial:
                        experimental_trials.append("C")
                    else: 
                        experimental_trials.append("W")                                
                if re.search(r'\blight_on_5_1\b', trial):
                    intended_trials.append("five")
                    if 'reward' in trial:
                        experimental_trials.append("C")
                    else: 
                        experimental_trials.append("W")                                
                if re.search(r'\blight_on_6_1\b', trial):
                    intended_trials.append("six")
                    if 'reward' in trial:
                        experimental_trials.append("C")
                    else: 
                        experimental_trials.append("W")                                
                if re.search(r'\blight_on_7_1\b', trial):
                    intended_trials.append("seven")
                    if 'to_state_3_2' in trial:
                        experimental_trials.append("W")
                    else: 
                        experimental_trials.append("C")
                        
            for i, j in enumerate(experimental_trials):
                if j == 'C':
                    c_pos.append(i)
            for i, j in enumerate(experimental_trials):
                if j == 'W':
                    w_pos.append(i)
            for i, j in enumerate(intended_trials):
                if j == 'zero':
                    zero_pos.append(i)
            for i, j in enumerate(intended_trials):
                if j == 'one':
                    one_pos.append(i)
            for i, j in enumerate(intended_trials):
                if j == 'two':
                    two_pos.append(i)
            for i, j in enumerate(intended_trials):
                if j == 'three':
                    three_pos.append(i)
            for i, j in enumerate(intended_trials):
                if j == 'four':
                    four_pos.append(i)
            for i, j in enumerate(intended_trials):
                if j == 'five':
                    five_pos.append(i)
            for i, j in enumerate(intended_trials):
                if j == 'six':
                    six_pos.append(i)
            for i, j in enumerate(intended_trials):
                if j == 'seven':
                    seven_pos.append(i)
            
    #                    print(intended_trials)
    #                    print("trial count", count_trials)
    #                    print("inten. trial count", len(intended_trials))
            
            p0_count = (len(zero_pos))
            p0_count_c = (len(set(zero_pos).intersection(c_pos)))
            p0_perc_c = 100 - ((p0_count_c / p0_count) * 100)
            master_p0.append(p0_perc_c)
    
            p1_count = (len(one_pos))
            p1_count_c = (len(set(one_pos).intersection(c_pos)))
            p1_perc_c = 100 - ((p1_count_c / p1_count) * 100)
            master_p1.append(p1_perc_c)
            
            p2_count = (len(two_pos))
            p2_count_c = (len(set(two_pos).intersection(c_pos)))
            p2_perc_c = 100 - ((p2_count_c / p2_count) * 100)
            master_p2.append(p2_perc_c)
    
            p3_count = (len(three_pos))
            p3_count_c = (len(set(three_pos).intersection(c_pos)))
            p3_perc_c = 100 - ((p3_count_c / p3_count) * 100)
            master_p3.append(p3_perc_c)
    
            p4_count = (len(four_pos))
            p4_count_c = (len(set(four_pos).intersection(c_pos)))
            p4_perc_c = (p4_count_c / p4_count) * 100
            master_p4.append(p4_perc_c)
    
            p5_count = (len(five_pos))
            p5_count_c = (len(set(five_pos).intersection(c_pos)))
            p5_perc_c = (p5_count_c / p5_count) * 100
            master_p5.append(p5_perc_c)
    
            p6_count = (len(six_pos))
            p6_count_c = (len(set(six_pos).intersection(c_pos)))
            p6_perc_c = (p6_count_c / p6_count) * 100
            master_p6.append(p6_perc_c)
    
            p7_count = (len(seven_pos))
            p7_count_c = (len(set(seven_pos).intersection(c_pos)))
            p7_perc_c = (p7_count_c / p7_count) * 100
            master_p7.append(p7_perc_c)             
            
            
            intended_trials.clear()
            experimental_trials.clear()
            c_pos.clear()
            w_pos.clear()  
            zero_pos.clear()
            one_pos.clear()
            two_pos.clear()
            three_pos.clear()
            four_pos.clear()
            five_pos.clear()
            six_pos.clear()
            seven_pos.clear()
            del p0_count
            del p0_count_c
            del p0_perc_c
            del p1_count
            del p1_count_c
            del p1_perc_c
            del p2_count
            del p2_count_c
            del p2_perc_c
            del p3_count
            del p3_count_c
            del p3_perc_c
            del p4_count
            del p4_count_c
            del p4_perc_c
            del p5_count
            del p5_count_c
            del p5_perc_c
            del p6_count
            del p6_count_c
            del p6_perc_c
            del p7_count
            del p7_count_c
            del p7_perc_c    
    
            
    
    master_array = np.array([master_p0, master_p1, master_p2, master_p3, master_p4, master_p5, master_p6, master_p7])
    #    for i in range(len(master_p0)):
    
    #        plt.figure()
    #        plt.plot(master_array[:,i])
    #        plt.xlabel('Left to Right Light Displays')
    #        plt.ylabel('Percent Lick Right')
    #        plt.axhline(50, color="gray")
    #        
    #        print("Left to Right Panels...")
    #        print(master_array[:,i])
    #        
    #        print(master_array)
    #        print(master_array[7,:])
        
    p0_tot = master_array[0,:]
    p1_tot = master_array[1,:]
    p2_tot = master_array[2,:]
    p3_tot = master_array[3,:]
    p4_tot = master_array[4,:]
    p5_tot = master_array[5,:]
    p6_tot = master_array[6,:]
    p7_tot = master_array[7,:]
    
    p0_avg = statistics.mean(p0_tot)
    p1_avg = statistics.mean(p1_tot)
    p2_avg = statistics.mean(p2_tot)
    p3_avg = statistics.mean(p3_tot)
    p4_avg = statistics.mean(p4_tot)
    p5_avg = statistics.mean(p5_tot)
    p6_avg = statistics.mean(p6_tot)
    p7_avg = statistics.mean(p7_tot)
    
    pall_avg.append(p0_avg)
    pall_avg.append(p1_avg)
    pall_avg.append(p2_avg)
    pall_avg.append(p3_avg)
    pall_avg.append(p4_avg)
    pall_avg.append(p5_avg)
    pall_avg.append(p6_avg)
    pall_avg.append(p7_avg)
    
    all_sem.append(stats.sem(p0_tot))
    all_sem.append(stats.sem(p1_tot))
    all_sem.append(stats.sem(p2_tot))
    all_sem.append(stats.sem(p3_tot))
    all_sem.append(stats.sem(p4_tot))
    all_sem.append(stats.sem(p5_tot))
    all_sem.append(stats.sem(p6_tot))
    all_sem.append(stats.sem(p7_tot))
    
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
    
#    plt.savefig(r'Z:\Ali O\Behavioral Training\behavioral figures\muscAll_psycho' + '.pdf', bbox_inches='tight')
#    plt.savefig(r'Z:\Ali O\Behavioral Training\behavioral figures\muscAll_psycho' + '.eps', format='eps', dpi=1200)
