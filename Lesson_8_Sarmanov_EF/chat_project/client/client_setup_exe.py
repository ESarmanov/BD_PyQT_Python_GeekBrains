import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["lib", "logs", "client"],
}
setup(
    name="mini_chat_client",
    version="0.0.2",
    description="mini_chat_client",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('client.py',
                            base='Win32GUI',
                            targetName='client.exe',
                            )]
)

