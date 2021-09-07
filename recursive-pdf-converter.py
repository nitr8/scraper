import os
import subprocess
import sys
import getopt
import glob

#print os.path.dirname(os.path.abspath(__file__));
#print  os.getcwd();

def main(argv):

   indir = os.path.dirname(os.path.abspath(__file__));
   outdir = os.path.dirname(os.path.abspath(__file__));
   extensions = ['docx', 'doc', 'rtf', 'txt', 'otf'];
   recursive = 0;

   try:
      opts, args = getopt.getopt(argv,"ioer",["in=","out=", "ext=", "recursive="])
   except getopt.GetoptError:
      print('not good')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--in"):
         indir = arg
      elif opt in ("-o", "--out"):
         outdir = arg
      elif opt in ("-e", "--ext"):
        extensions = arg.split(' ')
      elif opt in ("-r", "--recursive"):
         recursive = 1

   convertThis(indir, outdir, extensions)

   print('--- Done')


def convertThis(indir, outdir, extensions):

     print('--- Starting unoconv listener (just wait 20 seconds)')
     os.system('unoconv --listener & sleep 20')
     print('--- OK, let\'s go')
     
     for root, subdirs, files in os.walk(indir):
        print(root)
        
        os.chdir(root)  
        
        files = [fn for fn in os.listdir(root)
            if any(fn.endswith(ext) for ext in extensions)]
        
        for filename in files:
            path = root + '/' + filename
            cmd = 'unoconv -f pdf --output="' + path + '.pdf"' + ' "' + path + '"'
            print('--- Converting: ' + path)
            os.system(cmd)
        else:
            print("--- No files for conversion found in this folder")
               
     
     os.system('kill -15 %-')


if __name__ == "__main__":
   main(sys.argv[1:])
