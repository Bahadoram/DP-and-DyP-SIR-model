from initialize import initial_conf
from algorithm import update_conf
import numpy as np

"""for tau and critical ratio estimation """
def main_tau(N, ratio_list, average_over, p_2):
    init_conf = initial_conf(N, 1, 2)
    rec_list =           []
    big_cluster_list   = []
    for ratio in ratio_list:
        config = init_conf.copy()
        each_cluster_list   = []
        for ens in np.arange(average_over):
            config = init_conf.copy()
            rec_list   = []
            for t in np.arange(10000):
                if np.count_nonzero(config == 1)==0:
                    break
                config, rec_list = update_conf(config, ratio, 2, rec_list, p_2)
            each_cluster_list.append(len(rec_list))
        big_cluster_list.append(each_cluster_list) 
    return(big_cluster_list)           

"""for mean number of recovered,<Nr> per length,L """
def main_gamma_nu(L_list, average_over, p_2, critic_ratio):
    big_recovered_list = []
    big_squared_recovered = []
    rec_list =           []
    for N in np.arange(10,70,6):
        init_conf = initial_conf(N, 1, 2)
        config = init_conf.copy()
        each_recovered_list = []
        each_squared_recovered = []
        for ens in np.arange(average_over):   
            config = init_conf.copy()
            rec_list   = []
            for t in np.arange(10000):
                if np.count_nonzero(config == 1)==0:
                    break
                config, rec_list = update_conf(config, critic_ratio, 2, rec_list, p_2)
            each_recovered_list.append(len(rec_list))                  
            each_squared_recovered.append(len(rec_list)**2)
        big_recovered_list.append(np.mean(each_recovered_list))        
        big_squared_recovered.append(np.mean(each_squared_recovered)) 
    return(big_recovered_list, big_squared_recovered)

"""for finding Niu, the big loop over different length and different ratios"""
def main_nu(L_list, ratio_list, average_over, p_2, c_r):
    Y_list =             []
    rec_list =           []
    for L in [10,20,40,60]:
        big_recovered_list = []
        y_list = []
        for ratio in np.linspace(1, 9 , 5):
            init_conf = initial_conf(L, 1, 2)
            config = init_conf.copy()
            each_recovered_list = []
            for ens in np.arange(average_over): 
                config = init_conf.copy()
                rec_list   = []
                for t in np.arange(10000):
                    if np.count_nonzero(config == 1)==0:
                        break
                    config, rec_list = update_conf(config, c_r, 2, rec_list, p_2)
                each_recovered_list.append(len(rec_list))              
            big_recovered_list.append(np.mean(each_recovered_list))   
            y_list.append(np.mean(each_recovered_list) * (L** 2.157))   
        Y_list.append(y_list)
    return(Y_list)

def main_theta(N, time_steps, ratio_list, avg, p_2):
    init_conf = initial_conf(N, 1,  2)
    rec_list =           []
    big_epoch_list =     []
    for ratio in ratio_list:
        config = init_conf.copy()
        Epoch_list =          []
        for ens in np.arange(avg):
            config = init_conf.copy()
            epoch_list = []
            rec_list   = []
            for t in time_steps:
                # if np.count_nonzero(config == 1)==0:
                #     break
                config, rec_list = update_conf(config, ratio, 2, rec_list, p_2)
                epoch_list.append(np.count_nonzero(config == 1))
            Epoch_list.append(epoch_list)
        big_epoch_list.append(np.mean(Epoch_list, axis = 0))   
    return(big_epoch_list)