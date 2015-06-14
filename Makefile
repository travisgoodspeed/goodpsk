VLC=/Applications/VLC.app/Contents/MacOS/VLC

clean:
	rm -f *.wav
all:
#Simple test.
	./goodpsk -o out.wav -b 00000000000000000000000000000 \
		-t "The quick brown fox jumped over the lazy dog." \
		-b 000000000000
#Morse/PSK Polyglot.
	./goodpsk -o morse.wav \
	-b "000000       00       000000              " \
	-b "000000       00       000000              "




play: all
	afplay morse.wav
transmit: all
	$(VLC) -I dummy --auhal-audio-device=69 out.wav vlc://quit
	$(VLC) -I dummy --auhal-audio-device out.wav vlc://quit

