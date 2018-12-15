#import gpib
from Gpib import *
import sys

v=Gpib('LIA')
file = open(sys.argv[1]+"log.txt" ,"w")

print ('Harmonics')
v.write('HARM?');
Harmonics=str(v.read());
print (Harmonics)
file.write(" Harmonics = %s " %Harmonics +"\n" );
file.write("############################################################################"+"\n");

print('###################################################################')


print ('Time constant')
v.write('OFLT?');
tc=str(v.read());
file.write(" Time constant = %s " %tc +"\n" ); 
print (tc)

print ( ' 0 = 10 us');
file.write("0 = 10 us"+"\n");
print ( ' 1 = 30 us');
file.writelines("1 = 30 us"+"\n");
print ( ' 3 = 300 us');
file.writelines("3 = 300 us"+"\n");
print ( ' 5 = 3 ms');
file.write("5 = 3 ms"+"\n");
print ( ' 7 = 30 ms');
file.write("7 = 30 ms"+"\n");
print ( ' 9 = 300 ms');
file.write( "9 = 300 ms "+"\n");
print ( ' 10 = 1s');
file.write( "10 = 1s "+"\n");
print ( ' 11 = 3s');
file.write( "11 = 3s "+"\n");

file.write( " refer manual for more values : http://www.thinksrs.com/downloads/PDFs/Manuals/SR830m.pdf"+"\n")

file.write(" ###########################################################################"+"\n");

print('###################################################################') 

print ('Sensitivity')
v.write('SENS?');
sens=str(v.read());
file.write("Sensitivity = %s" %sens +"\n" )
print (sens)



print ( ' 0 = 2nV/fA');
file.write("0 = 2nV/fA"+"\n");
print ( ' 3 = 20nV/fA');
file.write("3 = 20nV/fA"+"\n");
print ( ' 6 = 200nV/fA');
file.write("6 = 200nV/fA"+"\n");
print ( ' 9 = 2 uV/pA');
file.write("9 = 2 uV/pA"+"\n");
print ( ' 12 = 20 uV/pA');
file.write("12 = 20 uV/pA"+"\n");
print ( ' 15 = 200 uA/pA');
file.write("15 = 200 uA/pA"+"\n");
print ( ' 18 = 2mV/nA');
file.write("18 = 2mV/nA"+"\n")
print ( ' 21 = 20mV/nA');
file.write("21 = 20mV/nA"+"\n");

file.write( " refer manual for more values : http://www.thinksrs.com/downloads/PDFs/Manuals/SR830m.pdf"+"\n")


file.write("#####################################################################"+"\n");
print('###################################################################') 

print('Lowpass filter slope')
v.write('OFSL?');
lowpass=str(v.read());
print(lowpass);
file.write("Lowpass filter slope = %s " %lowpass +"\n");
print(' Either 6 db/oct or 12 db/oct or 18 db/oct or 24 db/oct')
file.write("Either 6 db/oct or 12 db/oct or 18 db/oct or 24 db/oct"+"\n" );

#v.write('*IDN?');
#print v.read()
