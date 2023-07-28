from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment,Message
from nonebot.params import ArgPlainText,CommandArg

map1=on_command("攻略N",priority=10,block=True)
map2=on_command("攻略H",priority=10,block=True)
way=on_command("攻略",priority=10,block=True)
opaz=on_command("欧帕兹",aliases={"材料","opaz"},priority=10,block=True)


keyword1=on_command("创建nexon",priority=10,block=True)
keyword2=on_command("创建outlook",priority=10,block=True)

menu=on_command("帮助",aliases={'help','菜单'},priority=10,block=True)

#千里眼
clairvoyance=on_command("未来视",aliases={"卡池千里眼","卡池未来视", "千里眼"},priority=10,block=True)


@clairvoyance.handle()
async def _():
        await clairvoyance.finish(MessageSegment.image("https://cdnimg.gamekee.com/wiki2.0/images/w_2568/h_6088/829/43637/2023/6/25/334321.png?x-image-process=image/resize,m_lfit,w_1600"))




#创建字典
mapn={'6-1':'https://s1.ax1x.com/2023/06/12/pCemYAU.png','6-2':'https://s1.ax1x.com/2023/06/12/pCeKHUK.png','6-3':'https://s1.ax1x.com/2023/06/12/pCe1jFP.png','6-4':'https://s1.ax1x.com/2023/06/12/pCe3SSS.png','6-5':'https://s1.ax1x.com/2023/06/12/pCe3pQg.png',
     '7-1':'https://s1.ax1x.com/2023/06/12/pCe3U6e.png','7-2':'https://s1.ax1x.com/2023/06/12/pCe3ot0.png','7-3':'https://s1.ax1x.com/2023/06/12/pCe8aCV.png','7-4':'https://s1.ax1x.com/2023/06/12/pCe3v7R.png','7-5':'https://s1.ax1x.com/2023/06/12/pCe8mNt.png',
     '8-1':'https://s1.ax1x.com/2023/06/12/pCe8xKg.png','8-2':'https://s1.ax1x.com/2023/06/12/pCeGExU.png','8-3':'https://s1.ax1x.com/2023/06/12/pCeGuZ9.png','8-4':'https://s1.ax1x.com/2023/06/12/pCeGrz8.png','8-5':'https://s1.ax1x.com/2023/06/12/pCeGIzT.png',
     '9-1':'https://s1.ax1x.com/2023/06/12/pCeJ9yD.png','9-2':'https://s1.ax1x.com/2023/06/12/pCeJmSf.png','9-3':'https://s1.ax1x.com/2023/06/12/pCeJNlT.png','9-4':'https://s1.ax1x.com/2023/06/12/pCeJwm4.png','9-5':'https://s1.ax1x.com/2023/06/12/pCeJ00J.png',
     '10-1':'https://s1.ax1x.com/2023/06/12/pCeJrkR.png','10-2':'https://s1.ax1x.com/2023/06/12/pCeJb1f.png','10-3':'https://s1.ax1x.com/2023/06/12/pCet3R0.png','10-4':'https://s1.ax1x.com/2023/06/12/pCet5Wt.png','10-5':'https://s1.ax1x.com/2023/06/12/pCeNFw4.png',
     '11-1':'https://s1.ax1x.com/2023/06/12/pCeNRXT.png','11-2':'https://s1.ax1x.com/2023/06/12/pCeNIAJ.png','11-3':'https://s1.ax1x.com/2023/06/12/pCeNThR.png','11-4':'https://s1.ax1x.com/2023/06/12/pCeNXnO.png','11-5':'https://s1.ax1x.com/2023/06/12/pCeNjBD.png',
     '12-1':'https://s1.ax1x.com/2023/06/12/pCeUKCn.png','12-2':'https://s1.ax1x.com/2023/06/12/pCeU3uT.png','12-3':'https://s1.ax1x.com/2023/06/12/pCeUsbD.png','12-4':'https://s1.ax1x.com/2023/06/12/pCeUf2t.png','12-5':'https://s1.ax1x.com/2023/06/12/pCeaPIJ.png',
     '13-1':'https://s1.ax1x.com/2023/06/12/pCeaExx.png','13-2':'https://s1.ax1x.com/2023/06/12/pCeaDWn.png','13-3':'https://s1.ax1x.com/2023/06/12/pCea6yV.png','13-4':'https://s1.ax1x.com/2023/06/12/pCeaHOK.png','13-5':'https://s1.ax1x.com/2023/06/12/pCeaLwD.png',
     '14-1':'https://s1.ax1x.com/2023/06/12/pCedmpn.png','14-2':'https://s1.ax1x.com/2023/06/12/pCedrAe.png','14-3':'https://s1.ax1x.com/2023/06/12/pCedc9A.png','14-4':'https://s1.ax1x.com/2023/06/12/pCedRjP.png','14-5':'https://s1.ax1x.com/2023/06/12/pCedhB8.png',
     '15-1':'https://img1.imgtp.com/2023/06/12/m4kcxhTi.png','15-2':'https://img1.imgtp.com/2023/06/12/ErKXL4ET.png','15-3':'https://img1.imgtp.com/2023/06/12/wNC73AAa.png','15-4':'https://img1.imgtp.com/2023/06/12/kSK1CAch.png','15-5':'https://img1.imgtp.com/2023/06/12/GK7ajFw5.png',
     '16-1':'https://img1.imgtp.com/2023/06/12/X6aK5M5g.png','16-2':'https://img1.imgtp.com/2023/06/12/KnmjwDrd.png','16-3':'https://img1.imgtp.com/2023/06/12/AOaObRzu.png','16-4':'https://img1.imgtp.com/2023/06/12/KIpUQ0UE.png','16-5':'https://img1.imgtp.com/2023/06/12/HDyqebaE.png',
     '17-1':'https://img1.imgtp.com/2023/06/12/AD4tErgO.png','17-2':'https://img1.imgtp.com/2023/06/12/S17V01ao.png','17-3':'https://img1.imgtp.com/2023/06/12/E8rKkUar.png','17-4':'https://img1.imgtp.com/2023/06/12/6uytF26c.png','17-5':'https://img1.imgtp.com/2023/06/12/RGSI6VO7.png',
     '18-1':'https://img1.imgtp.com/2023/06/12/x7xdhO2i.png','18-2':'https://img1.imgtp.com/2023/06/12/pu46GUxD.png','18-3':'https://img1.imgtp.com/2023/06/12/GHEpExxg.png','18-4':'https://img1.imgtp.com/2023/06/12/W9BawC3s.png','18-5':'https://img1.imgtp.com/2023/06/12/pJRMpfLh.png',
     '19-1':'https://img1.imgtp.com/2023/06/12/vjSMLPZl.png','19-2':'https://img1.imgtp.com/2023/06/12/tB0hTsIC.png','19-3':'https://img1.imgtp.com/2023/06/12/KiHHbEo0.png','19-4':'https://img1.imgtp.com/2023/06/12/xCkuq1BI.png','19-5':'https://img1.imgtp.com/2023/06/12/HB0uqa0d.png',
     '20-1':'https://img1.imgtp.com/2023/06/12/uCAnTssY.png','20-2':'https://img1.imgtp.com/2023/06/12/rXOGd74H.png','20-3':'https://img1.imgtp.com/2023/06/12/AwS2lItn.png','20-4':'https://img1.imgtp.com/2023/06/12/GbQAcKPI.png','20-5':'https://img1.imgtp.com/2023/06/12/35D4Y9sb.png',
     '21-1':'https://img1.imgtp.com/2023/06/12/lPSHEoGu.png','21-2':'https://img1.imgtp.com/2023/06/12/k0LS0uAz.png','21-3':'https://img1.imgtp.com/2023/06/12/1xYkQrA4.png','21-4':'https://img1.imgtp.com/2023/06/12/itFafQ8u.png','21-5':'https://img1.imgtp.com/2023/06/12/13vYfEMU.png',
     '22-1':'https://img1.imgtp.com/2023/06/12/MZVtxj3P.png','22-2':'https://img1.imgtp.com/2023/06/12/MsRoFCQ9.png','22-3':'https://img1.imgtp.com/2023/06/12/2RzBqf8T.png','22-4':'https://img1.imgtp.com/2023/06/12/fu0hOgcM.png','22-5':'https://img1.imgtp.com/2023/06/12/Gzv4pWmn.png',
     '23-1':'https://img1.imgtp.com/2023/06/12/LzAYgDpv.png','23-2':'https://img1.imgtp.com/2023/06/12/JNCfSVm8.png','23-3':'https://img1.imgtp.com/2023/06/12/DTZgWhbr.png','23-4':'https://img1.imgtp.com/2023/06/12/eOKT98AG.png','23-5':'https://img1.imgtp.com/2023/06/12/bxdJjtuZ.png',}

maph={'6-1':'https://img1.imgtp.com/2023/06/12/jh5akHeT.png','6-2':'https://img1.imgtp.com/2023/06/12/csTQIcjk.png','6-3':'https://img1.imgtp.com/2023/06/12/LaYUGUMz.png',
      '7-1':'https://img1.imgtp.com/2023/06/12/d6xmwLpr.png','7-2':'https://img1.imgtp.com/2023/06/12/8UudmXWx.png','7-3':'https://img1.imgtp.com/2023/06/12/S3F910bT.png',
      '8-1':'https://img1.imgtp.com/2023/06/12/SmCHR8XN.png','8-2':'https://img1.imgtp.com/2023/06/12/IfZIxuUg.png','8-3':'https://img1.imgtp.com/2023/06/12/78AEyRWu.png',
      '9-1':'https://img1.imgtp.com/2023/06/12/PVqunLeJ.png','9-2':'https://img1.imgtp.com/2023/06/12/V37wKCzg.png','9-3':'https://img1.imgtp.com/2023/06/12/YSg1NppE.png',
      '10-1':'https://img1.imgtp.com/2023/06/12/M48iPkG3.png','10-2':'https://img1.imgtp.com/2023/06/12/JFyU3ltJ.png','10-3':'https://img1.imgtp.com/2023/06/12/HFeuCiCi.png',
      '11-1':'https://img1.imgtp.com/2023/06/12/EJXkCIhZ.png','11-2':'https://img1.imgtp.com/2023/06/12/QPlFtwFK.png','11-3':'https://img1.imgtp.com/2023/06/12/X1W3UfzP.png',
      '12-1':'https://img1.imgtp.com/2023/06/12/521vu0Z5.png','12-2':'https://img1.imgtp.com/2023/06/12/7JmkCkZz.png','12-3':'https://img1.imgtp.com/2023/06/12/IwNjo8l0.png',
      '13-1':'https://img1.imgtp.com/2023/06/12/WMcMO7eQ.png','13-2':'https://img1.imgtp.com/2023/06/12/PDraVdFp.png','13-3':'https://img1.imgtp.com/2023/06/12/GFCJQW1i.png',
      '14-1':'https://img1.imgtp.com/2023/06/12/AtnRVNIo.png','14-2':'https://img1.imgtp.com/2023/06/12/1KUCsj9X.png','14-3':'https://img1.imgtp.com/2023/06/12/cjo6Tcuu.png',
      '15-1':'https://img1.imgtp.com/2023/06/12/nXvly9pa.png','15-2':'https://img1.imgtp.com/2023/06/12/cpndjXUf.png','15-3':'https://img1.imgtp.com/2023/06/12/3e7v4nI0.png',
      '16-1':'https://img1.imgtp.com/2023/06/12/ZREMIlG1.png','16-2':'https://img1.imgtp.com/2023/06/12/fotPfsIC.png','16-3':'https://img1.imgtp.com/2023/06/12/5crhkiIh.png',
      '17-1':'https://img1.imgtp.com/2023/06/12/aqLuJsAG.png','17-2':'https://img1.imgtp.com/2023/06/12/S17V01ao.png','17-3':'https://img1.imgtp.com/2023/06/12/cOJ3EGJH.png',
      '18-1':'https://img1.imgtp.com/2023/06/12/zsy9GxBx.png','18-2':'https://img1.imgtp.com/2023/06/12/2objLTYR.png','18-3':'https://img1.imgtp.com/2023/06/12/JQOwWEr5.png',
      '19-1':'https://img1.imgtp.com/2023/06/12/n9uw7Eim.png','19-2':'https://img1.imgtp.com/2023/06/12/RZcYCIYT.png','19-3':'https://img1.imgtp.com/2023/06/12/Hiz7NTFl.png',
      '20-1':'https://img1.imgtp.com/2023/06/12/9ZzGNQjh.png','20-2':'https://img1.imgtp.com/2023/06/12/C1eh59Yw.png','20-3':'https://img1.imgtp.com/2023/06/12/SYJNTdjL.png',
      '21-1':'https://img1.imgtp.com/2023/06/12/qZpc9jdB.png','21-2':'https://img1.imgtp.com/2023/06/12/V2fNKd6c.png','21-3':'https://img1.imgtp.com/2023/06/12/dRpWfCah.png',
      '22-1':'https://img1.imgtp.com/2023/06/12/dXoqFVzY.png','22-2':'https://img1.imgtp.com/2023/06/12/AGRvP84h.png','22-3':'https://img1.imgtp.com/2023/06/12/ww4iJZYz.png',
      '23-1':'https://img1.imgtp.com/2023/06/12/D8284J0F.png','23-2':'https://img1.imgtp.com/2023/06/12/xVuRaLsb.png','23-3':'https://img1.imgtp.com/2023/06/12/ZefhlBM5.png',}

ways={'配队':'https://img1.imgtp.com/2023/06/20/gmC0P6o5.jpg','刷初始':'https://i0.hdslb.com/bfs/article/4008f0ec2583478f46309e22c4691d8cec3f91ca.png@1256w_1620h_!web-article-pic.webp',
      '服务器':'https://img1.imgtp.com/2023/06/20/xgLlUUOO.png','礼物':'https://img1.imgtp.com/2023/07/28/I7eGqcXw.jpg',
      '总评':'https://cdnimg.gamekee.com/wiki2.0/images/w_3876/h_4464/829/43637/2023/6/25/782516.png?x-image-process=image/resize,m_lfit,w_1600'
      }


opazs={'艾米':'https://img1.imgtp.com/2023/07/17/SfXGwjay.png','爱莉':'https://img1.imgtp.com/2023/07/17/VhQJQN79.png','阿露':'https://img1.imgtp.com/2023/07/17/5Xa08n0B.png',
       '春阿露':'https://img1.imgtp.com/2023/07/17/9gDvJyJ9.png','爱丽丝':'https://img1.imgtp.com/2023/07/17/65yO8oSa.png','女仆爱丽丝':'https://img1.imgtp.com/2023/07/17/2ryM5loC.png',
       '白子':'https://img1.imgtp.com/2023/07/17/pldzhL1v.png','单车白子':'https://img1.imgtp.com/2023/07/17/iQDGFMFA.png','吹雪':'https://img1.imgtp.com/2023/07/17/aSNvrtIZ.png',
       '椿':'https://img1.imgtp.com/2023/07/17/xzl9vaWE.png','淳子':'https://img1.imgtp.com/2023/07/17/qT8BvuBd.png','春淳子':'https://img1.imgtp.com/2023/07/17/MmUmNcMp.png',
       '菲娜':'https://img1.imgtp.com/2023/07/17/Emy6NNgM.png','枫':'https://img1.imgtp.com/2023/07/17/nZkl4Tkj.png','枫香':'https://img1.imgtp.com/2023/07/17/3sdUXDQZ.png',
       '春枫香':'https://img1.imgtp.com/2023/07/17/MAFNYxmK.png','果穗':'https://img1.imgtp.com/2023/07/17/3HcBAKfr.png','歌原':'https://img1.imgtp.com/2023/07/17/bqAPU5zk.png',
       '应援团歌原':'https://img1.imgtp.com/2023/07/17/HNSjH4wZ.png','宫子':'https://img1.imgtp.com/2023/07/17/4ECVDqm7.png','水宫子':'https://img1.imgtp.com/2023/07/17/WqC8PVJf.png',
       '好美':'https://img1.imgtp.com/2023/07/17/XrQb5Wek.png','和纱':'https://img1.imgtp.com/2023/07/17/vQdEXxTp.png','和香':'https://img1.imgtp.com/2023/07/17/GRETC6oj.png',
       '温泉和香':'https://img1.imgtp.com/2023/07/17/Y4hx7MDL.png','鹤城':'https://img1.imgtp.com/2023/07/17/gZjSqISo.png','水鹤城':'https://img1.imgtp.com/2023/07/17/imbi5cmE.png',
       '花江':'https://img1.imgtp.com/2023/07/17/AOjIX8u8.png','圣诞花江':'https://img1.imgtp.com/2023/07/17/iHp5QgvG.png','花凛':'https://img1.imgtp.com/2023/07/17/MzQcbqu5.png',
       '兔花凛':'https://img1.imgtp.com/2023/07/17/c37lVQkK.png','花子':'https://img1.imgtp.com/2023/07/17/6lCRPK8J.png','惠':'https://img1.imgtp.com/2023/07/17/0j3Q6gMK.png',
       '佳代子':'https://img1.imgtp.com/2023/07/17/KNEHnrKH.png','春佳代子':'https://img1.imgtp.com/2023/07/17/VDT3b7My.png','堇':'https://img1.imgtp.com/2023/07/17/qtyS1YyJ.png',
       '静子':'https://img1.imgtp.com/2023/07/17/wSP8rvlx.png','水静子':'https://img1.imgtp.com/2023/07/17/2tkEgFeS.png','柯托莉':'https://img1.imgtp.com/2023/07/17/g9f6OZz1.png',
       '濑名':'https://img1.imgtp.com/2023/07/17/7WQAdoNA.png','莲见':'https://img1.imgtp.com/2023/07/17/nWrb8DZX.png','体莲见':'https://img1.imgtp.com/2023/07/17/idGkYdQI.png',
       '玲纱':'https://img1.imgtp.com/2023/07/17/WWZVmTUG.png','铃美':'https://img1.imgtp.com/2023/07/17/ug4MZ1dp.png','绫音':'https://img1.imgtp.com/2023/07/17/CiaIBPEr.png',
       '水绫音':'https://img1.imgtp.com/2023/07/17/F0dkAtmS.png','瑠美':'https://img1.imgtp.com/2023/07/17/3JDj3PId.png','绿':'https://img1.imgtp.com/2023/07/17/HK9RsvWL.png',
       '玛丽':'https://img1.imgtp.com/2023/07/17/GiZ4ZWq8.png','体玛丽':'https://img1.imgtp.com/2023/07/17/4z8o59zL.png','玛丽娜':'https://img1.imgtp.com/2023/07/17/ZityECFY.png',
       '满':'https://img1.imgtp.com/2023/07/17/1Qeyuzml.png','美弥':'https://img1.imgtp.com/2023/07/17/D7OrPCNT.png','美咲':'https://img1.imgtp.com/2023/07/17/XTtRr6Dm.png',
       '美游':'https://img1.imgtp.com/2023/07/17/hnoQtOt3.png','水美游':'https://img1.imgtp.com/2023/07/17/073ZWbze.png','萌绘':'https://img1.imgtp.com/2023/07/17/Rt6vMOj8.png',
       '弥奈':'https://img1.imgtp.com/2023/07/28/kUR7zOOe.png','明里':'https://img1.imgtp.com/2023/07/28/Gpu2uQmz.png','明日奈':'https://img1.imgtp.com/2023/07/28/Q1fBafqO.png',
       '兔明日奈':'https://img1.imgtp.com/2023/07/28/HsWURmuo.png','睦月':'https://img1.imgtp.com/2023/07/28/p3IPHodG.png','春睦月':'https://img1.imgtp.com/2023/07/28/m1ipsq8h.png',
       '尼禄':'https://img1.imgtp.com/2023/07/28/2gMwnW63.png','兔尼禄':'https://img1.imgtp.com/2023/07/28/fJDMmfXp.png','诺亚':'https://img1.imgtp.com/2023/07/28/40wcOhbT.png',
       '千世':'https://img1.imgtp.com/2023/07/28/4FNPWkby.png','水千世':'https://img1.imgtp.com/2023/07/28/5A3PBXX7.png','千夏':'https://img1.imgtp.com/2023/07/28/VvZhMWP1.png',
       '温泉千夏':'https://img1.imgtp.com/2023/07/28/phxBlbX7.png','茜':'https://img1.imgtp.com/2023/07/28/rUoGswFG.png','兔茜':'https://img1.imgtp.com/2023/07/28/QGhReDg6.png',
       '千寻':'https://img1.imgtp.com/2023/07/28/DTPaP3Dc.png','切里诺':'https://img1.imgtp.com/2023/07/28/6Z1wjQOw.png','温泉切里诺':'https://img1.imgtp.com/2023/07/28/cW0CkBr2.png',
       '芹香':'https://img1.imgtp.com/2023/07/28/GS56gCoG.png','春芹香':'https://img1.imgtp.com/2023/07/28/i4yFh4ny.png','芹奈':'https://img1.imgtp.com/2023/07/28/IFOGPcRh.png',
       '圣诞芹奈':'https://img1.imgtp.com/2023/07/28/RVJd01WL.png','晴':'https://img1.imgtp.com/2023/07/28/xhauZGq3.png','晴奈':'https://img1.imgtp.com/2023/07/28/6ciLmGIH.png',
       '春晴奈':'https://img1.imgtp.com/2023/07/28/7ajpe6dE.png','泉':'https://img1.imgtp.com/2023/07/28/65kdp0bx.png','水泉':'https://img1.imgtp.com/2023/07/28/1yzwd6GL.png',
       '泉奈':'https://img1.imgtp.com/2023/07/28/bAoIpNEM.png','水泉奈':'https://img1.imgtp.com/2023/07/28/lduGPOPZ.png','日富美':'https://img1.imgtp.com/2023/07/28/7Sv4ITWg.png',
       '水日富美':'https://img1.imgtp.com/2023/07/28/WQfbUdyd.png','日鞠':'https://img1.imgtp.com/2023/07/28/JpRsOTA7.png','日和':'https://img1.imgtp.com/2023/07/28/FdKp9uN3.png',
       '日奈':'https://img1.imgtp.com/2023/07/28/bBteR0HL.png','水日奈':'https://img1.imgtp.com/2023/07/28/VHsPx9Ym.png','日向':'https://img1.imgtp.com/2023/07/28/y1EPz5M0.png',
       '若藻':'https://img1.imgtp.com/2023/07/28/a90PRHTZ.png','水若藻':'https://img1.imgtp.com/2023/07/28/1D7fHjNz.png','三森':'https://img1.imgtp.com/2023/07/28/6kfycgDp.png',
       '纱绫':'https://img1.imgtp.com/2023/07/28/QJlrsXhl.png','私服纱绫':'https://img1.imgtp.com/2023/07/28/QJlrsXhl.png','纱织':'https://img1.imgtp.com/2023/07/28/vjbJCrMJ.png',
       '时':'https://img1.imgtp.com/2023/07/28/hxVRUMob.png','兔时':'https://img1.imgtp.com/2023/07/28/rI361pIF.png','实里':'https://img1.imgtp.com/2023/07/28/YlliQPfR.png',
       '时雨':'https://img1.imgtp.com/2023/07/28/VTirljXc.png','瞬':'https://img1.imgtp.com/2023/07/28/MT6jNNKA.png','幼瞬':'https://img1.imgtp.com/2023/07/28/AJyl9gNW.png',
       '桃井':'https://img1.imgtp.com/2023/07/28/UYurvSH8.png','桐乃':'https://img1.imgtp.com/2023/07/28/nwFZz1A4.png','未花':'https://img1.imgtp.com/2023/07/28/kS27xvqP.png',
       '小夏':'https://img1.imgtp.com/2023/07/28/dG1uhZdI.png','响':'https://img1.imgtp.com/2023/07/28/fYllgF8O.png','应援团响':'https://img1.imgtp.com/2023/07/28/FfYhAmRW.png',
       '小春':'https://img1.imgtp.com/2023/07/28/HLIUXq1H.png','咲':'https://img1.imgtp.com/2023/07/28/3woNgtaS.png','水咲':'https://img1.imgtp.com/2023/07/28/Hvj46bCB.png',
       '小玉':'https://img1.imgtp.com/2023/07/28/Md6B007c.png','小雪':'https://img1.imgtp.com/2023/07/28/KGhYUsG9.png','心奈':'https://img1.imgtp.com/2023/07/28/TR0deQ8v.png',
       '星野':'https://img1.imgtp.com/2023/07/28/7CU3gYqg.png','水星野':'https://img1.imgtp.com/2023/07/28/XCkbCNL0.png','亚子':'https://img1.imgtp.com/2023/07/28/M5MFBhIW.png',
       '亚津子':'https://img1.imgtp.com/2023/07/28/lQo9wPS0.png','遥香':'https://img1.imgtp.com/2023/07/28/XQzhgKyC.png','春遥香':'https://img1.imgtp.com/2023/07/28/LgaxKLQ7.png',
       '野宫':'https://img1.imgtp.com/2023/07/28/6yda3iVf.png','水野宫':'https://img1.imgtp.com/2023/07/28/AH2ZPYB5.png','叶渚':'https://img1.imgtp.com/2023/07/28/Ikj2KMw2.png',
       '伊吕波':'https://img1.imgtp.com/2023/07/28/zpyOSnDw.png','伊织':'https://img1.imgtp.com/2023/07/28/FJesdEvg.png','水伊织':'https://img1.imgtp.com/2023/07/28/Dsc2K5EO.png',
       '樱子':'https://img1.imgtp.com/2023/07/28/858dhpB9.png','优香':'https://img1.imgtp.com/2023/07/28/9CbHZA5X.png','体优香':'https://img1.imgtp.com/2023/07/28/1vqtx2ui.png',
       '忧':'https://img1.imgtp.com/2023/07/28/WVrF40rV.png','柚子':'https://img1.imgtp.com/2023/07/28/z2oPMqZM.png','女仆柚子':'https://img1.imgtp.com/2023/07/28/F3KbQkTk.png',
       '月咏':'https://img1.imgtp.com/2023/07/28/rzDyUOxK.png','智惠':'https://img1.imgtp.com/2023/07/28/dWts7GeN.png','真白':'https://img1.imgtp.com/2023/07/28/qJe1ojbW.png',
       '水真白':'https://img1.imgtp.com/2023/07/28/gEdaaQBt.png','真纪':'https://img1.imgtp.com/2023/07/28/4On3NWBb.png','朱莉':'https://img1.imgtp.com/2023/07/28/209Ri6vg.png',
       '志美子':'https://img1.imgtp.com/2023/07/28/kiQlL2Kw.png','渚':'https://img1.imgtp.com/2023/07/28/nWOJN1Bi.png','梓':'https://img1.imgtp.com/2023/07/28/9ZRd1B7m.png','水梓':'https://img1.imgtp.com/2023/07/28/tLZNH9qb.png',
       
       '=======学生外号=======':'https://zi-feng-0109.github.io/',

       '冰激凌':'https://img1.imgtp.com/2023/07/17/VhQJQN79.png',
       '傻子':'https://img1.imgtp.com/2023/07/17/5Xa08n0B.png','阿鲁':'https://img1.imgtp.com/2023/07/17/5Xa08n0B.png',
       '春阿鲁':'https://img1.imgtp.com/2023/07/17/9gDvJyJ9.png',
       '狗盾':'https://img1.imgtp.com/2023/07/17/xzl9vaWE.png',
       '小火龙':'https://img1.imgtp.com/2023/07/17/qT8BvuBd.png',
       '煮饭婆':'https://img1.imgtp.com/2023/07/17/3sdUXDQZ.png',
       '春锅':'https://img1.imgtp.com/2023/07/17/MAFNYxmK.png',
       '咏叶':'https://img1.imgtp.com/2023/07/17/bqAPU5zk.png',
       '应援团咏叶':'https://img1.imgtp.com/2023/07/17/HNSjH4wZ.png',
       '大护士':'https://img1.imgtp.com/2023/07/17/AOjIX8u8.png',
       '圣诞大护士':'https://img1.imgtp.com/2023/07/17/iHp5QgvG.png',
       '喷火龙':'https://img1.imgtp.com/2023/07/17/0j3Q6gMK.png','大火龙':'https://img1.imgtp.com/2023/07/17/0j3Q6gMK.png',
       '救护车':'https://img1.imgtp.com/2023/07/17/7WQAdoNA.png','急救车':'https://img1.imgtp.com/2023/07/17/7WQAdoNA.png',
       '闪光弹':'https://img1.imgtp.com/2023/07/17/ug4MZ1dp.png',
       '直升机':'https://img1.imgtp.com/2023/07/17/F0dkAtmS.png',
       '炒饭婆':'https://img1.imgtp.com/2023/07/17/3JDj3PId.png',
       '小绿':'https://img1.imgtp.com/2023/07/17/HK9RsvWL.png',
       '保洁':'https://img1.imgtp.com/2023/07/17/ZityECFY.png','阿姨':'https://img1.imgtp.com/2023/07/17/ZityECFY.png','保洁阿姨':'https://img1.imgtp.com/2023/07/17/ZityECFY.png',
       '团长':'https://img1.imgtp.com/2023/07/17/D7OrPCNT.png',
       '垃圾兔':'https://img1.imgtp.com/2023/07/17/hnoQtOt3.png','垃姬兔':'https://img1.imgtp.com/2023/07/17/hnoQtOt3.png',
       '水垃圾兔':'https://img1.imgtp.com/2023/07/17/073ZWbze.png','水垃姬兔':'https://img1.imgtp.com/2023/07/17/073ZWbze.png',
       '近卫南':'https://img1.imgtp.com/2023/07/28/kUR7zOOe.png','小马哥':'https://img1.imgtp.com/2023/07/28/kUR7zOOe.png','发哥':'https://img1.imgtp.com/2023/07/28/kUR7zOOe.png',
       '亚丝娜':'https://img1.imgtp.com/2023/07/28/Q1fBafqO.png',
       '兔亚丝娜':'https://img1.imgtp.com/2023/07/28/HsWURmuo.png',
       '尼露':'https://img1.imgtp.com/2023/07/28/2gMwnW63.png',
       '兔尼露':'https://img1.imgtp.com/2023/07/28/fJDMmfXp.png',
       '卑女':'https://img1.imgtp.com/2023/07/28/40wcOhbT.png',
       '知世':'https://img1.imgtp.com/2023/07/28/4FNPWkby.png',
       '水知世':'https://img1.imgtp.com/2023/07/28/5A3PBXX7.png',
       '朱音':'https://img1.imgtp.com/2023/07/28/rUoGswFG.png',
       '兔朱音':'https://img1.imgtp.com/2023/07/28/QGhReDg6.png',
       '斯大萝':'https://img1.imgtp.com/2023/07/28/6Z1wjQOw.png',
       '温泉斯大萝':'https://img1.imgtp.com/2023/07/28/cW0CkBr2.png',
       '茜香':'https://img1.imgtp.com/2023/07/28/GS56gCoG.png',
       '春茜香':'https://img1.imgtp.com/2023/07/28/i4yFh4ny.png',
       '小护士':'https://img1.imgtp.com/2023/07/28/IFOGPcRh.png',
       '圣诞小护士':'https://img1.imgtp.com/2023/07/28/RVJd01WL.png',
       '羽留奈':'https://img1.imgtp.com/2023/07/28/6ciLmGIH.png',
       '春羽留奈':'https://img1.imgtp.com/2023/07/28/7ajpe6dE.png',
       '老八':'https://img1.imgtp.com/2023/07/28/65kdp0bx.png',
       '水老八':'https://img1.imgtp.com/2023/07/28/1yzwd6GL.png',
       '忍忍':'https://img1.imgtp.com/2023/07/28/bAoIpNEM.png','小狐狸':'https://img1.imgtp.com/2023/07/28/bAoIpNEM.png',
       '水忍忍':'https://img1.imgtp.com/2023/07/28/lduGPOPZ.png','水小狐狸':'https://img1.imgtp.com/2023/07/28/bAoIpNEM.png',
       '轮椅':'https://img1.imgtp.com/2023/07/28/JpRsOTA7.png','otto':'https://img1.imgtp.com/2023/07/28/JpRsOTA7.png',
       '大狐狸':'https://img1.imgtp.com/2023/07/28/a90PRHTZ.png',
       '水大狐狸':'https://img1.imgtp.com/2023/07/28/1D7fHjNz.png',
       '鼠鼠':'https://img1.imgtp.com/2023/07/28/QJlrsXhl.png',
       '私服鼠鼠':'https://img1.imgtp.com/2023/07/28/QJlrsXhl.png',
       'toki':'https://img1.imgtp.com/2023/07/28/hxVRUMob.png',
       '兔toki':'https://img1.imgtp.com/2023/07/28/rI361pIF.png',
       '工头':'https://img1.imgtp.com/2023/07/28/YlliQPfR.png',
       '小桃':'https://img1.imgtp.com/2023/07/28/UYurvSH8.png',
       'mika':'https://img1.imgtp.com/2023/07/28/kS27xvqP.png',
       '啦啦响':'https://img1.imgtp.com/2023/07/28/FfYhAmRW.png',
       '大叔':'https://img1.imgtp.com/2023/07/28/7CU3gYqg.png',
       '水大叔':'https://img1.imgtp.com/2023/07/28/XCkbCNL0.png',
       '野乃美':'https://img1.imgtp.com/2023/07/28/6yda3iVf.png','富婆':'https://img1.imgtp.com/2023/07/28/6yda3iVf.png',
       '水野乃美':'https://img1.imgtp.com/2023/07/28/AH2ZPYB5.png','水富婆':'https://img1.imgtp.com/2023/07/28/AH2ZPYB5.png',
       '局长':'https://img1.imgtp.com/2023/07/28/Ikj2KMw2.png','狂犬':'https://img1.imgtp.com/2023/07/28/Ikj2KMw2.png',
       '老婆':'https://img1.imgtp.com/2023/07/28/zpyOSnDw.png',
       '佐仓':'https://img1.imgtp.com/2023/07/28/FJesdEvg.png', '佐三枪':'https://img1.imgtp.com/2023/07/28/FJesdEvg.png',
       '水佐仓':'https://img1.imgtp.com/2023/07/28/Dsc2K5EO.png','水佐三枪':'https://img1.imgtp.com/2023/07/28/Dsc2K5EO.png',
       '邮箱':'https://img1.imgtp.com/2023/07/28/9CbHZA5X.png',
       '体邮箱':'https://img1.imgtp.com/2023/07/28/1vqtx2ui.png','体香':'https://img1.imgtp.com/2023/07/28/1vqtx2ui.png',
       '巨忍':'https://img1.imgtp.com/2023/07/28/rzDyUOxK.png',
       '真寄':'https://img1.imgtp.com/2023/07/28/4On3NWBb.png',

       }


@menu.handle()
async def menu_handle():
    await menu.finish(Message("指令使用方法如下：\n\n查看角色评分：/ba角评 学生名\n\n查看角色l2d：/ba羁绊 学生名\n\n查看总力战：/ba总力战 boss名\n\n查看最近日程：/ba日程表\n\n查看学生图鉴：/ba学生图鉴 学生名\n\n查询学生语音：/ba语音 学生名\n\n模拟抽卡：\n  1、切换卡池：/ba切换卡池 角色名\n  2、抽卡：/ba抽卡 0-90\n\n查看关卡攻略(只有6后)：\n  NORMAL：/攻略N 关卡数\n  HARD：/攻略H 关卡数\n\n如何创建outlook邮箱：\n  /创建outlook\n\n如何创建nexon账号：\n  /创建nexon\n\n查看卡池千里眼：/千里眼\n\n查询欧帕兹：\欧帕兹 学生名"))

@keyword1.handle()
async def keyword1_handle():
    await keyword1.send(Message("感谢原作者子封的博客，本博客的源地址：https://zi-feng-0109.github.io/posts/7e128cf7.html"))
    await keyword1.finish(MessageSegment.image('https://img1.imgtp.com/2023/06/20/b33KIfed.png'))

@keyword2.handle()
async def keyword2_handle():
    await keyword2.send(Message("感谢原作者子封的博客，本博客的源地址：https://zi-feng-0109.github.io/posts/b6ba17ab.html"))
    await keyword2.finish(MessageSegment.image('https://img1.imgtp.com/2023/06/20/gUM7anXF.png'))

@map1.handle()
async def handle_function(args: Message = CommandArg()):
    if location := args.extract_plain_text():
        await map1.finish(MessageSegment.image(mapn[location]))

@map1.got("location", prompt="请输入关卡名，如6-1")
async def got_location(location: str = ArgPlainText()):
    await map1.finish(MessageSegment.image(mapn[location]))

@map2.handle()
async def handle_function(args: Message = CommandArg()):
    if location := args.extract_plain_text():
        await map2.finish(MessageSegment.image(maph[location]))

@map2.got("location", prompt="请输入关卡名，如6-1")
async def got_location(location: str = ArgPlainText()):
    await map2.finish(MessageSegment.image(maph[location]))

@way.handle()
async def handle_function(args: Message = CommandArg()):
    if location := args.extract_plain_text():
        await way.finish(MessageSegment.image(ways[location]))

@way.got("location", prompt="请输入您的问题:配队,服务器,刷初始,礼物表")
async def got_location(location: str = ArgPlainText()):
    await way.finish(MessageSegment.image(ways[location]))

##欧帕兹
@opaz.handle()
async def handle_function(args: Message = CommandArg()):
    if location := args.extract_plain_text():
        await opaz.finish(MessageSegment.image(opazs[location]))

@opaz.got("location", prompt="请输入学生:\n皮肤前缀如下:\n泳装:水\n体操服:体\n温泉:温泉\n女仆:女仆\n新春:春\n兔女郎:兔\n应援团:应援团\n圣诞:圣诞\n特殊:单车白子，幼瞬，私服鼠鼠")
async def got_location(location: str = ArgPlainText()):
    await opaz.finish(MessageSegment.image(opazs[location]))