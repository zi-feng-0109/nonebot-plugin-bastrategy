from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment,Message
from nonebot.params import ArgPlainText,CommandArg
#from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import GROUP_ADMIN,GROUP_OWNER
import json

role=on_command("角色",priority=10,block=True,aliases={'攻略','角评'})
clairvoyance=on_command("未来视",aliases={"卡池千里眼","卡池未来视", "千里眼","国际服千里眼","国际服未来视"},priority=10,block=True)
Zhclairvoyance=on_command("国服未来视",aliases={"国服卡池千里眼","国服卡池未来视", "国服千里眼"},priority=10,block=True)
checkpoint=on_command("关卡",priority=10,block=True)
menu=on_command("帮助",aliases={"help","菜单"},priority=10,block=True)
nickname=on_command("添加外号",priority=10,block=True,permission=GROUP_ADMIN | GROUP_OWNER,)
delname=on_command("删除外号",priority=10,block=True,permission=GROUP_ADMIN | GROUP_OWNER,)

##添加角色外号json的函数
def add_key_value_to_json(file_path, key, value):
    # 读取JSON文件并转换为字典
    with open(file_path, 'r',encoding='utf-8') as file:
        json_data = file.read()  
    print("已打开文件")  
    data_dict = json.loads(json_data)
    # 向字典中添加新的键值对
    data_dict[key] = value
    # 将字典转换回JSON格式
    updated_json_data = json.dumps(data_dict)
    # 将更新后的JSON写入文件中
    with open(file_path, 'w') as file:
        file.write(updated_json_data)
    print("已更新文件")
    # 关闭文件
    file.close()
    print("已关闭文件")

##读取角色外号
def read_json_to_dict(file_path):
    # 读取JSON文件并转换为字典
    with open(file_path, 'r',encoding='utf-8') as file:
        json_data = file.read()
    print("已打开文件") 
    data_dict = json.loads(json_data)
    print("已读取文件") 
    return data_dict

##删除对应key
def remove_key_from_json_file(file_path, key):
    # 读取 JSON 文件内容
    with open(file_path) as file:
        json_data = json.load(file)
    # 删除键值对
    if key in json_data:
        del json_data[key]
    # 将更新后的数据写入到 JSON 文件
    with open(file_path, 'w') as file:
        json.dump(json_data, file)


##菜单
@menu.handle()
async def menu_handle():
     await menu.finish(MessageSegment.image("https://img1.imgtp.com/2023/08/28/h8LmYNhH.png"))

##角色攻略
@role.handle()
async def role_handle(args: Message = CommandArg()):
    if location := args.extract_plain_text():
        base_url="https://arona.cdn.diyigemt.com/image/student_rank/"
        roles=read_json_to_dict("./data/roles.json")
        if location in roles:    
            url = base_url+roles[location]+".png"
            await role.finish(MessageSegment.image(url))
        else:
             await role.finish(Message("请先添加学生或者外号哟~"))
@role.got("location", prompt="请输入学生姓名")
async def got_location(location: str = ArgPlainText()):
    base_url="https://arona.cdn.diyigemt.com/image/student_rank/"
    roles=read_json_to_dict("./data/roles.json")
    if location in roles:    
        url = base_url+roles[location]+".png"
        await role.finish(MessageSegment.image(url))
    else:
        await role.finish(Message("请先添加学生或者外号哟~"))

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

##添加学生外号
@nickname.handle()
async def nickname_handle(args: Message = CommandArg()):
     key_value=args.extract_plain_text().split("-")
     key=key_value[0]
     value=key_value[1]
     add_key_value_to_json('./data/roles.json',key,value)
     await nickname.finish(Message("【"+key+"】"+"已经添加为学生："+value+"的新外号"))

##删除学生外号
@delname.handle()
async def delname_handle(args: Message = CommandArg()):
     key=args.extract_plain_text()
     roles=read_json_to_dict("./data/roles.json")
     if key in roles:
        remove_key_from_json_file("./data/roles.json",key=key)
        await delname.finish(Message("已经成功删除该外号"))
     else:
        await delname.finish(Message("不存在该外号或学生"))

