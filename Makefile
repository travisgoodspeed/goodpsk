VLC=/Applications/VLC.app/Contents/MacOS/VLC

all: tests lectures
clean:
	rm -rf *.wav *~ __pycache__ *.pyc

lectures: *.py goodpsk
	./lecture0.py >lecture0.log
	./lecture1.py >lecture1.log
	./lecture2.py >lecture2.log


tests: *.py goodpsk
#       #Simple test.
	./goodpsk -o out.wav -b 00000000000000000000000000000       \
		-t "The quick brown fox jumped over the lazy dog."  \
		-b 000000000000
#       #Simple test.
	./goodpsk --nofilter                                        \
	        -o nofilter.wav -b 00000000000000000000000000000         \
		-t "The quick brown fox jumped over the lazy dog."  \
		-b 000000000000

#       #Morse/PSK Polyglot.
	./goodpsk -o longmorse.wav \
		-b "000000000000000000000000000000000000000000000000000"                      \
		-t "PSK31 Polyglot test by KK4VCZ, valid as PSK31 and CW.  "                  \
		-t "If this works, the letters of my call will appear inside their Morse..  " \
		-b "00001011111100       0000       00000000000000              "             \
		-b "00001011111100       0000       00000000000000              "             \
		-b "0000       0000       0000       0000       00010111011100              " \
		-b "0000       0000       0000       00000010111100             "             \
		-b "00000101111000       0000       00000000000000       0000               " \
		-b "00011101010100       00000000000000       0000       0000               " \
		-b "000000000000000000000000000000000000000000000000000"                      \
		-t "Test concluded.  I hope you liked that, but there are more clever ones "  \
		-t "to come.  73 de KK4VCZ. k"                                                \
		-b "000000000000000000000000000000000000000000000000000"

#       #Morse/PSK Polyglot.
	./goodpsk --filterall -o morse.wav \
		-b "00001011111100       0000       00000000000000              "             \
		-b "00001011111100       0000       00000000000000              "             \
		-b "0000       0000       0000       0000       00010111011100              " \
		-b "0000       0000       0000       00000010111100             "             \
		-b "00000101111000       0000       00000000000000       0000               " \
		-b "00011101010100       00000000000000       0000       0000               " \




play: all
	afplay morse.wav
transmit: all
#       #Transmit the sound.
	$(VLC) -I dummy --auhal-audio-device=69 lecture0.wav vlc://quit
#       #Reset VLC to the default card.
	$(VLC) -I dummy --auhal-audio-device vlc://quit

