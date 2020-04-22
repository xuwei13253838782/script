from django.db import models

# Create your models here.


class Node(models.Model):

    # 产品节点
    product_node = models.CharField(max_length=200, null=True)
    # 现场节点
    real_node = models.CharField(max_length=200, null=True)
    # 节点值
    node_value = models.CharField(max_length=2000, null=True)
    # 交易码
    trans_code = models.CharField(max_length=200)
