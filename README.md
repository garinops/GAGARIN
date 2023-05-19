# GAGARIN
## Api for https://developers.garinasset.com/tools/
***
- 封装依赖
```shell
pip freeze > requirements.txt
```

***
## 一、虚拟环境
- 下载源代码
```shell
git clone git@github.com:garinops/GAGARIN.git

mv GAGARIN server.gagarin-uvicorn
```
- 创建虚拟环境
```shell
cd server.gagarin-uvicorn/

python3.11 -m venv venv-gagarin-uvicorn
```
- 激活虚拟环境
```shell
source venv-gagarin-uvicorn/bin/activate
```
***
## 二、pip依赖安装
- 依赖安装
```shell
pip install -r requirements.txt

# 安装uvicorn后端
pip install uvicorn
```
***
## 三、uvicorn服务配置 

- 配置开机启动(关键是处理其中所涉及权限)
```shell
sudo nano /lib/systemd/system/gagarin-uvicorn.service
```
```cfg
[Unit]

Description=Uvicorn Daemon for FastAPI Demo Application

After=network.target


[Service]

User=ubuntu

Group=ubuntu

WorkingDirectory=/home/ubuntu/server.gagarin-uvicorn/

ExecStart=/home/ubuntu/server.gagarin-uvicorn/venv-gagarin-uvicorn/bin/uvicorn main:gagarin --host 0.0.0.0 --port 8080 --root-path /gagarin


[Install]

WantedBy=multi-user.target
```
```shell
sudo systemctl daemon-reload
```
```shell
sudo systemctl enable gagarin-uvicorn.service
```
## 四、运行gagarin-uvicorn服务
```shell
# gagarin-uvicorn服务运行后， 依据启动项配置，监听0.0.0.0:8080
sudo systemctl start gagarin-uvicorn.service
```
***

