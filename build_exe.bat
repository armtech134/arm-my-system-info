@echo off
uv run pyinstaller src\main.py --clean --onedir --strip --noconsole --upx-dir=C:\Upx --add-data="bin;bin"