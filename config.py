# -*- coding: utf-8 -*-
# 这个文件是配置文件

# 手动搜索Appfilter并保存到本地(会覆盖下面的设置，若开启，下面全部内容失效，未开工)
mannualAppfilterMode = False

# 是否输入Iconpack.xml所需内容
needIconpackXml = True

# 是是否生成Drawable.xml所需内容
needDrawableXml = True

# 是否联网获取Appfilter.xml
needAppfilterXml = True

# 设置搜索结果上限(<=128)
# 对 index.py 和 getAppfilter.py 同时使用（LoopMode）
maxResults = 10

# 是否生成主题图标文件（未开工）
needXUIIconFile = False

#------以下是getAppfilter.py的配置------#

# 循环模式，直到不输入任何内容直接回车才停止
infiniteLoop = True