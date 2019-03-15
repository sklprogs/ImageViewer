#!/usr/bin/python3

import tkinter          as tk
from PIL import Image   as ig
from PIL import ImageTk as it
import shared           as sh
import sharedGUI        as sg

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('ImageViewer','../resources/locale')


# How to combine frames, scrollbars and canvas
class ImageViewer:
    
    def __init__(self,parent,picture=None):
        self._size    = 0
        self._picture = picture
        self.parent   = parent
        self.gui()
        self.pic()
        # Set the scrolling region only after setting a picture
        if self._size:
            self.canvas.region (x = self._size[0]
                               ,y = self._size[1]
                               )
        self.canvas.scroll()
        
    def gui(self):
        self.parent = sg.objs.new_top()
        sg.Geometry(parent=self.parent).set('1024x768')
        self.frames()
        self.canvas = sg.Canvas(parent = self.frame1)
        self.label  = sg.Label (parent = self.frame1
                               ,expand = True
                               ,fill   = 'both'
                               )
        self.canvas.embed(self.label)
        self.scrollbars()
        self.canvas.focus()
        self.title()
        self.icon()
        self.bindings()
        self.canvas.top_bindings(top=self.parent)
        
    def title(self,arg=None):
        if not arg:
            arg = _('Image') + ':'
        self.parent.title(arg)
    
    def scrollbars(self):
        self.xscroll = sg.Scrollbar (parent = self.frame_x
                                    ,scroll = self.canvas
                                    ,Horiz  = True
                                    )
        self.yscroll = sg.Scrollbar (parent = self.frame_y
                                    ,scroll = self.canvas
                                    )

    def frames(self):
        self.frame   = sg.Frame (parent = self.parent)
        self.frame_x = sg.Frame (parent = self.frame
                                ,expand = False
                                ,fill   = 'x'
                                ,side   = 'bottom'
                                )
        self.frame_y = sg.Frame (parent = self.frame
                                ,expand = False
                                ,fill   = 'y'
                                ,side   = 'right'
                                )
        # This frame must be created after the bottom frame
        self.frame1  = sg.Frame (parent = self.frame)
    
    def pic(self):
        if self._picture:
            if sh.File(file=self._picture).Success:
                loader = ig.open(self._picture)
                self._size = loader.size
                image = it.PhotoImage(loader)
                self.label.widget.config(image=image)
                # This prevents the garbage collector from deleting the image
                self.label.widget.image = image
            else:
                sh.log.append ('ImageViewer.pic'
                              ,_('WARNING')
                              ,_('Wrong input data!')
                              )
        else:
            sh.log.append ('ImageViewer.pic'
                          ,_('WARNING')
                          ,_('Empty input is not allowed!')
                          )
        
    def bindings(self):
        sg.bind (obj      = self.parent
                ,bindings = ['<Control-q>','<Control-w>','<Escape>']
                ,action   = self.close
                )

    def show(self,event=None):
        self.parent.show()
        
    def close(self,event=None):
        self.parent.close()
        
    def icon(self,path=None):
        if path:
            self.parent.icon(path)
        else:
            self.parent.icon (sh.objs.pdir().add ('..'
                                                 ,'resources'
                                                 ,'icon_64x64_viewer.gif'
                                                 )
                             )


if __name__ == '__main__':
    sg.objs.start()
    iv = ImageViewer (parent  = sg.objs.root()
                     ,picture = sh.objs.pdir().add ('..','resources'
                                                   ,'Gnu_(PSF).png'
                                                   )
                     )
    iv.show()
    sg.objs.end()
