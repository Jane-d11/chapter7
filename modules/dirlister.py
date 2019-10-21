# -*- coding: utf-8 -*-
import os

def run(**args):   # ¥i±µ¨ü¥iÅÜ¼Æ¶qªº¤Þ­z
   print "[*] In dirlister module."
   files = os.listdir(".")  # ¥Ø«eÀÉ®×§¨¤U©Ò¦³ÀÉ®×
   
   return str(files)
   