import os
import re
import sys

names = {sys.argv[1]+f: sys.argv[1]+''.join(re.split(r"(\-\d{1,}\.)", f)[:1]
    + ['.'] + re.split(r"(\-\d{1,}\.)", f)[2:]) for f in os.listdir(sys.argv[1])}
[os.rename(old, new) for old, new in names.items()]
