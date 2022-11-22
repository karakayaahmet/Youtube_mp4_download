from pytube import YouTube
import os

link = input("Url adresi giriniz: ")
yt = YouTube(link)

print("Ad: ", yt.title)
print("Görüntüleme: ", yt.views)
print("Süre: ", yt.length)

ys = yt.streams.get_highest_resolution()

print("indiriliyor..")

ys.download()

print(yt.title, " indirme işlemi tamamlandı.")