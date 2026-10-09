# Wi-Fi Fixer

A one-click Windows 10/11 tool (Python + Tkinter) that fixes the Wi-Fi problems that normally force you to restart your PC: the Wi-Fi button greyed out, the Wi-Fi icon or adapter gone, or Wi-Fi connected but no internet.

Instead of typing commands in PowerShell every time, open the app and press a button.

## Features

- **Fix Wi-Fi** for a greyed-out or missing Wi-Fi button. It rescans hardware to re-detect the adapter, force-kills a stuck WLAN AutoConfig service (`WlanSvc`), starts it again, re-enables the Wi-Fi adapter and restarts Explorer.
- **Reset Network** for "connected but no internet". It resets Winsock and the IP stack, releases and renews the IP, and flushes DNS.
- Dark UI with a live log, a progress bar and ⓘ tooltips that explain what each button does.
- Asks for administrator rights automatically.

## ASUS TUF users

ASUS TUF owners have reported Wi-Fi randomly disappearing or the Wi-Fi button going grey, especially after sleep or a restart. Examples on ASUS and Microsoft forums:

- TUF F17 (FX706HE) with a **MediaTek MT7921** card: Wi-Fi and Bluetooth vanish from Device Manager.
- TUF A15 (FA506II) with a **Realtek 8822CE** card: Wi-Fi drops, then the icon and adapter disappear.

If this is you, try **Fix Wi-Fi** first. If it keeps coming back, also try:

1. Device Manager → Network adapters → your Wi-Fi adapter → Properties → Power Management → untick **Allow the computer to turn off this device to save power**.
2. Update the Wi-Fi driver from the ASUS support page for your exact model.
3. Turn off Fast Startup (Control Panel → Power Options → Choose what the power buttons do).
4. Shut down fully, hold the power button for about 30 seconds, then turn on again.

If the adapter never comes back, even after a driver reinstall and BIOS update, the Wi-Fi card itself may be faulty. Software can't fix that, so contact ASUS service.

## Build the exe

```
py -m pip install pyinstaller
py -m PyInstaller --onefile --noconsole --uac-admin --icon icon.ico fixwifi.py
```

The exe appears in `dist/`. Windows SmartScreen may warn about it since it's unsigned: click **More info → Run anyway**.

## Disclaimer

This tool runs system commands (`taskkill`, `net start`, `netsh`, `ipconfig`, `pnputil`) with administrator rights. Read `fixwifi.py` first if you want to see exactly what it does. Use at your own risk.
