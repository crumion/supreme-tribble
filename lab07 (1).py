#!/usr/bin/env python
# coding: utf-8

# # Lab 07: The Internet
# 
# - **Name**:  Colton R. Crum
# - **Netid**: ccrum

# ## Activity 1: SpeedTest
# 
# For the first activity, you are to measure the speed of various networking technologies by using the [SpeedTest] website.  You are to use the following three connection types:
# 
# 1. **Wired connection from your laptop or a lab machine**
# 
# 2. **Wireless connection from your laptop**
# 
# 3. **Cellular connection from your phone (make sure you are using 4G/LTE and not WiFi)**
# 
# 
# To test the speed of each connection, simply go to the website on the appropriate device: www.speedtest.net and hit the `Go` button.  This will measure your **Ping**, **Download**, and **Upload** speeds to generate a result such as:
# 
# <img src="https://www.speedtest.net/result/8129841449.png">
# <img src="https://www.speedtest.net/result/8129848300.png">
# 
# [SpeedTest]: https://www.speedtest.net/

# ### Speed Tests
# 
# Run the [SpeedTest] on each connection type a few times to get a representative sample and then complete the table below:
# 
# | Connection Type | Ping (ms) | Download (Mbps) | Upload (Mbps) |
# |-----------------|-----------|-----------------|---------------|
# | Wireless        | 1         | 91.49               | 80.59             |
# | Wired           | 1         | 843.90               | 931.06             |
# | Cellular        | 27         | 40.40               | 5.12             |
# 
# <center><font color="red"></font></center>
# 
# [SpeedTest]: https://www.speedtest.net/

# ### Analysis
# 
# After completing the table above with your speed tests, analyze the results by answering the following questions:
# 
# 1. Which connection type had the best **latency**?  Explain.
# 
#     <font color="red">The wired desktop connection and the wireless connection both had the best latency, at 1 ms. Latency is a measure of delay, or how quickly the service responds to my request. </font>
# 
# 2. Which connection type had the best **bandwidth**?  Explain.
# 
#     <font color="red">The wired desktop connection had the best bandwidth, at 843.90 Mbps download and 931.06 Mbps upload. It had almost ten times more bandwidth than a wireless connection, and over twenty times more than my cellular connection. This measures the amount or capacity of data we can transfer over a period of time. The wireless connection and cellular connection are slower than the wired connection because wireless connections are slowed down by interference from other devices emitting radio waves. </font>
#     
# 3. What difference (if any) did you notice between **download** and **upload** speeds?  Discuss why this could be.
#     
#     <font color="red">On the cellular and wireless connections, the download speed was faster than the upload speed, and sometimes a lot more (8 times greater for cellular). However, with the wired connection, the upload speed was faster. These connections carry upstream and downstream data, and the bandwidth being used on both channels changes with the amount of traffic. At Notre Dame, there would be more students on a wireless connection, making a wired connection not only faster because of the wire, but also since less bandwidth is being used by other users. This would account for some of the differences between upload and download speeds. </font>
# 
# 4. Overall, which connection type was the **best**?  Explain.
# 
#     <font color="red">The wired connection was the best overall. It had the fastest latency, and largest bandwidth, making it a superior connection to any of the others.</font>

# ## Activity 2: Bandwidth and Latency
# 
# For the second activity, you are to write two functions that you can utilize to perform your own **bandwidth** and **latency** measurements.  The first is `measure_bandwidth`, which uses [requests] to download data from a web server, while the second is `measure_latency` which uses a low-level [socket] to connect to a remote server.  For timing, we will use Python's [time] module:
# 
#     current_time = time.time()
# 
# [requests]: http://docs.python-requests.org/en/master/
# [socket]: https://docs.python.org/3/library/socket.html
# [time]: https://docs.python.org/3/library/time.html

# ### Measure Bandwidth

# In[26]:


import requests
import time

def measure_bandwidth(url):
    ''' Measure bandwidth by doing the following:
    
    1. Record start time.
    2. Download data specified by url.
    3. Record end time.
    4. Compute bandwidth:
    
        bandwidth = (Amount of Data / Elapsed Time) / 2**20
    '''
    
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    bandwidth = ((len(response.content) / ((end_time) - (start_time)) / (2**20)))
    

    
    return bandwidth


# In[70]:


URLS = {
    'Slack': 'https://downloads.slack-edge.com/releases_x64/SlackSetup.exe',
    'Discord'  : 'https://dl.discordapp.net/apps/win/0.0.305/DiscordSetup.exe',
    'Firefox': 'https://download-installer.cdn.mozilla.net/pub/firefox/releases/66.0/linux-x86_64/en-US/firefox-66.0.tar.bz2'
}

for url in URLS:
    print('Downloaded {} with bandwidth of {:.2f} MBps'.format(url, measure_bandwidth(URLS[url])))


# ### Measure Latency

# In[71]:


import socket
import time

def measure_latency(domain):
    ''' Measure latency by doing the following:
    
    1. Create streaming internet socket.
    2. Record start time.
    3. Connect to specified domain at port 80.
    4. Record end time.
    5. Compute latency:
    
        latency = Elapsed Time * 1000
    '''
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_time = time.time()
    s.connect((domain, 80))
    end_time = time.time()
    latency = (((end_time) - (start_time)) *1000)
    
    
    return latency


# In[72]:


DOMAINS = [
    'facebook.com',
    'cnn.com',
    'google.com',
    'nd.edu',
    'amazon.co.uk',
    'baidu.com',
    'europa.eu',
    'yahoo.co.jp',
]


# In[69]:


for domain in DOMAINS:
    print('Connection to {} has latency of {:.2f} ms'.format(domain, measure_latency(domain)))


# ### Analysis
# 
# After writing the `measure_bandwidth` and `measure_latency` functions above and testing them, answer the following questions:
# 
# 1. Which applications had the best bandwidth?  How do these bandwidth measurements compare to the ones you had in Activity 1?  What explains the differences?
# 
#     <font color="red">Discord had the best bandwidth at 6.18 MBps, followed by Firefox and Slack, 3.36 MBps and 1.33 MBps respectively. These bandwidths are far worse than the ones in activity 1. This is because we never tested bandwidth for downloading something in activity 1, whereas this activity was a real world test of bandwidth, even against downloads from different urls.</font>
# 
# 2. Which domains had the best latency?  Which ones had the worst latency?  What explains these differences?
# 
#     <font color="red">CNN.com had the best latency at 8.01 ms, and yahoolco.jp had the worst latency at 296.45 ms. CNN is located in the United States, making the distance much shorter than Yahoo Japan, where its servers are located in Asia. This distance affects the responsiveness of the service.  </font>

# ## Activity 3: EggHead's Adventure
# 
# For the last activity, you are play the following educational game created by the [Office of Digital Learning] as an experiment:
# 
# - [Introduction to Networks](https://s3.us-east-2.amazonaws.com/cs4all/cs4all-game/story_html5.html)
# 
# - [Network Toolkit](https://s3.us-east-2.amazonaws.com/cs4all/Network-toolkit/story_html5.html)
# 
# Once you have completed the game, please fill out the following [survey](https://goo.gl/forms/AfUJ5b4cQfVqwCof1).
# 
# [Office of Digital Learning]: https://online.nd.edu/
