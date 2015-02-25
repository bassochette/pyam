# -*- coding : utf8 -*-

LOGGING = True
def log(tag , msg):
	if LOGGING:
		print("[%s] %r"%( tag, msg))