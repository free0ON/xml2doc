from cx_Freeze import setup, Executable

base = 'Win32GUI'

target = Executable (
    script = "MCLinkReport.py",
    base = "Win32GUI",
    icon = "icon.ico"
)

setup(
    name = "MCLinkReport",
    version = "1.7",
    description = "Программа для автоматического создания отчетов MCLink",
    executables = [target]

)
