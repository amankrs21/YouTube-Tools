import os
try:
    from pytube import YouTube
except:
    os.system("pip install pytube")
    from pytube import YouTube
    
SAVE_PATH = os.getcwd()

link = input("\n Enter YouTube Video link to Download : ")

try:
    print("Connecting . . .")
    yt = YouTube(link)
    main_title = yt.title
    main_title = main_title + '.mp4'
    main_title = main_title.replace('|', '')
    vid = yt.streams.filter(progressive=True, file_extension='mp4', res="720p").first()
    print('Downloading. . . ' + vid.default_filename + ' and its file size -> ' + str(round(vid.filesize / (1024 * 1024), 2)) + ' MB.')
    vid.download(SAVE_PATH)
    print("Video Downloaded and Successfully saved to --> ",SAVE_PATH)
        
except:
    print('Connection Problem... Unable to fetch video info')
