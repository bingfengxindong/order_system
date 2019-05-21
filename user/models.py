from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.UUIDField(verbose_name="编号")
    u_name = models.CharField(max_length=200,verbose_name="用户名")
    u_username = models.CharField(max_length=200,verbose_name="账号")
    u_password = models.CharField(max_length=200,verbose_name="密码")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.u_name)

    class Meta:
        ordering = ["pk"]
        verbose_name = "用户表"
        verbose_name_plural = "用户表"