card_list = []


# 显示功能菜单
def menu():
    print('欢迎进入名片系统 V1.0')
    print('1. 新建名片')
    print('2. 显示所有名片')
    print('3. 查找名片')
    print('')
    print('0. 退出系统')


# 新建名片
def new_card():
    # 用户输入信息
    print('【添加新名片】')
    print('请根据提示输入信息')
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    email = input('请输入邮箱：')
    card_list.append({'name': name, 'phone': phone, 'email': email})
    print('新名片添加成功！')
    print(card_list)


# 显示所有名片
def all_cards():
    if not card_list:
        print('没有任何名片！')
    else:
        print('{}\t\t{}\t\t{}'.format('姓名', '电话', '邮箱'))
        print('-' * 50)
        for i in card_list:
            print('{}\t\t\t{}\t\t\t{}'.format(i['name'], i['phone'], i['email']))
            print('-' * 50)


# 查询名片
def search_card():
    # 用户输入姓名进行名片查询
    print('【查找名片】')
    find_list = []
    # 判断系统中是否存在名片
    if not card_list:
        print('系统中没有任何名片')
    else:
        find_name = input('请输入要查找的姓名：')
        for i in card_list:
            if i['name'] == find_name:
                find_list.append(i)
        if not find_list:
            pass
            # 没有找到对应的名片
            # 1. 提示用户未找到
            print('没有找到【{}】的名片信息！'.format(find_name))

        else:
            # 查询到对应名片
            print('{}\t\t{}\t\t{}'.format('姓名', '电话', '邮箱'))
            for i in find_list:
                print('{}\t\t\t{}\t\t\t{}'.format(i['name'], i['phone'], i['email']))
                print('-' * 50)
