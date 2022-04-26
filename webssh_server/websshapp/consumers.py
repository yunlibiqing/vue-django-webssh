
from channels.generic.websocket import WebsocketConsumer
import paramiko
import threading
import time


# 配置服务器信息
HOSTS = "xxx"  # IP
PORT = 22  # 端口
USERNAME = "xxx"  # 用户名
PASSWORD = "xxx"  # 密码


class MyThread(threading.Thread):
    def __init__(self, chan):
        threading.Thread.__init__(self)
        self.chan = chan

    def run(self):
        while not self.chan.chan.exit_status_ready():
            time.sleep(0.1)
            try:
                data = self.chan.chan.recv(1024)
                self.chan.send(data.decode("utf-8").replace("\n", "\r\n"))
            except Exception as ex:
                print(str(ex))
        self.chan.sshclient.close()
        return False


class WebSSHService(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.sshclient = paramiko.SSHClient()
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshclient.connect(HOSTS, PORT, USERNAME, PASSWORD)
        self.chan = self.sshclient.invoke_shell(term='xterm')
        self.chan.settimeout(0)
        t1 = MyThread(self)
        t1.setDaemon(True)
        t1.start()

    def receive(self, text_data=None, bytes_data=None):
        self.chan.send(text_data)

    def disconnect(self, code):
        self.sshclient.close()