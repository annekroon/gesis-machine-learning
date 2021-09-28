
## Code example for reading in alternative filetypes

If you want to convert `.docx`, `.pdf` or `.rtf` files to `str` objects in python, you need some additional packages.
Please find some suggestions below (there are probably different packages that will get the job done, but these seem to work!)

- for`.docx` : `docx2txt`. To install: `pip install doc2text`
- for `.pdf` : `pdfminer`: To install: `pip install pdfminer`
- for `.RTF` : `striprtf` : To install: `pip install striprtf`


```python
import docx2txt
from pdfminer.high_level import extract_text
from striprtf.striprtf import rtf_to_text

import os
```

After loading the packages, you can:
- loop over the different filetypes that you may have in a directory (in this case, in `data/raw/`);
- split the filenames to identify the filetype (e.g., `.docx` or `.pdf`);
- read the data in the files as `str` object using the packages mentioned above;
- append the `list` `text_files`.


```python
text_files = []

for document in os.listdir('data/raw/'):
    fname = document.split('.')[0]

    if document.endswith(".docx"):
        text = docx2txt.process(f"data/raw/{document}")
        text_files.append(text)

    elif document.endswith(".pdf"):
        text = extract_text(f"data/raw/{document}")
        text_files.append(text)

    elif document.endswith(".rtf"):
        text = rtf_to_text(f"data/raw/{document}")
        text_files.append(text)

    else:
        print(f"{document}")
  ```
