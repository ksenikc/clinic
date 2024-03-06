from django.shortcuts import render, redirect


def index(request):
    return render(request, 'clinic/index.html')


def price(request):
    data = {'posts': [{'title': 'Консультация', 'price1': 300, 'price2': 0},
                      {'title': 'Диагностическое вмешательство', 'price1': 1500, 'price2': 1500},
                      {'title': 'Имплантация эмали (лечение кариеса)', 'price1': 2500, 'price2': 2500},
                      {'title': 'Лечение поверхностного и начального кариеса', 'price1': 2800, 'price2': 3000},
                      {'title': 'Лечение поверхностного и начального кариеса', 'price1': 2800, 'price2': 3000},
                      {'title': 'Имплантация эмали (лечение кариеса)', 'price1': 2500, 'price2': 2500},
                      {'title': 'Диагностическое вмешательство', 'price1': 1500, 'price2': 1500},
                      {'title': 'Имплантация эмали (лечение кариеса)', 'price1': 2500, 'price2': 2500},
                      {'title': 'Консультация', 'price1': 300, 'price2': 0},
                      ]}
    return render(request, 'clinic/price.html', context=data)


def contacts(request):
    data = {'adress': 'г. Чебоксары, пр. М.Горького 18',
            'phone': '+7 (8352) 36-36-36 ',
            'email': 'denta21@mail.ru',
            'time': 'Понедельник - пятница 8:00 - 20:00, Суббота 8:00-14:00, Воскресенье - выходной'}
    return render(request, 'clinic/contacts.html',context=data )
