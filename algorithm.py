import numpy as np

def normalize_probs(inf_prob, rec_prob):
    return(inf_prob/(inf_prob+rec_prob), rec_prob/(inf_prob+rec_prob))

def infection_rate(rec_rate, ratio, n, d): #for the old algorithm 
    return(rec_rate* ratio * (n/(2*d)))

def update_conf(conf, ratio,  d, rec_list, p_2):
    if d==1:
        try:
            chosen_inx = np.random.choice(np.where(conf==1)[0])
        except ValueError:
            return(conf, rec_list)
        
        rec_rate = 1/(1+ratio)

        if np.random.rand() < rec_rate:
            conf[chosen_inx] = 0
        else:
            if chosen_inx == np.shape(conf)[0] - 1:
                conf[np.random.choice([0, np.shape(conf)[0] - 2])] = int(1)
            else:
                conf[np.random.choice([chosen_inx - 1, chosen_inx + 1])] = 1

    elif d==2:
        try:
            candids = list(zip(np.where(conf==1)[0],np.where(conf==1)[1]))
            chosen_inx = candids[np.random.choice([i for i in range(len(candids))])]
        except ValueError:
            return(conf, rec_list)
        
        rec_rate = int(1)/(1+ratio)

        if np.random.rand() < rec_rate:
            conf[chosen_inx[0], chosen_inx[1]] = int(0)
            if [chosen_inx[0], chosen_inx[1]] not in rec_list:
                rec_list.append([chosen_inx[0], chosen_inx[1]])
        
        else:
            direct = np.random.choice(['N', 'S', 'W', 'E'])

            if direct=='N': 
                if [chosen_inx[0] -1, chosen_inx[1]] in rec_list:
                    if np.random.rand() < p_2:
                        conf[chosen_inx[0] -1, chosen_inx[1] ] = int(1)
                else:
                        conf[chosen_inx[0] -1, chosen_inx[1] ] = int(1)            

            elif direct=='W': 
                if [chosen_inx[0] , chosen_inx[1] - 1] in rec_list:
                    if np.random.rand() < p_2:
                        conf[chosen_inx[0] , chosen_inx[1] - 1]= int(1)
                else:
                    conf[chosen_inx[0] , chosen_inx[1] - 1]= int(1)

            elif direct=='S': 
                if chosen_inx[0]==np.shape(conf)[0] -1: 
                    if [0, chosen_inx[1]] in rec_list:
                        if np.random.rand() < p_2:
                            conf[0, chosen_inx[1]] = int(1)
                    else:
                        conf[0, chosen_inx[1]] = int(1)

                else: 
                    if [chosen_inx[0] -1, chosen_inx[1]] in rec_list:
                        if np.random.rand() < p_2:
                            conf[chosen_inx[0] -1, chosen_inx[1] ] = int(1)
                    else:
                        conf[chosen_inx[0] -1, chosen_inx[1] ] = int(1)

            elif direct=='E': 
                if chosen_inx[1]==np.shape(conf)[1] -1: 
                    if [chosen_inx[0], 0] in rec_list:
                        if np.random.rand() < p_2:
                            conf[chosen_inx[0], 0] = int(1)
                    else:
                        conf[chosen_inx[0], 0] = int(1)

                else:
                    if [chosen_inx[0] , chosen_inx[1] + 1] in rec_list:
                        if np.random.rand() < p_2:
                            conf[chosen_inx[0] , chosen_inx[1] + 1] = int(1)
                    else:
                        conf[chosen_inx[0] , chosen_inx[1] + 1] = int(1)
                        
    return(conf, rec_list)
