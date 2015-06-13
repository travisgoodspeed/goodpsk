

clean:
	rm -f *.wav
all:
	./test.py
play: all
	mplayer noise.wav
