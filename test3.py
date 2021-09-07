import os
import glob
from pathlib import Path

indir = "/Users/whumphrey/projects/scraper/samples/"
outdir = "/Users/whumphrey/projects/scraper/output/"

# r=root, d=directories, f = files
for r, d, f in os.walk(indir):
    for file in f:
        if file.endswith(".docx"):
            #print (os.path.splitext(file)[0])
            #print(os.path.join(r, file))
            print("dir_and_filename  '% s' " % os.path.join(r, file))
            print("filename:         '% s' " % file)
            print("name:             '% s' " % os.path.splitext(file)[0])
            print("extension:        '% s' " % os.path.splitext(file)[1])
            print("destination:      '% s' " % outdir)
            print("relitive path:    '% s' " % os.path.relpath(os.path.join(r, os.path.splitext(file)[0]), indir))
            print("new_path:         '% s' " % os.path.join(outdir, os.path.relpath(os.path.join(r, file), indir)))
            print("folder structure: '% s' " % r)
            print("new path:         '% s' " % os.path.join(outdir, os.path.relpath(os.path.join(r, os.path.splitext(file)[0] + '.pdf'), indir)))
            print("new path2:         '% s' " % os.path.join(outdir, os.path.relpath(os.path.join(r), indir)), "\n")

arr = os.listdir('.')

#old_path='/abc/ghi/f.txt'
#print("old_path: % s" % old_path)
#rel = os.path.relpath(old_path, '/abc/')
#print("rel:      % s" % rel)
#new_path = os.path.join('/var', rel)
#print("new_path: % s" % new_path, "\n")