# Varicode class for PSK31.

class Varicode:
    """This class implements the PSK31 varicode alphabet."""

    def __init__(self):
        """Initialization function."""
    def encode(self,text):
        """Encodes a string to a string of bits."""
        out="";
        for c in text:
            print(c);
            word=self.characters[c]+self.delim;
            out=out+word;
            #print("%c -- %s"%(c,word));
        return out;
    def decode(self,bits):
        """Decodes a string of bits to a string of letters."""
        return "TEST";

    delim="000000";
    characters={
        "\n": "11101",
        " ":  "1",
        
        #Numbers
        "0":  "10110111",
        "1":  "10111101",
        "2":  "11101101",
        "3":  "11111111",
        "4":  "101110111",
        "5":  "101011011",
        "6":  "101101011",
        "7":  "110101101",
        "8":  "110101011",
        "9":  "110110111",
        
        #Lowercase
        "a": "1011",
        "b": "1011111",
        "c": "101111",
        "d": "101101",
        "e": "11",
        "f": "111101",
        "g": "1011011",
        "h": "101011",
        "i": "1101",
        "j": "111101011",
        "k": "10111111",
        "l": "11011",
        "m": "111011",
        "n": "1111",
        "o": "111",
        "p": "111111",
        "q": "110111111",
        "r": "10101",
        "s": "10111",
        "t": "101",
        "u": "110111",
        "v": "1111011",
        "w": "1101011",
        "x": "11011111",
        "y": "1011101",
        "z": "111010101",
        
        #Uppercase
        "A": "1111101",
        "B": "11101011",
        "C": "10101101",
        "D": "10110101",
        "E": "1110111",
        "F": "11011011",
        "G": "11111101",
        "H": "101010101",
        "I": "1111111",
        "J": "111111101",
        "K": "101111101",
        "L": "11010111",
        "M": "10111011",
        "N": "11011101",
        "O": "10101011",
        "P": "11010101",
        "Q": "111011101",
        "R": "10101111",
        "S": "1101111",
        "T": "1101101",
        "U": "101010111",
        "V": "110110101",
        "W": "101011101",
        "X": "101110101",
        "Y": "101111011",
        "Z": "1010101101",

        #Symbols
        "": "",

    };
