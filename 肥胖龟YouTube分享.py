import tkinter as tk
import os
import requests
from bs4 import BeautifulSoup
import urllib.request
import qrcode
from PIL import ImageTk,Image

url_bl = 'https://www.youtube.com/watch?v=ofimgaO7Qck'
text_bl  = '我在YouTube上发现了一个精彩视频，快来看看吧！'

magic_bl = 'on'
FATTURTLE_BL = 'on'

window = tk.Tk()
window.title('肥胖龟YouTube分享启动器')
window.geometry('466x500')

var = tk.StringVar()
command = tk.Label(window, textvariable=var, bg='white', font=('Arial,12'), width=25, height=2)
command.place(x=0,y=0)
var.set('肥胖龟YouTube分享启动器')


url = tk.Entry(window,show=None)
url.place(x=50,y=50,width=300,height=35)

text = tk.Entry(window,show=None)
text.place(x=50,y=100,width=300,height=35)

url_text = tk.Label(window,text='链接',width=5,height=2,bg='white', font=('Arial,12'))
url_text.place(x=0,y=50)

text_text = tk.Label(window,text='文本',width=5,height=2,bg='white', font=('Arial,12'))
text_text.place(x=0,y=100)

def set_url():
    global url_bl
    url_bl = url.get()
    var.set('已设置链接')

url_Button = tk.Button(window,text='设置链接', width=12, height=2, command=set_url)
url_Button.place(x=360, y=50)

def set_text():
    global text_bl
    text_bl = text.get()
    var.set('已设置文本')

text_Button = tk.Button(window,text='设置文本', width=12, height=2, command=set_text)
text_Button.place(x=360, y=100)

def Start():
    Start_window = tk.Toplevel()

    Start_window.geometry('645x463')



    # 获取当前文件所在的目录路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 用户输入YouTube视频链接
    video_link = url.get()

    # 发送GET请求获取视频页面内容
    response = requests.get(video_link)
    content = response.text

    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(content, 'html.parser')

    # 爬取视频名称
    video_title = soup.find('title').text.strip()

    # 爬取视频封面并保存
    video_thumbnail = soup.find('meta', property='og:image')['content']
    urllib.request.urlretrieve(video_thumbnail, os.path.join(current_dir, 'image.png'))

    # 存储视频名称到变量name
    name = video_title
    Start_window.title(name)
    
    # 生成二维码并保存
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(video_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(os.path.join(current_dir, 'qrcode.png'))

    print("视频名称：", name)
    print("视频封面已保存为image.png")
    print("链接二维码已保存为qrcode.png")

    global text_bl
    text2 = tk.Label(Start_window, text=text_bl, bg='white', font=('Arial,12'), width=75, height=2)
    text2.place(x=0,y=0)

    text3 = tk.Label(Start_window, text=name, bg='white', font=('Arial,12'), width=75, height=2)
    text3.place(x=0,y=50)

    # 获取当前执行脚本文件名
    filename = __file__
    # 获取脚本文件名所在绝对路径
    abspath = os.path.abspath (filename)
    # 获取脚本文件所在目录
    dname = os.path.dirname (abspath)
    # 改变当前工作目录为dname
    os.chdir (dname)


    fm1=Image.open('image.png')
    fm2 = fm1.resize((645, 363), Image.LANCZOS)
    # 保存新图片文件
    fm2.save("image_new.png")
    fm3=Image.open('image_new.png')
    fm4=ImageTk.PhotoImage(fm3)
    fm5=tk.Label(Start_window,text='彩蛋',image=fm4)
    fm5.place(x=0,y=100)

    qrcode1=Image.open('qrcode.png')
    qrcode2 = qrcode1.resize((95, 95), Image.LANCZOS)
    # 保存新图片文件
    qrcode2.save("qrcode_new.png")
    qrcode3=Image.open('qrcode_new.png')
    qrcode4=ImageTk.PhotoImage(qrcode3)
    qrcode5=tk.Label(Start_window,text='彩蛋',image=qrcode4)
    qrcode5.place(x=550,y=0)

    Start_window.mainloop()

Start_button = tk.Button(window,text='生成分享图', width=15, height=2, command=Start)
Start_button.place(x=213, y=0)

def kaiyuan():
    os.system('start https://github.com/FatTurtle2022/FatTurtle_YouTube_Share/releases')

kaiyuan_Button = tk.Button(window,text='开源', width=15, height=2, command=kaiyuan)
kaiyuan_Button.place(x=338, y=0)

# 获取当前执行脚本文件名
filename = __file__
# 获取脚本文件名所在绝对路径
abspath = os.path.abspath (filename)
# 获取脚本文件所在目录
dname = os.path.dirname (abspath)
# 改变当前工作目录为dname
os.chdir (dname)


xftp1=Image.open('xftp.png')
xftp2=ImageTk.PhotoImage(xftp1)
xftp3=tk.Label(window,text='彩蛋',image=xftp2)
xftp3.place(x=0,y=150)

window.mainloop()