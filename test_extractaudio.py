import subprocess

inputFile = "IosaWkNnRYw.mp4"
#outputFile = "IosaWkNnRYw.flac"
outputFile = "IosaWkNnRYw.wav"

## flac
#cmd = "ffmpeg -i {0} -vn -ar 44100 -ac 2 -acodec flac -f flac {1}".format(inputFile, outputFile)
cmd = "ffmpeg -i {0} -f wav {1}".format(inputFile, outputFile)
subprocess.call(cmd, shell=True)
