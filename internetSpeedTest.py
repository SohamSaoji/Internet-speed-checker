# pip install speedtest-cli

from speedtest import Speedtest

st = Speedtest()

print("your connection's Download speed is :", st.download)

print("your connection's upload speed is :", st.upload)
