from pytube import YouTube

Youtube_link = input("Enter a Youtube Video Link That You Want To Download: ")
Youtube_Connection = YouTube(Youtube_link)
index = 1

link_title = Youtube_Connection.title
print("\n")
print(link_title)
print("\n")

Download_format = input("DO YOU WANT TO DOWNLOAD A VIDEO OR AUDIO" "\n" "Enter V for video or A for audio (V / A): ")


if(Download_format == "V" or Download_format == "v"):
    print("Here Are All The Video Files" "\n")
    video_type = Youtube_Connection.streams.filter(type = 'video')
    for stream in video_type:   
        print(str(index) + " " + str(stream))
        index += 1
    
    User_download_index = int(input("Enter the Format Number That You Want To Download: "))
    downloading_File = video_type[User_download_index - 1]

    
print("\n")

if(Download_format == "A" or Download_format == "a"):
    print("Here Are All The Audio Files" "\n")
    audio_type = Youtube_Connection.streams.filter(only_audio = True)
    for audio in audio_type:
        print(str(index) + " " + str(audio))
        index += 1

    User_download_index = int(input("Enter the Format Number That You Want To Download: "))
    downloading_File = audio_type[User_download_index - 1]
  
print("\n")

print(downloading_File)  

download_request = input("DO YOU WANT TO DOWNLOAD THIS FILE (Y / N): " "\n")

if(download_request == 'y' or download_request == 'Y'):
    print("Your Video or Audio is Being Downloaded" "\n")
    downloading_File.download() 
    print("The File has been downloaded")
else:
    print("The Program will End.") 

