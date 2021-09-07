import os
import glob
from pathlib import Path

id = "/Users/whumphrey/projects/scraper/samples/"
od = "/Users/whumphrey/projects/scraper/output/"

# r=root, d=directories, f=files, id=input_directory, od=output_directory
for r, d, f in os.walk(id):
    for file in f:
        #if file.endswith(".docx"):
        if file.endswith((".doc", ".docx", ".mp3")):
            Path(os.path.join(od, os.path.relpath(os.path.join(r), id))).mkdir(parents=True, exist_ok=True)
            cnvt = 'curl --request POST \'http://docker.nfye.com:3000/forms/libreoffice/convert\' --form \'files=@"' + os.path.join(r, file) + '"\' -o ' + os.path.join(od, os.path.relpath(os.path.join(r, os.path.splitext(file)[0] + os.path.splitext(file)[1] + '.pdf'), id))
            #os.system(cnvt)
            print(cnvt)

arr = os.listdir('.')