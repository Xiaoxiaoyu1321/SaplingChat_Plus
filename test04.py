import socket
import wx
import _thread
#设置服务器信息
host ="111.67.198.246"
port = 19730
fuck = "@#y!h(d^l?"
Client = socket.socket()
version = "1.0"
Client.connect((host,port))
print("Connect to Server")

def SendMessage(event):
    print(event)
    userin = send_text.GetValue()
    msg = username_text.GetValue() + fuck + send_text.GetValue()
    Client.send(msg.encode('gbk'))
    send_text.SetValue("")
    print("SendMessageSuccess")
def  GetMessage():
    print("GetMessageLoaded")
    while True:
        WillGet = Client.recv(1024).decode('gbk')
        havehistory =str(chathistory_text.GetValue())
        global sb
        sb =  havehistory + "\n" + WillGet
        chathistory_text.SetValue(sb)
        print("GetMessageSuccess")
_thread.start_new_thread(GetMessage,())
app = wx.App()#实例化一个主循环
frame = wx.Frame(None,title="SaplingChat_Plus V" + version,pos=(200,200),size=(600,410))#实例化一个窗口

username_text = wx.TextCtrl(frame,pos=(5,5),size=(570,30))
chathistory_text = wx.TextCtrl(frame,-1,pos=(5,35),size=(570,300),style= wx.TE_MULTILINE)
send_text= wx.TextCtrl(frame,pos=(5,335),size=(530,30))
send_button = wx.Button(frame,label="发送",pos=(535,335),size=(50,30))
send_button.Bind(wx.EVT_BUTTON,SendMessage)
chathistory_text.SetValue("欢迎来到橘子树聊天室，此版本由Xiaoxiaoyu开发，版本：" + version)
#panel = wx.Panel(self, -1)  
frame.Show()
app.MainLoop()#启动主循环
