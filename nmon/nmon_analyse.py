# -*- coding:utf-8 -*-

from nmon import ExcelMicro
from nmon import NmonResult
from nmon import RConfig
from nmon import SSHSokcet
from nmon.NmonLog import log

import traceback
import os
import sys


def get_all_nmon_file(path):
    if os.path.isfile(path):
        extend = path.rsplit(".", 1)
        if(len(extend) == 2):
            if extend[1] == "nmon":
                file_list.append(path)

    elif os.path.isdir(path):
        for file in os.listdir(path):
            get_all_nmon_file(path+"\\"+file)


def analyse_file(config):
    MircoFilePath = config.nmon_analyse_file
    get_all_nmon_file(config.nmon_file_dir)
    nmon_tuple = file_list
    path = config.nmon_result_file
    log.info("开始解析文件")
    result = ExcelMicro.get_nmon_result_file(MircoFilePath, nmon_tuple, path)
    log.info("解析文件结束")
    log.info("开始提取数据")
    nr = NmonResult.NmonResult(result)
    log.info("数据提取完成")
    nr.get_file(path=path)


def download_file(config):
    log.info("读取配置文件")
    hostname = config.ip
    remotePath = config.remote_dir
    localPath = config.local_dir
    uesrname = config.username
    password = config.password
    ssh = SSHSokcet.sshSocket(hostname=hostname, username=uesrname, password=password)
    files = ssh.get_all_file(remotePath, remotePath, [])
    ssh.download_file(files, localPath, remotePath)


try:
    file_list = []
    config = RConfig.Config()
    config.reload_all_value()
    download_flag = config.download_flag
    if download_flag == 'True':
        download_file(config=config)
    elif download_flag != 'False':
        log.error("无法识别的下载标识")
        sys.exit()

    analyse_file(config=config)
except SystemExit:
    input("按任意键退出程序:")
except:
    error_msg = traceback.format_exc()
    log.error(error_msg)
    input("按任意键退出程序:")
