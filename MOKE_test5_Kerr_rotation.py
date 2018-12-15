import sys
import numpy as np
import os
import time

#Max=5.0;
Max=float(sys.argv[1])
Min=-Max;
#Nsteps=200;
Nsteps=int(sys.argv[2])
yy=0.0;
dH=Max/Nsteps;
v=Gpib('LIA')
rt = 0.003; #rest time
#second harmonics

v.write('HARM2');

Nameoffolder=sys.argv[3];
#Nameoffolder='Test_24102017_10_A-B__wopolariser';
#os.chdir('/media/e16310')
os.makedirs(Nameoffolder)
os.chdir('/home/mokeuser/Downloads/linux-gpib-4.0.4rc2/language/python/'+Nameoffolder)
#os.chdir('/media/e16310/'+Nameoffolder)

output_voltage_array=[];
Final=[];
Mean=[];
Voltage=[];
loop = [[]] * 10


# to go to -H ramping
for l in range(0,Nsteps):
    H=-l*dH;
    #print(H);
    v.write('AUXV1{,%f}'%H);
    time.sleep(0.003);

#real measurement starts for one hysteresis loop
    
for i in range(0,20):
    import time
    ts = time.time()
    import datetime
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    filename=open("data_"+st+".txt","a");
    
# -ve to +ve values

    for j in range(0,Nsteps):
        H = -Max + 2*j*dH;
        v.write('AUXV1{,%f}'%H);
        print (H);
        time.sleep(rt) #pause for 3ms
        output_voltage=0;
        for k in range(0,5):
            #v.write('OUTP?1')
            #v.write('SNAP?1,5,2,3')#1 = kerr rotation,5 = DC laser
            v.write('SNAP?3,5')#1 = kerr rotation,5 = DC laser
            temp1=str(v.read());
            split = temp1.split(',');
            kr=float(split[0]);
            sigdc=float(split[1]);
            #Ysig=float(split[2]);
            #Rsig=float(split[3]);
            temp = kr/sigdc;
            output_voltage=output_voltage + temp;
	filename.write("%f %e \n" %(H, output_voltage/5));
        #filename.write("%f %e %e %e %e %e \n" %(H, output_voltage/5,kr,Ysig,Rsig,sigdc));  
# second slope from +ve to -ve

    for j in range(0,Nsteps):
        H= Max - 2*j*dH;
        v.write('AUXV1{,%f}'%H);
        print (H);
        time.sleep(rt) #pause for 3ms
        output_voltage=0;
        for k in range(0,5):
            #v.write('OUTP?1')
            #v.write('SNAP?1,5,2,3')# 1 = kerr rotation,5 = DC laser
            v.write('SNAP?3,5');
            temp1=str(v.read());
            split = temp1.split(',');
            kr = float(split[0]);
            sigdc=float(split[1]);
            #Ysig=float(split[2]);
            #Rsig=float(split[3]);
            temp = kr/sigdc;
            output_voltage=output_voltage + temp;
        filename.write("%f %e \n" %(H, output_voltage/5));
       #filename.write("%f %e %e %e %e %e \n" %(H, output_voltage/5,kr,Ysig,Rsig,sigdc)); 
#to ramp down to 0V

for l in range(0,Nsteps):
    H=-Max + l*dH;
    print(H);
    v.write('AUXV1{,%f}'%H);
    time.sleep(0.003);
filename.close()
v.write('AUXV1{,0}');
print('Measurement complete wait for analysis')


os.chdir('/home/mokeuser/Downloads/linux-gpib-4.0.4rc2/language/python')
