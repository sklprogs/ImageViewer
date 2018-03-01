#!/usr/bin/python3

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('shared','./locale')

import tkinter as tk
from PIL import Image as ig
from PIL import ImageTk as it
import shared as sh
import sharedGUI as sg


# How to combine frames, scrollbars and canvas
class ImageViewer:
    
    def __init__(self,parent,picture=None):
        self._size    = 0
        self._picture = picture
        self.parent   = parent
        self.gui()
        self.pic()
        # Set the scrolling region only after setting a picture
        self.scrollregion()
        self.scroll2start()
        
    def gui(self):
        self.obj = sg.objs.new_top(Maximize=False)
        sg.Geometry(parent=self.obj).set('1024x768')
        self.title()
        self.frames()
        self.canvas = sg.Canvas(parent = self.frame1)
        self.label  = sg.Label (parent = self.frame1
                               ,expand = True
                               ,fill   = 'both'
                               )
        self.canvas.embed(self.label)
        self.scroll_x()
        self.scroll_y()
        self.canvas.focus()
        self.bindings()
        
    def title(self,arg=None):
        if not arg:
            arg = 'Image:'
        self.obj.title(arg)
    
    def scroll_x(self):
        self.xscroll = tk.Scrollbar (master = self.frame_x.widget
                                    ,orient = tk.HORIZONTAL
                                    )
        self.xscroll.pack (expand = True
                          ,fill   = 'x'
                          )
        self.canvas.widget.config(xscrollcommand=self.xscroll.set)
        self.xscroll.config(command=self.canvas.widget.xview)
    
    def scroll_y(self):
        self.yscroll = tk.Scrollbar(master=self.frame_y.widget)
        self.yscroll.pack (expand = True
                          ,fill   = 'y'
                          )
        self.canvas.widget.config(yscrollcommand=self.yscroll.set)
        self.yscroll.config(command=self.canvas.widget.yview)
        
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
            
    def scrollregion(self):
        if self._size:
            x, y = self._size
            self.canvas.widget.configure (scrollregion = (-x/2,-y/2
                                                         , x/2, y/2
                                                         )
                                         )
        else:
            sh.log.append ('ImageViewer.scrollregion'
                          ,_('WARNING')
                          ,_('Empty input is not allowed!')
                          )
                          
    def scroll2start(self,event=None):
        self.canvas.widget.xview_moveto(0)
        self.canvas.widget.yview_moveto(0)
        
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
                     ,picture = '/home/pete/pics/240255-1366x768.jpg'
                     )
    iv.show()
    sg.objs.end()
