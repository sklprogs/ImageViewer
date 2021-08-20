#!/usr/bin/python3

from skl_shared.localize import _
import skl_shared.shared as sh
import skl_shared.image.controller as im

ICON = sh.objs.get_pdir().add('..','resources','icon_64x64_viewer.gif')


class ImageViewer(sh.ScrollableC):
    # How to combine frames, scrollbars and a canvas
    def __init__ (self,ScrollX=True,title=_('Scrollable widget')
                 ,icon='',width=800,height=600,xborder=0,yborder=0
                 ,Maximize=False,image_path=''
                 ):
        super().__init__ (ScrollX = ScrollX
                         ,title = title
                         ,icon = icon
                         ,width = width
                         ,height = height
                         ,xborder = xborder
                         ,yborder = yborder
                         ,Maximize = Maximize
                         )
        self.image_path = image_path
        self.update_gui()
        
    def set_image(self):
        f = '[ImageViewer] viewer.ImageViewer.set_image'
        if self.image_path:
            if sh.File(self.image_path).Success:
                iimage = im.Image()
                iimage.open(self.image_path)
                self.lbl_img.widget.config(image=iimage.image)
                ''' This prevents the garbage collector from deleting
                    the image.
                '''
                self.lbl_img.widget.image = iimage.image
            else:
                mes = _('Wrong input data!')
                sh.objs.get_mes(f,mes,True).show_warning()
        else:
            sh.com.rep_empty(f)
    
    def set_image_label(self):
        self.lbl_img = sh.Label (parent = self.get_content_frame()
                                ,text = _('Image')
                                )
    
    def update_gui(self):
        self.set_image_label()
        self.set_image()
        self.adjust_by_content()


if __name__ == '__main__':
    sh.com.start()
    ImageViewer (ScrollX = True
                ,title = _('Image') + ':'
                ,icon = ''
                ,width = 1024
                ,height = 768
                ,xborder = 0
                ,yborder = 0
                ,Maximize = False
                ,image_path = sh.objs.get_pdir().add ('..','resources'
                                                     ,'Gnu_(PSF).png'
                                                     )
                ).show()
    sh.com.end()
