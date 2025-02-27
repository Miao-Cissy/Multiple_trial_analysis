import numpy as np

def rearing_detection(z, height_thresh = 0.6):
    '''
    detect rearing by the height_thresh, if z[i]> = height_thresh, then the time of z[i] if rearing time
    z: array of height in time series
    height_thresh :threshold to determine the rearing
    
    return:
    r: array of index of rearing time
    '''
    
    return np.argwhere(z>= height_thresh).flatten()
    

def generate_tau_sample(before_matrix, tau = 10, step = 2, T = 200, k = 4):
    '''
    generate a matrix of tau length sample by slicing the window along the whole time series
    features: [n,k,T]
    
    n: number of rearing events
    k: number of the features interested in
    
    
    return : array in[n*m, tau*k], m is the number of slice of tau for T long period
    '''
    # determine the size of the final output
    
    # use a time window to slip along T and get slice of tau, combine different features horizontally, 

    num_slice = (T-tau)//step +1  # if step = tau, no overlap
    num_events = before_matrix.shape[0]
    x_matrix = np.zeros((num_events * num_slice, tau * k))


    for i, end_idx in enumerate(np.arange(tau, T+1, step)):

        x_matrix[i*num_events: (i+1)*num_events, :] = np.hstack(np.transpose(before_matrix[:,:,end_idx - tau:end_idx],(1,0,2))) 
    
    
    return x_matrix