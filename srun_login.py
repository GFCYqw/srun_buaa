import requests
import time
import re
import os
import textwrap
from encryption.srun_md5 import *
from encryption.srun_sha1 import *
from encryption.srun_base64 import *
from encryption.srun_xencode import *


os.system("cls")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}
init_url = "https://gw.buaa.edu.cn/cgi-bin"
get_challenge_api = "https://gw.buaa.edu.cn/cgi-bin/get_challenge"
srun_portal_api = "https://gw.buaa.edu.cn/cgi-bin/srun_portal"
n = "200"
type = "1"
ac_id = "68"
enc = "srun_bx1"


def loading_msg(msg):
    print(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + " " + msg,
        end="",
    )
    for i in range(3):
        print(
            ".",
            end="",
            flush=True,
        )
        time.sleep(0.2)
    print()


def get_ip():
    loading_msg("获取 ip")
    global ip
    init_res = requests.get(init_url, headers=header)
    ip = re.search('id="user_ip" value="(.*?)"', init_res.text).group(1)
    print(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + " ip: " + ip
    )


def get_token():
    loading_msg("获取 token")
    global token
    get_challenge_params = {
        "callback": "jQuery1124016663493398496798_" + str(int(time.time() * 1000)),
        "username": username,
        "ip": ip,
        "_": int(time.time() * 1000),
    }
    get_challenge_res = requests.get(
        get_challenge_api, params=get_challenge_params, headers=header
    )
    # print(get_challenge_res)
    token = re.search('"challenge":"(.*?)"', get_challenge_res.text).group(1)
    print(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        + " token: "
        + token,
        flush=True,
    )


def get_chksum():
    chkstr = token + username
    chkstr += token + hmd5
    chkstr += token + ac_id
    chkstr += token + ip
    chkstr += token + n
    chkstr += token + type
    chkstr += token + i
    return chkstr


def get_info():
    info_temp = {
        "username": username,
        "password": password,
        "ip": ip,
        "acid": ac_id,
        "enc_ver": enc,
    }
    i = re.sub("'", '"', str(info_temp))
    i = re.sub(" ", "", i)
    return i


def do_complex_work():
    loading_msg("开始加密")
    global i, hmd5, chksum
    i = get_info()
    i = "{SRBX1}" + get_base64(get_xencode(i, token))
    hmd5 = get_md5(password, token)
    chksum = get_sha1(get_chksum())
    print(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + " 加密已完成"
    )


def login():
    srun_portal_params = {
        "callback": "jQuery1124016663493398496798_" + str(int(time.time() * 1000)),
        "action": "login",
        "username": username,
        "password": "{MD5}" + hmd5,
        "ac_id": ac_id,
        "ip": ip,
        "chksum": chksum,
        "info": i,
        "n": n,
        "type": type,
        "os": "windows+10",
        "name": "windows",
        "double_stack": "0",
        "_": int(time.time() * 1000),
    }
    # print(srun_portal_params)
    srun_portal_res = requests.get(
        srun_portal_api, params=srun_portal_params, headers=header
    )
    print(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        + " 请求(GET)已发送"
    )
    try:
        print(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            + " 服务器响应(suc_msg): "
            + re.search('"suc_msg":"(.*?)"', str(srun_portal_res.text)).group(1)
        )
    except:
        print(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            + " 服务器响应(original): ",
            end="\n",
        )
        srun_portal_res_text = textwrap.fill(srun_portal_res.text, 150)
        srun_portal_res_text = textwrap.indent(
            srun_portal_res_text, prefix="                    "
        )
        print(srun_portal_res_text)


def is_connected():
    try:
        loading_msg("测试连接(https://bilibili.com)")
        session = requests.Session()
        html = session.get("https://bilibili.com", timeout=2)
    except:
        return False
    return True


if __name__ == "__main__":
    global username, password
    username = "23374311"
    password = "asd20050115a"
    get_ip()
    get_token()
    do_complex_work()
    login()
    if is_connected():
        print(
            "{0} 连接成功！".format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            ),
            flush=True,
        )
    else:
        print(
            "{0} 连接失败！".format(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            ),
            flush=True,
        )
