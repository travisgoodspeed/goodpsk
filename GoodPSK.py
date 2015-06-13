# GoodPSK by Travis Goodspeed
# KK4VCZ
#
# This is a quick and dirty PSK31 encoded, used for some polyglot
# research.  If you find it handy, send me a pull request!

from Varicode import Varicode;
import wave;
import random;
import struct;
import math;

class GoodPSK:
    mode="psk";
    audiorate=48000;
    rate=31;
    phases=2;
    varicode=Varicode();
    outfile=None;
    symbols=[]
    textsymbols=[0,1,2,3];
    def __init__(self, rate=31, phases=2):
        """Initializes the encoder."""
        self.set_rate(rate,phases);
        #print("Initialized to %iPSK%i." % (phases,rate));
    
    def set_rate(self,rate=31,phases=2):
        """Generates sample sets for each symbol."""
        self.rate=rate;
        self.phases=phases;
        self.symbols=[]; 
        
        length=int(self.audiorate/31.25);
        #print("%i samples per symbol.\n"%length);
        divisor=self.audiorate/1000.0;
        volume=32767.0/5;
        
        for phase in range(0,phases):
            #print("Generating phase %i."%phase);
            
            a=math.sin(math.pi*phase+2*math.pi*(0))*volume;
            b=math.sin(math.pi*phase+2*math.pi*((length)/divisor))*volume;
            if a>1 or b>1:
                print "Warning, sign doesn't zero at the end of the sample period."
            
            values=[];
            for i in range(0, length):
                #TODO The frequency should be chosen to get a zero crossing.
                value = int(math.sin(math.pi*phase+2*math.pi*(i/divisor))*volume)
                #print(value);
                packed_value = struct.pack('h', value)
                values.append(packed_value)
                #values.append(packed_value) #Second channel, unused.
            value_str = ''.join(values)
            self.symbols.append(value_str);
        
    def open_file(self,filename):
        """Opens a file for output."""
        self.outfile = wave.open(filename, 'w')
        # Mono wave file, 48k
        self.outfile.setparams((1, 2, self.audiorate, 0, 'NONE', 'not compressed'))

    
    def write(self,towrite):
        """Accepts an ASCII string to print."""
        print("ASCII: %s"%towrite);
        bits=self.varicode.encode(towrite);
        self.writebits(bits);

    def writebits(self,towrite):
        """Accepts raw bits to write out."""
        for bit in towrite:
            self.writesymbol(int(bit));
    lastsymbol=0;
    def writesymbol(self,symbol):
        """Accepts a single bit to write."""
        if symbol==0:
            self.lastsymbol=self.lastsymbol^1;
        if self.outfile:
            self.outfile.writeframes(self.symbols[self.lastsymbol]);
        #FIXME Sound output here on Linux, Mac, and Windows.


