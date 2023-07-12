import matplotlib.pyplot as plt
import speedtest
import time

list_download_speed = []
list_upload_speed = []

for i in range(5):
    st = speedtest.Speedtest()
    download_s = round(st.download() / 1000000, 2)
    list_download_speed.append(download_s)
    upload_s = round(st.upload() / 1000000, 2)
    list_upload_speed.append(upload_s)
    time.sleep(60)
    x = [1, 2, 3, 4, 5]

plt.figure(figsize=(15, 7))
plt.plot(x, list_download_speed, label="download speed")
plt.legend()
plt.plot(x, list_upload_speed, label="upload speed")
plt.legend()
plt.title("Speed Test")
plt.show()
