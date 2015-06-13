

clean:
	rm -f *.wav
all:
	./goodpsk -o out.wav -b 00000000000000000000000000000 \
		-t "The quick brown fox jumped over the lazy dog." \
		-b 000000000000
play: all
	mplayer out.wav
