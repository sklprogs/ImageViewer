#!/usr/bin/python3

from skl_shared.localize import _
import skl_shared.shared as sh
import skl_shared.image.controller as im

ICON = sh.objs.get_pdir().add('..','resources','icon_64x64_viewer.gif')


# How to combine frames, scrollbars and canvas
class ImageViewer:
    
    def __init__(self,parent,picture=None):
        self.size = 0
        self.picture = picture
        self.parent = parent
        self.set_gui()
        self.set_pic()
        # Set the scrolling region only after setting a picture
        if self.size:
            self.canvas.set_region (x = self.size[0]
                                   ,y = self.size[1]
                                   )
        self.canvas.scroll()
        
    def set_gui(self):
        self.parent = sh.Top (icon = ICON
                             ,title = _('Image') + ':'
                             )
        sh.Geometry(self.parent).set('1024x768')
        self.set_frames()
        self.canvas = sh.Canvas(parent = self.frm_sub)
        self.label = sh.Label (parent = self.frm_sub
                               ,expand = True
                               ,fill = 'both'
                               )
        self.canvas.embed(self.label)
        self.set_scroll()
        self.canvas.focus()
        self.set_bindings()
        self.canvas.set_top_bindings (top = self.parent
                                     ,Ctrl = False
                                     )
        
    def set_title(self,arg=None):
        if not arg:
            arg = _('Image') + ':'
        self.parent.set_title(arg)
    
    def set_scroll(self):
        self.scr_hor = sh.Scrollbar (parent = self.frm_hor
                                    ,scroll = self.canvas
                                    ,Horiz = True
                                    )
        self.scr_ver = sh.Scrollbar (parent = self.frm_ver
                                    ,scroll = self.canvas
                                    )

    def set_frames(self):
        self.frm_prm = sh.Frame (parent = self.parent)
        self.frm_hor = sh.Frame (parent = self.frm_prm
                                ,expand = False
                                ,fill = 'x'
                                ,side = 'bottom'
                                )
        self.frm_ver = sh.Frame (parent = self.frm_prm
                                ,expand = False
                                ,fill = 'y'
                                ,side = 'right'
                                )
        # This frame must be created after the bottom frame
        self.frm_sub = sh.Frame (parent = self.frm_prm)
    
    def set_pic(self):
        f = '[ImageViewer] ImageViewer.ImageViewer.set_pic'
        if self.picture:
            if sh.File(self.picture).Success:
                iimage = im.Image()
                iimage.open(self.picture)
                self.size = iimage.loader.size
                self.label.widget.config(image=iimage.image)
                ''' This prevents the garbage collector from deleting
                    the image.
                '''
                self.label.widget.image = iimage.image
            else:
                mes = _('Wrong input data!')
                sh.objs.get_mes(f,mes,True).show_warning()
        else:
            sh.com.rep_empty(f)
        
    def set_bindings(self):
        sh.com.bind (obj = self.parent
                    ,bindings = ('<Control-q>','<Control-w>','<Escape>')
                    ,action = self.close
                    )

    def show(self,event=None):
        self.parent.show()
        
    def close(self,event=None):
        self.parent.close()
        
    def set_icon(self,path=None):
        if path:
            self.parent.set_icon(path)
        else:
            self.parent.set_icon(ICON)


if __name__ == '__main__':
    sh.com.start()
    ImageViewer (parent = sh.objs.get_root()
                ,picture = sh.objs.get_pdir().add ('..','resources'
                                                  ,'Gnu_(PSF).png'
                                                  )
                ).show()
    sh.com.end()
