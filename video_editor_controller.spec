# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
_name = 'Udeo v1.3'
_dir  = 'D:\\Pycharm Projects\\videoEditor'

added_files = [('addedFiles/bin','bin'),
                ('elasticsearch_config.ini','.'),
                ('addedFiles/PySide6','PySide6'),
                ('addedFiles/clr_loader','clr_loader'),
                ('fonts/','fonts'),
                ('CAVOLINI.TTF','.'),
                ('CAVOLINIBOLD.TTF','.'),
                ('CAVOLINIBOLDITALIC.TTF','.'),
                ('CAVOLINIITALIC.TTF','.'),
                ('QuantumProfit.ttf','.'),
                ('MFA','MFA/'),
                ('AutoServerConnector_DLLs', 'AutoServerConnector_DLLs/'),
                ('AppSettings.json', '.'),
                ('icon.ico','.')]

a = Analysis(['video_editor_controller.py'],
             pathex=[_dir],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
	      icon='icon.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=_name)
