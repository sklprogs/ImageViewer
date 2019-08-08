#!/usr/bin/python3

import skl_shared.shared as sh

import gettext
import skl_shared.gettext_windows
skl_shared.gettext_windows.setup_env()
gettext.install('ImageViewer','../resources/locale')

ICON = sh.objs.pdir().add('..','resources','icon_64x64_viewer.gif')


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
        self.parent = sh.Top()
        sh.Geometry(self.parent).set('1024x768')
        self.frames()
        self.canvas = sh.Canvas(parent = self.frame1)
        self.label  = sh.Label (parent = self.frame1
                               ,expand = True
                               ,fill   = 'both'
                               )
        self.canvas.embed(self.label)
        self.scrollbars()
        self.canvas.focus()
        self.title()
        self.icon()
        self.bindings()
        self.canvas.top_bindings (top  = self.parent
                                 ,Ctrl = False
                                 )
        
    def title(self,arg=None):
        if not arg:
            arg = _('Image') + ':'
        self.parent.title(arg)
    
    def scrollbars(self):
        self.xscroll = sh.Scrollbar (parent = self.frame_x
                                    ,scroll = self.canvas
                                    ,Horiz  = True
                                    )
        self.yscroll = sh.Scrollbar (parent = self.frame_y
                                    ,scroll = self.canvas
                                    )

    def frames(self):
        self.frame   = sh.Frame (parent = self.parent)
        self.frame_x = sh.Frame (parent = self.frame
                                ,expand = False
                                ,fill   = 'x'
                                ,side   = 'bottom'
                                )
        self.frame_y = sh.Frame (parent = self.frame
                                ,expand = False
                                ,fill   = 'y'
                                ,side   = 'right'
                                )
        # This frame must be created after the bottom frame
        self.frame1  = sh.Frame (parent = self.frame)
    
    def pic(self):
        f = '[ImageViewer] ImageViewer.ImageViewer.pic'
        if self._picture:
            if sh.File(file=self._picture).Success:
                iimage = sh.Image()
                iimage.open(self._picture)
                self._size = iimage._loader.size
                self.label.widget.config(image=iimage._image)
                ''' This prevents the garbage collector from deleting
                    the image.
                '''
                self.label.widget.image = iimage._image
            else:
                mes = _('Wrong input data!')
                sh.Message(f,mes,True).warning()
        else:
            sh.com.empty(f)
        
    def bindings(self):
        sh.com.bind (obj      = self.parent
                    ,bindings = ('<Control-q>','<Control-w>','<Escape>')
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
            self.parent.icon(ICON)


if __name__ == '__main__':
    sh.com.start()
    iv = ImageViewer (parent  = sh.objs.root()
                     ,picture = sh.objs.pdir().add ('..','resources'
                                                   ,'Gnu_(PSF).png'
                                                   )
                     )
    iv.show()
    sh.com.end()
