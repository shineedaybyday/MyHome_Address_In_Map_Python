from cpca import drawer
import cpca
myhome = ["河北省石家庄市新华区"]
df = cpca.transform(myhome, pos_sensitive=True)
drawer.draw_locations(df[cpca._ADCODE], "xingtai.html")