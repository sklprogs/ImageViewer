#!/usr/bin/python3

from skl_shared.localize import _
import skl_shared.shared as sh
import skl_shared.image.controller as im
import viewer as vw

IMAGE = sh.objs.get_pdir().add('..','resources','Gnu_(PSF).png')


class ImageViewer(vw.ImageViewer):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def add_paths(self):
        self.icn_top = sh.objs.get_pdir().add ('..','resources'
                                              ,'buttons'
                                              ,'icon_36x36_up.gif'
                                              )
        self.icn_btm = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'icon_36x36_down.gif'
                                        )
    
    def add_buttons(self):
        self.btn_top = sh.Button (parent = self.frm_top
                                 ,hint = _('This button is at the top')
                                 ,text = _('Top')
                                 ,hdir = 'bottom'
                                 ,active = self.icn_top
                                 ,inactive = self.icn_top
                                 )
        self.btn_btm = sh.Button (parent = self.frm_btm
                                 ,hint = _('This button is at the bottom')
                                 ,text = _('Bottom')
                                 ,hdir = 'top'
                                 ,active = self.icn_btm
                                 ,inactive = self.icn_btm
                                 )
    
    def add_frames(self):
        self.frm_top = sh.Frame (parent = self.obj.parent
                                ,expand = False
                                ,fill = 'x'
                                ,side = 'top'
                                )
        self.frm_btm = sh.Frame (parent = self.obj.parent
                                ,expand = False
                                ,fill = 'x'
                                ,side = 'bottom'
                                )
    
    def update_gui(self):
        self.add_paths()
        self.add_frames()
        self.add_buttons()
        self.set_image_label()
        self.set_image()
        self.adjust_by_content()


if __name__ == '__main__':
    ImageViewer (image_path = IMAGE
                ,title = _('A more complex widget:')
                ).show()