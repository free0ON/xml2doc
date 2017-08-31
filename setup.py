from cx_Freeze import setup, Executable

target = Executable (
    script = "MCLinkReport.py",
    base = "Win32GUI",
    icon = "icon.ico"
)

setup(
    name = "MCLinkReport",
    version = "1.4",
    description = "Программа для автоматического создания отчетов MCLink",
    executables = [Executable("MCLinkReport.py")]

)