import re

regex = re.compile("^.+(sub-.+)_(ses-.+)_(mod-.+)")

strings = ["abcsub-033_ses-01_mod-mri", "defsub-044_ses-01_mod-mri", "ghisub-055_ses-02_mod-ctscan"]
print([regex.findall(s) [0] for s in strings])