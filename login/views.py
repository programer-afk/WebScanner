from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as Login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import json
import socket
from .forms import RegisterForm

# Create your views here.

def login(request):
    msg = {
        'site_title': "WebScanner",
        'site_header': "WebScanner 登录",
        'error': '',
        'color': 'transparent',
    }
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            msg['error'] = "用户名或密码错误！"
            msg['color'] = "#fef0f0"
        else:
            Login(request, user)
            return redirect("/index")
        # print(user)
        # print(msg)
    return render(request, "login.html", msg)


def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()
            # 注册成功，跳转回首页
            return redirect('/login/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'register.html', context={'form': form})


def login_out(request):
    logout(request)  # 注销
    return redirect("/index")  # 页面跳转

def forgot_password(request):
    msg = {
        'site_title': "WebScanner",
        'site_header': "WebScanner 找回密码",
        'error': '',
        'color': 'transparent',
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        # 检查邮箱是否存在
        if not User.objects.filter(email=email).exists():
            msg['error'] = "该邮箱地址未注册！"
            msg['color'] = "#fef0f0"
            return render(request, 'forgot_password.html', msg)
            
        # 创建密码重置表单
        form = PasswordResetForm({'email': email})
        if form.is_valid():
            try:
                # 获取用户
                user = User.objects.get(email=email)
                # 生成令牌
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                # 构建邮件正文
                email_template_name = "registration/password_reset_email.html"
                context = {
                    "email": user.email,
                    "domain": request.get_host(),
                    "site_name": "WebScanner",
                    "uid": uid,
                    "user": user,
                    "token": token,
                    "protocol": "http" if not request.is_secure() else "https",
                }
                email_body = render_to_string(email_template_name, context)
                
                # 发送邮件
                try:
                    send_mail(
                        subject="重置您的WebScanner密码",
                        message=email_body,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email],
                        fail_silently=False,
                    )
                    msg['error'] = "重置密码链接已发送到您的邮箱，请查收！"
                    msg['color'] = "#f0f9eb"
                except BadHeaderError:
                    msg['error'] = "邮件发送失败，请稍后重试！"
                    msg['color'] = "#fef0f0"
                except socket.gaierror as e:
                    # 处理DNS解析错误
                    if e.errno == socket.EAI_NONAME or e.errno == 11001:  # 11001是Windows中的WSAHOST_NOT_FOUND
                        msg['error'] = "邮件服务器连接失败，请检查网络连接或联系管理员！"
                    else:
                        msg['error'] = f"网络错误：{e.strerror}"
                    msg['color'] = "#fef0f0"
                except ConnectionRefusedError:
                    msg['error'] = "无法连接到邮件服务器，请联系管理员！"
                    msg['color'] = "#fef0f0"
                except TimeoutError:
                    msg['error'] = "连接邮件服务器超时，请稍后重试！"
                    msg['color'] = "#fef0f0"
                except Exception as e:
                    # 其他异常
                    msg['error'] = f"发送邮件时出错：{str(e)}"
                    msg['color'] = "#fef0f0"
            except Exception as e:
                msg['error'] = f"处理请求时出错：{str(e)}"
                msg['color'] = "#fef0f0"
        else:
            msg['error'] = "邮箱格式不正确！"
            msg['color'] = "#fef0f0"
    
    return render(request, 'forgot_password.html', msg)