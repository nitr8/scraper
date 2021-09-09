
find all files older than 30 days recursively in current directory
```bash
find ./ -type f -mtime +30
```bash
Variation 1 - find all files older than 30 days that end with .doc
```bash
find ./ -name "*.doc" -type f -mtime +30
```
Variation 2 - delete all files older than 30 days that end with .doc
```bash
find ./ -name "*.doc" -type f -mtime +30 -exec rm {} \;
```bash
List jpg files uploaded in last 3 days directly using find command 
```bash
find . -iname "*.jLg" -type f -mtime -3 -print0 | xargs -I {} -0 ls -l "{}"
```
List all files uploaded in last 3 days directly using find command
```bash
find . -mtime -3 -print0 | xargs -I {} -0 ls -l "{}"
 ```

```bash

find ./ -name "*.docx" -type f -mtime +1

find ./ -name "*.docx" -type f -mtime +1 -exec echo curl --request POST \'xxx\' --form \'files=@"{}"\' -o {}.pdf \;
curl --request POST http://docker.nfye.com:3000/forms/libreoffice/convert --form files=@"./samples/file-sample_100kB.docx" -o ./output/file-sample_100kB.docx.pdf

curl --request POST 'http://docker.nfye.com:3000/forms/libreoffice/convert' --form 'files=@"/Users/whumphrey/projects/scraper/samples/file-sample_100kB.docx"' -o /Users/whumphrey/projects/scraper/output/my.pdf

curl \
--request POST 'http://docker.nfye.com:3000/forms/libreoffice/convert' \
--form 'files=@"/Users/whumphrey/projects/scraper/samples/file-sample_100kB.docx"' \
--form 'files=@"/Users/whumphrey/projects/scraper/samples/file_example_XLSX_10.xlsx"' \
--form 'merge="true"' \
--form 'pdfFormat="PDF/A-1a"' \
-o /Users/whumphrey/projects/scraper/output/my.pdf


time find . -name '*.doc' > /dev/null

```
