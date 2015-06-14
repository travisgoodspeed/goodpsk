VLC=/Applications/VLC.app/Contents/MacOS/VLC

clean:
	rm -f *.wav
all:
	./goodpsk -o out.wav -b 00000000000000000000000000000 \
		-t "The quick brown fox jumped over the lazy dog." \
		-b 000000000000
play: all
	mplayer out.wav
transmit: all
	$(VLC) -I dummy --auhal-audio-device=69 out.wav vlc://quit
	$(VLC) -I dummy --auhal-audio-device out.wav vlc://quit

