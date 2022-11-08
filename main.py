import speedtest
test = speedtest.Speedtest()

print("Test Download Speed...")

download_result = test.download()/1025/1024
print(f"Your download speed is:{download_result:.2f}mbit/s")

print("Test Upload Speed...")
upload_result = test.upload()/1024/1024
print(f"upload speed is:{upload_result:.2f}mbit/s")

