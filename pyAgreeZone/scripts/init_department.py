import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyAgreeZone.settings")
django.setup()

from apps.api import models

result = models.Department.objects.bulk_create([
    models.Department(name='金融服务事业部'),
    models.Department(name='技术管理中心'),
    models.Department(name='咨询事部'),
    models.Department(name='销售中心'),
    models.Department(name='市场部'),
    models.Department(name='西北事务中心'),
    models.Department(name='华北事务中心'),
    models.Department(name='华南事务中心'),
    models.Department(name='华东事务中心'),
    models.Department(name='公共关系部'),
    models.Department(name='合作者关系部'),
    models.Department(name='信息技术部'),
    models.Department(name='人力资源部'),
    models.Department(name='运营服务中心'),
    models.Department(name='运营服务中心'),
    models.Department(name='法律事务部'),
    models.Department(name='资本运作部'),
    models.Department(name='计财部'),
    models.Department(name='总裁办'),
    models.Department(name='董事会办公室'),
    models.Department(name='董事会'),
])
print(result)
