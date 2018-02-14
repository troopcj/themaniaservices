import sys
import xbmc,xbmcaddon,xbmcvfs
import sqlite3
import subprocess

ADDON = xbmcaddon.Addon(id='plugin.video.maniaguide')

channel = sys.argv[1]
start = sys.argv[2]

if ADDON.getSetting('playing.channel') != channel:
    quit()

if ADDON.getSetting('playing.start') != start:
    quit()

ADDON.setSetting('playing.channel','')
ADDON.setSetting('playing.start','')

script = "special://profile/addon_data/plugin.video.maniaguide/stopwith.py"
if xbmcvfs.exists(script):
    xbmc.executebuiltin('RunScript(%s,%s,%s)' % (script,channel,start))
xbmc.Player().stop()
