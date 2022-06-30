# pwnagotchi_LCD_colorized_darkmode
This is a mod to change the LCD and web UI of a pwnagotchi with a colorized dark mode

Colorized darkmode for the Pwnagotchi with a 1.33" LCD waveshare ST7789V hat & soon it will manage the ST7735S 1.44 
--------------
  
You need to activate the waveshare LCDHAT display on the pwnagotchi.  
You have to place this modified files on your pwnagotchi.

The image is add to the pwnagothci image background inside the `view.py`.  
The Darkmode is added inside the `epd.py` for the LCD screen and inside the `__init__.py` for the web UI.  

Sometimes when their is no background image, I got a minor error on boot, but I don't know why exactly.
```
[WARNING] non fatal error while updating view: dictionary changed size during iteration
```
  
- change for the background image option  
```
/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/view.py  
```
- change for the darkmode of LCD screen  (for ST7789)
```
/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/libs/waveshare/lcdhat/epd.py  
```
-change for darkmode of LCD screen (for ST7735S)
```
/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/libs/waveshare/lcdhat144/epd.py
```
- change for darkmode of web UI  
```
/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/web/__init__.py
```
  
- change for the preview image dimension and position from the web UI  
```
/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/web/static/css/style.css  
```
  
- options inside the /etc/pwnagotchi/config.toml  (I added my config.toml to have the base of my plugins and options activated)
- 3 images are available for test,
   - ui-bg-w.png is for the 1.33
   - ui-bg-w-s.png is for the 1.44 "hi-resolution"
   - ui-bg-w-s-1.png is for the 1.44 "low-resolution"
```
ui.display.enabled = true
ui.display.type = "lcdhat"
ui.display.color = "lime"
ui.display.rotation = 0
ui.display.darkmode = true
ui.display.bg = true
ui.display.bg_path = "/home/pi/img/ui-bg-w.png"
ui.display.hi-res = true

#if you use the crack_house.py:
main.plugins.crack_house.enabled = true
main.plugins.crack_house.orientation = "vertical"
main.plugins.crack_house.files = [
 "/root/handshakes/wpa-sec.cracked.potfile",
 "/root/handshakes/my.potfile",
 "/root/handshakes/OnlineHashCrack.potfile",
]
main.plugins.crack_house.saving_path = "/root/handshakes/crackhouse.potfile"
main.plugins.crack_house.display_stats = true

```
  
- change for the main interface positions (and I added a third line to the UI then I add the base.py file too)
```
/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/base.py
/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/lcdhat.py
/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/components.py
```  

- all custom positions inside plugins  

inside: /usr/local/lib/python3.7/dist-packages/pwnagotchi/plugins/default/  
memtemp.py  
bt-tether.py  

inside: your custom plugins folder (mine: /home/pi/plugins/)  
clock.py  
crack_house.py or display-password.py  
pisugar2.py  
   
- files for images  
```
/home/pi/img/
```

