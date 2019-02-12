#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import configparser

cur_path = os.path.dirname(os.path.relpath(__file__))
configpath  = os.path.join(cur_path,"cfg.ini")
conf = configparser.ConfigParser()
conf.read(configpath)

send_mail = conf.get('email','send_mail')

send_user = conf.get('email','send_user')

login = conf.get('email','server.login')

send_mail_ren = conf.get('email','send_mail_ren')


