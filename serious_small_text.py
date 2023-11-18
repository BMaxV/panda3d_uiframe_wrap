import random
import time
import textwrap

from panda_interface_glue import panda_interface_glue as pig
from panda_interface_glue import drag_main
from panda3d.core import ClockObject
from panda3d.core import TextureStage
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectFrame
from panda3d.core import TransparencyAttrib

class Wrapper2:
    def __init__(self):
        """
        this is the more advanced idea of having a defined frame size and using that as the limits
        for the decoration. so ideally you should be able to wrap these around your existing UIs.
        """
        self.b = ShowBase()
        
        content_pos = (0.2,0,0.1)
        content_frame_size = (0,0.3,0,0.3)
        DirectFrame(pos = content_pos,frameSize = content_frame_size)
        
        # the frame size will still mess with the lower parts if you set it up "wrong", that should be fixed,
        # there shouldn't be a "wrong" way to set this up.
        
        # I am assuming I can divide the frame into these bits.
        normalized_size = 0.1
        
        xm = int(round(content_frame_size[1]/normalized_size,0)+2)
        ym = int(round(content_frame_size[3]/normalized_size,0)+2)
        
        # this is for scaling the different parts of the frame.
        f = 0.1 # controlls the size of the corners
        f2 = 0.08 #controlls the width of the border
        
        # I am going around the side.
        # this does what I want, the question is if it's untuitive.
        
        y=0
        while y < ym:
            x=0
            while x < xm:
                pos = (content_pos[0]+normalized_size*x, 0, content_pos[2]-normalized_size*(y-3))
                
                if x ==0 and y ==0:
                    frame_size = (-f,0,-0,f)
                    F=DirectFrame(pos=pos,frameSize=frame_size)
                    tex = loader.loadTexture("topleftcorner_rendered.png")
                    F["frameTexture"]=(tex)
                
                if x == xm-2 and y ==0:
                    frame_size = (0,f,0,f)
                    F=DirectFrame(pos=pos,frameSize=frame_size)
                    tex = loader.loadTexture("toprightcorner_rendered.png")
                    F["frameTexture"]=(tex)
                    
                if x == 0 and y ==ym-1:
                    frame_size = (-f,0,0,f)
                    F = DirectFrame(pos=pos,frameSize=frame_size)
                    tex = loader.loadTexture("bottomleftcorner_rendered.png")
                    F["frameTexture"]=(tex)
                    
                if x == xm-2 and y == ym-1:
                    frame_size = (-0,f,-0,f)
                    F = DirectFrame(pos=pos,frameSize=frame_size)
                    tex = loader.loadTexture("bottomrightcorner_rendered.png")
                    F["frameTexture"] = (tex)
                    
                if y == 0 and 0 <= x < xm-2:
                    frame_size = (-0,0.1,-0,f2)
                    F=DirectFrame(pos=pos,frameSize=frame_size)
                    tex = loader.loadTexture("upborder_rendered.png")
                    F["frameTexture"]=(tex)
                    
                if x == 0 and 0 < y < ym-1:
                    frame_size = (-f2,0,-0,0.1)
                    F=DirectFrame(pos=pos,frameSize=frame_size)
                    tex = loader.loadTexture("leftborder_rendered.png")
                    F["frameTexture"]=(tex)
               
                if x == xm-2 and 0 < y < ym-1:
                    frame_size = (-0,f2,-0,0.1)
                    F=DirectFrame(pos=pos,frameSize=frame_size)
                    tex = loader.loadTexture("leftborder_rendered.png")#"rightborder.png")
                    F["frameTexture"]=(tex)

                if y == ym-2 and 0 <= x < xm-2:
                    frame_size = (-0,0.1,-f2,0)
                    F=DirectFrame(pos=pos,frameSize=frame_size)
                    tex = loader.loadTexture("upborder_rendered.png")#"downborder.png")
                    F["frameTexture"]=(tex)
            
                x+=1
                continue
            y+=1

class Wrapper:
    """ this is the simpler version to show the basic idea
    """
    def __init__(self):

        # this is required for this demo
        self.b = ShowBase()
        
        # this is where we are positioning everything.
        pos = (0,0,-0.3)
        
        # f is your normalized tile size I'm building this with here.
        f = 0.1
        
        # this is the size of our grid.
        xm = 7
        ym = 5
        
        # this creates one big frame where you should put your content.
        content_frame_size = (-0,(xm-2)*f,-0,(ym-2)*f)
        content_pos = (pos[0],0,pos[2]-f)
        DirectFrame(pos=content_pos,frameSize=content_frame_size)
        
        f = 0.095
        f = 0.1
        frame_size = (-0,f,-0,f)
        
        # and these loops create lots of smaller frames that form
        # the decoration.
        
        y = 0
        while y < ym:
            x=0
            while x < xm:
                pos= (0.1*x-f,0,-0.1*y-f)
                if not (0 < x < xm-1 and 0 < y < ym-1):
                    F=DirectFrame(pos=pos,frameSize=frame_size)
                
                if x ==0 and y ==0:
                    #tex = loader.loadTexture("topleftcorner.png")
                    tex = loader.loadTexture("gradient_topleft.png")
                    
                    F["frameTexture"]=(tex)
                if x ==xm-1 and y ==0:
                    #tex = loader.loadTexture("toprightcorner.png")
                    tex = loader.loadTexture("gradient_topright.png")
                    
                    F["frameTexture"]=(tex)
                if x ==0 and y ==ym-1:
                    #tex = loader.loadTexture("bottomleftcorner.png")
                    tex = loader.loadTexture("gradient_bottomleft.png")
                    
                    F["frameTexture"]=(tex)
                if x ==xm-1 and y ==ym-1:
                    #tex = loader.loadTexture("bottomrightcorner.png")
                    tex = loader.loadTexture("gradient_bottomright.png")
                    
                    F["frameTexture"]=(tex)
                if y == 0 and 0 < x < xm-1:
                    #tex = loader.loadTexture("upborder.png")
                    tex = loader.loadTexture("gradient_top.png")
                    
                    F["frameTexture"]=(tex)
                if x == 0 and 0 < y < ym-1:
                    #tex = loader.loadTexture("leftborder.png")
                    tex = loader.loadTexture("gradient_left.png")
                    
                    F["frameTexture"]=(tex)
                if y == ym-1 and 0 < x < xm-1:
                    #tex = loader.loadTexture("downborder.png")
                    tex = loader.loadTexture("gradient_bottom.png")
                    
                    F["frameTexture"]=(tex)
                if x == xm-1 and 0 < y < ym-1:
                    #tex = loader.loadTexture("rightborder.png")
                    tex = loader.loadTexture("gradient_right.png")
                    
                    F["frameTexture"]=(tex)
                F.setTransparency(TransparencyAttrib.MAlpha)    
                x+=1
            y+=1

def main():
    # comment and uncomment here according to taste.
    W = Wrapper()
    # W = Wrapper2()
    while True:
        W.b.taskMgr.step()
    
if __name__=="__main__":
    main()
