#!python3
import os
import os.path as path
import sys
import getopt
import fnmatch
import time
from pathlib import Path

# ./test.py --in=/Users/whumphrey/projects/scraper/samples --out=/Users/whumphrey/projects/scraper/output --ext="*.doc"

def main(argv):
   extensions = ['docx', 'doc', 'rtf', 'txt', 'otf'];
   recursive = 0;

   try:
      opts, args = getopt.getopt(argv,"ioer",["in=","out=", "ext="])
   except getopt.GetoptError:
      print('not good')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--in"):
         indir = arg
      elif opt in ("-o", "--out"):
         outdir = arg
      elif opt in ("-e", "--ext"):
        extension = arg
      elif opt in ("-d", "--days"):
        extension = arg

   convertPDF(indir, outdir, extension)
   print('--- Done')

def convertPDF(indir, outdir, extension):
   matches = []
   def find(dirname=None, newerThan=3*24*3600, olderThan=None):
      print('--- Converting: ' + indir)
      print (newerThan/24/3600)
      for root, dirnames, filenames in os.walk(indir):
         for filename in fnmatch.filter(filenames, extension):
               filepath = os.path.join(root, filename)
               matches.append(path)
               ts_now = time.time()
               newer = ts_now - path.getmtime(filepath) < newerThan
               older = ts_now - path.getmtime(filepath) > newerThan

               if newerThan and newer or olderThan and older: 
                  print('newer - ' + filepath)

               print('normal - ' + filepath)
               print("new path:         '% s' " % os.path.join(outdir, os.path.relpath(os.path.join(root, os.path.splitext(filename)[0] + '.pdf'), indir)))
               #pdfname = Path(filename).with_suffix('.pdf')
               #print (pdfname)
               #print (outdir + pdf)
               #print ('curl --request POST \'http://docker.nfye.com:3000/forms/libreoffice/convert\' --form \'files=@"' + filepath + '"\' -o ' + outdir + '/' + filename + '.pdf')
               cmd = 'curl --request POST \'http://docker.nfye.com:3000/forms/libreoffice/convert\' --form \'files=@"' + filepath + '"\' -o ' + outdir + '/' + filename + '.pdf'
               #os.system(cmd)
   find('.')

if __name__ == "__main__":
   main(sys.argv[1:])