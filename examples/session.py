#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

# To import 'InstagramAPI' that is in the parent directory of your current module add parent directory in 'PYTHONPATH':
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from InstagramAPI import InstagramAPI

api = InstagramAPI("ad.min5709", "developers")
save_session = {}
if (api.login()):
  save_session = {
    'token': api.token,
    'username_id': api.username_id,
    'rank_token': api.rank_token,
    'uuid': api.uuid,
    'session': api.s.cookies.get_dict(),
    'user_agent': api.USER_AGENT,
    'device_id': api.device_id
  }
  print("Login success!")
  api.logout()
else:
  print("Can't login!")

api.set_session(**save_session)
print(api.isLoggedIn)