import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F

class Policy:
    def __init__(self) -> None:
        env_param = {
            'obs': 26, 
            'goal': 3, 
            'action': 8, 
            'action_max': 1.0
        }
        self.actor_network = actor(env_params=env_param)
        pass
    
    def obs_parser(self, x):
        task_obs_size = 12 * 1 # number of blocks
        goal_size = 3 * 1 # number of blocks
        # robot0
        robot0_obs = x[..., :self.robot_obs_size_0]
        # robot0_pos = robot0_obs[..., :3]
        # robot0_vel = robot0_obs[..., 3:6]
        # robot0_finger = robot0_obs[..., 6]
        # robot1
        robot1_obs = x[..., self.robot_obs_size_0:self.robot_obs_size]
        # robot1_pos = robot1_obs[..., :3]
        # robot1_vel = robot1_obs[..., 3:6]
        # robot1_finger = robot1_obs[..., 6]
        # task
        task_obs = x[..., self.robot_obs_size:self.robot_obs_size+task_obs_size]
        # obj_pos, obj_ori, obj_vel, obj_angvel = [], [], [], []
        # for i in range(self.task.num_blocks):
        #     obj_pos.append(task_obs[..., 12*i:12*i+3])
        #     obj_ori.append(task_obs[..., 12*i+3:12*i+6])
        #     obj_vel.append(task_obs[..., 12*i+6:12*i+9])
        #     obj_angvel.append(task_obs[..., 12*i+9:12*i+12])
        if contain_goal:
            goal = x[..., self.robot_obs_size+task_obs_size:self.robot_obs_size+task_obs_size+goal_size]

    def get_action(self, x):
        input_tensor = self._preproc_inputs(x)
        action = self.actor_network(input_tensor)
        return action

    def _preproc_inputs(self, obs, g):
        obs_norm = self.o_norm.normalize(obs)
        g_norm = self.g_norm.normalize(g)
        # concatenate the stuffs
        inputs = np.concatenate((obs_norm, g_norm), axis=-1)
        inputs = torch.tensor(inputs, dtype=torch.float32).unsqueeze(0)
        return inputs
    
class actor(nn.Module):
    def __init__(self, env_params, dropout_vel_rate = 0):
        super(actor, self).__init__()
        self.dropout_vel_rate = dropout_vel_rate
        self.max_action = env_params['action_max']
        self.fc1 = nn.Linear(env_params['obs'] + env_params['goal'], 256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 256)
        self.action_out = nn.Linear(256, env_params['action'])

    def forward(self, x):
        # dropout vel
        x[..., 20:26] = torch.zeros_like(x[..., 20:26]
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        actions = self.max_action * torch.tanh(self.action_out(x))

        return actions