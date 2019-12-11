# tdog舔狗果蔬超市👅🐶

## 环境
python3.7
pip

## django安装命令
pip3 install django==2.2.5


## 命令（在项目目录下）
### 运行 python3 manage.py runserver 8000
#### 8000为端口号，可省略，如果不写则默认为8000端口
### 创建新app python3 manage.py startapp xxx(app name) 
#### 例如 python3 manage.py startapp users 
### 数据库迁移（每次更改app中的models.py后需要执行）
#### 1. pyhton3 manage.py makemigrations
#### 2. python3 manage.py migrate
### 创建管理员 python3 manage.py createsuperuser

## 进入管理界面
#### 进入管理界面需要有superuser，如果没有，先使用python3 manage.py createsuperuser命令创建管理员，数据库中UserProfile的主键为phone，故在申请的时候请不要使用相同的手机号码
#### 1. 启动服务python3 manage.py runserver
#### 2. 输入url http://127.0.0.1:8000/admin
