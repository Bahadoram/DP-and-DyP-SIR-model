from initialize import initial_conf
from algorithm import update_conf, scaling_timegrid, normalize_timegrid
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
            real_time = 0

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
    for N in L_list:
        init_conf = initial_conf(N, 1, 2)
        config = init_conf.copy()
        e_r_l = []
        e_s_r = []
        for ens in np.arange(average_over):   
            config = init_conf.copy()
            rec_list   = []
            for t in np.arange(10000):
                if np.count_nonzero(config == 1)==0:
                    break
                config, rec_list = update_conf(config, critic_ratio, 2, rec_list, p_2)
            e_r_l.append(len(rec_list))                  
            e_s_r.append(len(rec_list)**2)

        big_recovered_list.append(np.mean(e_r_l))        
        big_squared_recovered.append(np.mean(e_s_r)) 
    return(big_recovered_list, big_squared_recovered)

"""for finding Niu, the big loop over different length and different ratios"""
def main_nu(L_list, ratio_list, average_over, p_2, c_r, est_GammaNu):
    Y_list =             []
    rec_list =           []
    for L in L_list:
        big_recovered_list = []
        y_list = []
        for ratio in ratio_list:
            init_conf = initial_conf(L, 1, 2)
            config = init_conf.copy()
            e_r_l = []
            for ens in np.arange(average_over): 
                config = init_conf.copy()
                rec_list   = []
                for t in np.arange(10000):
                    if np.count_nonzero(config == 1)==0:
                        break
                    config, rec_list = update_conf(config, ratio, 2, rec_list, p_2)
                e_r_l.append(len(rec_list)) 
            big_recovered_list.append(np.mean(e_r_l))   
            y_list.append(np.mean(e_r_l) * (L** est_GammaNu))   
        Y_list.append(y_list)
    return(Y_list)


"""For epoch analysis in the case of DyP"""
def main_epoch(N, time_steps, ratio_list, avg, p_2):
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
            scaled_timegrid = scaling_timegrid(epoch_list)
            epoch_list      = normalize_timegrid(N, scaled_timegrid, epoch_list)[0]
            Epoch_list.append(epoch_list)
        Epoch_list = [x[:np.min([len(l) for l in Epoch_list])] for x in Epoch_list] #equal length for different ens
        big_epoch_list.append(np.mean(Epoch_list, axis = 0))   
    return(big_epoch_list)