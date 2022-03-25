# after converting (x,y) coordinates into degrees (theta1, theta2),
# now we convert degrees (theta1, theta2) into (pwm1, pwm2)

# takes a list of lists
# ex. [[60,75],[30,50],[120,20]]
def angle_to_pwm(array_of_angles):
    k = 8 # number of bits
    pwm_resolution = 2**k - 1 # resolution of pwm
    array_of_pwm = []
    for pair in array_of_angles:
        pair_list = []
        for angle in pair:
            pwm = (angle / 180)*pwm_resolution
            pair_list.append(pwm)
        array_of_pwm.append(pair_list)
    return array_of_pwm

