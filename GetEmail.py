import imapclient


def getEmailByImap(email='Mr_Qian_Ives@163.com', password='KJSMBAIGAJFJITBR'):
    import imaplib
    # 设置最大尺寸
    imaplib._MAXLINE = 10000000

    # 登录
    imapObj = imapclient.IMAPClient('imap.163.com', ssl=True, port=993)
    imapObj.login(email, password)

    # 选择文件夹列表
    imapObj.select_folder("INBOX",readonly=True)

    UIDs = imapObj.search(['ALL'])
    # search()方法不返回电子邮件本身，而是返回邮件的唯一整数ID（UID）。然后，可以将这些UID传入fetch()方法，获得邮件内容。
    # 第二个参数代表取出正文部分
    rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
    # 因为fetch出来的内容，人是看不懂的，需要通过pyzmail进行解析
    import pyzmail
    message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
    message.get_subject()
    message.get_addresses('from')
    message.get_addresses('to')
    # 抄送
    message.get_addresses('cc')
    # 密件抄送
    message.get_addresses('bcc')
    #电子邮件可以是纯文本、HTML 或两者的混合。纯文本电子邮件只包含文本，而HTML电子邮件可以有颜色、字体、图像和其他功能，
    # 使得电子邮件看起来像一个小网页。如果电子邮件仅仅是纯文本，它的PyzMessage对象会将html_part属性设为None。
    # 同样，如果电子邮件只是HTML，它的PyzMessage对象会将text_part属性设为None。
    # 获得字节类型的数据，然后对其解析
    message.text_part != None
    message.text_part.get_payload().decode(message.text_part.charset)
    message.html_part != None
    message.html_part.get_payload().decode(message.html_part.charset)
    # 删除邮件
    imapObj.select_folder('INBOX', readonly=False)
    UIDs = imapObj.search(['ON 09-Jul-2015'])
    imapObj.delete_messages(UIDs)
    imapObj.expunge()
    # 退出服务器
    imapObj.logout()
