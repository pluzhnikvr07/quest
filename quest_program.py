while True: #Основной цикл для того, чтобы срабатывали концовки(break)
    invent = [] #инвентарь
    ne_vzyal_kristall = 0 #если не взял кристалл(9 выбор(отсылка к 3 выбору))
    x = 'посох с красным кристаллом' #если в инвентаре есть посох, то соответственный текст. если нету, то другой.(100 строка)
    umer = 0 #если умер(11 и 13 выборы)
    print('Здравствй, дорогой друг! В этой игре тебе придётся пройти испытания и вступить в бой с тёмными силами, чтобы спасти себя и других.') #Приветствие
    vibor1 = input('Ты гулял по лесу и увидел странное свечение. \n 1)Пойти посмотреть \n 2)Выйти из леса другой дорогой \n Ответ: ') #1 выбор
    if '1' in vibor1:
        vibor2 = input('Ты подошёл поближе и увидел портал. \n 1)Выйти из леса, рассказать родителям \n 2)Шагнуть в портал \n Ответ: ') #2 выбор
        if '1' in vibor2:
            print('Родители приняли тебя за сумасшедшего. Тебя положили в психбольницу, где ты и сошёл с ума окончательно. Начни игру заново')
            break #концовка после 2 выбора
        elif '2' in vibor2:
            vibor3 = input('Шагнув в портал ты оказался в волшебном лесу и сразу же наткнулся на красный кристалл. \n 1)Взять с собой \n 2)Не брать \n 3)Выкинуть его подальше от себя \n Ответ: ') #3 выбор
            if '3' in vibor3:
                print('Ты решил выкинуть кристалл подальше от себя, но как оказалось за тобой наблюдал хозяин леса.')
                print('Ему не понравилось, что ты наводишь свои порядки и заколдовал тебя в глыбу камня.')
                print('Начни игру заново.')
                break #концовка после 3 выбора
            elif '1' in vibor3:
                print('Оп! Теперь он у тебя в инвентаре!')
                invent.append('красный кристалл') #красный кристалл в инвентаре
            elif '2' in vibor3:
                print('Ты решил не брать кристалл. Ну и ладно...')
            print('Идя дальше ты встретил старушку, сидящую возле реки.')
            vibor4 = input('Ты решил заговорить с ней. \n 1) -Здравствуйте, не подскажите где я? \n 2) -Извините..? \n 3) -Слышь, старая! Где я? \n Ответ: ') #4 выбор
            if '3' in vibor4:
                print('Ты оказался слишком грубым! Иди поучись манерам!')
                print('Начни игру заново.')
                break #концовка после 4 выбора
            elif '1' in vibor4 or '2' in vibor4:
                print('В ответ последовала тишина')
                vibor5 = input(' 1) -Вы меня слышите? \n 2) -Эй! Я кому говорю?! \n 3) -Эй! \n Ответ: ') #5 выбор
                if '2' in vibor5:
                    print('Ты как со старшими разговариваешь?! Иди поучись манерам!')
                    print('Начни игру заново.')
                    break #концовка после 5 выбора
                elif '1' in vibor5 or '3' in vibor5:
                    print('Ответа всё так же не поcледовало.')
                    vibor6 = input(' 1)Потрести старушку за плечо \n 2)Пройти мимо(видимо не судьба) \n Ответ: ') #6 выбор
                    if '1' in vibor6:
                        print('Оказывается это оказалась не старушка, а монстр...')
                        print('Начни игру заново.')
                        break #концовка после 6 выбора
                    if '2' in vibor6:
                        print('Пройдя дальше ты увидел старца. Убедившись, что он настоящий ты решил задать ему несколько вопросов.')
                        while True: #позволяет задавать вопросы бесконечное количество раз, пока не будет введен нужный вариант(1) на 8 выборе
                            vibor7 = input(' 1)Где я оказался? \n 2)Кто вы? \n 3)Почему тогда я здесь? \n 4)Что мне делать? \n Ответ: ') #7 выбор(вопросы)
                            if '1' in vibor7: #1 вопрос
                                print('-Ты оказался в волшебном лесу.')
                                vibor8 = input('-Поможешь нам? \n 1)Да! \n 2)Я постараюсь \n 3)Я не совсем понимаю о чём Вы... \n Ответ: ') #8 выбор
                                if '1' in vibor8 or '2' in vibor8:
                                    break #выход из цикла while и продолжение сюжета
                            if '2' in vibor7: #2 вопрос
                                print('-Я - волшебник. В нашем мире полно зла и оно уже пробралось и в ваш мир. Если допустить хоть маленькую ошибку, то мы все погибнем!')
                                vibor8 = input('-Поможешь нам? \n 1)Да! \n 2)Я постараюсь \n 3)Я не совсем понимаю о чём Вы... \n Ответ: ') #8 выбор
                                if '1' in vibor8 or '2' in vibor8:
                                    break #выход из цикла while и продолжение сюжета
                            if '3' in vibor7: #3 вопрос
                                print('-Нам кажется, что ты отлично подходишь под роль того, кто нам нужен. В свою очередь, я и остальные добрые волшебники будем помогать тебе. Да и ты будь аккуратен, надейся только на себя!')
                                vibor8 = input('-Поможешь нам? \n 1)Да! \n 2)Я постараюсь \n 3)Я не совсем понимаю о чём Вы... \n Ответ: ') #8 выбор
                                if '1' in vibor8 or '2' in vibor8:
                                    break #выход из цикла while и продолжение сюжета
                            if '4' in vibor7: #4 вопрос
                                print('-Тебе нужно будет попасть туда, куда мы не можем из за наших нечеловеческих способностей и победить нашего главного врага')
                                vibor8 = input('-Поможешь нам? \n 1)Да! \n 2)Я постараюсь \n 3)Я не совсем понимаю о чём Вы... \n Ответ: ') #8 выбор
                                if '1' in vibor8 or '2' in vibor8:
                                    break #выход из цикла while и продолжение сюжета
                        while True: #цикл. защита от обманщиков.
                            vibor9 = input('-Я надеюсь ты взял красный кристалл? \n 1)Да \n 2)Нет.. \n Ответ: ') #9 выбор
                            if '2' in vibor9:
                                if invent:
                                    print('Ах ты ж обманщик... Отвечай честно!')
                                if not invent:
                                    print('-Что же ты наделал! Быстро беги обратно, если ещё не приключилось что нибудь плохое...')
                                    print('Прибежав к порталу ты увидел, что кристалла нет. Обернувшись назад ты увидел ту самую старушку. Оказывается она не так доброжелаткльна, как тебе казалось...')
                                    print('Начни игру заново.')
                                    ne_vzyal_kristall += 100 #не взял кристалл
                                    break #выход из цикла, так как не взял кристалл, а затем конец игры
                            elif '1' in vibor9:
                                if not invent:
                                    print('Ах ты ж обманщик... Отвечай честно!')
                                if invent:
                                    print('-Это очень хорошо! Дай мне его и я сделаю тебе посох.')
                                    break #выход из цикла, так как кристалл у нас
                        if ne_vzyal_kristall == 100:
                            break #концовка после 9 выбора(отсылка к 3 выбору)        
                        vibor10  = input(' 1)Отдать \n 2)Не отдавать \n Ответ: ') #10 выбор
                        if '1' in vibor10: #посох
                            print('-Вот и твой посох, удачи!')
                            invent.remove('красный кристалл') #красный кристалл больше не в инвентаре
                            invent.append('посох с красным кристаллом') #посох с красным кристаллом в инвентаре
                        if '2' in vibor10: #палка и верёвка
                            print('-Зря ты отказался... Ну ладно, держи палку и веревку, если передумаешь - сам сделаешь.')
                            invent.append('верёвка') #верёвка в инвентаре
                            invent.append('палка') #палка в инвентаре
                        print('Так или иначе, ты двинулся к темной пещере по наставлению старца.')
                        print('Подойдя к пещере ты ужаснулся её величиной. Но вспомнив что тебе говорил волшебник, двинулся дальше.')
                        print('Зайдя в пещере ты увидел огромного дракона, цвет кожи которого светился как красный кристалл.')
                        for i in invent: #проверяем есть ли посох в инвентаре
                            if i == x:
                                print('Так как твой кристалл ярко светился, а посох ты держал в руках, ведь в карман его не положишь, дракон обернулся на неожиданный источник света и заметил тебя.')
                                vibor11 = input('Теперь у тебя всего два варианта: \n 1)Бросить посох как копье \n 2)Воткнуть посох в землю и надеяться на чудо... \n Ответ: ') #11 выбор
                                if '1' in vibor11:
                                    print('Была ни была... Ты решил кинуть посох, но не учёл что кристал не был заточен...')
                                    print('Дракон посмеялся над тобой и опалил пламенем...')
                                    print('Начни игру заново.')
                                    umer += 100
                                    break #выход из цикла
                                if '2' in vibor11:
                                    print('Ты воткнул посох в землю, но... ничего не происходило...')
                                    print('Хаха! Ты что, в себя поверил?!')
                                    print('Да, это ведь волшебный лес, но если бы можно было сразиться с драконом волшебством - обошлись бы и без тебя... Ты как старца слушал?')
                                    print('Дракон посмеялся над тобой и опалил пламенем...')
                                    print('Начни игру заново.')
                                    umer += 100
                                    break #выход из цикла
                        if umer == 100:
                            break #концовка после 11 выбора(отсылка к 10 выбору)
                        print('Ты вошёл очень тихо, поэтому он тебя не заметил.')
                        vibor12 = input('И теперь ты задумался... \n 1)Сделать посох \n 2)Обойтись самому с помощью верёвки и палки \n Ответ: ')
                        if '1' in vibor12:
                            print('Ты быстро и тихо сделал посох.')
                            vibor13 = input('Теперь у тебя всего два варианта: \n 1)Бросить посох как копье \n 2)Воткнуть посох в землю и надеяться на чудо... \n Ответ: ') #13(11) выбор
                            if '1' in vibor11:
                                print('Была ни была... Ты решил кинуть посох, но не учёл что кристал не был заточен...')
                                print('Дракон посмеялся над тобой и опалил пламенем...')
                                print('Начни игру заново.')
                                umer += 100
                                break #выход из цикла
                            if '2' in vibor13:
                                print('Ты воткнул посох в землю, но... ничего не происходило...')
                                print('Хаха! Ты что, в себя поверил?!')
                                print('Да, это ведь волшебный лес, но если бы можно было сразиться с драконом волшебством - обошлись бы и без тебя... Ты как старца слушал?')
                                print('Дракон посмеялся над тобой и опалил пламенем...')
                                print('Начни игру заново.')
                                umer += 100
                                break #выход из цикла
                        if umer == 100:
                            break #концовка после 13 выбора(отсылка к 12 выбору)
                        if '2' in vibor12: #НАКОНЕЦ ТО КОНЕЦ!
                            print('Тихо подойдя к дракону, ты распустил верёвку и полностью обошёл его вокруг, затянув узел. От неожиданности дракон выпустил пламя изо рта.')
                            print('Подойдя к лицу дракона ты ухмыльнулся и воткнул в него палку')
                            print('Дракон скончался. Ты победил!')
                            print('Когда ты вышел из пещеры тебя ждала толпа волшебников и волшебниц, радостно тебя встретивших.')
                            print('Проведя до выхода они ещё раз поблагодарили тебя и разрешили забрать с собой красный кристалл!')
                            print('Поздравляю! Ты выиграл!')
                            break #Хорошая концовка игры!!!
    elif '2' in vibor1:
        print('Бежав из леса ты споткнулся о сучок и упал, сильно поранившись.')
        print('Начни игру заново.')
        break #концовка после 1 выбора
    
