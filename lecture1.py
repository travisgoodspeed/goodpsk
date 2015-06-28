#!/usr/bin/python

from GoodPSK import GoodPSK;
from config import *;
from Lecture import Lecture;

psk=GoodPSK();

lecture=Lecture(psk);
lecture.open_file("lecture1.wav");

lecture.intro();




lecture.write("""

Part 1;
Generating Waves in Python; or,
Our Heroes Generate Hopeless Noisy Spectrum

Generating sound from Python is hopelessly platform-specific, but it's
easy enough to generate a .WAV file.  Normal CD-quality audio is
sampled at 44,100 samples per second, but PSK31 was designed for
1990's DSP hardware, which samples at 8,000 samples per second.  We'll
use a rate of 44,800, which works quite well for this.

Additionally, the file has 1 channel and 2 bytes per sample.

import wave
outfile=wave.open("output.wav",'w')
outfile.setparams((1, 2, 48000, 0, 'NONE', 'not compressed'))

We want each wave to have a frequency of 1kHz, to put it smack dab in
the middle of the voice range of the Upper Side Band.  So to get a
thousand cycles a second, each cycle will take 48 samples.

Let's define some constants:

volume=32767.0
audiorate=48000
length=int(audiorate/31.25)
divisor=audiorate/10000.0
pi=math.pi
sin=math.sin #(radians, not degrees)

Additionally, the phase is 0 or 1, and an index i is in the range of 0
to length.  Note that the phase is not the same as the bit; it is the
value that the bit flips!  Also note that while our index could be
within a recording, it is much more efficient to generate chunks of
samples and append those chunks to the .WAV.

The scalar sample at that point will be something like the following.

value = sin(pi*phase+2*pi*(i/divisor))*volume

By collecting these points into a collection of frames, then rendering
a long string into a .WAV file, you will generate a functional--if
terribly noisy and spectrum-inefficient--PSK31 audio file.


""");

lecture.close();

