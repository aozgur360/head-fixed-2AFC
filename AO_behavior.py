from __future__ import division
def stage_3(dataDir, stage, mouse):   
    import os
    import glob
    import re
    import matplotlib.pyplot as plt
    import numpy as np 
    import statistics 

    
    x_count = 0
    x_results = []
    y_results = []  
    
    trials_sep = []
    spoutLR_sep = []
    p0_trials = []
    p9_trials = []
    p7_trials =[]
    
    avg_start_times = []
    avg_completion_times = []
    avg_reaction_times = []
    avg_LR_reward_times = []
    avg_decision_times = []

    
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
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
    
            count_total_attempts = txt.count("to_state_3_")
            attempts_value = count_total_attempts / count_trials
            
            print(os.path.basename(filename))
            
            edit_notes = (re.split(r'edit:', txt, flags=re.MULTILINE))
            
            
            
            
            
            #to ignore first 10 trials
#            start = 'to_state_2'
#            end = 'ignore'
#            for i in range(11,count_trials):
#                trials_sep.append((txt.split(start))[i].split(end)[0])
            
            #check for version with new notes
            if "light8" in txt:
                for line in txt.split('\n'):    
                    if "lick_count_requirement" in line:
                        lick_count = (line.split()[1])
                    if "lick_time_requirement" in line:
                        lick_time = (line.split()[1])
                    if "ex_duration" in line:
                        ex_dur = (line.split()[1])
                    if "airpuff_duration" in line:
                        airpuff = (line.split()[1])
                    if "per_R" in line:
                        per_R = (line.split()[1])
                    if "punishment_time1" in line:
                        timeout_punishment_dur = (line.split()[1])
                    if "number_of_stim_cycles" in line:
                        number_of_stim_cycles = (line.split()[1])
                    if "stim_cycle_duration" in line:
                        stim_cycle_duration = (line.split()[1])
                    if "stim_duration" in line:
                        stim_duration = (line.split()[1])
                    if "stim_start_delay" in line:
                        stim_start_delay = (line.split()[1])
                    if "spout_available" in line:
                        tsa = (line.split()[1])
                    if "no_test_punishment" in line:
                        no_test_punishment = (line.split()[1])
                    if "tsa_no_reward" in line:
                        tsa_no_reward = (line.split()[1])
                    if "training_reward" in line:
                        no_retrial_reward = (line.split()[1])
                    if "cspout_no_reward" in line:
                        cspout_no_reward = (line.split()[1])
                    if "lights8" in line:
                        p6_mode = (line.split()[1])
                    if "lights2" in line:
                        p2_mode = (line.split()[1])
                    if "training_mode" in line:
                        retrial_mode = (line.split()[1])
                    if "timeout_punishment" in line:
                        timeout_punishment = (line.split()[1])
                    if "punishment_active" in line:
                        wrong_lick_punishment = (line.split()[1])
#                    if "edit" in line:
#                        edit = line
                
                if float(retrial_mode) > 0:
                    print("retrial mode")
                if float(no_retrial_reward) > 0:
                    print("no retrial reward")
                if float(tsa_no_reward) > 0:
                    print("TSA no reward")
                if float(cspout_no_reward) > 0:
                    print("no c_reward")
                if float(wrong_lick_punishment) > 0 :
                    print("wrong lick punishment")
                print("ex_time: " + ex_dur + ", lick req: " + lick_count + ", lick time: " + lick_time + ", per_R: " + per_R + ", air: " + airpuff + ", timeout_punish: " + timeout_punishment_dur + ", stim delay: " + stim_start_delay + ", TSA: " + tsa + ", num stim cycles: " + number_of_stim_cycles + ", stim cycle dur: " + stim_cycle_duration + ", stim dur: " + stim_duration)
#                if len(edit.split()) > 1:
#                    print(edit)
                if "edit:" in txt:
                    if any(c.isalpha() for c in edit_notes[1]) == True:
                        print(edit_notes[1].strip())
                    
            
            #if want to keep first 10 trials
            if 'start_of_new_trial' in txt:
                trials_sep = (re.split(r'start_of_new_trial', txt, flags=re.MULTILINE))
            if 'reward_9 ' in txt:
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
            elif 'reward_7 ' in txt:
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
                
            #for lickLorR after spoutLR
            if 'to_state_2' in txt:
                spoutLR_sep = (re.split(r'to_state_2',txt,flags=re.MULTILINE))
                
            #for split by wrong_spout
#            if 'wrong' in txt:
#                wrong_sep = (re.split(r'wrong',txt,flags=re.MULTILINE))
            
#            subtract 10 to ignore first 10 trials
            print("Number of trials:", count_trials)
            print("percent correct:", percent_correct)
            print("attempts value:", attempts_value)
            
            #########TESTING
            master_start_list = []
            master_lick_list = []
            master_reward_list = []
            master_spoutLR_list = []
            master_firstchoice_list = []
            master_decision_list = []
            
            for i in trials_sep:
            ###TIME SPENT STARTING TRIAL
                start_list = []
                lick_list =[]
                reward_list = []
                decision_list = []
#                spoutLR_list = []
#                firstchoice_list = []
                for line in (i.split('\n')):  
                        if "spouts_16_12" in line:
                            start_list.append(float(line[0:6]))
                            master_start_list.append(min(start_list))
                        if "lckC" in line:
                            lick_list.append(float(line[0:6]))
                            master_lick_list.append(min(lick_list))
    #                        print(min(lick_list))
                            
                ###TIME TO COMPLETE TRIAL
                        if "reward_7" in line:
                            reward_list.append(float(line[0:6]))
                            master_reward_list.append(min(reward_list))
                            decision_list.append(float(line[0:6]))
                            master_decision_list.append(min(decision_list))
                        if "reward_0" in line:
                            reward_list.append(float(line[0:6]))
                            master_reward_list.append(min(reward_list)) 
                            decision_list.append(float(line[0:6]))
                            master_decision_list.append(min(decision_list)) 
                        if "to_state_45" in line:
                                decision_list.append(float(line[0:6]))
                                master_decision_list.append(min(decision_list))
                        
                        
#            for i in wrong_sep:
#                for line in i.split('\n'):
#                        decision_list.append(float(line[0:6]))
#                        decision_list.append(min(decision_list))
            
            
                
            for i in spoutLR_sep:
                spoutLR_list = []
                firstchoice_list = []
                for line in i.split('\n'):
                
                
        ## FIRST REACTION TIME
                    if "spout_LR" in line:
                        spoutLR_list.append(float(line[0:6]))
                        master_spoutLR_list.append(min(spoutLR_list))
                    if "lckL" in line:
                        firstchoice_list.append(float(line[0:6]))
                        master_firstchoice_list.append(min(firstchoice_list))      
                    if "lckR" in line:
                        firstchoice_list.append(float(line[0:6]))
                        master_firstchoice_list.append(min(firstchoice_list)) 
                            
                        



                        

            
            #remove duplicates from master_firstchoice_list
            master_firstchoice_list = list(dict.fromkeys(master_firstchoice_list)) 
            
            
            master_decision_list = set(master_decision_list)
            master_decision_list = sorted(master_decision_list, key=float)
            
            
            master_spoutLR_list = set(master_spoutLR_list)
            master_spoutLR_list = sorted(master_spoutLR_list, key=float)
            

            master_reward_list = set(master_reward_list)
            master_reward_list = sorted(master_reward_list, key=float)            
                        
            
            master_lick_list = set(master_lick_list)
            master_lick_list = sorted(master_lick_list, key=float) 
#            print(master_lick_list)
#            mlick = [float(x.strip(' "')) for x in master_lick_list]
#            
            master_start_list = set(master_start_list)
            master_start_list = sorted(master_start_list, key=float)  
#            mstart = [float(x.strip(' "')) for x in master_start_list]
            
#            master_spoutLR_list2 = master_spoutLR_list.copy()
#                      
            ####CHECK LEN FOR LAST TRIAL ERROR
            master_start_list2 = master_start_list.copy()
            master_spoutLR_list2 = master_spoutLR_list.copy()
            master_reward_list2 = master_reward_list.copy()
            master_spoutLR_list3 = master_spoutLR_list.copy()
            
            if len(master_start_list) != len(master_lick_list):
                master_start_list = master_start_list[:-1]
            
            if len(master_start_list2) != len(master_reward_list):
                master_start_list2 = master_start_list2[:-1]
                
            if len(master_spoutLR_list) != len(master_firstchoice_list):
                master_spoutLR_list = master_spoutLR_list[:-1] 
            
            if len(master_spoutLR_list2) != len(master_reward_list2):
                master_spoutLR_list2 = master_spoutLR_list2[:-1] 
                
            if len(master_spoutLR_list3) != len(master_decision_list):
                master_spoutLR_list3 = master_spoutLR_list3[:-1] 
                
                
                
                
                
                
                       
#            if len(master_start_list2) != len(master_firstchoice_list):
#                master_start_list2 = master_start_list2[:-1]
            
                #########################################
                     
#            master_firstchoice_list = list(set(master_firstchoice_list))
#            master_firstchoice_list.sort()
#            master_start_list2 = list(set(master_start_list2))
#            master_start_list2.sort()
#            copy_mfcl = master_firstchoice_list.copy()
##            copy_msl = master_start_list.copy()
#            
#            for i in range(1,len(master_firstchoice_list)-1):
#                if master_firstchoice_list[i] < master_firstchoice_list[i-1] + 5:
#                    copy_mfcl.remove(master_firstchoice_list[i])
#                    master_start_list2.remove(master_start_list2[i])
                    
                    
                    
#            print(master_start_list2)
#            print(copy_mfcl)
#            print(master_start_list2)      
                
                ########################################
                
            
                
                
                

                
            zip(master_lick_list, master_start_list)
            start_times = [x - y for x, y in zip(master_lick_list, master_start_list)]
            if len(start_times) > 0:
                avg_start_times.append(statistics.mean(start_times))
                print("average start time: " , statistics.mean(start_times))
                
            zip(master_reward_list, master_start_list2)
            completion_times = [x - y for x, y in zip(master_reward_list, master_start_list2)]
            if len(completion_times) > 0:
                avg_completion_times.append(statistics.mean(completion_times))
                print("average completion time: " , statistics.mean(completion_times))
                
            zip(master_firstchoice_list, master_spoutLR_list)
            reaction_times = [x - y for x, y in zip(master_firstchoice_list, master_spoutLR_list)]
            if len(reaction_times) > 0:
                avg_reaction_times.append(statistics.mean(reaction_times))
                print("average any reaction time: " , statistics.mean(reaction_times)) 
                
            zip(master_reward_list2, master_spoutLR_list2)
            LR_reward_times = [x - y for x, y in zip(master_reward_list2, master_spoutLR_list2)]
            if len(LR_reward_times) > 0:
                avg_LR_reward_times.append(statistics.mean(LR_reward_times))
                print("average LR_spout to Reward time: " , statistics.mean(LR_reward_times)) 
                
            zip(master_decision_list, master_spoutLR_list3)
            decision_times = [x - y for x, y in zip(master_decision_list, master_spoutLR_list3)]
            if len(decision_times) > 0:
                avg_decision_times.append(statistics.mean(decision_times))
                print("average decision time: " , statistics.mean(decision_times))
                   

#            print(master_firstchoice_list)
#            print(master_spoutLR_list)
            
            
#            print(master_reward_list)
#            print(master_start_list)
            
            
#            print(mstart)
            
#            print(statistics.mean(start_times))
            
#            average_start_time = sum(start_times) / len(start_times)
#            print(average_start_time)
            
            
#            avg_start_time = statistics.mean(start_times)
#            print(avg_start_time)

#
#            print(master_spoutLR_list3)
#            print(master_decision_list)













                    
                    

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
                
                print("Percent Left Correct:", p0_percent_correct)
                print("Percent Right Correct:", p9_percent_correct)
                print(" ")
                
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
                    
                    print("Percent Left Correct:", p0_percent_correct)
                    print("Percent Right Correct:", p7_percent_correct)                    
                    print("left:", count_p0_trials)
                    print("right:", count_p7_trials)
                    print(" ")                    
        else:
            print("Data not available since there are less than 10 trials") 
            print(" ")
            
        del count_trials
        trials_sep.clear()
        p0_trials.clear()
        p9_trials.clear()
        p7_trials.clear()
        
    
    x = (np.hstack(x_results))
    y = (np.hstack(y_results))
#    plt.xlabel('Session Number')
#    plt.ylabel('Percent Correct')
#    plt.axhline(50, color="gray")
    plt.figure(0)
    plt.title('Learning')
#    plt.plot(x,y, "-o")
    plt.plot(x,y)
    #make average trace for figure(delete later)
    y_avg_fig = [47.354342,53.688388,47.16262,47.185804,46.99463,53.091484,54.027736,53.792994,54.979288,67.425886,54.548702,57.06281,60.91894,67.021104,65.569084,69.908066,66.587066,72.324432,73.008308,75.50978,70.947542,69.770354,77.036042,73.947394,73.06758,79.14195,80.24691]
    x_fig = range(1,len(y_avg_fig)+1)
    plt.plot(x_fig,y_avg_fig, 'k')

    listOf_Xticks = [0, 5, 10, 15, 20, 25]
    plt.xticks(listOf_Xticks)
    listOf_Yticks = [50, 60, 70, 80, 90]
    plt.yticks(listOf_Yticks)
    print(y_results)


    
    plt.figure(6)
    plt.title('Learning')
    plt.plot(x,y, "-o")

    
#    print(avg_start_times)
    x = range(len(avg_start_times))
    y = avg_start_times
#    plt.xlabel('Session Number')
#    plt.ylabel('Average Start Time')
    plt.figure(1)
    plt.title('Avg Start Times')
    plt.plot(x,y, "-o")
    
#    print(avg_completion_times)
    x = range(len(avg_completion_times))
    y = avg_completion_times
#    plt.xlabel('Session Number')
#    plt.ylabel('Average Average Time')
    plt.figure(2)
    plt.title('Avg Completion Times')
    plt.plot(x,y, "-o")
    
    #    print(avg_first_reaction_times)
    x = range(len(avg_reaction_times))
    y = avg_reaction_times
#    plt.xlabel('Session Number')
#    plt.ylabel('Average Average Time')
    plt.figure(3)
    plt.title('Avg SpoutLR to Any Reaction Times')
    plt.plot(x,y, "-o")
    
    #    print(avg_LR_reward_times)
    x = range(len(avg_LR_reward_times))
    y = avg_LR_reward_times
#    plt.xlabel('Session Number')
#    plt.ylabel('Average Average Time')
    plt.figure(4)
    plt.suptitle('Avg SpoutLR to Reward Times')
    plt.plot(x,y, "-o")
    
    #    print(avg_decision_times)
    x = range(len(avg_decision_times))
    y = avg_decision_times
#    plt.xlabel('Session Number')
#    plt.ylabel('Average Average Time')
    plt.figure(5)
    plt.suptitle('Avg SpoutLR to any decision Times')
    plt.plot(x,y, "-o")
    
    
    
#%%
def stage_4_multicurve(dataDir, stage, mouse):  

    import os
    import glob
    import re
    import matplotlib.pyplot as plt
    import numpy as np 
    
    trials_sep = []
    p1_trials = []
    p2_trials = []
    p3_trials = []
    p4_trials = []
    p5_trials = []
    p6_trials = []
    p7_trials = []
    p8_trials = []
    p0_trials = []
    p9_trials = []
    att = []
    x_axis = range(0,10)
    x_axis_6p = range(0,8)
    pall_percents = []
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
                

        count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))
        
        count_test0 = sum(1 for match in re.finditer(r"\blight_on_0_1\b", txt))
        count_test1 = sum(1 for match in re.finditer(r"\blight_on_1_1\b", txt))
        count_test2 = sum(1 for match in re.finditer(r"\blight_on_2_1\b", txt))
        count_test3 = sum(1 for match in re.finditer(r"\blight_on_3_1\b", txt))
        count_test4 = sum(1 for match in re.finditer(r"\blight_on_4_1\b", txt))
        count_test5 = sum(1 for match in re.finditer(r"\blight_on_5_1\b", txt))
        count_test6 = sum(1 for match in re.finditer(r"\blight_on_6_1\b", txt))
        count_test7 = sum(1 for match in re.finditer(r"\blight_on_7_1\b", txt))
        count_test8 = sum(1 for match in re.finditer(r"\blight_on_8_1\b", txt))
        count_test9 = sum(1 for match in re.finditer(r"\blight_on_9_1\b", txt))
               
        if 'start_of_new_trial' in txt:
            trials_sep = (re.split(r'start_of_new_trial', txt, flags=re.MULTILINE))
        else:
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
            
        #look for p0 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_0_1 ' in s]
        for i in indices:
            p0_trials.append(trials_sep[i].count("light_on_0_1 "))
            count_p0_trials = len(p0_trials)
            count_correct_p0_trials = p0_trials.count(1)
            p0_decimal_correct = count_correct_p0_trials / count_p0_trials
            p0_percent_correct = p0_decimal_correct * 100
            #print("P0: ", p0_percent_correct)
                
        #look for p9 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_9_1 ' in s]
        for i in indices:
            p9_trials.append(trials_sep[i].count("light_on_9_1 "))
            count_p9_trials = len(p9_trials)
            count_correct_p9_trials = p9_trials.count(1)
            p9_decimal_correct = count_correct_p9_trials / count_p9_trials
            p9_percent_correct = p9_decimal_correct * 100
            #print("P9: ", p9_percent_correct)
        
        #look for p1 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_1_1 ' in s]
        for i in indices:
            p1_trials.append(trials_sep[i].count("light_on_1_1 "))
            count_p1_trials = len(p1_trials)
            count_correct_p1_trials = p1_trials.count(1)
            p1_decimal_correct = count_correct_p1_trials / count_p1_trials
            p1_percent_correct = p1_decimal_correct * 100
        #print("P1: ", p1_percent_correct)
        
        #look for p2 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_2_1 ' in s]
        for i in indices:
            p2_trials.append(trials_sep[i].count("light_on_2_1 "))
            count_p2_trials = len(p2_trials)
            count_correct_p2_trials = p2_trials.count(1)
            p2_decimal_correct = count_correct_p2_trials / count_p2_trials
            p2_percent_correct = p2_decimal_correct * 100
        #print("P2: ", p2_percent_correct)
        
        #look for p3 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_3_1 ' in s]
        for i in indices:
            p3_trials.append(trials_sep[i].count("light_on_3_1 "))
            count_p3_trials = len(p3_trials)
            count_correct_p3_trials = p3_trials.count(1)
            p3_decimal_correct = count_correct_p3_trials / count_p3_trials
            p3_percent_correct = p3_decimal_correct * 100
        #print("P3: ", p3_percent_correct)
        
        #look for p4 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_4_1 ' in s]
        for i in indices:
            p4_trials.append(trials_sep[i].count("light_on_4_1 "))
            count_p4_trials = len(p4_trials)
            count_correct_p4_trials = p4_trials.count(1)
            p4_decimal_correct = count_correct_p4_trials / count_p4_trials
            p4_percent_correct = p4_decimal_correct * 100
        #print("P4: ", p4_percent_correct)
        
        #look for p5 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_5_1 ' in s]
        for i in indices:
            p5_trials.append(trials_sep[i].count("light_on_5_1 "))
            count_p5_trials = len(p5_trials)
            count_correct_p5_trials = p5_trials.count(1)
            p5_decimal_correct = count_correct_p5_trials / count_p5_trials
            p5_percent_correct = p5_decimal_correct * 100
        #print("P5: ", p5_percent_correct)
        
        #look for p6 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_6_1 ' in s]
        for i in indices:
            p6_trials.append(trials_sep[i].count("light_on_6_1 "))
            count_p6_trials = len(p6_trials)
            count_correct_p6_trials = p6_trials.count(1)
            p6_decimal_correct = count_correct_p6_trials / count_p6_trials
            p6_percent_correct = p6_decimal_correct * 100
        #print("P6: ", p6_percent_correct)
        
        #look for p7 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_7_1 ' in s]
        for i in indices:
            p7_trials.append(trials_sep[i].count("light_on_7_1 "))
            count_p7_trials = len(p7_trials)
            count_correct_p7_trials = p7_trials.count(1)
            p7_decimal_correct = count_correct_p7_trials / count_p7_trials
            p7_percent_correct = p7_decimal_correct * 100
        #print("P7: ", p7_percent_correct)
        
        #look for p8 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_8_1 ' in s]
        for i in indices:
            p8_trials.append(trials_sep[i].count("light_on_8_1 "))
            count_p8_trials = len(p8_trials)
            count_correct_p8_trials = p8_trials.count(1)
            p8_decimal_correct = count_correct_p8_trials / count_p8_trials
            p8_percent_correct = p8_decimal_correct * 100

        if count_test9 > count_test7:
            if count_test1 + count_test2 + count_test3 + count_test4 + count_test5 + count_test6 + count_test7 + count_test8 > 10:

                indices = [i for i, s in enumerate(trials_sep) if 'light_on_' in s]
                for i in indices:
                    att.append(trials_sep[i].count("to_state_3_"))
                    count_1st_att = att.count(1)
                    num_incorrect_trials = len(att) - count_1st_att
                    #print(num_incorrect_trials)
                    count_2nd_att = att.count(2)
                    #print(count_2nd_att)
                    if num_incorrect_trials > 0:
                        percent_2nd_att_from_incorrect_trials = (count_2nd_att / num_incorrect_trials) * 100
                        
                print(' ')
                print(os.path.basename(filename))
                print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
                
                
                pall_percents.append(100 - p0_percent_correct)
                pall_percents.append(100 - p1_percent_correct)
                pall_percents.append(100 - p2_percent_correct)
                pall_percents.append(100 - p3_percent_correct)
                pall_percents.append(100 - p4_percent_correct)
                pall_percents.append(p5_percent_correct)
                pall_percents.append(p6_percent_correct)
                pall_percents.append(p7_percent_correct)
                pall_percents.append(p8_percent_correct)
                pall_percents.append(p9_percent_correct)
                
    #            test_count_correct_left = count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials + count_correct_p4_trials
    #            test_count_left = count_p1_trials + count_p2_trials + count_p3_trials + count_p4_trials
    #            test_decimal_correct_left = test_count_correct_left / test_count_left
    #            test_percent_correct_left = test_decimal_correct_left * 100
                
    #            test_count_correct_right = count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials + count_correct_p8_trials
    #            test_count_right = count_p5_trials + count_p6_trials + count_p7_trials + count_p8_trials
    #            test_decimal_correct_right = test_count_correct_right / test_count_right
    #            test_percent_correct_right = test_decimal_correct_right * 100
                
                all_count_correct_left = count_correct_p0_trials + count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials + count_correct_p4_trials
                all_count_left = count_p0_trials + count_p1_trials + count_p2_trials + count_p3_trials + count_p4_trials
                all_decimal_correct_left = all_count_correct_left / all_count_left
                all_percent_correct_left = all_decimal_correct_left * 100
                
                all_count_correct_right = count_correct_p9_trials + count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials + count_correct_p8_trials
                all_count_right = count_p9_trials + count_p5_trials + count_p6_trials + count_p7_trials + count_p8_trials
                all_decimal_correct_right = all_count_correct_right / all_count_right
                all_percent_correct_right = all_decimal_correct_right * 100
                #print("Testing Percent Correct Left: ", test_percent_correct_left)
                #print("Testing Percent Correct Right: ", test_percent_correct_right)
                #print(" ")
                print("Number of trials: ", count_trials)
                print("Total Percent Correct Left: ", all_percent_correct_left)
                print("Total Percent Correct Right: ", all_percent_correct_right)
    
                #print(pall_percents)
                x = (np.hstack(x_axis))
                y = (np.hstack(pall_percents))
                plt.xlabel('Left to Right Light Displays')
                plt.ylabel('Percent Lick Right')
                plt.axhline(50, color="gray")
                plt.plot(x,y)
            
        elif count_test7 > count_test9:
            if count_test1 + count_test2 + count_test3 + count_test4 + count_test5 + count_test6:
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_' in s]
                for i in indices:
                    att.append(trials_sep[i].count("to_state_3_"))
                    count_1st_att = att.count(1)
                    num_incorrect_trials = len(att) - count_1st_att
                    #print(num_incorrect_trials)
                    count_2nd_att = att.count(2)
                    #print(count_2nd_att)
                    if num_incorrect_trials > 0:
                        percent_2nd_att_from_incorrect_trials = (count_2nd_att / num_incorrect_trials) * 100
    
                print(' ')
                print(os.path.basename(filename))
                print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
                
                
                pall_percents.append(100 - p0_percent_correct)
                pall_percents.append(100 - p1_percent_correct)
                pall_percents.append(100 - p2_percent_correct)
                pall_percents.append(100 - p3_percent_correct)
                pall_percents.append(p4_percent_correct)
                pall_percents.append(p5_percent_correct)
                pall_percents.append(p6_percent_correct)
                pall_percents.append(p7_percent_correct)
                
                all_count_correct_left = count_correct_p0_trials + count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials
                all_count_left = count_p0_trials + count_p1_trials + count_p2_trials + count_p3_trials
                all_decimal_correct_left = all_count_correct_left / all_count_left
                all_percent_correct_left = all_decimal_correct_left * 100
                
                all_count_correct_right = count_correct_p4_trials + count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials
                all_count_right = count_p4_trials + count_p5_trials + count_p6_trials + count_p7_trials
                all_decimal_correct_right = all_count_correct_right / all_count_right
                all_percent_correct_right = all_decimal_correct_right * 100
                #print("Testing Percent Correct Left: ", test_percent_correct_left)
                #print("Testing Percent Correct Right: ", test_percent_correct_right)
                #print(" ")
                print("Number of trials: ", count_trials)
                print("Total Percent Correct Left: ", all_percent_correct_left)
                print("Total Percent Correct Right: ", all_percent_correct_right)
    
                #print(pall_percents)
                x = (np.hstack(x_axis_6p))
                y = (np.hstack(pall_percents))
                plt.xlabel('Left to Right Light Displays')
                plt.ylabel('Percent Lick Right')
                plt.axhline(50, color="gray")
                plt.plot(x,y)
            
        else:
            print("Data not available") 
            
        del count_trials
        trials_sep.clear()
        p0_trials.clear()
        p9_trials.clear()
        p1_trials.clear()
        p2_trials.clear()
        p3_trials.clear()
        p4_trials.clear()
        p5_trials.clear()
        p6_trials.clear()
        p7_trials.clear()
        p8_trials.clear()
        p0_trials.clear()
        p9_trials.clear()
        att.clear()
        pall_percents.clear()
#%%
def stage_4_singlecurve(dataDir, stage, mouse):  

    import os
    import glob
    import re
    import matplotlib.pyplot as plt
    import numpy as np 
    
    
    trials_sep = []
    p1_trials = []
    p2_trials = []
    p3_trials = []
    p4_trials = []
    p5_trials = []
    p6_trials = []
    p7_trials = []
    p8_trials = []
    p0_trials = []
    p9_trials = []
    att = []
    x_axis = range(0,10)
    x_axis_6p = range(0,8)
    pall_percents = []
    
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
            

        
#        list_files = os.listdir(filepath)
#        number_of_files = len(list_files)
                

        count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))
        
        count_test1 = sum(1 for match in re.finditer(r"\blight_on_1_1\b", txt))
        count_test2 = sum(1 for match in re.finditer(r"\blight_on_2_1\b", txt))
        count_test3 = sum(1 for match in re.finditer(r"\blight_on_3_1\b", txt))
        count_test4 = sum(1 for match in re.finditer(r"\blight_on_4_1\b", txt))
        count_test5 = sum(1 for match in re.finditer(r"\blight_on_5_1\b", txt))
        count_test6 = sum(1 for match in re.finditer(r"\blight_on_6_1\b", txt))
        count_test7 = sum(1 for match in re.finditer(r"\blight_on_7_1\b", txt))
        count_test8 = sum(1 for match in re.finditer(r"\blight_on_8_1\b", txt))
        count_test9 = sum(1 for match in re.finditer(r"\blight_on_9_1\b", txt))
               
        if 'start_of_new_trial' in txt:
            trials_sep = (re.split(r'start_of_new_trial', txt, flags=re.MULTILINE))
        else:
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
            
        #look for p0 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_0_1 ' in s]
        for i in indices:
            p0_trials.append(trials_sep[i].count("light_on_0_1"))
            count_p0_trials = len(p0_trials)
            count_correct_p0_trials = p0_trials.count(1)
            p0_decimal_correct = count_correct_p0_trials / count_p0_trials
            p0_percent_correct = p0_decimal_correct * 100
            #print("P0: ", p0_percent_correct)
                
        #look for p9 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_9_1 ' in s]
        for i in indices:
            p9_trials.append(trials_sep[i].count("light_on_9_1 "))
            count_p9_trials = len(p9_trials)
            count_correct_p9_trials = p9_trials.count(1)
            p9_decimal_correct = count_correct_p9_trials / count_p9_trials
            p9_percent_correct = p9_decimal_correct * 100
            #print("P9: ", p9_percent_correct)
        
        #look for p1 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_1_1 ' in s]
        for i in indices:
            p1_trials.append(trials_sep[i].count("light_on_1_1 "))
            count_p1_trials = len(p1_trials)
            count_correct_p1_trials = p1_trials.count(1)
            p1_decimal_correct = count_correct_p1_trials / count_p1_trials
            p1_percent_correct = p1_decimal_correct * 100
        #print("P1: ", p1_percent_correct)
        
        #look for p2 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_2_1 ' in s]
        for i in indices:
            p2_trials.append(trials_sep[i].count("light_on_2_1 "))
            count_p2_trials = len(p2_trials)
            count_correct_p2_trials = p2_trials.count(1)
            p2_decimal_correct = count_correct_p2_trials / count_p2_trials
            p2_percent_correct = p2_decimal_correct * 100
        #print("P2: ", p2_percent_correct)
        
        #look for p3 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_3_1 ' in s]
        for i in indices:
            p3_trials.append(trials_sep[i].count("light_on_3_1 "))
            count_p3_trials = len(p3_trials)
            count_correct_p3_trials = p3_trials.count(1)
            p3_decimal_correct = count_correct_p3_trials / count_p3_trials
            p3_percent_correct = p3_decimal_correct * 100
        #print("P3: ", p3_percent_correct)
        
        #look for p4 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_4_1 ' in s]
        for i in indices:
            p4_trials.append(trials_sep[i].count("light_on_4_1 "))
            count_p4_trials = len(p4_trials)
            count_correct_p4_trials = p4_trials.count(1)
            p4_decimal_correct = count_correct_p4_trials / count_p4_trials
            p4_percent_correct = p4_decimal_correct * 100
        #print("P4: ", p4_percent_correct)
        
        #look for p5 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_5_1 ' in s]
        for i in indices:
            p5_trials.append(trials_sep[i].count("light_on_5_1 "))
            count_p5_trials = len(p5_trials)
            count_correct_p5_trials = p5_trials.count(1)
            p5_decimal_correct = count_correct_p5_trials / count_p5_trials
            p5_percent_correct = p5_decimal_correct * 100
        #print("P5: ", p5_percent_correct)
        
        #look for p6 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_6_1 ' in s]
        for i in indices:
            p6_trials.append(trials_sep[i].count("light_on_6_1 "))
            count_p6_trials = len(p6_trials)
            count_correct_p6_trials = p6_trials.count(1)
            p6_decimal_correct = count_correct_p6_trials / count_p6_trials
            p6_percent_correct = p6_decimal_correct * 100
        #print("P6: ", p6_percent_correct)
        
        #look for p7 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_7_1 ' in s]
        for i in indices:
            p7_trials.append(trials_sep[i].count("light_on_7_1 "))
            count_p7_trials = len(p7_trials)
            count_correct_p7_trials = p7_trials.count(1)
            p7_decimal_correct = count_correct_p7_trials / count_p7_trials
            p7_percent_correct = p7_decimal_correct * 100
        #print("P7: ", p7_percent_correct)
        
        #look for p8 trials
        indices = [i for i, s in enumerate(trials_sep) if 'light_on_8_1 ' in s]
        for i in indices:
            p8_trials.append(trials_sep[i].count("light_on_8_1 "))
            count_p8_trials = len(p8_trials)
            count_correct_p8_trials = p8_trials.count(1)
            p8_decimal_correct = count_correct_p8_trials / count_p8_trials
            p8_percent_correct = p8_decimal_correct * 100

        if count_test9 > count_test7:
            if count_test1 + count_test2 + count_test3 + count_test4 + count_test5 + count_test6 + count_test7 + count_test8 > 10:

                indices = [i for i, s in enumerate(trials_sep) if 'light_on_' in s]
                for i in indices:
                    att.append(trials_sep[i].count("to_state_3_"))
                    count_1st_att = att.count(1)
                    num_incorrect_trials = len(att) - count_1st_att
                    #print(num_incorrect_trials)
                    count_2nd_att = att.count(2)
                    #print(count_2nd_att)
                    if num_incorrect_trials > 0:
                        percent_2nd_att_from_incorrect_trials = (count_2nd_att / num_incorrect_trials) * 100
    
#                print(' ')
#                print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
                
                
                pall_percents.append(100 - p0_percent_correct)
                pall_percents.append(100 - p1_percent_correct)
                pall_percents.append(100 - p2_percent_correct)
                pall_percents.append(100 - p3_percent_correct)
                pall_percents.append(100 - p4_percent_correct)
                pall_percents.append(p5_percent_correct)
                pall_percents.append(p6_percent_correct)
                pall_percents.append(p7_percent_correct)
                pall_percents.append(p8_percent_correct)
                pall_percents.append(p9_percent_correct)
                
    #            test_count_correct_left = count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials + count_correct_p4_trials
    #            test_count_left = count_p1_trials + count_p2_trials + count_p3_trials + count_p4_trials
    #            test_decimal_correct_left = test_count_correct_left / test_count_left
    #            test_percent_correct_left = test_decimal_correct_left * 100
                
    #            test_count_correct_right = count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials + count_correct_p8_trials
    #            test_count_right = count_p5_trials + count_p6_trials + count_p7_trials + count_p8_trials
    #            test_decimal_correct_right = test_count_correct_right / test_count_right
    #            test_percent_correct_right = test_decimal_correct_right * 100
                
                all_count_correct_left = count_correct_p0_trials + count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials + count_correct_p4_trials
                all_count_left = count_p0_trials + count_p1_trials + count_p2_trials + count_p3_trials + count_p4_trials
                all_decimal_correct_left = all_count_correct_left / all_count_left
                all_percent_correct_left = all_decimal_correct_left * 100
                
                all_count_correct_right = count_correct_p9_trials + count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials + count_correct_p8_trials
                all_count_right = count_p9_trials + count_p5_trials + count_p6_trials + count_p7_trials + count_p8_trials
                all_decimal_correct_right = all_count_correct_right / all_count_right
                all_percent_correct_right = all_decimal_correct_right * 100
                #print("Testing Percent Correct Left: ", test_percent_correct_left)
                #print("Testing Percent Correct Right: ", test_percent_correct_right)
                #print(" ")
                print(" ")
                print(os.path.basename(filename))
                print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
                print("Number of trials: ", count_trials)
                print("Total Percent Correct Left: ", all_percent_correct_left)
                print("Total Percent Correct Right: ", all_percent_correct_right)
                plt.figure()
                x = (np.hstack(x_axis))
                y = (np.hstack(pall_percents))
                plt.xlabel('Left to Right Light Displays')
                plt.ylabel('Percent Lick Right')
                plt.axhline(50, color="gray")
                plt.plot(x,y)   
                
                del count_trials
                trials_sep.clear()
                p0_trials.clear()
                p9_trials.clear()
                p1_trials.clear()
                p2_trials.clear()
                p3_trials.clear()
                p4_trials.clear()
                p5_trials.clear()
                p6_trials.clear()
                p7_trials.clear()
                p8_trials.clear()
                p0_trials.clear()
                p9_trials.clear()
                att.clear()
                pall_percents.clear()
            
        elif count_test7 > count_test9:
            if count_test1 + count_test2 + count_test3 + count_test4 + count_test5 + count_test6:
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_' in s]
                for i in indices:
                    att.append(trials_sep[i].count("to_state_3_"))
                    count_1st_att = att.count(1)
                    num_incorrect_trials = len(att) - count_1st_att
                    #print(num_incorrect_trials)
                    count_2nd_att = att.count(2)
                    #print(count_2nd_att)
                    if num_incorrect_trials > 0:
                        percent_2nd_att_from_incorrect_trials = (count_2nd_att / num_incorrect_trials) * 100
    
#                print(' ')
#                print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
                
                
                pall_percents.append(100 - p0_percent_correct)
                pall_percents.append(100 - p1_percent_correct)
                pall_percents.append(100 - p2_percent_correct)
                pall_percents.append(100 - p3_percent_correct)
                pall_percents.append(p4_percent_correct)
                pall_percents.append(p5_percent_correct)
                pall_percents.append(p6_percent_correct)
                pall_percents.append(p7_percent_correct)
                
                all_count_correct_left = count_correct_p0_trials + count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials
                all_count_left = count_p0_trials + count_p1_trials + count_p2_trials + count_p3_trials
                all_decimal_correct_left = all_count_correct_left / all_count_left
                all_percent_correct_left = all_decimal_correct_left * 100
                
                all_count_correct_right = count_correct_p4_trials + count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials
                all_count_right = count_p4_trials + count_p5_trials + count_p6_trials + count_p7_trials
                all_decimal_correct_right = all_count_correct_right / all_count_right
                all_percent_correct_right = all_decimal_correct_right * 100
                #print("Testing Percent Correct Left: ", test_percent_correct_left)
                #print("Testing Percent Correct Right: ", test_percent_correct_right)
                #print(" ")
                print(" ")
                print(os.path.basename(filename))
                print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
                print("Number of trials: ", count_trials)
                print("Total Percent Correct Left: ", all_percent_correct_left)
                print("Total Percent Correct Right: ", all_percent_correct_right)
                plt.figure()
                x = (np.hstack(x_axis_6p))
                y = (np.hstack(pall_percents))
                plt.xlabel('Left to Right Light Displays')
                plt.ylabel('Percent Lick Right')
                plt.axhline(50, color="gray")
                plt.plot(x,y)   
                
                del count_trials
                trials_sep.clear()
                p0_trials.clear()
                p9_trials.clear()
                p1_trials.clear()
                p2_trials.clear()
                p3_trials.clear()
                p4_trials.clear()
                p5_trials.clear()
                p6_trials.clear()
                p7_trials.clear()
                p8_trials.clear()
                p0_trials.clear()
                p9_trials.clear()
                att.clear()
                pall_percents.clear()
            
        else:
            print("Data not available") 
#%%
def stage_4_avgcurve(dataDir, stage, mouse):  

    import os
    import glob
    import re
    import matplotlib.pyplot as plt
    import numpy as np
    import statistics
    from scipy import stats
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
    
        trials_sep = []
                
        p1_trials = []
        p2_trials = []
        p3_trials = []
        p4_trials = []
        p5_trials = []
        p6_trials = []
        p7_trials = []
        p8_trials = []
                
        x_axis = range(0,10)
        

        p0_trials = []
        p9_trials = []
        p0_tot = []
        p1_tot = []
        p2_tot = []
        p3_tot = []
        p4_tot = []
        p5_tot = []
        p6_tot = []
        p7_tot = []
        p8_tot = []
        p9_tot = []
        
        
        
        pall_avg = []
        
        all_sem = []
        
        for filename in glob.glob(os.path.join(filepath, '*.txt')):
                with open(filename, 'r') as f:
                    txt = f.read()
                  
        

                
                
#                count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))

               
                
                if 'start_of_new_trial' in txt:
                    trials_sep = (re.split(r'start_of_new_trial', txt, flags=re.MULTILINE))
                else:
                    trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
                    
                
                    
                #look for p0 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_0_1 ' in s]
                for i in indices:
                    p0_trials.append(trials_sep[i].count("light_on_0_1 "))
                    count_p0_trials = len(p0_trials)
                    count_correct_p0_trials = p0_trials.count(1)
                    p0_decimal_correct = count_correct_p0_trials / count_p0_trials
                    p0_percent_correct = p0_decimal_correct * 100
                    #print("P0: ", p0_percent_correct)
                        
                #look for p9 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_9_1 ' in s]
                for i in indices:
                    p9_trials.append(trials_sep[i].count("light_on_9_1 "))
                    count_p9_trials = len(p9_trials)
                    count_correct_p9_trials = p9_trials.count(1)
                    p9_decimal_correct = count_correct_p9_trials / count_p9_trials
                    p9_percent_correct = p9_decimal_correct * 100
                    #print("P9: ", p9_percent_correct)
                
                #look for p1 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_1_1 ' in s]
                for i in indices:
                    p1_trials.append(trials_sep[i].count("light_on_1_1 "))
                    count_p1_trials = len(p1_trials)
                    count_correct_p1_trials = p1_trials.count(1)
                    p1_decimal_correct = count_correct_p1_trials / count_p1_trials
                    p1_percent_correct = p1_decimal_correct * 100
                #print("P1: ", p1_percent_correct)
                
                #look for p2 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_2_1 ' in s]
                for i in indices:
                    p2_trials.append(trials_sep[i].count("light_on_2_1 "))
                    count_p2_trials = len(p2_trials)
                    count_correct_p2_trials = p2_trials.count(1)
                    p2_decimal_correct = count_correct_p2_trials / count_p2_trials
                    p2_percent_correct = p2_decimal_correct * 100
                #print("P2: ", p2_percent_correct)
                
                #look for p3 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_3_1 ' in s]
                for i in indices:
                    p3_trials.append(trials_sep[i].count("light_on_3_1 "))
                    count_p3_trials = len(p3_trials)
                    count_correct_p3_trials = p3_trials.count(1)
                    p3_decimal_correct = count_correct_p3_trials / count_p3_trials
                    p3_percent_correct = p3_decimal_correct * 100
                #print("P3: ", p3_percent_correct)
                
                #look for p4 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_4_1 ' in s]
                for i in indices:
                    p4_trials.append(trials_sep[i].count("light_on_4_1 "))
                    count_p4_trials = len(p4_trials)
                    count_correct_p4_trials = p4_trials.count(1)
                    p4_decimal_correct = count_correct_p4_trials / count_p4_trials
                    p4_percent_correct = p4_decimal_correct * 100
                #print("P4: ", p4_percent_correct)
                
                #look for p5 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_5_1 ' in s]
                for i in indices:
                    p5_trials.append(trials_sep[i].count("light_on_5_1 "))
                    count_p5_trials = len(p5_trials)
                    count_correct_p5_trials = p5_trials.count(1)
                    p5_decimal_correct = count_correct_p5_trials / count_p5_trials
                    p5_percent_correct = p5_decimal_correct * 100
                #print("P5: ", p5_percent_correct)
                
                #look for p6 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_6_1 ' in s]
                for i in indices:
                    p6_trials.append(trials_sep[i].count("light_on_6_1 "))
                    count_p6_trials = len(p6_trials)
                    count_correct_p6_trials = p6_trials.count(1)
                    p6_decimal_correct = count_correct_p6_trials / count_p6_trials
                    p6_percent_correct = p6_decimal_correct * 100
                #print("P6: ", p6_percent_correct)
                
                #look for p7 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_7_1 ' in s]
                for i in indices:
                    p7_trials.append(trials_sep[i].count("light_on_7_1 "))
                    count_p7_trials = len(p7_trials)
                    count_correct_p7_trials = p7_trials.count(1)
                    p7_decimal_correct = count_correct_p7_trials / count_p7_trials
                    p7_percent_correct = p7_decimal_correct * 100
                #print("P7: ", p7_percent_correct)
                
                #look for p8 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_8_1 ' in s]
                for i in indices:
                    p8_trials.append(trials_sep[i].count("light_on_8_1 "))
                    count_p8_trials = len(p8_trials)
                    count_correct_p8_trials = p8_trials.count(1)
                    p8_decimal_correct = count_correct_p8_trials / count_p8_trials
                    p8_percent_correct = p8_decimal_correct * 100
        
                    
                p0_tot.append(p0_percent_correct)
                    
                p1_tot.append(p1_percent_correct)
                    
                p1_tot.append(p1_percent_correct)
                                
                p2_tot.append(p2_percent_correct)
                                
                p3_tot.append(p3_percent_correct)
                
                p4_tot.append(p4_percent_correct)
                                
                p5_tot.append(p5_percent_correct)
                
                p6_tot.append(p6_percent_correct)
                
                p7_tot.append(p7_percent_correct)
                
                p8_tot.append(p8_percent_correct)
                    
                p9_tot.append(p9_percent_correct)
        
        
        p0_avg = statistics.mean(p0_tot)
        p1_avg = statistics.mean(p1_tot)
        p2_avg = statistics.mean(p2_tot)
        p3_avg = statistics.mean(p3_tot)
        p4_avg = statistics.mean(p4_tot)
        p5_avg = statistics.mean(p5_tot)
        p6_avg = statistics.mean(p6_tot)
        p7_avg = statistics.mean(p7_tot)
        p8_avg = statistics.mean(p8_tot)
        p9_avg = statistics.mean(p9_tot)
        
        pall_avg.append(100 - p0_avg)
        pall_avg.append(100 - p1_avg)
        pall_avg.append(100 - p2_avg)
        pall_avg.append(100 - p3_avg)
        pall_avg.append(100 - p4_avg)
        pall_avg.append(p5_avg)
        pall_avg.append(p6_avg)
        pall_avg.append(p7_avg)
        pall_avg.append(p8_avg)
        pall_avg.append(p9_avg)
        
        all_sem.append(stats.sem(p0_tot))
        all_sem.append(stats.sem(p1_tot))
        all_sem.append(stats.sem(p2_tot))
        all_sem.append(stats.sem(p3_tot))
        all_sem.append(stats.sem(p4_tot))
        all_sem.append(stats.sem(p5_tot))
        all_sem.append(stats.sem(p6_tot))
        all_sem.append(stats.sem(p7_tot))
        all_sem.append(stats.sem(p8_tot))
        all_sem.append(stats.sem(p9_tot))
        
    x = (np.hstack(x_axis))
    y = (np.hstack(pall_avg))
    err = (np.hstack(all_sem))
    plt.xlabel('Left to Right Light Displays')
    plt.ylabel('Percent Lick Right')
    plt.axhline(50, color="gray")
    plt.errorbar(x,y,err)     
#%%
def stage_4_fitavgcurve(dataDir, stage, mouse):  

    import os
    import glob
    import re
    import matplotlib.pyplot as plt
    import numpy as np
    import statistics
    from scipy.optimize import curve_fit
    import scipy as sy
    
    filepath = dataDir + 'stage ' + str(stage) + '//' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
    
        trials_sep = []
                
        p1_trials = []
        p2_trials = []
        p3_trials = []
        p4_trials = []
        p5_trials = []
        p6_trials = []
        p7_trials = []
        p8_trials = []
                
        x_axis = range(0,10)
        
        p0_trials = []
        p9_trials = []
        p0_tot = []
        p1_tot = []
        p2_tot = []
        p3_tot = []
        p4_tot = []
        p5_tot = []
        p6_tot = []
        p7_tot = []
        p8_tot = []
        p9_tot = []
        
        
        
        pall_avg = []
        
        
        for filename in glob.glob(os.path.join(filepath, '*.txt')):
                with open(filename, 'r') as f:
                    txt = f.read()
                  
        
#                start = "to_state_2"
#                end = "to_state_1"
                
                
#                count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))

               
                
                if 'start_of_new_trial' in txt:
                    trials_sep = (re.split(r'start_of_new_trial', txt, flags=re.MULTILINE))
                else:
                    trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
                    
                
                    
                #look for p0 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_0_1 ' in s]
                for i in indices:
                    p0_trials.append(trials_sep[i].count("light_on_0_1 "))
                    count_p0_trials = len(p0_trials)
                    count_correct_p0_trials = p0_trials.count(1)
                    p0_decimal_correct = count_correct_p0_trials / count_p0_trials
                    p0_percent_correct = p0_decimal_correct * 100
                    #print("P0: ", p0_percent_correct)
                        
                #look for p9 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_9_1 ' in s]
                for i in indices:
                    p9_trials.append(trials_sep[i].count("light_on_9_1 "))
                    count_p9_trials = len(p9_trials)
                    count_correct_p9_trials = p9_trials.count(1)
                    p9_decimal_correct = count_correct_p9_trials / count_p9_trials
                    p9_percent_correct = p9_decimal_correct * 100
                    #print("P9: ", p9_percent_correct)
                
                #look for p1 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_1_1 ' in s]
                for i in indices:
                    p1_trials.append(trials_sep[i].count("light_on_1_1 "))
                    count_p1_trials = len(p1_trials)
                    count_correct_p1_trials = p1_trials.count(1)
                    p1_decimal_correct = count_correct_p1_trials / count_p1_trials
                    p1_percent_correct = p1_decimal_correct * 100
                #print("P1: ", p1_percent_correct)
                
                #look for p2 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_2_1 ' in s]
                for i in indices:
                    p2_trials.append(trials_sep[i].count("light_on_2_1 "))
                    count_p2_trials = len(p2_trials)
                    count_correct_p2_trials = p2_trials.count(1)
                    p2_decimal_correct = count_correct_p2_trials / count_p2_trials
                    p2_percent_correct = p2_decimal_correct * 100
                #print("P2: ", p2_percent_correct)
                
                #look for p3 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_3_1 ' in s]
                for i in indices:
                    p3_trials.append(trials_sep[i].count("light_on_3_1 "))
                    count_p3_trials = len(p3_trials)
                    count_correct_p3_trials = p3_trials.count(1)
                    p3_decimal_correct = count_correct_p3_trials / count_p3_trials
                    p3_percent_correct = p3_decimal_correct * 100
                #print("P3: ", p3_percent_correct)
                
                #look for p4 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_4_1 ' in s]
                for i in indices:
                    p4_trials.append(trials_sep[i].count("light_on_4_1 "))
                    count_p4_trials = len(p4_trials)
                    count_correct_p4_trials = p4_trials.count(1)
                    p4_decimal_correct = count_correct_p4_trials / count_p4_trials
                    p4_percent_correct = p4_decimal_correct * 100
                #print("P4: ", p4_percent_correct)
                
                #look for p5 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_5_1 ' in s]
                for i in indices:
                    p5_trials.append(trials_sep[i].count("light_on_5_1 "))
                    count_p5_trials = len(p5_trials)
                    count_correct_p5_trials = p5_trials.count(1)
                    p5_decimal_correct = count_correct_p5_trials / count_p5_trials
                    p5_percent_correct = p5_decimal_correct * 100
                #print("P5: ", p5_percent_correct)
                
                #look for p6 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_6_1 ' in s]
                for i in indices:
                    p6_trials.append(trials_sep[i].count("light_on_6_1 "))
                    count_p6_trials = len(p6_trials)
                    count_correct_p6_trials = p6_trials.count(1)
                    p6_decimal_correct = count_correct_p6_trials / count_p6_trials
                    p6_percent_correct = p6_decimal_correct * 100
                #print("P6: ", p6_percent_correct)
                
                #look for p7 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_7_1 ' in s]
                for i in indices:
                    p7_trials.append(trials_sep[i].count("light_on_7_1 "))
                    count_p7_trials = len(p7_trials)
                    count_correct_p7_trials = p7_trials.count(1)
                    p7_decimal_correct = count_correct_p7_trials / count_p7_trials
                    p7_percent_correct = p7_decimal_correct * 100
                #print("P7: ", p7_percent_correct)
                
                #look for p8 trials
                indices = [i for i, s in enumerate(trials_sep) if 'light_on_8_1 ' in s]
                for i in indices:
                    p8_trials.append(trials_sep[i].count("light_on_8_1 "))
                    count_p8_trials = len(p8_trials)
                    count_correct_p8_trials = p8_trials.count(1)
                    p8_decimal_correct = count_correct_p8_trials / count_p8_trials
                    p8_percent_correct = p8_decimal_correct * 100
        
                    
                p0_tot.append(p0_percent_correct)
                    
                p1_tot.append(p1_percent_correct)
                    
                p1_tot.append(p1_percent_correct)
                                
                p2_tot.append(p2_percent_correct)
                                
                p3_tot.append(p3_percent_correct)
                
                p4_tot.append(p4_percent_correct)
                                
                p5_tot.append(p5_percent_correct)
                
                p6_tot.append(p6_percent_correct)
                
                p7_tot.append(p7_percent_correct)
                
                p8_tot.append(p8_percent_correct)
                    
                p9_tot.append(p9_percent_correct)
        
        
        p0_avg = statistics.mean(p0_tot)
        p1_avg = statistics.mean(p1_tot)
        p2_avg = statistics.mean(p2_tot)
        p3_avg = statistics.mean(p3_tot)
        p4_avg = statistics.mean(p4_tot)
        p5_avg = statistics.mean(p5_tot)
        p6_avg = statistics.mean(p6_tot)
        p7_avg = statistics.mean(p7_tot)
        p8_avg = statistics.mean(p8_tot)
        p9_avg = statistics.mean(p9_tot)
        
        pall_avg.append(100 - p0_avg)
        pall_avg.append(100 - p1_avg)
        pall_avg.append(100 - p2_avg)
        pall_avg.append(100 - p3_avg)
        pall_avg.append(100 - p4_avg)
        pall_avg.append(p5_avg)
        pall_avg.append(p6_avg)
        pall_avg.append(p7_avg)
        pall_avg.append(p8_avg)
        pall_avg.append(p9_avg)
        
           
        
    #fitted pyschometric curve
    d = np.array(x_axis, dtype=float)
    p2 = np.array(pall_avg,  dtype=float) # scale to 0..1
    
    
    LL = pall_avg[0]
    RL = 100 - pall_avg[-1]
    
    
    def pf(x, alpha, beta):
        return LL + (100 - LL - RL) / (1 + np.exp( -(x-alpha)/beta ))
        
        
    par0 = sy.array([0., 1.]) # use some good starting values, reasonable default is [0., 1.]
    par, mcov = curve_fit(pf, d, p2, par0)
    print(par)
    print("Left Lapse Rate:", LL)
    print("Right Lapse Rate:", RL)
    plt.xlabel('Left to Right Light Displays')
    plt.ylabel('Percent Lick Right')
    plt.axhline(50, color="gray")
    plt.plot(d, p2, 'ro')
    plt.plot(d, pf(d, par[0], par[1]))
    plt.show()
#%%
def stage_4_lastfile(dataDir, stage, mouse):  

    import os
#    import glob
    import re
    import matplotlib.pyplot as plt
    import numpy as np 
    
    
#    list_files = []
    trials_sep = []
    p1_trials = []
    p2_trials = []
    p3_trials = []
    p4_trials = []
    p5_trials = []
    p6_trials = []
    p7_trials = []
    p8_trials = []
    p0_trials = []
    p9_trials = []
    att = []
    x_axis = range(0,10)
    x_axis_6p = range(0,8)
    pall_percents = []
    
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
#    for filename in glob.glob(os.path.join(filepath, '*.txt')):
#        latest_file = max(filename, key=os.path.getctime)
#        with open(latest_file, 'r') as f:
#            txt = f.read()
    
#    for filename in glob.glob(os.path.join(filepath, '*.txt')):
#        with open(filename, 'r') as f:
#            atxt = f.read()
#            list_files.append(atxt)
#    last_file = list_files[-1]
#    f = open(last_file)
#    txt = f.read()
    
    list_of_files = os.listdir(filepath) #glob.glob(filepath)
    latest_file = list_of_files[-1] #max(list_of_files, key=os.path.getctime)
    f = open(filepath + '/' + latest_file, 'r')
    txt = f.read()
    
#    for list_of_files in glob.glob(filepath):
#        latest_file = max(list_of_files, key=os.path.getctime)
#        with open(latest_file, 'r') as f:
#            txt = f.read()
            

        
#        list_files.append(os.listdir(filepath))
#        open(list_files[-1], 'r') as f:
#            txt = f.read()
            
#        number_of_files = len(list_files)
                

    count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))
    
    count_test0 = sum(1 for match in re.finditer(r"\blight_on_0_1\b", txt))
    count_test1 = sum(1 for match in re.finditer(r"\blight_on_1_1\b", txt))
    count_test2 = sum(1 for match in re.finditer(r"\blight_on_2_1\b", txt))
    count_test3 = sum(1 for match in re.finditer(r"\blight_on_3_1\b", txt))
    count_test4 = sum(1 for match in re.finditer(r"\blight_on_4_1\b", txt))
    count_test5 = sum(1 for match in re.finditer(r"\blight_on_5_1\b", txt))
    count_test6 = sum(1 for match in re.finditer(r"\blight_on_6_1\b", txt))
    count_test7 = sum(1 for match in re.finditer(r"\blight_on_7_1\b", txt))
    count_test8 = sum(1 for match in re.finditer(r"\blight_on_8_1\b", txt))
    count_test9 = sum(1 for match in re.finditer(r"\blight_on_9_1\b", txt))
           
    if 'start_of_new_trial' in txt:
        trials_sep = (re.split(r'start_of_new_trial', txt, flags=re.MULTILINE))
    else:
        trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
        
    #look for p0 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_0_1 ' in s]
    for i in indices:
        p0_trials.append(trials_sep[i].count("light_on_0_1"))
        count_p0_trials = len(p0_trials)
        count_correct_p0_trials = p0_trials.count(1)
        p0_decimal_correct = count_correct_p0_trials / count_p0_trials
        p0_percent_correct = p0_decimal_correct * 100
        #print("P0: ", p0_percent_correct)
            
    #look for p9 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_9_1 ' in s]
    for i in indices:
        p9_trials.append(trials_sep[i].count("light_on_9_1 "))
        count_p9_trials = len(p9_trials)
        count_correct_p9_trials = p9_trials.count(1)
        p9_decimal_correct = count_correct_p9_trials / count_p9_trials
        p9_percent_correct = p9_decimal_correct * 100
        #print("P9: ", p9_percent_correct)
    
    #look for p1 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_1_1 ' in s]
    for i in indices:
        p1_trials.append(trials_sep[i].count("light_on_1_1 "))
        count_p1_trials = len(p1_trials)
        count_correct_p1_trials = p1_trials.count(1)
        p1_decimal_correct = count_correct_p1_trials / count_p1_trials
        p1_percent_correct = p1_decimal_correct * 100
    #print("P1: ", p1_percent_correct)
    
    #look for p2 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_2_1 ' in s]
    for i in indices:
        p2_trials.append(trials_sep[i].count("light_on_2_1 "))
        count_p2_trials = len(p2_trials)
        count_correct_p2_trials = p2_trials.count(1)
        p2_decimal_correct = count_correct_p2_trials / count_p2_trials
        p2_percent_correct = p2_decimal_correct * 100
    #print("P2: ", p2_percent_correct)
    
    #look for p3 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_3_1 ' in s]
    for i in indices:
        p3_trials.append(trials_sep[i].count("light_on_3_1 "))
        count_p3_trials = len(p3_trials)
        count_correct_p3_trials = p3_trials.count(1)
        p3_decimal_correct = count_correct_p3_trials / count_p3_trials
        p3_percent_correct = p3_decimal_correct * 100
#    print("P3 count:", count_p3_trials)
    print("P3: ", p3_percent_correct)
    
    #look for p4 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_4_1 ' in s]
    for i in indices:
        p4_trials.append(trials_sep[i].count("light_on_4_1 "))
        count_p4_trials = len(p4_trials)
        count_correct_p4_trials = p4_trials.count(1)
        p4_decimal_correct = count_correct_p4_trials / count_p4_trials
        p4_percent_correct = p4_decimal_correct * 100
    #print("P4: ", p4_percent_correct)
    
    #look for p5 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_5_1 ' in s]
    for i in indices:
        p5_trials.append(trials_sep[i].count("light_on_5_1 "))
        count_p5_trials = len(p5_trials)
        count_correct_p5_trials = p5_trials.count(1)
        p5_decimal_correct = count_correct_p5_trials / count_p5_trials
        p5_percent_correct = p5_decimal_correct * 100
    #print("P5: ", p5_percent_correct)
    
    #look for p6 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_6_1 ' in s]
    for i in indices:
        p6_trials.append(trials_sep[i].count("light_on_6_1 "))
        count_p6_trials = len(p6_trials)
        count_correct_p6_trials = p6_trials.count(1)
        p6_decimal_correct = count_correct_p6_trials / count_p6_trials
        p6_percent_correct = p6_decimal_correct * 100
    #print("P6: ", p6_percent_correct)
    
    #look for p7 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_7_1 ' in s]
    for i in indices:
        p7_trials.append(trials_sep[i].count("light_on_7_1 "))
        count_p7_trials = len(p7_trials)
        count_correct_p7_trials = p7_trials.count(1)
        p7_decimal_correct = count_correct_p7_trials / count_p7_trials
        p7_percent_correct = p7_decimal_correct * 100
    #print("P7: ", p7_percent_correct)
    
    #look for p8 trials
    indices = [i for i, s in enumerate(trials_sep) if 'light_on_8_1 ' in s]
    for i in indices:
        p8_trials.append(trials_sep[i].count("light_on_8_1 "))
        count_p8_trials = len(p8_trials)
        count_correct_p8_trials = p8_trials.count(1)
        p8_decimal_correct = count_correct_p8_trials / count_p8_trials
        p8_percent_correct = p8_decimal_correct * 100
    
    if count_test9 > count_test7:
        if count_test1 + count_test2 + count_test3 + count_test4 + count_test5 + count_test6 + count_test7 + count_test8 > 10:
            
            indices = [i for i, s in enumerate(trials_sep) if 'light_on_' in s]
            for i in indices:
                att.append(trials_sep[i].count("to_state_3_"))
                count_1st_att = att.count(1)
                num_incorrect_trials = len(att) - count_1st_att
                #print(num_incorrect_trials)
                count_2nd_att = att.count(2)
                #print(count_2nd_att)
                if num_incorrect_trials > 0:
                    percent_2nd_att_from_incorrect_trials = (count_2nd_att / num_incorrect_trials) * 100
        
        #            print(' ')
        #            print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
            
            
            pall_percents.append(100 - p0_percent_correct)
            pall_percents.append(100 - p1_percent_correct)
            pall_percents.append(100 - p2_percent_correct)
            pall_percents.append(100 - p3_percent_correct)
            pall_percents.append(100 - p4_percent_correct)
            pall_percents.append(p5_percent_correct)
            pall_percents.append(p6_percent_correct)
            pall_percents.append(p7_percent_correct)
            pall_percents.append(p8_percent_correct)
            pall_percents.append(p9_percent_correct)
            
        #            test_count_correct_left = count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials + count_correct_p4_trials
        #            test_count_left = count_p1_trials + count_p2_trials + count_p3_trials + count_p4_trials
        #            test_decimal_correct_left = test_count_correct_left / test_count_left
        #            test_percent_correct_left = test_decimal_correct_left * 100
            
        #            test_count_correct_right = count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials + count_correct_p8_trials
        #            test_count_right = count_p5_trials + count_p6_trials + count_p7_trials + count_p8_trials
        #            test_decimal_correct_right = test_count_correct_right / test_count_right
        #            test_percent_correct_right = test_decimal_correct_right * 100
            
            all_count_correct_left = count_correct_p0_trials + count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials + count_correct_p4_trials
            all_count_left = count_p0_trials + count_p1_trials + count_p2_trials + count_p3_trials + count_p4_trials
            all_decimal_correct_left = all_count_correct_left / all_count_left
            all_percent_correct_left = all_decimal_correct_left * 100
            
            all_count_correct_right = count_correct_p9_trials + count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials + count_correct_p8_trials
            all_count_right = count_p9_trials + count_p5_trials + count_p6_trials + count_p7_trials + count_p8_trials
            all_decimal_correct_right = all_count_correct_right / all_count_right
            all_percent_correct_right = all_decimal_correct_right * 100
            #print("Testing Percent Correct Left: ", test_percent_correct_left)
            #print("Testing Percent Correct Right: ", test_percent_correct_right)
            #print(" ")
        #            print("Number of trials: ", count_trials)
        #            print("Total Percent Correct Left: ", all_percent_correct_left)
        #            print("Total Percent Correct Right: ", all_percent_correct_right)
            
            
            print(" ")
#            print(os.path.basename(filename))
            print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
            print("Number of trials: ", count_trials)
            print("Total Percent Correct Left: ", all_percent_correct_left)
            print("Total Percent Correct Right: ", all_percent_correct_right)
            plt.figure()
            x = (np.hstack(x_axis))
            y = (np.hstack(pall_percents))
            plt.xlabel('Left to Right Light Displays')
            plt.ylabel('Percent Lick Right')
            plt.axhline(50, color="gray")
            plt.plot(x,y)   
            
            del count_trials
            trials_sep.clear()
            p0_trials.clear()
            p9_trials.clear()
            p1_trials.clear()
            p2_trials.clear()
            p3_trials.clear()
            p4_trials.clear()
            p5_trials.clear()
            p6_trials.clear()
            p7_trials.clear()
            p8_trials.clear()
            p0_trials.clear()
            p9_trials.clear()
            att.clear()
            pall_percents.clear()
    elif count_test7 > count_test9:
        if count_test1 + count_test2 + count_test3 + count_test4 + count_test5 + count_test6 > 10:
            
            indices = [i for i, s in enumerate(trials_sep) if 'light_on_' in s]
            for i in indices:
                att.append(trials_sep[i].count("to_state_3_"))
                count_1st_att = att.count(1)
                num_incorrect_trials = len(att) - count_1st_att
                #print(num_incorrect_trials)
                count_2nd_att = att.count(2)
                #print(count_2nd_att)
                if num_incorrect_trials > 0:
                    percent_2nd_att_from_incorrect_trials = (count_2nd_att / num_incorrect_trials) * 100
        
        #            print(' ')
        #            print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
            
            
            pall_percents.append(100 - p0_percent_correct)
            pall_percents.append(100 - p1_percent_correct)
            pall_percents.append(100 - p2_percent_correct)
            pall_percents.append(100 - p3_percent_correct)
            pall_percents.append(p4_percent_correct)
            pall_percents.append(p5_percent_correct)
            pall_percents.append(p6_percent_correct)
            pall_percents.append(p7_percent_correct)
            
        #            test_count_correct_left = count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials + count_correct_p4_trials
        #            test_count_left = count_p1_trials + count_p2_trials + count_p3_trials + count_p4_trials
        #            test_decimal_correct_left = test_count_correct_left / test_count_left
        #            test_percent_correct_left = test_decimal_correct_left * 100
            
        #            test_count_correct_right = count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials + count_correct_p8_trials
        #            test_count_right = count_p5_trials + count_p6_trials + count_p7_trials + count_p8_trials
        #            test_decimal_correct_right = test_count_correct_right / test_count_right
        #            test_percent_correct_right = test_decimal_correct_right * 100
            
            all_count_correct_left = count_correct_p0_trials + count_correct_p1_trials + count_correct_p2_trials + count_correct_p3_trials
            all_count_left = count_p0_trials + count_p1_trials + count_p2_trials + count_p3_trials
            all_decimal_correct_left = all_count_correct_left / all_count_left
            all_percent_correct_left = all_decimal_correct_left * 100
            
            all_count_correct_right = count_correct_p4_trials + count_correct_p5_trials + count_correct_p6_trials + count_correct_p7_trials
            all_count_right = count_p4_trials + count_p5_trials + count_p6_trials + count_p7_trials
            all_decimal_correct_right = all_count_correct_right / all_count_right
            all_percent_correct_right = all_decimal_correct_right * 100
            #print("Testing Percent Correct Left: ", test_percent_correct_left)
            #print("Testing Percent Correct Right: ", test_percent_correct_right)
            #print(" ")
        #            print("Number of trials: ", count_trials)
        #            print("Total Percent Correct Left: ", all_percent_correct_left)
        #            print("Total Percent Correct Right: ", all_percent_correct_right)
            
            
            print(" ")
#            print(os.path.basename(filename))
            print('Percent of 2nd attempts out of all incorrect trials: ', percent_2nd_att_from_incorrect_trials)
            print("Number of trials: ", count_trials)
            print("Total Percent Correct Left: ", all_percent_correct_left)
            print("Total Percent Correct Right: ", all_percent_correct_right)
            plt.figure()
            x = (np.hstack(x_axis_6p))
            y = (np.hstack(pall_percents))
            plt.xlabel('Left to Right Light Displays')
            plt.ylabel('Percent Lick Right')
            plt.axhline(50, color="gray")
            plt.plot(x,y)   
            
            del count_trials
            trials_sep.clear()
            p0_trials.clear()
            p9_trials.clear()
            p1_trials.clear()
            p2_trials.clear()
            p3_trials.clear()
            p4_trials.clear()
            p5_trials.clear()
            p6_trials.clear()
            p7_trials.clear()
            p8_trials.clear()
            p0_trials.clear()
            p9_trials.clear()
            att.clear()
            pall_percents.clear()
            
        
    else:
        print("Data not available since there are less than 10 trials")
#%%
def previous_trial_bias(dataDir, stage, mouse):   
    import os
    import glob
    import re
    
    intended_trials = []
    intended_trials_TF = []
    experimental_trials = []
    c_pos = []
    w_pos = []
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
            
            count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))
            
            count_test7 = sum(1 for match in re.finditer(r"\blight_on_7_1\b", txt))
            count_test9 = sum(1 for match in re.finditer(r"\blight_on_9_1\b", txt))
            
            if count_trials > 10:
            
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
                
                if count_test9 > count_test7:
                    for trial in trials_sep:
                        if re.search(r'\blight_on_0_1\b', trial):
                            intended_trials.append("L")
                        if re.search(r'\blight_on_9_1\b', trial):
                            intended_trials.append("R")
                        if re.search(r'\bto_state_3_2\b', trial):
                            experimental_trials.append("W")
                        else:
                            experimental_trials.append("C")
                
                if count_test7 > count_test9:
                    for trial in trials_sep:
                        if re.search(r'\blight_on_0_1\b', trial):
                            intended_trials.append("L")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")
                        if re.search(r'\blight_on_7_1\b', trial):
                            intended_trials.append("R")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")
                                
                                ###look for test trials too
                                
                        if re.search(r'\blight_on_1_1\b', trial):
                            intended_trials.append("L")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")   
                        if re.search(r'\blight_on_2_1\b', trial):
                            intended_trials.append("L")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")     
                        if re.search(r'\blight_on_3_1\b', trial):
                            intended_trials.append("L")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")     


                        if re.search(r'\blight_on_4_1\b', trial):
                            intended_trials.append("R")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")     
                        if re.search(r'\blight_on_5_1\b', trial):
                            intended_trials.append("R")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")     
                        if re.search(r'\blight_on_6_1\b', trial):
                            intended_trials.append("R")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")                                     
                              
                                

                                
                                
#                        if re.search(r'\bto_state_3_2\b', trial):
#                            experimental_trials.append("W")
#                        else:
#                            experimental_trials.append("C")
                                
                                
                   ### t (for true) is if the intended trial being looked at is the same as the previous intended trial
                   ### f (for false) is if the intended trial being looked at is different than the previous intended trial        
                intended_trials_TF = [ intended_trials[i]==intended_trials[i-1] for i in range(len(intended_trials)) ]
                
                ### give the position of the t's or f's in their respective lists
                t_pos = [i for i, x in enumerate(intended_trials_TF) if x]
                f_pos = [i for i, x in enumerate(intended_trials_TF) if not x]
                
                 ### give location of correction trials (C) and wrong trials (W)               
                for i, j in enumerate(experimental_trials):
                    if j == 'C':
                        c_pos.append(i)
                
                for x, a in enumerate(experimental_trials):
                    if a == 'W':
                        w_pos.append(x)
                
                
            ### for example, number of correct and true trials = the number of trials where the position of the trues is the same as the... 
            ### ...position of the correct trials
                num_t_trials = len(t_pos)
                num_correct_t = (len(set(t_pos).intersection(c_pos)))
#                num_incorrect_t = (len(set(t_pos).intersection(w_pos)))
                
                num_f_trials = len(f_pos)
                num_correct_f = (len(set(f_pos).intersection(c_pos)))
#                num_incorrect_f = (len(set(f_pos).intersection(w_pos)))
                
                
                if num_t_trials > 0 and num_f_trials > 0:
                
                    c_t_percent = (num_correct_t / num_t_trials) * 100
#                    w_t_percent = (num_incorrect_t / num_t_trials) * 100
                    
                    c_f_percent = (num_correct_f / num_f_trials) * 100
#                    w_f_percent = (num_incorrect_f / num_f_trials) * 100   
                    
                    ratio = c_t_percent / c_f_percent
                
                    print(os.path.basename(filename))
                    print("Percent correct when previous trial was the SAME:", c_t_percent)
                    print("Percent correct when previous trial was the DIFFERENT:", c_f_percent)
                    print("same/dif ratio:", ratio)
                    
                    #print("Percent INCORRECT when previous trial was the same:", w_t_percent)
                    print(" ")
                    
#                    print("num t trials", num_t_trials)
#                    print("num correct t", num_correct_t)
#                    print(experimental_trials)
                
                intended_trials.clear()
                intended_trials_TF.clear()
                experimental_trials.clear()
                c_pos.clear()
                w_pos.clear()
            
            else: 
                print("Data not available since there are less than 10 trials")
                print(" ")
#%%
def previous_trial_bias_avg(dataDir, stage, mouse):   
    import os
    import glob
    import re
#    import matplotlib.pyplot as plt
#    import numpy as np 
    
    intended_trials = []
    intended_trials_TF = []
    experimental_trials = []
    c_pos = []
    w_pos = []
    
    total_num_t_trials = []
    total_num_correct_t = []
#    total_num_incorrect_t = []
    total_num_f_trials = []
    total_num_correct_f = []
#    total_num_incorrect_f = []
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
            
            count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))
            
            count_test7 = sum(1 for match in re.finditer(r"\blight_on_7_1\b", txt))
            count_test9 = sum(1 for match in re.finditer(r"\blight_on_9_1\b", txt))
            
            if count_trials > 10:
            
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
                
    #for b and w
    #mark each trial as either a left intended trial (L) or a right intended trial (R)
    #"to_state_3_2" tells us that the mouse's choice AKA experimental trial was wrong (W)
    #if the phrase is not present within the trial, then it was correct (C)
                if count_test9 > count_test7:
                    for trial in trials_sep:
                        if re.search(r'\blight_on_0_1\b', trial):
                            intended_trials.append("L")
                        if re.search(r'\blight_on_9_1\b', trial):
                            intended_trials.append("R")
                        if re.search(r'\blight_on_1_1\b', trial):
                            intended_trials.append("L")                            
                        if re.search(r'\blight_on_2_1\b', trial):
                            intended_trials.append("L")
                        if re.search(r'\blight_on_3_1\b', trial):
                            intended_trials.append("L")
                        if re.search(r'\blight_on_4_1\b', trial):
                            intended_trials.append("L")
                        if re.search(r'\blight_on_5_1\b', trial):
                            intended_trials.append("R")                            
                        if re.search(r'\blight_on_6_1\b', trial):
                            intended_trials.append("R")
                        if re.search(r'\blight_on_7_1\b', trial):
                            intended_trials.append("R")
                        if re.search(r'\blight_on_8_1\b', trial):
                            intended_trials.append("R")                           
                        if re.search(r'\bto_state_3_2\b', trial):
                            experimental_trials.append("W")
                        else:
                            experimental_trials.append("C")
                            
        #for newer mice        
                if count_test7 > count_test9:
                    for trial in trials_sep:
                        if re.search(r'\blight_on_0_1\b', trial):
                            intended_trials.append("L")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")
                        if re.search(r'\blight_on_7_1\b', trial):
                            intended_trials.append("R")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")
                                

                                ###look for test trials too
                                ###Note that incorrect test trials do not have a "to_state_3_2" indicator like the others...
                                ###...so we look for "reward", which tells us the test trial is correct (C)
                                ###if "reward" is not present within the test trial, then it is wrong (W)
                        if re.search(r'\blight_on_1_1\b', trial):
                            intended_trials.append("L")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")   
                        if re.search(r'\blight_on_2_1\b', trial):
                            intended_trials.append("L")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")     
                        if re.search(r'\blight_on_3_1\b', trial):
                            intended_trials.append("L")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")     


                        if re.search(r'\blight_on_4_1\b', trial):
                            intended_trials.append("R")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")     
                        if re.search(r'\blight_on_5_1\b', trial):
                            intended_trials.append("R")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")     
                        if re.search(r'\blight_on_6_1\b', trial):
                            intended_trials.append("R")
                            if re.search(r'\breward\b', trial):
                                experimental_trials.append("C")
                            else:
                                experimental_trials.append("W")                                  
                                
                                
                                
                                
                                
                                
                                
                                
                                
                            
            
                     ### t (for true) is if the intended trial being looked at is the same as the previous intended trial
                     ### f (for false) is if the intended trial being looked at is different than the previous intended trial
                intended_trials_TF = [ intended_trials[i]==intended_trials[i-1] for i in range(len(intended_trials)) ]
                
                ### give the position of the t's or f's in their respective lists
                t_pos = [i for i, x in enumerate(intended_trials_TF) if x]
                f_pos = [i for i, x in enumerate(intended_trials_TF) if not x]
                
                ### give location of correction trials (C) and wrong trials (W)
                for i, j in enumerate(experimental_trials):
                    if j == 'C':
                        c_pos.append(i)
                
                for x, a in enumerate(experimental_trials):
                    if a == 'W':
                        w_pos.append(x)
                                        
                num_t_trials = len(t_pos)
                num_f_trials = len(f_pos)
                
                if num_t_trials > 0 and num_f_trials > 0: 
                    
                    ### for example, number of correct and true trials = the number of trials where the position of the trues is the same as the... 
                    ### ...position of the correct trials
                    
                    num_correct_t = (len(set(t_pos).intersection(c_pos)))
#                    num_incorrect_t = (len(set(t_pos).intersection(w_pos)))
                    
                    num_correct_f = (len(set(f_pos).intersection(c_pos)))
#                   num_incorrect_f = (len(set(f_pos).intersection(w_pos)))
                    
                    total_num_t_trials.append(num_t_trials)
                    total_num_correct_t.append(num_correct_t)
#                    total_num_incorrect_t.append(num_incorrect_t)
                    
                    total_num_f_trials.append(num_f_trials)
                    total_num_correct_f.append(num_correct_f)
#                    total_num_incorrect_f.append(num_incorrect_f)
                
                intended_trials.clear()
                intended_trials_TF.clear()
                experimental_trials.clear()
                c_pos.clear()
                w_pos.clear()            
    
    final_num_t_trials = sum(total_num_t_trials)
    final_num_correct_t = sum(total_num_correct_t)
#    final_num_incorrect_t = sum(total_num_incorrect_t)
    
    final_num_f_trials = sum(total_num_f_trials)
    final_num_correct_f = sum(total_num_correct_f)
#    final_num_incorrect_f = sum(total_num_incorrect_f)
    
    c_t_percent = (final_num_correct_t / final_num_t_trials) * 100
#    w_t_percent = (final_num_incorrect_t / final_num_t_trials) * 100
    
    c_f_percent = (final_num_correct_f / final_num_f_trials) * 100
#    w_f_percent = (num_incorrect_f / num_f_trials) * 100 
    
    ratio = c_t_percent / c_f_percent
           
    print("Percent correct when previous trial was the SAME:", c_t_percent)
#    print("Percent INCORRECT when previous trial was the same:", w_t_percent)
    print("Percent correct when previous trial was the DIFFERENT:", c_f_percent)
    print("same/dif ratio:", ratio)
#%%
def testtrials_previous_trial_bias_avg(dataDir, stage, mouse):   
    import os
    import glob
    import re
    import statistics
#    import matplotlib.pyplot as plt
#    import numpy as np 
    
#    testtrials = []    
    ratios = []
    
#    intended_trials = []
#    intended_trials_TF = []
#    experimental_trials = []
#    c_pos = []
#    w_pos = []
#    ttest_pos = []
#    ftest_pos = []
    
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
            
            intended_trials = []
            intended_trials_TF = []
            experimental_trials = []
            c_pos = []
            w_pos = []
            ttest_pos = []
            ftest_pos = []
            testtrials = []  
            
            count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))
            
            count_test7 = sum(1 for match in re.finditer(r"\blight_on_7_1\b", txt))
            count_test9 = sum(1 for match in re.finditer(r"\blight_on_9_1\b", txt))
            
            if count_trials > 10:
            
                trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
                
    #for older mice cohorts we used such as with w and b
                if count_test9 > count_test7:
                    for trial in trials_sep:                            
                        if re.search(r'\blight_on_0_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("o")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")
                        if re.search(r'\blight_on_9_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("o")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")                         

                                ###look for test trials too
                                
                        if re.search(r'\blight_on_1_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("t")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")   
                        if re.search(r'\blight_on_2_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("t")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")                                   
                        if re.search(r'\blight_on_3_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("t")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")                                   
                        if re.search(r'\blight_on_4_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("t")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")  

                        if re.search(r'\blight_on_5_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("t")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")                                    
                        if re.search(r'\blight_on_6_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("t")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")                                
                        if re.search(r'\blight_on_7_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("t")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")                                
                        if re.search(r'\blight_on_8_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("t")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")                                
                            
                            
                            
                            
      #for newer mice          
                if count_test7 > count_test9:
                    for trial in trials_sep:
                        if re.search(r'\blight_on_0_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("o")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")
                        if re.search(r'\blight_on_7_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("o")
                            if re.search(r'\bto_state_3_2\b', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")
                                

                                ###look for test trials too
                                
                        if re.search(r'\blight_on_1_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("t")
                            if re.search(r'wrong', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")   
                        if re.search(r'\blight_on_2_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("t")
                            if re.search(r'wrong', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")     
                        if re.search(r'\blight_on_3_1\b', trial):
                            intended_trials.append("L")
                            testtrials.append("t")
                            if re.search(r'wrong', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")     


                        if re.search(r'\blight_on_4_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("t")
                            if re.search(r'wrong', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")     
                        if re.search(r'\blight_on_5_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("t")
                            if re.search(r'wrong', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")     
                        if re.search(r'\blight_on_6_1\b', trial):
                            intended_trials.append("R")
                            testtrials.append("t")
                            if re.search(r'wrong', trial):
                                experimental_trials.append("W")
                            else:
                                experimental_trials.append("C")                                  
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                

                #give position of test trials (which were previously marked with 't's ^)
                #give position of non-test trials (which were previously marked with 'o's)
                for i, j in enumerate(testtrials):
                    if j == 't':
                        ttest_pos.append(i)              
                for i, j in enumerate(testtrials):
                    if j == 'o':
                        ftest_pos.append(i)      
                
                
                     ### t (for true) is if the intended trial being looked at is the same as the previous intended trial
                     ### f (for false) is if the intended trial being looked at is different than the previous intended trial                        
                intended_trials_TF = [ intended_trials[i]==intended_trials[i-1] for i in range(len(intended_trials)) ]
                
                ### give the position of the t's or f's in their respective lists
                t_pos = [i for i, x in enumerate(intended_trials_TF) if x]
                f_pos = [i for i, x in enumerate(intended_trials_TF) if not x]
                
               ### give location of correction trials (C) and wrong trials (W)
                for i, j in enumerate(experimental_trials):
                    if j == 'C':
                        c_pos.append(i)
                
                for x, a in enumerate(experimental_trials):
                    if a == 'W':
                        w_pos.append(x)
                                        
#                num_t_trials = len(t_pos)
#                num_f_trials = len(f_pos)
                        
                        
             ### for example, number of correct and true trials = the number of trials where the position of the trues is the same as the... 
             ### ...position of the correct trials      
                tandc_pos2 = []
                tandc_pos2.append(list(set(t_pos).intersection(c_pos)))
                tandc_pos = tandc_pos2[0]

                tandttest_pos2 = []
                tandttest_pos2.append(list(set(t_pos).intersection(ttest_pos)))
                tandttest_pos = tandttest_pos2[0]
                
                fandc_pos2 = []
                fandc_pos2.append(list(set(f_pos).intersection(c_pos)))
                fandc_pos = fandc_pos2[0]
                
                fandttest_pos2 = []
                fandttest_pos2.append(list(set(f_pos).intersection(ttest_pos)))
                fandttest_pos = fandttest_pos2[0]
                
                
                a1 = len(set(tandc_pos).intersection(ttest_pos))
                a2 = len(tandttest_pos)
                b1 = len(set(fandc_pos).intersection(ttest_pos))
                b2 = len(fandttest_pos)
                
                
                ares = a1/a2
                bres = b1/b2
                if bres > 0:
                    ratio = ares/bres
                
                ratios.append(ratio)
                
                testtrials.clear()
                intended_trials.clear()
                intended_trials_TF.clear()
                experimental_trials.clear()
                t_pos.clear()
                w_pos.clear()
                c_pos.clear()
                w_pos.clear()    
                ttest_pos.clear
                ftest_pos.clear
                tandc_pos.clear()
                tandttest_pos.clear()
                fandc_pos.clear()
                fandttest_pos.clear()
                del a1
                del a2
                del b1
                del b2
                del ares
                del bres
     
    print(ratios)           
    avg_ratio = statistics.mean(ratios)
                
           
    print("On test trials only, Percent correct when previous trial was the SAME")
    print("versus")
    print("On test trials only, Percent correct when previous trial was the DIFFERENT")
    print("ratio:", avg_ratio)



#%%
def stage_2_learning_nolickcountreq(dataDir, stage, mouse):   
    import os
    import glob
    import re
    
    intended_trials = []
    experimental_trials = []
    trials_sep = []
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
            
            #get the total number of trials
            count_trials = sum(1 for match in re.finditer(r"\bto_state_2\b", txt))
            
            
            if count_trials > 10:
                
                start = 'to_state_2'
                end = 'reward'
                for i in range(count_trials):
                    trials_sep.append((txt.split(start))[i].split(end)[0])
                
                for trial in trials_sep:
                    
                    count_lckL = trial.count("lckL")
                    count_lckR = trial.count("lckR")
                    
                    if "light_on_0_1 " in trial:
                        intended_trials.append("L")
                        if count_lckR > 0:
                            experimental_trials.append("W")
                        else: 
                            experimental_trials.append("C")
                        
                    if "light_on_7_1 " in trial:
                        intended_trials.append("R")
                        if count_lckL > 0:
                            experimental_trials.append("W")
                        else:
                            experimental_trials.append("C")
                            
#                    if "light_on_0_1" in trial and count_lckR > 0:
#                        experimental_trials.append("W")
#                    if "light_on_0_1" in trial and count_lckR <= 0:
#                        experimental_trials.append("C")
#                    if "light_on_7_1" in trial and count_lckL > 0:
#                        experimental_trials.append("W")
#                    if "light_on_7_1" in trial and count_lckL <= 0:
#                        experimental_trials.append("C")
                            
                num_trials = len(experimental_trials)
                print("Number of trials:", num_trials)
                num_correct = experimental_trials.count("C")
                percent_correct = (num_correct / num_trials) * 100
                print("Percent correct:", percent_correct)
                print("")
                
                experimental_trials.clear()
                intended_trials.clear()
                del num_trials
                del num_correct
                del percent_correct
                
                
#                    
#                    print(os.path.basename(filename))
#                    print("Number of trials:", num_trials)
#                    print('Percent Correct on First Try:', percent_correct)
#                    print(" ")
#                
#                    experimental_trials.clear()
#                    intended_trials.clear()
#                    del num_trials
#                    del num_correct
#                    del percent_correct

#                    num_trials = len(experimental_trials)
#                    num_correct = experimental_trials.count("C")
#                    percent_correct = (num_correct / num_trials) * 100
##                print(experimental_trials)
#                
#                
#                    print(os.path.basename(filename))
#                    print("Number of trials:", num_trials)
#                    print('Percent Correct on First Try:', percent_correct)
#                    print(" ")
                    
#            experimental_trials.clear()
#            intended_trials.clear()
#            del num_trials
#            
#            
#            
##                    del num_correct
##                    del percent_correct
#                    
#
#            
#            else: 
#                print("Data not available since there are less than 10 trials")
#                print(" ")
#    
#%%
def stage_2_trial_counter(dataDir, stage, mouse):   
    import os
    import glob
    import re
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
            
            #get the notes
            edit_notes = (re.split(r'edit:', txt, flags=re.MULTILINE))
            
            #get the total number of trials
            count_trials = sum(1 for match in re.finditer(r"\bstart_of_new_trial\b", txt))
            if count_trials > 10:
                print(os.path.basename(filename))
                for line in txt.split('\n'):
                        if "lick_count_requirement" in line:
                            lick_count = (line.split()[1])
                            print("Lick req: ", lick_count)
                        if "lick_time_requirement" in line:
                            lick_time = (line.split()[1])
                            print("Lick time: ", lick_time)
                if "edit:" in txt:
                    if any(c.isalpha() for c in edit_notes[1]) == True:
                        print(edit_notes[1].strip())
                print("Trial Count:", count_trials)
                print("")
#%%
def stage_4_singlecurve_notestpunish(dataDir, stage, mouse):   
    import os
    import glob
    import re
    import numpy as np
    import matplotlib.pyplot as plt
    
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
    
    x_count = 0
    x_results = []
    y_results = []  
    
    trials_sep = []
    p0_trials = []
    p9_trials = []
    p7_trials =[]
    
    filepath = dataDir + 'stage ' + str(stage) + '/' + mouse
    
    for filename in glob.glob(os.path.join(filepath, '*.txt')):
        with open(filename, 'r') as f:
            txt = f.read()
            
            count_trials = (sum(1 for match in re.finditer(r"\bto_state_2\b", txt))) - 1
            stage_check = sum(1 for match in re.finditer(r"\blight_on_4_1\b", txt))
            
            TRAIN_count_initial_incorrect_trials = sum(1 for match in re.finditer(r"\bto_state_3_2\b", txt))
            TRAIN_count_correct_trials = count_trials - TRAIN_count_initial_incorrect_trials
            
            if stage_check < 3:
        
                if count_trials > 10:
                    decimal_correct = TRAIN_count_correct_trials / count_trials
                    percent_correct = decimal_correct * 100
                    
                
                    x_count = x_count + 1               
                    x_results.append(x_count)
                    y_results.append(percent_correct)
            
                    count_total_attempts = txt.count("to_state_3_")
                    attempts_value = count_total_attempts / count_trials
                    
                    print(os.path.basename(filename))
                    
                    edit_notes = (re.split(r'edit:', txt, flags=re.MULTILINE))
                    
                    #to ignore first 10 trials
        #            start = 'to_state_2'
        #            end = 'ignore'
        #            for i in range(11,count_trials):
        #                trials_sep.append((txt.split(start))[i].split(end)[0])
                    
                    #check for version with new notes
                    if "light8" in txt:
                        for line in txt.split('\n'):    
                            if "lick_count_requirement" in line:
                                lick_count = (line.split()[1])
                            if "lick_time_requirement" in line:
                                lick_time = (line.split()[1])
                            if "ex_duration" in line:
                                ex_dur = (line.split()[1])
                            if "airpuff_duration" in line:
                                airpuff = (line.split()[1])
                            if "per_R" in line:
                                per_R = (line.split()[1])
                            if "punishment_time1" in line:
                                timeout_punishment_dur = (line.split()[1])
                            if "number_of_stim_cycles" in line:
                                number_of_stim_cycles = (line.split()[1])
                            if "stim_cycle_duration" in line:
                                stim_cycle_duration = (line.split()[1])
                            if "stim_duration" in line:
                                stim_duration = (line.split()[1])
                            if "stim_start_delay" in line:
                                stim_start_delay = (line.split()[1])
                            if "spout_available" in line:
                                tsa = (line.split()[1])
                            if "no_test_punishment" in line:
                                no_test_punishment = (line.split()[1])
                            if "tsa_no_reward" in line:
                                tsa_no_reward = (line.split()[1])
                            if "training_reward" in line:
                                no_retrial_reward = (line.split()[1])
                            if "cspout_no_reward" in line:
                                cspout_no_reward = (line.split()[1])
                            if "lights8" in line:
                                p6_mode = (line.split()[1])
                            if "lights2" in line:
                                p2_mode = (line.split()[1])
                            if "training_mode" in line:
                                retrial_mode = (line.split()[1])
                            if "timeout_punishment" in line:
                                timeout_punishment = (line.split()[1])
                            if "punishment_active" in line:
                                wrong_lick_punishment = (line.split()[1])
        #                    if "edit" in line:
        #                        edit = line
                        
                        if float(retrial_mode) > 0:
                            print("retrial mode")
                        if float(no_retrial_reward) > 0:
                            print("no retrial reward")
                        if float(tsa_no_reward) > 0:
                            print("TSA no reward")
                        if float(cspout_no_reward) > 0:
                            print("no c_reward")
                        if float(wrong_lick_punishment) == 0 :
                            print("no wrong lick punishment")
                        print("ex_time: " + ex_dur + ", lick req: " + lick_count + ", lick time: " + lick_time + ", per_R: " + per_R + ", air: " + airpuff + ", timeout_punish: " + timeout_punishment_dur + ", stim delay: " + stim_start_delay + ", TSA: " + tsa + ", num stim cycles: " + number_of_stim_cycles + ", stim cycle dur: " + stim_cycle_duration + ", stim dur: " + stim_duration)
        #                if len(edit.split()) > 1:
        #                    print(edit)
                        if "edit:" in txt:
                            if any(c.isalpha() for c in edit_notes[1]) == True:
                                print(edit_notes[1].strip())
                            
                    
                    #if want to keep first 10 trials
                    if 'start_of_new_trial' in txt:
                        trials_sep = (re.split(r'start_of_new_trial', txt, flags=re.MULTILINE))
                    if 'reward_9 ' in txt:
                        trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
                    elif 'reward_7 ' in txt:
                        trials_sep = (re.split(r'spout_C', txt, flags=re.MULTILINE))
                    
        #            subtract 10 to ignore first 10 trials
                    print("Number of trials:", count_trials)
                    print("percent correct:", percent_correct)
                    print("attempts value:", attempts_value)
        
        
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
                        
                        print("Percent Left Correct:", p0_percent_correct)
                        print("Percent Right Correct:", p9_percent_correct)
                        print(" ")
                        
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
                            
                            print("Percent Left Correct:", p0_percent_correct)
                            print("Percent Right Correct:", p7_percent_correct)
                            print(" ")
                    del count_trials
                    trials_sep.clear()
                    p0_trials.clear()
                    p9_trials.clear()
                    p7_trials.clear()
                            
            elif stage_check > 3:
                if count_trials > 10:
                    trials_sep = (re.split(r'reward_C', txt, flags=re.MULTILINE))
                    for trial in trials_sep:
                        
        #                        count_tostate32 = sum(1 for match in re.finditer(r"\bto_state_3_2\b", trial))
        #                        count_reward = sum(1 for match in re.finditer(r"\breward\b", trial))
                        
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
                    
                    all_perc_cor = (experimental_trials.count("C") / len(experimental_trials)) * 100
                    print("overall percent correct: ", all_perc_cor)
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
                    
                    print("number of trials: ", count_trials)
                    print(p0_count)
                    print(p1_count)
                    print(p2_count)
                    print(p3_count)
                    print(p4_count)
                    print(p5_count)
                    print(p6_count)
                    print(p7_count)
                    
                    
                    print("")
         
                    
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
    for i in range(len(master_p0)):
    
        plt.figure()
        plt.plot(master_array[:,i])
        plt.xlabel('Left to Right Light Displays')
        plt.ylabel('Percent Lick Right')
        plt.axhline(50, color="gray")
    
        print("Left to Right Panels...")
        print(master_array[:,i])
    