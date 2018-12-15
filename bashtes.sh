#!/bin/bash

python Keithley_voltage.py 3

python MOKE_test5_Kerr_rotation.py 4 50 Test_01022018
 
python Keithley_voltage.py 5

python abort.py

#python log_MOKE.py Ta1Co6p5Pt1p5_Hor_19122017_Kerr_rotation_test2_1

#python loop_averaging.py Ta1Co6p5Pt1p5_Hor_19122017_Kerr_rotation_test2_1


#python MOKE_test5_Kerr_ellipticity.py 2 200 Co5Pt2_22112017_Ellipticity


#python log_MOKE.py Co5Pt2_22112017_Ellipticity_IP

#python loop_averaging.py Co5Pt2_22112017_Ellipticity_IP


 
