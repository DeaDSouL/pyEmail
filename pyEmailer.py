#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
#---------------------------------
#
# By: DeaDSouL (Mubarak Alrashidi)
#
#---------------------------------
#
# @TODO make it able to send emails
#
# ----------------------------------------------------------------------


from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from os import (
    path as os_path,
    access as os_access,
    R_OK as os_R_OK,
)
from getpass import (
    getpass,
    getuser
)
from keyring import (
    set_password,
    get_password
)


# ----------------------------------------
RECIPIENTS_FILE = 'recipients.txt'
MESSAGE_FILE = 'message.txt'
# --------------------
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USER = ''
MAIL_PASS = ''
# ----------------------------------------

