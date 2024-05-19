import numpy as np
import argparse
import config.folder_and_file_names as fname

# 12中不同的隐私预算分配
# generated_tras1.dat：[0.2, 0.4, 0.4]
# generated_tras2.dat：[0.2, 0.4, 0.4]
# generated_tras3.dat：[0.2, 0.52, 0.28]
# generated_tras4.dat：[0.3, 0.4, 0.3]
# generated_tras5.dat：[0.1. 0.5, 0.4]
# generated_tras6.dat：[0.2, 0.6, 0.2]		 best
# generated_tras7.dat：[0.15, 0.7, 0.15]
# generated_tras8.dat：[0.3, 0.35, 0.35]
# generated_tras9.dat：[0.2, 0.55, 0.25]
# generated_tras10.dat：[0.18, 0.58, 0.24]
# generated_tras11.dat：[0.17, 0.6, 0.23]
# generated_tras12.dat：[0.16, 0.61, 0.23]
class ParSetter:

    def __init__(self):
        pass

    def set_up_args(self, dataset_file_name=None, epsilon=False, epsilon_partition=False, level1_parameter=False, level2_parameter=False):
        parser = argparse.ArgumentParser()
        parser.add_argument('--dataset_file_name', type=str, default=fname.dataset_file_name)
        parser.add_argument('--subdividing_inner_parameter', type=float, default=200)
        parser.add_argument('--total_epsilon', type=float, default=2.0)
        # regularly, partition solution is suggested to be np.array([0.2, 0.52, 0.28]))
        parser.add_argument('--epsilon_partition', type=np.ndarray, default=np.array([0.2, 0.6, 0.2]))
        # this parameter indicates how many trajectories to generate
        parser.add_argument('--trajectory_number_to_generate', type=int, default=-1)
        args = vars(parser.parse_args())
        if epsilon is not False:
            args['total_epsilon'] = epsilon
        if epsilon_partition is not False:
            args['epsilon_partition'] = epsilon_partition
        if level1_parameter is not False:
            args['level1_divide_inner_parameter'] = level1_parameter
        if level2_parameter is not False:
            args['subdividing_inner_parameter'] = level2_parameter
        if dataset_file_name is not None:
            args['dataset_file_name'] = dataset_file_name
        print(args)
        return args




