import os
import re
try:
    import moviepy.editor as mp
except:
    os.system("pip install moviepy")
    import moviepy.editor as mp

# folder = "/home/aman/Desktop/Programs/RDWRNQ-"
folder = str(input("\n Enter Your Folder Location where all videos are stored : "))

for file in os.listdir(folder):
    if re.search('mp4', file):
        mp4_path = os.path.join(folder,file)
        mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)