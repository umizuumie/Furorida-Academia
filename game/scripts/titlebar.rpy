init python:
    import sys

    if sys.platform != "win32":
        def apply_system_titlebar():
            pass
    else:
        import ctypes
        import winreg

        _DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        _DWMWA_CAPTION_COLOR = 35

        def _is_dark_mode():
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
                )
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                winreg.CloseKey(key)
                return value == 0
            except Exception:
                return False

        def apply_system_titlebar():
            try:
                hwnd = ctypes.windll.user32.FindWindowW(None, config.name)

                dark = ctypes.c_int(1 if _is_dark_mode() else 0)
                ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    hwnd, _DWMWA_USE_IMMERSIVE_DARK_MODE,
                    ctypes.byref(dark), ctypes.sizeof(dark)
                )

                color = ctypes.c_int(0xFFFFFFFF)
                ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    hwnd, _DWMWA_CAPTION_COLOR,
                    ctypes.byref(color), ctypes.sizeof(color)
                )
            except Exception as e:
                renpy.log("Titlebar error: " + str(e))