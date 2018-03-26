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
        self.obj = sg.objs.new_top()
        sg.Geometry(parent=self.obj).set('1024x768')
        self.title()
        self.frames()
        self.canvas = sg.Canvas(parent = self.frame1)
        self.label  = sg.Label (parent = self.frame1
                               ,expand = True
                               ,fill   = 'both'
                               )
        self.canvas.embed(self.label)
        self.scrollbars()
        self.canvas.focus()
        self.bindings()
        
    def title(self,arg=None):
        if not arg:
            arg = _('Image') + ':'
        self.obj.title(arg)
    
    def scrollbars(self):
        self.xscroll = sg.Scrollbar (parent     = self.frame_x
                                    ,scroll     = self.canvas
                                    ,Horizontal = True
                                    )
        self.yscroll = sg.Scrollbar (parent = self.frame_y
                                    ,scroll = self.canvas
                                    )

    def frames(self):
        self.frame   = sg.Frame (parent = self.obj)
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
        sg.bind (obj      = self.obj
                ,bindings = ['<Control-q>','<Control-w>','<Escape>']
                ,action   = self.close
                )
        sg.bind (obj      = self.obj
                ,bindings = '<Down>'
                ,action   = self.move_down
                )
        sg.bind (obj      = self.obj
                ,bindings = '<Up>'
                ,action   = self.move_up
                )
        sg.bind (obj      = self.obj
                ,bindings = '<Left>'
                ,action   = self.move_left
                )
        sg.bind (obj      = self.obj
                ,bindings = '<Right>'
                ,action   = self.move_right
                )
        sg.bind (obj      = self.obj
                ,bindings = '<Next>'
                ,action   = self.move_bottom
                )
        sg.bind (obj      = self.obj
                ,bindings = '<Prior>'
                ,action   = self.move_top
                )
                
    def move_up(self,event=None):
        self.canvas.widget.yview_scroll(-1,'units')
    
    def move_down(self,event=None):
        self.canvas.widget.yview_scroll(1,'units')
        
    def move_left(self,event=None):
        self.canvas.widget.xview_scroll(-1,'units')
        
    def move_right(self,event=None):
        self.canvas.widget.xview_scroll(1,'units')
        
    def move_bottom(self,event=None):
        self.canvas.widget.yview_moveto('1.0')
        
    def move_top(self,event=None):
        self.canvas.widget.yview_moveto(0)

    def show(self,event=None):
        self.obj.show()
        
    def close(self,event=None):
        self.obj.close()


if __name__ == '__main__':
    sg.objs.start()
    iv = ImageViewer (parent  = sg.objs.root()
                     ,picture = '../resources/Gnu_(PSF).png'
                     )
    iv.show()
    sg.objs.end()
