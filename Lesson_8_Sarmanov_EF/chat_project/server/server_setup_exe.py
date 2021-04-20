import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["lib", "logs", "server"],
}
setup(
    name="mini_chat_server",
    version="0.0.2",
    description="mini_chat_server",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('server.py',
                            base='Win32GUI',
                            targetName='server.exe',
                            )]
)

