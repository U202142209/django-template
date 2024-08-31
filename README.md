# django模板

## 简介

1. 整理了常用的settings配置
2. 连接国歌数据库
3. 创建示例应用
4. 开箱即用，clone此项目即可开始你的创作

## 一些常用命令整理

创建虚拟环境

```text
conda create -n django_bkw python=3.8
conda activate django_bkw
pip3 install django
pip install mysqlclient
pip install django-cors-headers
```

manage.py

```text
python manage.py startapp schedule_app
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --database=default
python manage.py runserver
python manage.py runserver 0.0.0.0:60023

```
