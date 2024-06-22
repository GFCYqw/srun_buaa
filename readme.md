# BUAA SRUN LOGIN

## 介绍

**这是一个北航网络认证（srun）的模拟登录脚本，可以自行设置以实现自动登录。**

起因是作者购买了一个拓竹的 A1mini 3D 打印机，然后发现连接不了校园网（悲），只能开热点。故打算用 ESP32 做一个 WiFi “转换”装置。紧接着发现自己不会 ESP32 连接 PEAP 保护的 WiFi，只好另辟蹊径通过 GET 方法去模拟认证登录。

本项目为作者的测试项目，用于验证 GET 方法模拟认证的可行性，并打算后期迁移至 ESP32。

## 使用方法

运行 **srun_login.py** 即可

## 参考项目

[GitHub - iskoldt-X/SRUN-authenticator: 校园网深澜认证Python 脚本，支持Docker 旨在方便同学们的日常使用。默认国科大UCAS，其他学校也可以使用。](https://github.com/iskoldt-X/SRUN-authenticator)

[jxnu_srun/jxnu_wifi.py at master · huxiaofan1223/jxnu_srun · GitHub](https://github.com/huxiaofan1223/jxnu_srun)
