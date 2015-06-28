#!/usr/bin/python

from GoodPSK import GoodPSK;
from config import *;
from Lecture import Lecture;

psk=GoodPSK();

lecture=Lecture(psk);
lecture.open_file("lecture0.wav");



lecture.write("""


Howdy y'all,

The followin' is a radio lecture by KK4VCZ, addressed to all amateurs
domestic and foreign, that we might know a little more about the PSK31
protocol that we use each day.  If you have clear reception, consider
making an audio or text recording for later reference.  Anyone
retransmitting this message without my expressed permission, but under
his own call sign, is a good friend of me an' mine.

This is PSK31 Lecture Zero by Travis Goodspeed, KK4VCZ, concerning the
basics of PSK31 and how to write an encoder.  It is followed by
Lecture One, concerning the basics of writing a PSK31 decoder.
Further lectures will cover polyglots, schizophrens, and other strange
transmissions.

The examples in this lecture are accurate to the best of my
recollection, but they well require some tweaking and experimentation
on your side.

Part 0; or,
Basics of PSK31

PSK31 consists of phase changes, which is a fancy way of saying that
the transmitter alternatives between SIN() and COS() waves.  A Zero
bit is indicated by changing phase, while a One bit is indicated by
keeping the phase unchanged.  In the classic version, there are 31.25
symbols per second and only two phases.

It's a lie, but for now, you can pretend that the phase change is
abrupt, so it would look like this as a .WAV.  Here, amplitude is the
X axis and time is the Y axis.  (It's drawn this way to work better
with your PSK31 terminal, although a textbook would have time in X and
amplitude in Y.)

       _
         \\
          |
         /
       -
     /
    |
     \\
       -
         \\
          |
         /
       -    Phase Changes Here
         \\
          |
         /
       -
     /
    |
     \\
       -
         \\
          |
         /
       -
     /
    |
     \\
       -

While the transmitter knows that SIN() is used above and COS() below,
the receiver is really just looking at the difference.  We'll get to
exactly how the receiver does that in the next lecture, as for now
we're only dealing with the transmitter.


Let's get back to the symbol set for a bit.  PSK31 has bits of 0 and
1, where 0 is a phase change and 1 is no change.  So a stream of
zeroes will be flipping phase 31.25 times per second, while a stream
of ones will be a boring old carrier wave, with no transitions.

In the next part, we'll be dealing with the phase as a 1 or 0, and it
is very important not to confuse the phase for a symbol bit.  The phase
is the thing that is flipped, and the bit is the thing that decides
whether to flip the phase.


Above bits, we have letters.  Like Morse--and unlike ASCII and
RTTY--PSK31 has letters of variable bit lengths.

The alphabet used by PSK31 is called Varicode, and it consists of most
of the letters from the 7-bit ASCII table.  Varicode symbols always
begin and end with a 1, and they *NEVER* have more than single zero in
a row.  Two or more zeroes indicate a break between letters.

I don't have room for a complete alphabet here, but here's a partial
one.  Note that common letters are shorter, and that lowercase is
shorter than uppercase.

[space] 1  
e 11
E 1110111
C 10101101
Q 111011101
o 111
a 1011
s 10111
< 111101101

So "CQ CQ" might be rendered as any of the following.  (Spaces are to
separate meaningful symbols.  They are not transmitted.)

1. 10101101 00 111011101 00 10101101 00 111011101 00 
2. 10101101 000 111011101 0000 10101101 00 111011101 00 
3. 10101101 0000 111011101 00 10101101 00 111011101 00 

To help the receiver tune into the signal, it is customary to send a
long string of zeroes before the first meaningful letter.


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



Part 2; Tell Me, There is a Light; or,
Noisy PSK31 Becomes Clean!

Part 3; in which,
We Bring Back that Distinctive Warble

Part 4; in which,
We Tie it All Together




""");



lecture.close();

