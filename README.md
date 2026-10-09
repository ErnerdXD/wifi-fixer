# Wi-Fi Fixer

Small Windows tool to repair Wi-Fi problems with one click.

- **Fix Wi-Fi**: for a greyed-out or missing Wi-Fi button. Rescans hardware, force-kills a stuck WLAN service, restarts it, re-enables the adapter and restarts Explorer.
- **Reset Network**: for "connected but no internet". Resets Winsock and the IP stack, renews the IP and flushes DNS.

## Build the exe

```
py -m pip install pyinstaller
py -m PyInstaller --onefile --noconsole --uac-admin --icon icon.ico fixwifi.py
```

The exe appears in `dist/`. It asks for administrator rights when launched.
