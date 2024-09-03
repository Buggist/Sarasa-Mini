from fontTools.ttLib import TTFont


def rename_font(name):

    # 加载字体文件
    font = TTFont('-sarasa-mini-%s.ttf' % name)

    # 访问命名表
    nameTable = font['name']

    # 遍历命名表中的记录
    for nameRecord in nameTable.names:
        # 检查记录的名称 ID 是否为全名称（4）并且平台 ID 为 Windows (3)
        if nameRecord.nameID == 4 and nameRecord.platformID == 3:
            # 修改字体的全名称
            nameRecord.string = "Sarasa Mini %s" % name.title()

        if nameRecord.nameID == 1 and nameRecord.platformID == 3:
            # 修改字体的家族名称
            nameRecord.string = "Sarasa Mini"

    # 保存修改后的字体
    font.save('sarasa-mini-%s.ttf' % name)


for name in ["regular", "bold", "italic", "bolditalic"]:
    rename_font(name)
