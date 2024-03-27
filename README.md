> **Disclaimer:**

>All contents in this warehouse are for learning and reference only and are not allowed to be used for commercial purposes. No person or organization may use the contents of this warehouse for illegal purposes or infringe upon the legitimate rights and interests of others. The crawler technology involved in this warehouse is only used for learning and research, and may not be used to conduct large-scale crawling of other platforms or other illegal activities. This warehouse does not assume any responsibility for any legal liability arising from the use of the contents of this warehouse. By using the content of this repository, you agree to all terms and conditions of this disclaimer.

# Warehouse description

**Xiaohongshu crawler**, **Douyin crawler**, **Kuaishou crawler**, **B station crawler**, **Weibo crawler**….
Currently, it can capture videos, pictures, comments, likes, reposts and other information from Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo.

Principle: Use [playwright](https://playwright.dev/) to build a bridge, retain the contextual browser environment after successful login, and obtain some encryption parameters by executing JS expressions
By using this method, there is no need to reproduce the core encryption JS code, and the difficulty of reverse engineering is greatly reduced.

Reptile technology exchange group: [949715256](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=NFz-oY7Pek3gpG5zbLJFHARlB8lKL94f&authKey=FlxIQK99Uu90wddNV5W%2FBga6T6lXU5BRqyTTc26f2P2Z K5OW%2BDhHp7MwviX%2BbrPa&noverify=0&group_code=949715256), also welcome Everyone contributes code and submits PR


The IP proxy currently used by the crawler: <a href="https://www.jisuhttp.com/?pl=mAKphQ&plan=ZY&kd=Yang">Extremely fast HTTP proxy</a> New users can receive up to 12,000 IP for registration and certification, 0 yuan Trial<br>
<a href="https://www.jisuhttp.com/?pl=mAKphQ&plan=ZY&kd=Yang" target="_blank"><img src="https://s2.loli.net/2023/11/30 /RapQtL8A2w6TGfj.png" alt="Extremely fast HTTP proxy-official website picture"></a>


## function list
| Platform | Cookie login | QR code login | Mobile phone number login | Keyword search | Specified video/post ID crawling | Login status cache | Data saving | IP proxy pool | Slider verification code |
|:---:|:----------:|:------:|:------:|:------:|:------ -------:|:------:|:----:|:------:|:-----:|
| Xiao Hong Shu | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✕ |
| Tik Tok | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Kuaishou | ✅ | ✅ | ✕ | ✅ | ✅ | ✅ | ✅ | ✅ | ✕ |
| Bilibili | ✅ | ✅ | ✕ | ✅ | ✅ | ✅ | ✅ | ✅ | ✕ |
| Weibo | ✅ | ✅ | ✕ | ✅ | ✅ | ✅ | ✅ | ✅ | ✕ |


## Instructions

### Create and activate python virtual environment
    ```shell
    # Enter the project root directory
    cd MediaCrawler
   
    # Create virtual environment
    python3 -m venv venv
   
    # macos & linux activate virtual environment
    source venv/bin/activate

    # windows activate virtual environment
    venv\Scripts\activate

    ```

### Install dependent libraries

    ```shell
    pip3 install -r requirements.txt
    ```

### Install playwright browser driver

    ```shell
    playwright install
    ```

### Run the crawler program

    ```shell
    # Read keywords from the configuration file to search for relevant posts and crawl post information and comments
    python3 main.py --platform xhs --lt qrcode --type search
   
    # Read the specified post ID list from the configuration file to obtain the information and comment information of the specified post.
    python3 main.py --platform xhs --lt qrcode --type detail
  
    # Open the corresponding APP and scan the QR code to log in
     
    # For other platform crawler usage examples, execute the following command to view
    python3 main.py --help
    ```


### Data Saving
- Support saving to relational database (Mysql, PgSQL, etc.)
- Supports saving to csv (data/ directory)
-Supports saving to json (data/ directory)

## How to use IP proxy
➡️➡️➡️ [How to use IP proxy](docs/proxy usage.md)

## Run error FAQ Q&A
➡️➡️➡️ [FAQ](docs/FAQ.md)

## Project code structure
➡️➡️➡️ [Project code structure description](docs/project code structure.md)

## Mobile phone number login instructions
➡️➡️➡️ [Mobile phone number login instructions](docs/Mobile phone number login instructions.md)

## Reward

If you think the project is good, you can reward it. Your support is my biggest motivation!

You can note your name when tipping, and I will add you to the tipping list.
<p>
   <img alt="Reward-WeChat" src="static/images/wechat_pay.jpeg" style="width: 200px;margin-right: 140px;" />
   <img alt="Reward-Alipay" src="static/images/zfb_pay.jpeg" style="width: 200px" />
</p>

## Donation information

PS: If you are making a reward, please note the donor. If there is any omission, please contact me to add it (sometimes there may be too much information and it may be missed, I am very sorry)

| Donor | Donation amount | Donation date |
|---------|------|------------|
| He* | 100 yuan | 2024-01-21 |
| allen | 20 yuan | 2024-01-10 |
| llllll | 20 yuan | 2024-01-07 |
| Kwong*Yuan | 20 yuan | 2023-12-29 |
| 50chen | 50 yuan | 2023-12-22 |
| xiongot | 20 yuan | 2023-12-17 |
| atom.hu | 20 yuan | 2023-12-16 |
| Yidu | 20 yuan | 2023-12-01 |
| Fall | 50 yuan | 2023-11-08 |

## star trend chart
- If this project is helpful to you, star it ❤️❤️❤️

[![Star History Chart](https://api.star-history.com/svg?repos=NanmiCoder/MediaCrawler&type=Date)](https://star-history.com/#NanmiCoder/MediaCrawler&Date)




## refer to

- xhs client [ReaJason’s xhs repository](https://github.com/ReaJason/xhs)
- SMS forwarding [reference warehouse](https://github.com/pppscn/SmsForwarder)
- Intranet penetration tool [ngrok](https://ngrok.com/docs/)