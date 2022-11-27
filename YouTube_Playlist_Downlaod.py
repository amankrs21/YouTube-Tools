import os
import re
import requests
try:
    from pytube import YouTube
    import moviepy.editor as mp
except:
    os.system("pip install pytube")
    os.system("pip install movepy")
    from pytube import YouTube
    import moviepy.editor as mp


def foldertitle(url):
    try:
        res = requests.get(url)
    except:
        print('no internet')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]

    else:
        print('Incorrect attempt.')
        return False

    return cPL


def link_snatcher(url):
    our_links = []
    try:
        res = requests.get(url)
    except:
        print('no internet')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
    else:
        print('Sorry, Playlist not Found :(')
        return False

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, plain_text)

    for m in mat:
        new_m = m.replace('&amp;', '&')
        work_m = 'https://youtube.com/' + new_m
        if work_m not in our_links:
            our_links.append(work_m)

    return our_links


BASE_DIR = os.getcwd()

print("Welome to YouTube Playlist Downloader, Developed by - www.github.com/amankrs21")

url = str(input("\n Specify you playlist url : "))
user_res = str(input("\n Choose Video Quality (360P|720P) : ")).lower()

print("You Choosed ",user_res," resolution.")

our_links = link_snatcher(url)
os.chdir(BASE_DIR)
new_folder_name = foldertitle(url)
print(new_folder_name[:7])

try:
    os.mkdir(new_folder_name[:7])
except:
    print('Folder Already Exists')

os.chdir(new_folder_name[:7])
SAVEPATH = os.getcwd()
print(f'\n Video Files will be saved to {SAVEPATH}')

x=[]
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        pathh = os.path.join(root, name)

        
        if os.path.getsize(pathh) < 1:
            os.remove(pathh)
        else:
            x.append(str(name))

print('\nConnecting . . .\n')

for link in our_links:
    try:
        yt = YouTube(link)
        main_title = yt.title
        main_title = main_title + '.mp4'
        main_title = main_title.replace('|', '')
        
    except:
        print('Connection Problem... Unable to fetch video info')
        break
   
    if main_title not in x:
        if user_res == '360p' or user_res == '720p':
            vid = yt.streams.filter(progressive=True, file_extension='mp4', res=user_res).first()
            print('Downloading. . . ' + vid.default_filename + ' and its file size -> ' + str(round(vid.filesize / (1024 * 1024), 2)) + ' MB.')
            vid.download(SAVEPATH)
            print('Video Downloaded, Successfully')
        else:
            print('Something is wrong.. Please Try Again')

    else:
        print(f'\n Skipping "{main_title}" video \n')


print(" Downloading Finished, Thanks for using :)")

option = input("\n Do you want to Convert Videos into Audio, (Y|No) : ").lower()
if option == "y":
    for file in os.listdir(SAVEPATH):
        if re.search('mp4', file):
            mp4_path = os.path.join(SAVEPATH,file)
            mp3_path = os.path.join(SAVEPATH,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print(f' All Videos are converted into Audio, and saved at --> {SAVEPATH}')
else:
    print(f' All your videos are saved at --> {SAVEPATH}')
