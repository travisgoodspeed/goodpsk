#!/usr/local/bin/python

from GoodPSK import GoodPSK;



psk=GoodPSK(rate=31, phases=2);

psk.open_file("out.wav");
#psk.write("KC3BVL KC3BVL KC3BVL de KK4VCZ KK4VCZ KK4VCZ");


#message=[0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0];

#for s in message:
#    psk.writesymbol(s);



psk.writebits("11111111111111111");
psk.writebits("00000000000000000");

#psk.writebits("000000000000000000000000000000");
psk.write("1337 1377 13777");
psk.write("1337 1377 13777");
psk.write("1337 1377 13777");



print(len(psk.symbols[0]));
print(len(psk.symbols[1]));
