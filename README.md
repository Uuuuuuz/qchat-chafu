这是让qchatgpt机器人可以进行起源查服的插件：
使用方法
py文件扔进项目文件夹，napcatqq改下配置

此时curl -v -X POST http://127.0.0.1:5001/query_server -H "Content-Type: application/json" -d "{\"message\": \"查询服务器 gz1.himeneko.cn:20002\"}"
指令可以输出查服结果
chafu文件夹扔进plugin文件夹里

2.以下是napcatqq配置
{
    "http": {
        "enable": true,
        "host": "127.0.0.1:3000",
        "port": 3000,
        "secret": "",
        "enableHeart": false,
        "enablePost": true,
        "postUrls": ["http://127.0.0.1:5000/query_server"]
    },
    "ws": {
        "enable": false,
        "host": "",
        "port": 3001
    },
    "reverseWs": {
        "enable": false,
        "urls": []
    },
    "GroupLocalTime": {
        "Record": false,
        "RecordList": []
    },
    "debug": false,
    "heartInterval": 30000,
    "messagePostFormat": "array",
    "enableLocalFile2Url": true,
    "musicSignUrl": "",
    "reportSelfMessage": false,
    "token": ""
}

安装：pip install a2s flask
pip uninstall python-a2s
pip install python-a2s


