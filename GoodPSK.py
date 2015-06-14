# GoodPSK
# by Travis Goodspeed
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
    
    symbols=[];             # Symbols as repeated, with no attenuation.
    filter=True;            # Attenuate to reduce noise during phase change.
    symbolrise=[];          # Previous symbol was different.
    symbolfall=[];          # Next symbol is different.
    symbolrisefall=[];      # Previous and next symbols are different.
    symbolsilent=[];        # Empty symbols.
    textsymbols=[0,1];
    
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
        
        #Flat symbols
        for phase in range(0,phases):
            values=[];
            for i in range(0, length):
                
                value = 0
                #print(value);
                packed_value = struct.pack('h', value)
                values.append(packed_value)
                #values.append(packed_value) #Second channel, unused.
            value_str = ''.join(values)
            self.symbolsilent.append(value_str);
        
        
        #Flat symbols
        for phase in range(0,phases):
            a=math.sin(math.pi*phase+2*math.pi*(0))*volume;
            b=math.sin(math.pi*phase+2*math.pi*((length)/divisor))*volume;
            if a>1 or b>1:
                print "Warning, sign doesn't zero at the end of the sample period."
            
            values=[];
            for i in range(0, length):
                
                value = int(math.sin(math.pi*phase+2*math.pi*(i/divisor))*volume)
                #print(value);
                packed_value = struct.pack('h', value)
                values.append(packed_value)
                #values.append(packed_value) #Second channel, unused.
            value_str = ''.join(values)
            self.symbols.append(value_str);
        
        #Rising
        for phase in range(0,phases):
            a=math.sin(math.pi*phase+2*math.pi*(0))*volume;
            b=math.sin(math.pi*phase+2*math.pi*((length)/divisor))*volume;
            if a>1 or b>1:
                print "Warning, sign doesn't zero at the end of the sample period."
            
            values=[];
            for i in range(0, length):
                #Sharp linear.
                #atten=min(i,100)*1.0/100.0;
                
                #Gentle curve
                atten=1.0;
                if i<length/2:
                    atten=math.sin(i*math.pi/length);
                
                
                value = int(atten*math.sin(math.pi*phase+2*math.pi*(i/divisor))*volume)
                packed_value = struct.pack('h', value)
                values.append(packed_value)
                #values.append(packed_value) #Second channel, unused.
            value_str = ''.join(values)
            self.symbolrise.append(value_str);

        #Falling
        for phase in range(0,phases):
            a=math.sin(math.pi*phase+2*math.pi*(0))*volume;
            b=math.sin(math.pi*phase+2*math.pi*((length)/divisor))*volume;
            if a>1 or b>1:
                print "Warning, sign doesn't zero at the end of the sample period."
            
            values=[];
            for i in range(0, length):
                #Sharp linear
                atten=min(length-i,100)*1.0/100.0;
                
                #Gentle curve
                atten=1.0;
                if i>length/2:
                    atten=math.sin(i*math.pi/length);
                
                
                value = int(atten*math.sin(math.pi*phase+2*math.pi*(i/divisor))*volume)
                packed_value = struct.pack('h', value)
                values.append(packed_value)
                #values.append(packed_value) #Second channel, unused.
            value_str = ''.join(values)
            self.symbolfall.append(value_str);
        
        #Rising and Falling
        for phase in range(0,phases):
            a=math.sin(math.pi*phase+2*math.pi*(0))*volume;
            b=math.sin(math.pi*phase+2*math.pi*((length)/divisor))*volume;
            if a>1 or b>1:
                print "Warning, sign doesn't zero at the end of the sample period."
            
            values=[];
            for i in range(0, length):
                #Linear Drop off on both sides.
                #attenfall=min(length-i,100)*1.0/100.0;
                #attenrise=max(i,100)*1.0/100.0;
                #atten=min(attenrise,attenfall);
                
                #Gentle curve
                atten=math.sin(i*math.pi/length);
                
                value = int(atten*math.sin(math.pi*phase+2*math.pi*(i/divisor))*volume)
                packed_value = struct.pack('h', value)
                values.append(packed_value)
                #values.append(packed_value) #Second channel, unused.
            value_str = ''.join(values)
            self.symbolrisefall.append(value_str);
        
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
            self.writesymbol(bit);

    lastsymbol=0; #Last thing we sent.
    thissymbol=0; #Thing we're sending now.
    nextsymbol=0; #Thing we're enqueing now.
    def writesymbol(self,symbol):
        """Accepts a single bit to write."""
        self.lastsymbol=self.thissymbol;
        self.thissymbol=self.nextsymbol;
        
        #Janky hack to support silent periods.
        if symbol==" ":
            self.outfile.writeframes(self.symbolsilent[0]);
            return;
        
        #PSK31 bits are encoded as a change, not an absolute state.
        #So we flip for a 0 and don't flip for a 1.
        if symbol==0:
            self.nextsymbol=self.thissymbol^1;
        else:
            self.nextsymbol=self.thissymbol;
        
        if self.outfile:
            if ((self.lastsymbol==self.thissymbol and self.thissymbol==self.nextsymbol)
                  or self.filter==False):
                self.outfile.writeframes(self.symbols[self.thissymbol]);
            elif self.lastsymbol!=self.thissymbol and self.thissymbol==self.nextsymbol:
                self.outfile.writeframes(self.symbolrise[self.thissymbol]);
            elif self.lastsymbol==self.thissymbol and self.thissymbol!=self.nextsymbol:
                self.outfile.writeframes(self.symbolfall[self.thissymbol]);
            elif self.lastsymbol!=self.thissymbol and self.thissymbol!=self.nextsymbol:
                self.outfile.writeframes(self.symbolrisefall[self.thissymbol]);
            
        #FIXME Sound output here on Linux, Mac, and Windows.
        
        
        #We're done, so update lastsymbol.
        self.lastsymbol=self.nextsymbol;

