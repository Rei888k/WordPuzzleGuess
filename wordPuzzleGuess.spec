# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None

a = Analysis(
    ['src\\wordPuzzleGuess.py'],
    pathex=['src', '.', 'src\\font' ],
    binaries=[],
    datas=[('src\\font\\ipaexg.ttf', 'font')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
a.datas+=[('wordPuzzleGuess.kv','src\\wordPuzzleGuess.kv',"DATA")]
a.datas+=[('font\\ipaexg.ttf','src\\font\\ipaexg.ttf',"DATA")]

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    name='wordPuzzleGuess',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True
)

coll = COLLECT(exe, Tree('src'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='wordPuzzleGuess')