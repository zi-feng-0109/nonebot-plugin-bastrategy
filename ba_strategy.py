from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment,Message
from nonebot.params import ArgPlainText,CommandArg

role=on_command("角色",priority=10,block=True,aliases={'攻略','角评'})
clairvoyance=on_command("未来视",aliases={"卡池千里眼","卡池未来视", "千里眼","国际服千里眼","国际服未来视"},priority=10,block=True)
Zhclairvoyance=on_command("国服未来视",aliases={"国服卡池千里眼","国服卡池未来视", "国服千里眼"},priority=10,block=True)
checkpoint=on_command("关卡",priority=10,block=True)
##角色攻略
@role.handle()
async def role_handle(args: Message = CommandArg()):
    if location := args.extract_plain_text():
        base_url="https://arona.cdn.diyigemt.com/image/student_rank/"
        url = base_url+location+".png"
        await role.finish(MessageSegment.image(url))
@role.got("location", prompt="请输入学生姓名")
async def got_location(location: str = ArgPlainText()):
    base_url="https://arona.cdn.diyigemt.com/image/student_rank/"
    url = base_url+location+".png"
    await role.finish(MessageSegment.image(url))

##国际服千里眼
@clairvoyance.handle()
async def _():
        await clairvoyance.finish(MessageSegment.image("https://arona.cdn.diyigemt.com/image/some/%E5%9B%BD%E9%99%85%E6%9C%8D%E6%9C%AA%E6%9D%A5%E8%A7%86.png"))
##国服千里眼
@Zhclairvoyance.handle()
async def _():
        await Zhclairvoyance.finish(MessageSegment.image("https://arona.cdn.diyigemt.com/image/some/%E5%9B%BD%E6%9C%8D%E6%9C%AA%E6%9D%A5%E8%A7%86.png"))

##关卡攻略
@checkpoint.handle()
async def checkpoint_handle(args: Message = CommandArg()):
    if location := args.extract_plain_text():
        base_url="https://arona.cdn.diyigemt.com/image/chapter_map/"
        url = base_url+location+".png"
        await checkpoint.finish(MessageSegment.image(url))
@checkpoint.got("location", prompt="请输入关卡数")
async def got_location(location: str = ArgPlainText()):
    base_url="https://arona.cdn.diyigemt.com/image/chapter_map/"
    url = base_url+location+".png"
    await checkpoint.finish(MessageSegment.image(url))