from pyecharts import options as opts
from pyecharts.charts import Map

data = [
    ["浦东新区", 95],
    ["闵行区", 88],
    ["松江区", 75],
    ["徐汇区", 60],
    ["黄浦区", 40],
]

c = (
    Map(init_opts=opts.InitOpts(bg_color="#000000"))
    .add(
        series_name="系列名",
        data_pair=data,
        maptype="上海",
        is_map_symbol_show=False,

        # 默认区域 —— 深灰蓝，冷静高级
        itemstyle_opts=opts.ItemStyleOpts(
            area_color="#2A2D43",
            border_color="#4C5C96"
        ),

        # 悬停区域 —— 霓虹赛博蓝
        emphasis_itemstyle_opts=opts.ItemStyleOpts(
            area_color="#5F6FFF",
            border_color="#B8C1FF",
        ),

        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="上海地图 - 赛博蓝紫主题",
            title_textstyle_opts=opts.TextStyleOpts(color="#FFFFFF")
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{b}: {c}",
            textstyle_opts=opts.TextStyleOpts(color="#FFFFFF")
        ),
    )
)

c.render("shanghai_cyber_blue_map.html")
print("✅ 地图已生成：shanghai_cyber_blue_map.html（赛博蓝紫主题）")
