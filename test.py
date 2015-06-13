#!/usr/bin/python

from GoodPSK import GoodPSK;



psk=GoodPSK(rate=31, phases=2);

psk.open_file("out.wav");
#psk.write("KC3BVL KC3BVL KC3BVL de KK4VCZ KK4VCZ KK4VCZ");


#message=[0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0];

#for s in message:
#    psk.writesymbol(s);




psk.write("""
TEST TEST TEST by KK4VCZ KK4VCZ KK4VCZ

This is a test of a new PSK31 modulator.  I don't quite have all of
the filters in place, so please be kind and forgive me for any
accidental QRM.

Transmitting on 6 Meters from FM29jw, West Philadelphia.

""");

