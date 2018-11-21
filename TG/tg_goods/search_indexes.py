from haystack import indexes
from tg_goods.models import GoodsInfo
#指定对于某个类的某些数据建立索引
# 索引类名 :  模型类+indexex
class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    # 建立索引字段 use_template 指定数据表中的哪些字段建立索引文件
    # 吧说明放在文件中
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return GoodsInfo  # 返回模型类
    #  建立索引数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()