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
        "9":  "110110111"
    };
