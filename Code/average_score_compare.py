def better_than_average(class_points, your_points):
    y = sum(class_points)
    z = len(class_points)
    mean= y/z
    if your_points>mean:
        return True
    else : 
        return False
    
