import subprocess
search_keyword = input('- ')
# The path to the Python script you want to overwrite
target_file_path = '/Users/ethanwang/Downloads/MediaCrawler-main/config/base_config.py'

# The new content you want to put in the file
new_content = '''# 基础配置
PLATFORM = "xhs"
KEYWORDS = "''' + search_keyword + '''"
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookie
COOKIES = ""
CRAWLER_TYPE = "search"

# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 设置为True不会打开浏览器（无头浏览器），设置False会打开一个浏览器（小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码）
HEADLESS = True

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# 数据保存类型选项配置,支持三种类型：csv、db、json
SAVE_DATA_OPTION = "json" # csv or db or json

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 20

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 4


# 评论关键词筛选(只会留下包含关键词的评论,为空不限制)
COMMENT_KEYWORDS = [
    # "真棒"
    # ........................
]

# 指定小红书需要爬虫的笔记ID列表
XHS_SPECIFIED_ID_LIST = [
    "6422c2750000000027000d88",
    "64ca1b73000000000b028dd2",
    "630d5b85000000001203ab41",
    # ........................
]

# 指定抖音需要爬取的ID列表
DY_SPECIFIED_ID_LIST = [
    "7280854932641664319",
    "7202432992642387233"
    # ........................
]

# 指定快手平台需要爬取的ID列表
KS_SPECIFIED_ID_LIST = [
    "3xf8enb8dbj6uig",
    "3x6zz972bchmvqe"
]

# 指定B站平台需要爬取的视频bvid列表
BILI_SPECIFIED_ID_LIST = [
    "BV1d54y1g7db",
    "BV1Sz4y1U77N",
    "BV14Q4y1n7jz",
    # ........................
]

# 指定微博平台需要爬取的帖子列表
WEIBO_SPECIFIED_ID_LIST = [
    "4982041758140155",
    # ........................
]
'''
print(new_content)

# Write the new content to the target file
with open(target_file_path, 'w') as target_file:
    target_file.write(new_content)
venv_python = '/Users/ethanwang/Downloads/MediaCrawler-main/venv/bin/python3'

# Define the path to the script you want to run
script_path = '/Users/ethanwang/Downloads/MediaCrawler-main/main.py'

# Run your Python script using the Python interpreter in your virtual environment
##subprocess.run([venv_python, script_path], check=True)
