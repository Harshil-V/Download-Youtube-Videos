from pytube import YouTube

Youtube_link = input("Enter a Youtube Video Link That You Want To Download: ")
Youtube_Connection = YouTube(Youtube_link)

link_title = Youtube_Connection.title
print(link_title)

