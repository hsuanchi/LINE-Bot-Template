# LINE Bot Template

[![codecov](https://codecov.io/gh/hsuanchi/LINE-Bot-Template/branch/master/graph/badge.svg?token=HN2G37H56S)](https://codecov.io/gh/hsuanchi/LINE-Bot-Template)

## 1. Side Project 原由
最近加入早起團 AM 6:00 要起床打卡，看到大家用人工統計出席的方式很費時，所以寫了這隻群聊的打卡機器人，最後將程式整理成範本並包好 Docker 環境，有需要的人只需要申請 [LINE develops 帳戶](https://developers.line.biz/zh-hant/)和串接 [Google Sheets](https://pygsheets.readthedocs.io/en/stable/authorization.html#oauth-credentials) 就完成囉！

## 2. Requirements
- Python >= 3.4

## 3. Prerequisite Setup

1. 建立 [LINE develops 帳戶](https://developers.line.biz/zh-hant/)，並新增 Messaging API channel 機器人

2. 建立 Google Sheet API 權限，這邊使用 [pygsheets](https://pygsheets.readthedocs.io/en/stable/authorization.html#oauth-credentials) 套件，跟隨 [pygsheets document 步驟](https://pygsheets.readthedocs.io/en/stable/authorization.html#oauth-credentials) 就可以拿到 OAuth Credentials，讓我們可以使用對 Google Sheet 進行操作 (補充建置上有問題的話，也可以參考這篇 [python 串接 GoogleSheet 新增、讀取、更新和刪除](https://www.maxlist.xyz/2018/09/25/python_googlesheet_crud/))

3. 將剛剛第二步獲得的 Google OAuth Credentials 放到資料夾位置：`LINE-Bot-Template/bot/config/api-key.json`


4. 最後建立`LINE-Bot-Template/.flaskenv`，並將在第一步 LINE develops 帳戶中的 CHANNEL_ACCESS_TOKEN 和 CHANNEL_SECRET 填入，而 google_sheet_url 則是填入要操作的 google sheet 網址，範例如下：

```
export FLASK_APP=main.py

export CHANNEL_ACCESS_TOKEN="get your access token from Line developers page"

export CHANNEL_SECRET='yout line bot channel secret key'

export google_sheet_url='https://docs.google.com/spreadsheets/d/kkkkkk-aaaaaa-ssssss/'
```


## 4. Setup Development Environment & Run
▍Method 1 - Docker
```
$ bash boot.sh
```

▍Method 2 - Python Built-in venv

- Create your virtual environment
```
$ python3 -m venv venv
```
- And enable virtual environment
```
$ . venv/bin/activate
```
- Install requirements
```
$ pip install -r requirements.txt 
```
- Run Flask
```
$ flask run
```

▍Method 3 - Poetry
- Install requirements
```
$ poetry install
```
- And enable virtual environment
```
$ poetry shell
```
- Run Flask
```
$ flask run
```

## 5. Test
Run the following command:
```
$ flask test
```

To run tests with coverage report:
```
$ bash test.sh
```


## 6. 貢獻
PRs are welcome!
