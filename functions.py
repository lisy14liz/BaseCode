
def argmin(lst):
    return min(range(len(lst)), key=lst.__getitem__)

import os
import pickle




def get_data(*argv):
    return data
def get_data_and_save_pkl(pkl_filename, get_data, *argv, new_option=False):
    print(new_option)
    if new_option or (not os.path.exists(pkl_filename)):
        print('getting data')
        data = get_data(*argv)
        print('finish getting data')
        try:
            with open(pkl_filename, 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
            print('finish saving dataframe to pickle')
        except Exception as e:
            print(e)
    else:
        try:
            print('loading pickle', pkl_filename)
            with open(pkl_filename, 'rb') as f:
                data = pickle.load(f)
            print('finish loading pickle', pkl_filename)
        except Exception as e:
            print('loading Error:',e)
            return get_data_and_save_pkl(pkl_filename, get_data, *argv,new_option=True)
    return data

def read_file_and_save_pkl(filename, get_data):
    pkl_filename = os.path.splitext(filename)[0]+'.pkl'
    return get_data_and_save_pkl(pkl_filename, get_data, (filename))
