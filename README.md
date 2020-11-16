# LINE Bot Template

[![codecov](https://codecov.io/gh/hsuanchi/LINE-Bot-Template/branch/master/graph/badge.svg?token=HN2G37H56S)](https://codecov.io/gh/hsuanchi/LINE-Bot-Template)

## 1. Side Project 原由
最近加入早起團 AM 6:00 要起床打卡，看到大家用手動統計出席的方式很費時，所以寫了這隻 LINE Bot 群聊的打卡機器人，只需要在群組中輸入固定字詞，機器人就會將使用者姓名、打卡時間傳送至 Google Sheet，再串接 DataStudio 將資料視覺化。

#### Demo - 覺化圖表
<img src="https://github.com/hsuanchi/LINE-Bot-Template/blob/master/img/line_chart.jpg" width="800px" height="auto">

#### Demo - 出席統計 by month
<img src="https://github.com/hsuanchi/LINE-Bot-Template/blob/master/img/table_by_month.jpg" width="800px" height="auto">

#### Demo - 出席統計 by week
<img src="https://github.com/hsuanchi/LINE-Bot-Template/blob/master/img/table_by_week.jpg" width="800px" height="auto">

#### Demo - LINE Bot 群組
<img src="https://github.com/hsuanchi/LINE-Bot-Template/blob/master/img/line_bot_demo.jpg" width="200px" height="auto">

如果有想建置機器人的朋友，這份程式已經整理過，並包好 Docker 環境，有需要的朋友只需要依以下步驟建立，就可以快速完成一個打卡聊天機器人囉

## 2. Requirements
- Python >= 3.4

## 3. Prerequisite Setup

1. 首先建立 LINE develops 帳戶，請參考這篇 [[Flask – LINE Bot 教學] 事前準備篇 (一) - Max行銷誌](https://www.maxlist.xyz/2020/11/16/flask-line-bot-pre-set/)
- [ ] 取得 Channel secret
- [ ] 取得 Channel access token

2. 串接 Google Sheet 操作，請參考這篇 [python 串接 GoogleSheet 新增、讀取、更新和刪除 - Max行銷誌](https://www.maxlist.xyz/2018/09/25/python_googlesheet_crud/)
- [ ] 取得 Google OAuth Credentials

3. 將剛剛拿到的 Google OAuth Credentials 放到資料夾位置：`LINE-Bot-Template/bot/config/api-key.json`

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


## 6. Contributing
PRs are welcome!
