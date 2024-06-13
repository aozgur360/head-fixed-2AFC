from __future__ import division
#def learning_fig(dataDir, stage, mouse):   

import os
os.chdir(r"Z:\Ali O\Behavioral Training\Learning Mice Data\stage 3")
import glob
import re
import matplotlib.pyplot as plt
import numpy as np 


x_count = 0
#x_results = []
#y_results = []  

trials_sep = []
p0_trials = []
p9_trials = []
p7_trials =[]

mouse = ['b/fig','w/fig','c1/fig', 'm/fig', 'pg/fig']
#filepath = [r"Z:\Ali O\Behavioral Training\Learning Mice Data\stage 3\b"]

#        filepath = dataDir + 'stage ' + str(stage) + '/' + [i]
for i in mouse:
    filepath = 'Z:/Ali O/Behavioral Training/Learning Mice Data/stage 3' + '/' + i
    
    x_count = 0
    x_results = []
    y_results = []  
    
#    print(filepath)
#        for filename in glob.glob(os.path.join(filepath, '*.txt')):
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()

                    
        count_trials = (sum(1 for match in re.finditer(r"\bto_state_2\b", txt))) - 1
        TRAIN_count_initial_incorrect_trials = sum(1 for match in re.finditer(r"\bto_state_3_2\b", txt))
        TRAIN_count_correct_trials = count_trials - TRAIN_count_initial_incorrect_trials
        
        
    
        
        if count_trials > 10:
            decimal_correct = TRAIN_count_correct_trials / count_trials
            percent_correct = decimal_correct * 100
        
            x_count = x_count + 1               
            x_results.append(x_count)
            y_results.append(percent_correct)
            
            #if want to keep first 10 trials
            if 'start_of_new_trial' in txt:
                trials_sep = (re.split(r'start_of_new_trial', txt, flags=re.MULTILINE))
            if 'reward_9 ' in txt:
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
            elif 'reward_7 ' in txt:
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
    
    
            if 'reward_9 ' in txt:
            
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_0_1 ' in s]
                for i in indices:
                    p0_trials.append(trials_sep[i].count("light_on_0_1 "))
                    count_p0_trials = len(p0_trials)
                    count_correct_p0_trials = p0_trials.count(1)
                    p0_decimal_correct = count_correct_p0_trials / count_p0_trials
                    p0_percent_correct = p0_decimal_correct * 100
                
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_9_1 ' in s]
                for i in indices:
                    p9_trials.append(trials_sep[i].count("light_on_9_1 "))
                    count_p9_trials = len(p9_trials)
                    count_correct_p9_trials = p9_trials.count(1)
                    p9_decimal_correct = count_correct_p9_trials / count_p9_trials
                    p9_percent_correct = p9_decimal_correct * 100
                
    
                
            if 'light_on_7_1 ' in txt:
                    indices = [i for i, s in enumerate(trials_sep) if 'light_on_0_1 ' in s]
                    for i in indices:
                        p0_trials.append(trials_sep[i].count('light_on_0_1 '))
                        count_p0_trials = len(p0_trials)
                        count_correct_p0_trials = p0_trials.count(1)
                        p0_decimal_correct = count_correct_p0_trials / count_p0_trials
                        p0_percent_correct = p0_decimal_correct * 100
                    
                    indices = [i for i, s in enumerate(trials_sep) if 'light_on_7_1 ' in s]
                    for i in indices:
                        p7_trials.append(trials_sep[i].count('light_on_7_1 '))
                        count_p7_trials = len(p7_trials)
                        count_correct_p7_trials = p7_trials.count(1)
                        p7_decimal_correct = count_correct_p7_trials / count_p7_trials
                        p7_percent_correct = p7_decimal_correct * 100
    
            
        del count_trials
        trials_sep.clear()
        p0_trials.clear()
        p9_trials.clear()
        p7_trials.clear()
    
    #    plt.figure()
    x = (np.hstack(x_results))
    #    x = range(33)    
            
    y = (np.hstack(y_results))
    plt.xlabel('Session Number')
    plt.ylabel('Percent Correct')
    plt.axhline(50, color="gray")
    plt.plot(x,y)
    
#    x_results.clear()
#    y_results.clear()
    
    plt.savefig(r'Z:\Ali O\Behavioral Training\behavioral figures\learning' + '.pdf', bbox_inches='tight')
    plt.savefig(r'Z:\Ali O\Behavioral Training\behavioral figures\learning' + '.eps', format='eps', dpi=1200)
