from collections import OrderedDict
from sentinel import SentinelAPI

if __name__ == '__main__':
    # 登录信息
    api = SentinelAPI('dmy', "DMY13476054594")

    # 遥感影像文件名后缀(瓦片号标识)
    # 江陵县：49RFP
    # 沙洋县：49RFP
    # 武穴市：50RLU
    tiles = ['49RFP','49RFP','50RLU']

    # 影像查询关键参数
    query_kwargs = {
        'platformname': 'Sentinel-2',
        'producttype': 'S2MSI1C',
        'date': ('20181101', '20181130'),
        'cloudcoverpercentage': (0, 30)}


    products = OrderedDict()
    # 查询过程
    for tile in tiles:
        kw = query_kwargs.copy()
        kw['tileid'] = tile
        kw_lower = set(x.lower() for x in kw)
        # 进行查询
        pp = api.query(**kw)
        products.update(pp)

    # 打印查找到的遥感影像文件名
    for key, item in products.items():
        print(item['title'])

    # 进行下载，保存到相应的路径
    imgs=api.download_all(list(products), directory_path="D:\\sentinel\\")


