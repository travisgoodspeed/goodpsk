#!/usr/bin/python

from GoodPSK import GoodPSK;
from config import *;


psk=GoodPSK(rate=31, phases=2);

#Dump this to a .wav, for later broadcast.
psk.open_file("lecture0.wav");



psk.write("QST QST QST de %s %s %s.\n" % (CALL,CALL,CALL));
psk.write("QTH %s %s %s, %s.\n" % (LOCATOR,LOCATOR,LOCATOR,LOCATION));


psk.write("""
Howdy y'all,

The followin' is a radio lecture by KK4VCZ, addressed to all amateurs
domestic and foreign, that we might know a little more about the PSK31
protcol that we use each day.  If you have clear reception, consider
making an audio or text recording for later reference.  Anyone
retransmitting this message without my expressed permission, but under
his own call sign, is a good friend of me an' mine.

This is PSK31 Lecture Zero, concerning the basics of PSK31 and how
to write a modulator.


""");

