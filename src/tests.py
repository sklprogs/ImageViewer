#!/usr/bin/python3

from skl_shared.localize import _
import skl_shared.shared as sh
import skl_shared.image.controller as im
import viewer as vw

IMAGE = sh.objs.get_pdir().add('..','resources','Gnu_(PSF).png')


class Scrollable(sh.Scrollable):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def set_gui(self):
        self.add_paths()
        self.set_frames()
        self.add_buttons()
        self.set_scroll()
    
    def set_frames(self):
        ''' This frame should be created before others, otherwise,
            the scrollbar will have incorrect sizes.
        '''
        self.frm_ver = sh.Frame (parent = self.parent
                                ,expand = False
                                ,fill = 'y'
                                ,side = 'right'
                                )
        self.frm_lft = sh.Frame (parent = self.parent
                                ,expand = False
                                ,fill = 'y'
                                ,side = 'left'
                                )
        self.frm_rht = sh.Frame (parent = self.parent
                                ,expand = False
                                ,fill = 'y'
                                ,side = 'right'
                                )
        self.frm_top = sh.Frame (parent = self.parent
                                ,expand = False
                                ,fill = 'x'
                                ,side = 'top'
                                )
        self.frm_prm = sh.Frame (parent = self.parent
                                ,fill = 'both'
                                )
        self.widget = self.frm_prm.widget
        self.cvs_prm = sh.Canvas(self.frm_prm)
        self.frm_sec = sh.Frame (parent = self.frm_prm
                                ,fill = 'both'
                                )
        self.cvs_prm.embed(self.frm_sec)
        self.frm_cnt = sh.Frame (parent = self.frm_sec
                                ,expand = True
                                ,fill = 'both'
                                )
        if self.ScrollX:
            self.frm_hor = sh.Frame (parent = self.frm_prm
                                    ,expand = False
                                    ,fill = 'x'
                                    ,side = 'bottom'
                                    )
        self.frm_btm = sh.Frame (parent = self.parent
                                ,expand = False
                                ,fill = 'x'
                                ,side = 'bottom'
                                )
    
    def add_paths(self):
        self.icn_top = sh.objs.get_pdir().add ('..','resources'
                                              ,'buttons'
                                              ,'icon_36x36_up.gif'
                                              )
        self.icn_btm = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'icon_36x36_down.gif'
                                        )
        self.icn_lft = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'icon_36x36_left.gif'
                                        )
        self.icn_rht = sh.objs.pdir.add ('..','resources','buttons'
                                        ,'icon_36x36_right.gif'
                                        )
    
    def add_buttons(self):
        self.btn_top = sh.Button (parent = self.frm_top
                                 ,hint = _('This button is at the top')
                                 ,text = _('Top')
                                 ,hdir = 'bottom'
                                 ,active = self.icn_top
                                 ,inactive = self.icn_top
                                 ,expand = True
                                 )
        self.btn_btm = sh.Button (parent = self.frm_btm
                                 ,hint = _('This button is at the bottom')
                                 ,text = _('Bottom')
                                 ,hdir = 'top'
                                 ,active = self.icn_btm
                                 ,inactive = self.icn_btm
                                 ,expand = True
                                 )
        self.btn_lft = sh.Button (parent = self.frm_lft
                                 ,hint = _('This button is at the left')
                                 ,text = _('Left')
                                 ,hdir = 'bottom'
                                 ,active = self.icn_lft
                                 ,inactive = self.icn_lft
                                 )
        self.btn_rht = sh.Button (parent = self.frm_rht
                                 ,hint = _('This button is at the right')
                                 ,text = _('Right')
                                 ,hdir = 'bottom'
                                 ,active = self.icn_rht
                                 ,inactive = self.icn_rht
                                 )



class ImageViewer(vw.ImageViewer):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def set_gui(self):
        self.set_parent()
        self.obj = Scrollable (parent = self.parent
                              ,ScrollX = self.ScrollX
                              ,xborder = self.xborder
                              ,yborder = self.yborder
                              )
        self.set_bindings()


if __name__ == '__main__':
    ImageViewer (image_path = IMAGE
                ,title = _('A more complex widget:')
                ).show()