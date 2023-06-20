from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment,Message
from nonebot.params import ArgPlainText,CommandArg

map1=on_command("攻略N",priority=10,block=True)
map2=on_command("攻略H",priority=10,block=True)
way=on_command("攻略",priority=10,block=True)
menu=on_command("帮助",aliases={'help','菜单'},priority=10,block=True)

#千里眼
clairvoyance=on_command("未来视",aliases={"卡池千里眼","卡池未来视", "千里眼"},priority=10,block=True)


@clairvoyance.handle()
async def _():
        await clairvoyance.finish(MessageSegment.image("https://cdnimg.gamekee.com/wiki2.0/images/w_2456/h_5304/829/43637/2023/5/2/228349.png"))




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

ways={'配队':'https://img1.imgtp.com/2023/06/20/gmC0P6o5.jpg','刷初始':'https://img1.imgtp.com/2023/06/20/g8Gin7GP.png'}


@menu.handle()
async def menu_handle():
    await menu.finish(Message("指令使用方法如下：\n\n查看角色评分：/ba角评 学生名\n\n查看角色l2d：/ba羁绊 学生名\n\n查看总力战：/ba总力战 boss名\n\n查看最近日程：/ba日程表\n\n查看学生图鉴：/ba学生图鉴 学生名\n\n查询学生语音：/ba语音 学生名\n\n模拟抽卡：\n  1、切换卡池：/ba切换卡池 角色名\n  2、抽卡：/ba抽卡 0-90\n\n查看关卡攻略(只有6后)：\n  NORMAL：/攻略N 关卡数\n  HARD：/攻略H 关卡数"))

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

@way.got("location", prompt="请输入您的问题")
async def got_location(location: str = ArgPlainText()):
    await way.finish(MessageSegment.image(ways[location]))