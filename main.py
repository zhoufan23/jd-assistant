#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    asst = Assistant()      # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    asst.exec_reserve_seckill_by_time(sku_id='100012043978', buy_time='2020-06-23 10:00:00.000', retry=3, interval=0.5)
    # asst.exec_reserve_seckill_by_time(sku_id='7897905', buy_time='2020-06-23 9:25:00.000', retry=3, interval=0.1)
    
