> **Disclaimer:**
>
>All contents in this warehouse are for learning and reference only and are not allowed to be used for commercial purposes. No person or organization may use the contents of this warehouse for illegal purposes or infringe upon the legitimate rights and interests of others. The crawler technology involved in this warehouse is only used for learning and research, and may not be used to conduct large-scale crawling of other platforms or other illegal activities. This warehouse does not assume any responsibility for any legal liability arising from the use of the contents of this warehouse. By using the content of this repository, you agree to all terms and conditions of this disclaimer.
# **Social Media Crawler**

**Xiaohongshu crawler**, **Tik Tok crawler**, **Kuaishou crawler**, **Bilibili crawler**, **Weibo crawler**….
Currently, it can capture videos, pictures, comments, likes, reposts and other information from Xiaohongshu, Douyin, Kuaishou, Bilibili and Weibo.

Principle: Use [playwright](https://playwright.dev/) <img src="https://playwright.dev/img/playwright-logo.svg" alt="Playwright Logo" width="30"/>
 to build a bridge, retain the contextual browser environment after successful login, and obtain some encryption parameters by executing JS expressions
By using this method, there is no need to reproduce the core encryption JS code, and the difficulty of reverse engineering is greatly reduced.

## How to use

1.  Run command: `cd /path/to/MediaCrawler-main`
2.  Create venv by running: `python3 -m venv venv`
3.  Activate venv by running: `source venv/bin/activate`
4.  Install dependent librarys: `pip3 install -r requirements.txt`
5.  Install playwright: `playwright install`
6.  Read keywords from the configuration file to search for relevant posts and crawl post information and comments: `python3 main.py --platform xhs --lt qrcode --type search` or Read the specified post ID list from the configuration file to obtain the information and comment information of the specified post: `python3 main.py --platform xhs --lt qrcode --type detail`
7. Need help: `python3 main.py --help`
## Configure Crawler:
####      Open Config File: 
1. Find `config/base_config.py`
2. Open in editor **(IDLE, VS code, etc.)**
#### Configure:
##### Config Keywords:
Change `KEYWORDS = 'your keyword here'`
##### Config Platform:
Change `PLATFORM = 'xhs/douyin/kuaishou/bilibili/weibo'`
##### Config Save Option:
Change `SAVE_DATA_OPTION = 'json/db/csv/(txt option available for xhs)'` 
##### Config Crawler Max Notes:
 Change `CRAWLER_MAX_NOTES_COUNT = post count`
## Info
➡️➡️➡️ [How to use IP proxy](docs/proxy usage.md)

### Run error FAQ Q&A:
➡️➡️➡️ [FAQ](docs/FAQ.md)

### Project code structure:
➡️➡️➡️ [Project code structure description](docs/project code structure.md)

### Mobile phone number login instructions:
➡️➡️➡️ [Mobile phone number login instructions](docs/Mobile phone number login instructions.md)
<img src="https://i.ibb.co/W3yVXZK/Screenshot-2024-04-16-at-8-25-59-PM.png" width=300/>