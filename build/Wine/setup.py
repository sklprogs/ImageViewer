from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict (packages = []
                    ,includes = ['re','PIL._tkinter_finder']
                    ,excludes = []
                    )

executables = [Executable ('ImageViewer.py'
                          ,base = 'Win32GUI'
                          ,targetName = 'ImageViewer.exe'
                          )
              ]

setup (name        = 'ImageViewer'
      ,version     = '1'
      ,description = 'A very basic image viewer'
      ,options     = dict(build_exe=buildOptions)
      ,executables = executables
      )
