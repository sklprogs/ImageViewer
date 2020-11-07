from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict (packages = []
                    ,includes = ['re','PIL._tkinter_finder']
                    ,excludes = []
                    )

executables = [Executable ('ImageViewer.py'
                          ,base = 'Console'
                          ,icon = 'resources/icon_64x64_viewer.gif'
                          ,targetName = 'ImageViewer'
                          )
              ]

setup (name = 'ImageViewer'
      ,version = '1'
      ,description = 'A very basic image viewer'
      ,options = dict(build_exe=buildOptions)
      ,executables = executables
      )
