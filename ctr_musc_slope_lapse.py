
    import os
    import glob
    import re
    import numpy as np
    import matplotlib.pyplot as plt
    
    mouse = ['c1', 'c1/musc']
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
    
    x_count = 0
    x_results = []
    y_results = []  
    
    trials_sep = []
    p0_trials = []
    p9_trials = []
    p7_trials =[]
    
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
    