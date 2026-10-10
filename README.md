# Wi-Fi Fixer

A one-click Windows 10/11 tool (Python + Tkinter) that fixes the Wi-Fi problems that normally force you to restart your PC: the Wi-Fi button greyed out, the Wi-Fi icon or adapter gone, or Wi-Fi connected but no internet.

Instead of typing commands in PowerShell every time, open the app and press a button.

## Features

- **Fix Wi-Fi** for a greyed-out or missing Wi-Fi button. It rescans hardware to re-detect the adapter, force-kills a stuck WLAN AutoConfig service (`WlanSvc`), starts it again, re-enables the Wi-Fi adapter and restarts Explorer.
- **Reset Network** for "connected but no internet". It resets Winsock and the IP stack, releases and renews the IP, and flushes DNS.
- **Check Drivers** (new in v2.0) reads the driver version and date of your Wi-Fi and network adapters, flags drivers that look outdated, and gives you clickable links to the right download page. It picks the adapter maker's page (for example Intel for an AX200), your laptop maker's support page (ASUS, Lenovo, HP, Dell, Acer, MSI and others), a Windows Update shortcut, and a web search for your exact adapter.
- Dark UI with a live log, a progress bar and ⓘ tooltips that explain what each button does.
- Asks for administrator rights automatically.

### How Check Drivers decides

- For adapters it knows (currently the Intel Wi-Fi 6 AX200), it compares your version with the latest known release.
- For every other adapter it goes by driver age: under 1 year is fine, 1 to 2 years is flagged to check, over 2 years is flagged as likely outdated.
- Age is only a hint. A working adapter with an old driver isn't necessarily a problem.
- It never installs anything. It only opens download pages.

To keep the AX200 check current, update `KNOWN_LATEST` near the top of `fixwifi.py` when Intel releases a newer driver.

## ASUS TUF users

ASUS TUF owners have reported Wi-Fi randomly disappearing or the Wi-Fi button going grey, especially after sleep or a restart.

### Reported cases

These are user reports from public forums, not official failure statistics. The Wi-Fi chip seems to matter more than the laptop brand: the **MediaTek MT7921** appears in both the ASUS and HP reports.

| Laptop | Wi-Fi chip | What was reported | Source |
|---|---|---|---|
| ASUS TUF F17 (FX706HE) | MediaTek MT7921 | Wi-Fi and Bluetooth vanish from Device Manager almost daily, after startup or sleep. Driver reinstalls didn't help. ASUS replacing the card fixed it for only about two weeks. | [ASUS forum](https://zentalk.asus.com/t5/others/mediatek-bluetooth-and-wi-fi-mt7921-keeps-disappearing-from/m-p/329227) |
| ASUS TUF A15 (FA506II) | Realtek 8822CE | Wi-Fi drops, then the icon and adapter disappear. A moderator suspected a failing card. | [ASUS forum](https://zentalk.asus.com/en/discussion/63680/tuf-a15-fa506ii-wifi-problem-losing-connection) |
| HP ENVY 17 (17-ch2000) | MediaTek MT7921 | Adapter disappears and returns after entering BIOS and rebooting. Suggested a newer HP driver or an Intel AX210 card. | [HP forum](https://h30434.www3.hp.com/t5/Notebook-Wireless-and-Networking/MediaTek-MT7921/m-p/9297570) |
| Dell G7 7588 | Intel AC 9560 | Wi-Fi option vanished (Code 10). A BIOS reset helped only briefly, and replacing the card didn't fix it. | [Intel community](https://community.intel.com/t5/Wireless/error-in-INTEL-R-Wirelees-AC-9560-PC-does-not-recognize-code-10/m-p/549170/highlight/true) |

Other common causes listed in [this guide](https://cloudhousetechnologies.com/blog/how-to-fix-wifi-adapter-not-showing-windows-11-2026): Windows Update breaking drivers, power management turning off the adapter, a stopped WLAN AutoConfig service, and BIOS or kill-switch toggles.

### What to try

If this is you, try **Fix Wi-Fi** first. If it keeps coming back, also try:

1. Device Manager → Network adapters → your Wi-Fi adapter → Properties → Power Management → untick **Allow the computer to turn off this device to save power**.
2. Press **Check Drivers** in the app, or update the Wi-Fi driver from the ASUS support page for your exact model.
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

This tool runs system commands (`taskkill`, `net start`, `netsh`, `ipconfig`, `pnputil`) with administrator rights. Check Drivers only reads adapter information and opens web pages in your browser. Read `fixwifi.py` first if you want to see exactly what it does. Use at your own risk.
