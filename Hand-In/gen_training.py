import fileinput
import sys

if __name__ == "__main__":

    if len(sys.argv) == 3:
   
        input_file = str(sys.argv[1]) 
        output_file = str(sys.argv[2]) 
        f = open(output_file, 'w')
        i = 0 
        for line in fileinput.input([input_file]):
            i += 1
            if ( i >= 220000 and i <= 225499) or (i >= 1020000 and i <= 1025499):
                f.write(line)
                print i 
        f.close()
    else:
        print 'Usage: gen_training.py <input_file> <output_file>'
    
