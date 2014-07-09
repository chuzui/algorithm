import os

outputDir = "epod\\"

if not os.path.exists(outputDir):
    os.makedirs(outputDir)
for f in os.listdir():
    if os.path.isdir(f):
        for s in os.listdir(f):
            if s.endswith("pdf"):
                rate = s[11]
                oldDir = f
                newDir = os.path.join(outputDir, rate, f)
                if not os.path.exists(newDir):
                    os.makedirs(newDir)
                os.system("copy %s %s " % (oldDir, newDir))