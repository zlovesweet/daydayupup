import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from loguru import logger

SMTP_ADDRESS = {
    "qq": 'smtp.qq.com'
}


class EmailStmp:
    def __init__(self, addr=None, key=None, mode='qq'):
        """
        初始化EmailStmp
        :param addr: 发件人的地址
        :param key: stmp服务授权码
        :param mode: qq、163...
        """
        self.addr = addr
        self.key = key
        self.smtp = None
        self.mode = mode
        self.msg = MIMEMultipart('related')
        self.msg['From'] = self.addr

        mail_receivers = ['w15123293984@163.com']
        # 配置邮箱信息

    def _conn(self):
        self.smtp = smtplib.SMTP(SMTP_ADDRESS[self.mode])  # 配置QQ邮箱的smtp服务器地址
        self.smtp.starttls()
        self.smtp.login(self.addr, self.key)

    def edit_title(self, title='邮件标题'):
        # 邮件标题设置
        self.msg['Subject'] = title

    def edit_content(self, content='邮件内容', mode='plain'):
        # content = MIMEText(content, mode, 'utf-8')
        content = MIMEText(content, _subtype=mode, _charset="utf-8")
        self.msg.attach(content)

        # content = MIMEText('你好呀，这是来自QQ邮箱的信息--from python发送~!', 'plain', 'utf-8')
        #
        # content = MIMEText(
        #     "<html><h2>网页标题</h2>"
        #     "<br>"
        #     "<a href='https://www.baidu.com'>百度一下</a></html>"
        #     "<br>"
        #     "<font color='red' size='10'>红色字体</font>",
        #     _subtype="html", _charset="utf-8")

    def add_file(self, file_path=None):
        ...

        # 添加图片附件
        # imageFile = r"2111.jpg"
        # imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
        # imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
        # msg.attach(imageApart)

        # 添加Excel附件
        # excelFile = r'sample1.xlsx'
        # excelApart = MIMEApplication(open(excelFile, 'rb').read())
        # excelApart.add_header('Content-Disposition', 'attachment', filename=excelFile)
        # msg.attach(excelApart)

    def send(self, to_addr: list):
        try:
            self._conn()
            self.msg['to'] = ','.join(to_addr)
            self.smtp.sendmail(self.addr, to_addr, self.msg.as_string())
            logger.info('发送成功')
        except smtplib.SMTPException as e:
            logger.error(e)
        finally:
            self.smtp.quit()


if __name__ == '__main__':
    to_addr_list = ['']
    email = EmailStmp(addr='', key='', mode='qq')
    email.edit_title('大胆！')
    html = "<html>" \
           "<h2>商店刷新</h2>" \
           f"<p>本次刷新数次：{1}</p>" \
           f"<p>消耗钻石：{2}</p>" \
           f"<p>消耗钻石：{3}</p>" \
           f"<p>剩余金币：{4}</p>" \
           f"<p>剩余金币：{5}</p>" \
           f"<p>购买书签：{6}</p>" \
           f"<p>购买奖章：{7}</p>" \
           "<html>"

    # email.edit_content('你寄吧谁啊？')
    email.edit_content(content=html, mode='html')
    email.send(to_addr_list)
