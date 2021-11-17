import smtplib
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# 163邮箱只能发送纯文本，不可以添加附件和图片
def sendEmailBy163(title, info, receivers, senderEmail='Mr_Qian_Ives@163.com', password=os.environ["pass163"],
                   name="钱甫新"):
    # 163邮箱的服务器
    host = 'smtp.163.com'

    # 端口
    port = 465

    # 拼接昵称   钱先生 <Mr_Qian_Ives@163.com>
    name = name + " <" + senderEmail + ">"

    # 拼接发送的内容
    msg = '\n'.join(['From: {}'.format(name), 'Subject: {}'.format(title), '', info])

    # 发送的邮件使用加密形式
    try:
        smtp = smtplib.SMTP_SSL(host=host, port=port)
        # 登录账号
        res = smtp.login(user=senderEmail, password=password)

        # 发送邮件
        smtp.sendmail(from_addr=senderEmail, to_addrs=receivers, msg=msg.encode())

        # 退出
        smtp.quit()
        return True
    except Exception as e:
        print(e.args)
        smtp.quit()
        return False


# QQ邮箱可以发送文本、附件（仅限一个，多个文件请压缩）、图片（把图片当成附件）
def sendEmailByQQ(title, info, accessory, receivers, senderEmail='1356227919@qq.com', password=os.environ["passqq"],
                  name="钱甫新"):
    # QQ邮箱的服务器
    host = 'smtp.qq.com'

    # 端口
    port = 465

    # 拼接昵称   钱先生 <1356227919@qq.com>
    name = name + " <" + senderEmail + ">"

    # related类型，把其它内容以内嵌资源的方式存储在邮件中
    message = MIMEMultipart('related')

    # 设置发件人的信息
    message['From'] = Header(name, 'utf-8')

    # 设置邮件标题
    message['Subject'] = Header(title, 'utf-8')

    # html引入图片
    # alternative类型，超文本内容
    alt = MIMEMultipart('alternative')

    # msgAlternative加入message
    message.attach(alt)

    # html代码，使用img标签引入照片，照片的id在下方。
    html = """
    <p>""" + info + """</p>
   <p><img src="cid:image1"></p>
    """

    # 把html代码加入alt
    alt.attach(MIMEText(html, 'html', 'utf-8'))

    # 下面注释的代码是在邮件内容中加入图片，个人认为没啥意义，如果后期需要该功能，可以直接使用
    # # html中图片的路径
    # bgPath = "/Users/apple/PycharmProjects/pythonTest/WebWorm/WordAndPicture/shadiao/1616491998171.jpeg"
    #
    # # 读取图片
    # mim = MIMEImage(open(bgPath, 'rb').read())
    #
    # # 设置图片的ID，HTML文本中引用该ID
    # mim.add_header('Content-ID', '<image1>')
    #
    # # mim加入message
    # message.attach(mim)

    # 附件的名字
    accessoryPath = os.path.basename(accessory);

    # 打开文件
    accessoryObject = MIMEText(open(accessory, 'rb').read(), 'base64', 'utf-8')
    accessoryObject["Content-Type"] = 'application/octet-stream'

    # 设置附件名称
    accessoryObject.add_header("Content-Disposition", "attachment", filename=("utf-8", "", accessoryPath))

    # 添加附件
    message.attach(accessoryObject)

    # 发送的邮件使用加密形式
    try:
        smtp = smtplib.SMTP_SSL(host=host, port=port)
        # 登录账号
        res = smtp.login(user=senderEmail, password=password)
        # 发送邮件
        smtp.sendmail(from_addr=senderEmail, to_addrs=receivers, msg=message.as_string())
        # 退出
        smtp.quit()
        return True
    except Exception as e:
        print(e.args)
        smtp.quit()
        return False



sendEmailByQQ("请查看手机消息","立即查看","990509820@qq.com")