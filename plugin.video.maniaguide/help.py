import xbmc,xbmcaddon,xbmcvfs,xbmcgui
import sys
which = sys.argv[1]

ADDON = xbmcaddon.Addon(id='plugin.video.maniaguide')

if which == "commands":
    path = xbmc.translatePath('special://home/addons/plugin.video.maniaguide/commands.txt')
elif which == "autoplaywith":
    path = xbmc.translatePath('special://home/addons/plugin.video.maniaguide/resources/playwith/readme.txt')
f = xbmcvfs.File(path,"rb")
data = f.read()
dialog = xbmcgui.Dialog()
dialog.textviewer('Help', data)
