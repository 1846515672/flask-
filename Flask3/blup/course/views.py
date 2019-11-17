# """
# 视图文件
# """
from blup.course import course
# from flask import request
# from flask import Response
# from flask import session
# import random, os
# from blup import app
# from sqlalchemy import or_, and_
# from flask import redirect
# import hashlib
# from flask import render_template
# from blup.course.models import *

@course.route("/")
def index():
    return "course 'index hello world"




# @app.route("/", methods=["get","post"])
# def index():
#     register = request.args.get("register")
#     if request.method == "POST":
#         username = request.form.get("name")
#         email = request.form.get("email")
#         password = request.form.get("password")
#
#         user = User()
#         user.nick_name = username
#         user.password = set_password(password)
#         user.email = email
#         user.save()
#         register = True
#     response = Response(render_template("index.html", **locals()))
#     return response
#
#
# def set_password(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode())
#     result = md5.hexdigest()
#     return result
#
#
# @app.route("/login/",methods=["get","post"])
# def login():
#     response = redirect("/") #跳转回首页
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")
#
#         user = User.query.filter_by(email = email).first()
#         if user:
#             request_password = set_password(password)
#             if request_password == user.password:
#                 response.set_cookie("email", user.email)
#     return response
#
#
# @app.route("/logout/")
# def logout():
#     response = redirect("/")
#     response.delete_cookie("email")
#     return response
#
#
# @app.route("/courses/index/<path:url_arg>/")
# def courses_index(url_arg):
#     # 获取label，固定
#     label_list = Label.query.all()
#     # 获取url上匹配的过滤条件，并且使用/对过滤条件进行切分
#     args = url_arg.split("/")
#     # 测试过滤条件的长度
#     len_arg = len(args)
#     # 如果参数的个数是两个，那么安装参数1是类型 参数2是标签进行查询
#     # 设置全局参数，防止在判断的时候有条件分支缺失导致变量不存在
#     c_type = ""  # url传递过来的课程类型
#     label = ""  # url传递过来的课程标签
#     referer_url = ""  # 提供lable重新定位的参数
#     referer_url1 = ""  # 提供给c_type重新定位的参数
#     if len_arg == 2:  # 请求由类型也有标签
#         c_type, label = args  # 分解参数
#         # 查询python所有免费或者付费
#         referer_url = "/course/index/%s/" % c_type  # 定义lable标签的链接
#         referer_url1 = label + "/"  # 定义课程类型的链接
#         label_id = Label.query.filter_by(l_name=label)[0].id  # 获取对应的标签
#         course_list = Course.query.filter(
#             and_(
#                 Course.c_type == int(c_type),
#                 Course.label_id == label_id
#             )
#         )  # 查询所对应的多有课程
#         if int(c_type) == 3:
#             course_list = Course.query.filter(
#                 and_(
#                     Course.label_id == label_id
#                 )
#             )  # 查询所对应的多有课程
#     # url只有一个路由请求参数
#     elif len_arg == 1:
#         arg, = args  # 获取参数
#         if arg.isdigit():  # 通过类型判断参数是c_type 函数 lable
#             c_type = arg  # 请求参数是c_type
#             referer_url = "/course/index/%s/" % c_type  # 定义lable标签的链接
#             if int(c_type) == 3:  # 判断全部
#                 course_list = Course.query.all()
#             else:
#                 course_list = Course.query.filter_by(c_type=int(c_type))
#         else:
#             label = arg
#             referer_url1 = label + "/"  # 定义c_type标签的链接
#             course_list = Label.query.filter_by(l_name=label)[0].c_label
#     print("c_type: %s" % c_type)
#     print("label: %s" % label)
#     return render_template("courses/index.html", **locals())
#
#
# @app.route("/developer/index/")
# def developer_index():
#     return render_template("developer/index.html", **locals())
#
#
# @app.route("/paths/index/")
# def paths_index():
#     return render_template("paths/index.html", **locals())
#
#
# @app.route("/questions/index/")
# def questions_index():
#     return render_template("questions/index.html", **locals())
#
# @app.route("/questions/show/")
# def questions_show():
#     return render_template("questions/show.html", **locals())
#
#
# @app.route("/bootcamp/index/")
# def bootcamp_index():
#     return render_template("bootcamp/index.html", **locals())
#
#
# @app.route("/vip/index/")
# def vip_index():
#     return render_template("vip/index.html", **locals())
#
#
# @app.route("/privacy/index/")
# def privacy_index():
#     return render_template("privacy/index.html", **locals())
#
#
# @app.route("/labs/index/")
# def labs_index():
#     return render_template("labs/index.html", **locals())
#
#
# @app.route("/edu/index/")
# def edu_index():
#     return render_template("edu/index.html", **locals())
#
#
# @app.route("/courses/reports/")
# def courses_reports():
#     return render_template("courses/reports.html", **locals())
#
#
# @app.route("/courses/show/")
# def courses_show():
#     return render_template("courses/show.html", **locals())
#
#
# @app.route("/courses/show2/")
# def courses_show2():
#     return render_template("courses/show2.html", **locals())
#
#
# @app.route("/edu/uestc/")
# def edu_uestc():
#     return render_template("edu/uestc.html", **locals())
#
#
# # @app.route("/al/")
# # def add_label():
# #     # string = "Python C/C++ Linux Web 信息安全 PHP Java NodeJS Android GO Spark 计算机专业课 Hadoop HTML5 Scala Ruby R 网络 Git SQL NoSQL 算法 Docker Swift 汇编 Windows"
# #     string = "UI CAD"
# #     for i in string.split():
# #         l = Label()
# #         l.l_name = i
# #         l.description = "%s课啊，真滴好啊"%i
# #         l.save()
# #     return "hello world"
#
# # @app.route("/ac/")
# # def add_course():
# #     result = [
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/ncn63.jpg', 'alt': '新手指南之玩转实验楼'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/ncn1.jpg', 'alt': 'Linux 基础入门（新版）'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1480389303324.png', 'alt': 'Kali 渗透测试 - 后门技术实战（10个实验）'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1480389165511.png', 'alt': 'Kali 渗透测试 - Web 应用攻击实战'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1482113947345.png', 'alt': '使用OpenCV进行图片平滑处理打造模糊效果'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1482807365470.png', 'alt': '使用 Python 解数学方程'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1482215587606.png', 'alt': '跟我一起来玩转Makefile'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1480386391850.png', 'alt': 'Kali 渗透测试 - 服务器攻击实战（20个实验）'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1482113981000.png', 'alt': '手把手教你实现 Google 拓展插件'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1482113522578.png', 'alt': 'DVWA之暴力破解攻击'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1482113485097.png', 'alt': 'Python3实现简单的FTP认证服务器'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1481689616072.png', 'alt': 'SQLAlchemy 基础教程'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1481511769551.png', 'alt': '使用OpenCV&&C++进行模板匹配'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1481512189119.png', 'alt': 'Metasploit实现木马生成、捆绑及免杀'},
# #      {'src': 'https://dn-simplecloud.shiyanlou.com/1480644410422.png', 'alt': 'Python 3 实现 Markdown 解析器'}]
# #     for i in range(25):
# #         for cou in result:
# #             c = Course()
# #             name = cou.get("alt")
# #             if i != 0:
# #                 name +=" (%s)"%i
# #             c.c_name = name  # 课程名称
# #             c.description = "%s课程啊，真滴好啊"%name  # 课程描述
# #             c.picture = cou.get("src")  # 课程logo
# #             c.show_number = random.randint(1,100000)  # 观看人数
# #             c.c_time_number = random.randint(7,32)  # 课时
# #             c.class_label = random.choice(Label.query.all())
# #             c.save()
# #     return "hello world"
#
#
# @app.route("/get_test/", methods=["GET","POST"])
# def get_test():
#     course = ""
#     label_list = Label.query.all()
#     if request.method == "POST":
#         data = request.form
#         c_name = data.get("c_name")
#         show_number = data.get("show_number")
#         c_time_number = data.get("c_time_number")
#         label = data.get("label")
#         description = data.get("description")
#         logo = request.files.get("logo")
#
#         #保存文件分为两步
#         # 文件保存到服务器
#         file_path = os.path.join(
#             os.path.dirname(os.path.abspath(__file__)), "static\img\%s" % logo.filename
#         )
#         logo.save(file_path)
#         #文件路径保存到数据中
#         course = Course()
#         course.c_name = c_name
#         course.show_number = show_number
#         course.description = description
#         course.c_time_number = c_time_number
#         course.picture = "/static\img\%s" % logo.filename #保存图片路径
#         course.class_label = Label.query.get(int(label)) #保存外键
#         course.save()
#
#     return render_template("request_example.html", **locals())
#
#
# @app.route("/cookies/")
# def cookies():
#     session["username"] = "laobian" #设置session
#     session.get("username")  #获取session
#     del session["username"]  #删除session
#     return render_template("1.html")
#
#
# @app.route("/ajax/")
# def ajax_example():
#     return render_template("ajax_eample.html")
#
#
# @app.route("/ajax_user/",methods=["get","POST"])
# def ajax_user():
#     result = {"is_user":False}
#     if request.method == "POST":
#         nick_name = request.form.get("nick_name")
#         email = request.form.get("email")
#         password = request.form.get("password")
#         user = User()
#         user.nick_name = nick_name
#         user.email = email
#         user.password = set_password(password)
#         user.save()
#         result["is_user"] = True
#     return result