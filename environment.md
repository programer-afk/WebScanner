# Web-Scanner 环境配置说明

## 系统要求
- Python 3.7+
- Windows 10/11
- 至少 4GB RAM
- 至少 2GB 可用磁盘空间

## Python 依赖包
主要依赖包：
- Django==3.1.4
- django-simpleui==2021.1.1
- django-import-export==2.5.0
- django-password-reset==2.0
- requests==2.25.1
- beautifulsoup4==4.9.3
- python-docx==1.1.0
- pandas==1.3.5

完整依赖列表见 requirements.txt

## 数据库配置
- 数据库类型：SQLite
- 数据库文件：db.sqlite3
- 位置：项目根目录

## 服务器配置
- 开发服务器端口：9999
- 默认访问地址：http://127.0.0.1:9999
- 管理后台地址：http://127.0.0.1:9999/admin

## 环境变量配置
在 Web_Scanner/settings.py 中配置：
```python
# 调试模式
DEBUG = True

# 允许的主机
ALLOWED_HOSTS = ['*']

# 静态文件配置
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# 媒体文件配置
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

# 登录URL
LOGIN_URL = '/login/'
```

## 安装步骤
1. 创建虚拟环境：
```bash
python -m venv venv
```

2. 激活虚拟环境：
```bash
# Windows
venv\Scripts\activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 初始化数据库：
```bash
python manage.py migrate
```

5. 创建超级用户：
```bash
python manage.py createsuperuser
```

6. 运行服务器：
```bash
python manage.py runserver 9999
```

## 注意事项
1. 确保端口9999未被占用
2. 首次运行需要执行数据库迁移
3. 建议使用虚拟环境隔离项目依赖
4. 生产环境部署时请关闭DEBUG模式 