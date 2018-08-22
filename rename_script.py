import os
import re

names = {f: ''.join(re.split(r"(\-\d{1,}\.)", f)[:1] + ['.'] + re.split(r"(\-\d{1,}\.)", f)[2:]) for f in os.listdir('./')}
[os.rename(old, new) for old, new in names.items()]
