import card_tool


while True:
    print('*' * 50)
    # 显示功能菜单
    card_tool.menu()

    # 用户输入功能选择
    func = input('请选择功能：')

    # 判断用户选择
    if func in ['1', '2', '3']:
        if func == '1':
            card_tool.new_card()
        if func == '2':
            card_tool.all_cards()
        if func == '3':
            card_tool.search_card()

    elif func == '0':
        break

    else:
        print('输入错误，请重新选择功能')
