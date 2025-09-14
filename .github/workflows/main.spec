<<<<<<< HEAD
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['codes\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('codes/adasi.py', 'codes'), ('codes/aine.py', 'codes'), ('codes/arayesh.py', 'codes'), ('codes/atom.py', 'codes'), ('codes/chem.py', 'codes'), ('codes/col.py', 'codes'), ('codes/conv.py', 'codes'), ('codes/elec.py', 'codes'), ('codes/fisa.py', 'codes'), ('codes/fizik.py', 'codes'), ('codes/jazr.py', 'codes'), ('codes/masraf.py', 'codes'), ('codes/motegate.py', 'codes'), ('codes/movazene.py', 'codes'), ('codes/mv.py', 'codes'), ('codes/nogte_i.py', 'codes'), ('codes/ohm.py', 'codes'), ('codes/riazi.py', 'codes'), ('codes/shedat.py', 'codes'), ('codes/tavan.py', 'codes'), ('codes/bib.mp3', 'codes'), ('imagess/atom.png', 'imagess'), ('imagess/atom1.jpg', 'imagess'), ('imagess/atom2.jpg', 'imagess'), ('imagess/atom3.png', 'imagess'), ('imagess/wall1.jpg', 'imagess'), ('imagess/wall2.jpg', 'imagess'), ('imagess/wall3.jpg', 'imagess'), ('imagess/wall4.jpg', 'imagess'), ('imagess/wall5.jpg', 'imagess'), ('imagess/wall6.jpg', 'imagess'), ('imagess/wall7.jpg', 'imagess'), ('imagess/wall8.jpg', 'imagess'), ('imagess/yellow.jpg', 'imagess')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
=======
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['codes\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('codes/adasi.py', 'codes'), ('codes/aine.py', 'codes'), ('codes/arayesh.py', 'codes'), ('codes/atom.py', 'codes'), ('codes/chem.py', 'codes'), ('codes/col.py', 'codes'), ('codes/conv.py', 'codes'), ('codes/elec.py', 'codes'), ('codes/fisa.py', 'codes'), ('codes/fizik.py', 'codes'), ('codes/jazr.py', 'codes'), ('codes/masraf.py', 'codes'), ('codes/motegate.py', 'codes'), ('codes/movazene.py', 'codes'), ('codes/mv.py', 'codes'), ('codes/nogte_i.py', 'codes'), ('codes/ohm.py', 'codes'), ('codes/riazi.py', 'codes'), ('codes/shedat.py', 'codes'), ('codes/tavan.py', 'codes'), ('codes/bib.mp3', 'codes'), ('imagess/atom.png', 'imagess'), ('imagess/atom1.jpg', 'imagess'), ('imagess/atom2.jpg', 'imagess'), ('imagess/atom3.png', 'imagess'), ('imagess/wall1.jpg', 'imagess'), ('imagess/wall2.jpg', 'imagess'), ('imagess/wall3.jpg', 'imagess'), ('imagess/wall4.jpg', 'imagess'), ('imagess/wall5.jpg', 'imagess'), ('imagess/wall6.jpg', 'imagess'), ('imagess/wall7.jpg', 'imagess'), ('imagess/wall8.jpg', 'imagess'), ('imagess/yellow.jpg', 'imagess')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
>>>>>>> 86c6c39 (first commit)
