from pytube import Youtube

Youtube_link = input("Enter a Youtube Video Link That You Want To Download: ")
Youtube_Connection = Youtube(Youtube_link)

Video_versions = Youtube_Connection.streams.all()
print(Video_versions)
