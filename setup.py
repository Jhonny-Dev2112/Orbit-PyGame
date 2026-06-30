from cx_Freeze import setup, Executable

executables = [
    Executable(
        script="main.py",
        target_name="Orbit Shooter.exe",
        icon="OrbitIcon.ico"
    )
]

setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)