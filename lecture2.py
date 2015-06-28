#!/usr/bin/python

from GoodPSK import GoodPSK;
from config import *;
from Lecture import Lecture, SCHEDULE;

psk=GoodPSK();

lecture=Lecture(psk);
lecture.open_file("lecture2.wav");

lecture.intro();
lecture.write("""

Howdy y'all,

The followin' is a radio lecture by KK4VCZ, addressed to all amateurs
domestic and foreign, that we might know a little more about the PSK31
protocol that we use each day.  If you have clear reception, consider
making an audio or text recording for later reference.  Anyone
retransmitting this message without my expressed permission, but under
his own call sign, is a good friend of me an' mine.

This is PSK31 Lecture Two by Travis Goodspeed, KK4VCZ.  It is preceded
by Lecture One, in which we built a naive PSK31 encoder.  This lecture
will explain how to adjust your encoder to produce a proper and polite
wave form, one that doesn't create QRM on neighboring channels and is
suitable for transmissions.

The following are the lectures in this series:
%s

"""%SCHEDULE);




lecture.write("""

Part 2;
River Stay Away from my Door; or,
Noisy PSK31 Becomes Clean!

In the previous lectures of this series, we learned how PSK31 encodes
letters as bits using the Varicode alphabet, and also how bits are
encoded with a phase transition for a Zero and no transition for a
One.  We also learned how to create a sine wave in software, and how
to shift the phase of that sine wave to encode PSK31 bits.

If you have followed along and done your homework from the last
lecture, you should have a small little tool in Python or another
language that generates a .WAV file with abruptly shifting phases
when modulating PSK31.

The trouble though is that the file sounds terrible; it hurts your
ears nearly as much as it hurts your speakers.  If you were to
broadcast it--WHICH YOU SHOULD NOT!--it would cause QRM all around the
channel you broadcast it on.  The purpose of this lecture is to
explain how PSK31 encoders attenuate their output at just the right
moment to avoid this noise pollution.


In Audacity or any other simple audio editor, compare the wave form of
your PSK31 generator from Lecture 1 to a recording of a real PSK31
transmission, like the one your are receiving now.

The first thing you will notice is that the real signal fades in and
out a lot, and it does so sharply at the transition point.  Zooming in
closely, you'll see that your signal looks like the following.

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

While the real PSK31 signal gently fades to silence before fading in
with the new phase.  If you'll excuse my crude Varicode art, it looks
something like this.

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
       |
       |    Phase Changes Here
       |
       |
        /
      /
      |
       \\
        |
        /
       /
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


Zooming out, you'll find that the fading in and out has the shape of a
sine wave!  So all we need to do is create an attenuation factor that
varies over the duration of the symbol.

Recalling our constants from Lecture 1,

volume=32767.0
audiorate=48000
length=int(audiorate/31.25)
divisor=audiorate/10000.0
pi=math.pi
sin=math.sin #(radians, not degrees)

Let's introduce a new factor, atten, which varies with the curve.  If
the symbol is rising up from a transition, we attenuate the first
half.  If it is falling down to a transition at the end, we attenuate
the second half.  (So a series of zeroes will attenuate on both sides
of every symbol, while a series of ones will attenuate neither side.)

atten=1.0;
if (i<length/2 and rising) or
   (i>length/2 and falling):
  atten=math.sin(i*math.pi/length)

Then we attenuate the point value of each sample in the series.

value = atten*sin(pi*phase+2*pi*(i/divisor))*volume

""");

lecture.close();

