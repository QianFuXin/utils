from id_validator import validator


def judgeChinaIDIsValid(ID):
    # 判断身份证号码是否合法  合法返回True 反之返回False
    return validator.is_valid(ID)


def getInfoByID(ID):
    # 根据身份证号码返回个人信息
    return validator.get_info(ID)
    """
    address_code': 地址码,
    'abandoned':   地址码是否废弃，1为废弃的，0为正在使用的。
    'address': 地址
    'address_tree': 省市区三级列表
    'age':年龄
    'birthday_code': 出生日期
    'constellation': 星座
    'chinese_zodiac': 生肖
    'sex':  性别，1 为男性，0 为女性
    'length': 身份证长度
    'check_bit': 核对码
    """


def getFakeID(address=None, birthday=None, sex=None):
    # 生成一个虚假但是满足核对码的身份证
    # 参数可选，例如：地址为北京，生日为20000202，性别为男的虚假身份证号码
    return validator.fake_id(address=address, birthday=birthday, sex=sex)


print(getInfoByID("342225199809060518"))
