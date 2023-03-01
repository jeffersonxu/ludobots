import pyrosim.pyrosim as pyrosim
import numpy

def Generate_Horse(seed):
    numpy.random.seed(seed)

    links = {}
    joints = {}
    num_sec = numpy.random.randint(2,5)
    sec_width_range = sec_length_rage = (0.1, 0.6)
    sec_connection_type = "horse"
    leg_width_range = (0.1, 0.4)
    leg_length_range = (0.2, 0.7)  
    (body_size_x, body_size_y, body_size_z), (upper_leg_size_x, upper_leg_size_y, upper_leg_size_z), (lower_leg_size_x,lower_leg_size_y,lower_leg_size_z) = Get_Sizes(sec_width_range, sec_length_rage, leg_width_range, leg_length_range)
    
    for i in range(num_sec):
        body_pos_x  = body_size_x / 2.0
        body_pos_y  = 0
        body_pos_z = 0

        if not i:                        
            body_pos_z  = upper_leg_size_z + lower_leg_size_z                 
      
        links[f"body{i}"] = Get_Link(f"body{i}", [body_size_x, body_size_y, body_size_z], [body_pos_x, body_pos_y, body_pos_z])        
        
        upper_pos_x = 0
        right_upper_pos_y = -upper_leg_size_y / 2.0
        left_upper_pos_y = upper_leg_size_y / 2.0
        upper_pos_z = -upper_leg_size_z / 2.0            
                
        lower_pos_x = 0
        lower_pos_y = 0
        lower_pos_z = -lower_leg_size_z / 2.0
    
        links[f"RightUpperLeg{i}"] = Get_Link(f"RightUpperLeg{i}", [upper_leg_size_x, upper_leg_size_y, upper_leg_size_z], [upper_pos_x, right_upper_pos_y, upper_pos_z])
        links[f"LeftUpperLeg{i}"] = Get_Link(f"LeftUpperLeg{i}", [upper_leg_size_x, upper_leg_size_y, upper_leg_size_z], [upper_pos_x, left_upper_pos_y, upper_pos_z])        
        links[f"RightLowerLeg{i}"] = Get_Link(f"RightLowerLeg{i}", [lower_leg_size_x, lower_leg_size_y, lower_leg_size_z], [lower_pos_x, lower_pos_y, lower_pos_z])    
        links[f"LeftLowerLeg{i}"] = Get_Link(f"LeftLowerLeg{i}", [lower_leg_size_x, lower_leg_size_y, lower_leg_size_z], [lower_pos_x, lower_pos_y, lower_pos_z])

    for i in range(num_sec):
        if i < num_sec - 1:
            parent, child = f"body{i}", f"body{i+1}"
            joint_name = f"{parent}_{child}"
                
        pos_x = links[parent]["size"][0]
        pos_y = 0
        pos_z = 0        
        if not i: 
            pos_z = links[parent]["pos"][2]                    
        joints[joint_name] = {'name': joint_name, 'parent': parent, 'child': child, 'position': [pos_x, pos_y, pos_z], 'jointAxis': "0 0 1" if sec_connection_type == "snake" else "0 1 0"}

        parent, child  = f"body{i}", f"RightUpperLeg{i}"
        joint_name = f"{parent}_{child}"

        pos_x = links[parent]["size"][0] / 2.0
        pos_y = -links[parent]["size"][1] / 2.0
        pos_z = 0                
        if not i:
            pos_z = links[parent]["pos"][2]
        joints[joint_name] = {'name': joint_name,'parent': parent, 'child': child, 'position': [pos_x, pos_y, pos_z], 'jointAxis': "0 1 0"}

        parent, child  = f"body{i}", f"LeftUpperLeg{i}"
        joint_name = f"{parent}_{child}"
        pos_x = links[parent]["size"][0] / 2.0
        pos_y = links[parent]["size"][1] / 2.0
        pos_z = 0        
        if not i:
            pos_z = links[parent]["pos"][2]                                            
        joints[joint_name] = {'name': joint_name,'parent': parent, 'child': child, 'position': [pos_x, pos_y, pos_z], 'jointAxis': "0 1 0"}

        parent, child  = f"RightUpperLeg{i}", f"RightLowerLeg{i}"
        joint_name = f"{parent}_{child}"                        
        pos_x = 0
        pos_y = -links[parent]["size"][1] / 2.0
        pos_z = -links[parent]["size"][2]
        joints[joint_name] = {'name': joint_name,'parent': parent, 'child': child, 'position': [pos_x, pos_y, pos_z], 'jointAxis': "0 1 0"}

        parent, child  = f"LeftUpperLeg{i}", f"LeftLowerLeg{i}"
        joint_name = f"{parent}_{child}"    
        pos_x = 0
        pos_y = links[parent]["size"][1] / 2.0
        pos_z = -links[parent]["size"][2]
        joints[joint_name] = {'name': joint_name,'parent': parent, 'child': child, 'position': [pos_x, pos_y, pos_z], 'jointAxis': "0 1 0",}

    return list(links.values()), list(joints.values())


def Get_Link(name, size, pos):
    sensor_tag = numpy.random.choice([True, False])
    color_name = 'green' if sensor_tag else 'red'

    return {
        "name": name,
        "size": size,
        "pos": pos,
        'sensor_tag': sensor_tag,
        'color': '0 1.0 0 1.0' if sensor_tag else '0 0 1.0 1.0',
        'color_name': color_name
    }    

def Get_Sizes(sec_width_range, sec_length_range, leg_width_range, leg_length_range):
    body_size = (-1, 0, 0)
    upper_leg_size_x =  numpy.random.uniform(*leg_width_range)
    lower_leg_size_x = numpy.random.uniform(*leg_width_range)
    while body_size[0] < max(upper_leg_size_x, lower_leg_size_x):
        body_size = (numpy.random.uniform(*sec_length_range), numpy.random.uniform(*sec_width_range), numpy.random.uniform(*sec_width_range))
        upper_leg_size = (numpy.random.uniform(*leg_width_range), numpy.random.uniform(*leg_width_range), numpy.random.uniform(*leg_length_range))
        lower_leg_size = (numpy.random.uniform(*leg_width_range), numpy.random.uniform(*leg_width_range), numpy.random.uniform(*leg_length_range))

    return body_size, upper_leg_size, lower_leg_size