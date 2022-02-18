# panda_handover_trajectory

```
trajectory = {
                'obj_init_pos': task.get_achieved_goal(),
                'goal': task.get_goal(),
                'time': [0, 1/12, 2/12, ...],
                'panda0_ee': [robot0.get_ee_position(), ...], 
                'panda1_ee': [robot1.get_ee_position(), ...], 
                'panda0_joints': [robot0.get_joint_states(), ...], 
                'panda1_joints': [robot1.get_joint_states(), ...], 
                'panda0_finger': [robot0.get_fingers_width(), ...], 
                'panda1_finger': [robot1.get_fingers_width(), ...], 
                'panda0_open_finger_points': [time1, time2, ...]
                'panda0_close_finger_points': [time1, time2, ...]
                'panda1_open_finger_points': [time1, time2, ...]
                'panda1_close_finger_points': [time1, time2, ...]
            }
```