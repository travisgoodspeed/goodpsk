#!/usr/bin/python

from GoodPSK import GoodPSK;
from config import *;



SCHEDULE="""

PSK Lecture 0: Basics of PSK31
PSK Lecture 1: Building a Bad Encoder
PSK Lecture 2: Shaping a Clean Encoder

""";




class Lecture:
    def __init__(self, psk):
        """Initializes a lecture around its source string.  The configuration
is automatically added."""
        self.psk=psk;
    def open_file(self,filename):
        """Just calls PSK's version of the same script."""
        self.psk.open_file(filename);
    def intro(self):
        """Dumps the lecture into a file."""
        
        #First we send our call.
        self.write("QST QST QST de %s %s %s.\n" % (CALL,CALL,CALL));
        self.write("QTH %s %s %s, %s.\n" % (LOCATOR,LOCATOR,LOCATOR,LOCATION));
    def write(self,text):
        """Adds some text"""
        self.psk.write(text);
    
    def close(self):
        """Adds the closing text."""
        self.write("""

73 de Philly, New York, and Montreal,
--Travis KK4VCZ


This ends the lecture, transmitted by %s in %s.

"""%(CALL,LOCATOR));

