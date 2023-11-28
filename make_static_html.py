from geom import geom
from vector import vector



def box_with_frames(pos=(1, 1, 0),size=(5,3),f=0.2,small_f=0.1):
    
    V = vector.Vector
    f = f

    cx,cy=size

    x = cx*f
    y = cy*f
    
    dvec = vector.Vector(x, y, 0)
    lp = vector.Vector(*pos)
    l = [geom.rectangle(d_vec=dvec, local_position=lp)]
    
    f=small_f
    
    c = 0
    dvec = V(f, f, 0)
    while c < cx+2:
        lpx = V(lp[0]+(c-1)*small_f, lp[1]-small_f, 0)
        g_ob = geom.rectangle(d_vec=dvec, local_position=lpx)
        l.append(g_ob)
        c += 1

    c = 0
    while c < cx+2:
        lpx = V(lp[0]+(c-1)*small_f, lp[1]+y, 0)
        g_ob=geom.rectangle(d_vec=dvec, local_position=lpx)
        l.append(g_ob)
        c += 1

    c = 0
    while c < cy:
        lpx = V(lp[0]-small_f, lp[1]+c*small_f, 0)
        g_ob=geom.rectangle(d_vec=dvec, local_position=lpx)
        l.append(g_ob)
        c += 1

    c = 0
    while c < cy:
        lpx=V(lp[0]+x, lp[1]+c*small_f, 0)
        g_ob=geom.rectangle(d_vec=V(f, f, 0),local_position=lpx)
        l.append(g_ob)
        c += 1
    return l

def main():
    s = """<!doctype html>
<head>
    <title>MYUI</title>
    <meta charset="utf-8"> 
    <link rel="stylesheet" type="text/css" href="./../mainstyle.css"/>
    
</head>

<body>
<div width="100%">
<img src="this.svg"/>
</div>
</body>"""
    V = vector.Vector
    
    l=box_with_frames()
    
    view_box_d = geom.make_view_box_d(l)
    fl = []
    for x in l:
        fl.append(x.as_svg())
    geom.main_svg(fl, "this.svg", view_box_d=view_box_d)

    with open("this.html", "w") as f:
        f.write(s)

if __name__ == "__main__":
    main()
