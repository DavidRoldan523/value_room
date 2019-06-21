import csv

def json_to_csv(name, json):
    with open(f"{name}.csv", mode='w', newline='', encoding='utf-8') as file:
        employee_writer = csv.writer(file, delimiter=',')
        columns = ['medium', 'page_name', 'page_id', 'date_since',
                   'date_until', 'date', 'post_id', 'post_name',
                   'comment_text', 'polarity', 'word', 'frequency']
        employee_writer.writerow(columns)
        for m in json:
            medium = m['medium']
            page_name = m['page_name']
            page_id = m['page_id']
            date_since = m['date_since']
            date_until = m['date_until']
            for results in json[0]['results']:
                date = results['date']
                for comment in results['comments']:
                    post_id = comment['post_id']
                    post_name = comment['post_name']
                    for post in comment['results']:
                        comment_text = post['comment_text']
                        polarity = post['polarity']
                        for frequency in results['frequency_words']:
                            word = frequency['word']
                            freq = frequency['frequency']
                            string = f"{medium}|{page_name}|{page_id}|{date_since}|{date_until}|"\
                                     f"{date}|"\
                                     f"{post_id}|{post_name}|{comment_text}|{polarity}|"\
                                     f"{word}|{freq}"
                            response = string.split('|')
                            employee_writer.writerow(response)

if __name__ == '__main__':
    JSON = [
    {
        "medium": "facebook",
        "page_name": "Tigo El Salvador",
        "page_id": "113387205347979",
        "date_since": "2019-06-20",
        "date_until": "2019-06-21",
        "results": [
            {
                "date": "2019-06-20",
                "comments": [
                    {
                        "post_id": "2440228605997149",
                        "post_name": "¡GANATE 1 de 7 camisas originales de La Selecta! 🇸🇻 Nos enfrentamos ante los Reggae Boyz 🇯🇲 que buscan la revancha del último partido y nosotros la VICTORIA. \n\n▶ Comentá tu pronóstico del encuentro junto a la frase “Viví la emoción del fútbol con Tigo” para participar. ¡Los 7 ganadores serán elegidos al azar el día Viernes 21 de Junio a mediodía!",
                        "results": [
                            {
                                "comment_text": "yo lo que quiero es un plan de telefono",
                                "polarity": 0.16360041539574613
                            },
                            {
                                "comment_text": "Bueno señores mentirosos de tigo, dado el caso que no me han querido resolver un problema relacionado a mi línea de celular, comenzaré a hacer denuncias públicas ya que no hay voluntad para resolver la situación, les brinde el número de gestión que me dieron hace más de una semana y aun no me resuelven, háganse responsables así como cuando querían que yo renovará contrato me llamaba hasta 15 veces al día, pero mágicamente cuando son ustedes los que violan sus propios términos y condiciones como todo cobarde se hacen los locos, tomaré todas las acciones necesarias para cancelar el contrato sin que me carguen alguna clase de penalidad, y sus representantes de atención al cliente son igual de descarados y no le resuelven nada a uno, ya no sigan engañando a la gente",
                                "polarity": 0.00007876572407735612
                            },
                            {
                                "comment_text": "Gana la Selecta, El Salvador 2 - 0 Jamaica\n\"Viví la emoción del fútbol con Tigo\" 💙\n\nEspero ganar una linda camisa de la selección 🇸🇻 para lucirla orgullosamente gracias a los mejores Tigo El Salvador 👑🤩\n\nMira mi amor y suegrita Nicolás Villanueva Hernández Ana Maria Hernandez Godinez participen 😘 gracias a Tigo💙",
                                "polarity": 0.2044666485785637
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbonConTigo #TigoElSalvador gana la selecta 1 a 0 #VamosSelecta yo quiero mi camisa original! Gracias a #TigoElSalvador  👏🤗",
                                "polarity": 0.3317533583702045
                            },
                            {
                                "comment_text": "El salvador 2-1Jamaica Quiero esa playera De la selecta revisen mi muro de facebook subo reseñas futboleras de mi.selecta y otros me la merezco",
                                "polarity": 0.2002028507109609
                            },
                            {
                                "comment_text": "Creo que un 2-1 a favor de EL SALVADOR tenemos que ganar o ganar sino nos quedamos afuera!!!",
                                "polarity": 0.19341509785981859
                            },
                            {
                                "comment_text": "Aquí esperando mi jubilación solo para que tigo me responda desde ayer sigo esperando",
                                "polarity": 0.10695310188253693
                            },
                            {
                                "comment_text": "#ViviLaEmocionConTigo y a ganar se a dicho mi selecta\nGana 1 @ 0 jamaica",
                                "polarity": 0.032755298047529545
                            },
                            {
                                "comment_text": "Gana 2 a 1 El Salvador,Vivi la emoción de la copa oro con #Tigo",
                                "polarity": 0.562294462569685
                            },
                            {
                                "comment_text": "Apoyando a la selecta siempre orgulloso de nuestra azul y blanco y para que disfrutes más este partidazo \"viví la emisión del fútbol con Tigo\" ARRIBA CON  LA SELECCIÓN SALVADOREÑA",
                                "polarity": 0.8031717389250531
                            },
                            {
                                "comment_text": "Señores de Tigo tras que dan un mal servicio de cable ahora todos los días no tenemos red móvil",
                                "polarity": 0.01718551988379159
                            },
                            {
                                "comment_text": "Viva la emoción del football con Togo. El salv. 3 Jamaica 1",
                                "polarity": 0.04196397042590281
                            },
                            {
                                "comment_text": "Vivamos juntos el fútbol con Tigo que mi selecta gana a  Jamaica 2 a 0  a ganarme la camiseta de mi gran selección",
                                "polarity": 0.035958511672491554
                            },
                            {
                                "comment_text": "Nunca me e ganado nada en mi vida,  ni siquiera un vergazo. \n\nPero yo presiento que gana la selecta 2 - 1 a Jamaica y siento que esa camisita es mía a gracias a TIGO PAPÁ",
                                "polarity": 0.001696689525967103
                            },
                            {
                                "comment_text": "Pierde  2  a  1 la selecta saben xq estos sipotes an ganado amistosos pero ya peleando puntos no la asen fíjate q este de los Cobos no llamo a Joaquín rrivas buen jugador",
                                "polarity": 0.07083549893513945
                            },
                            {
                                "comment_text": "Vive la emoción del fútbol con TIGO 💙, mañana gana la azulita de mi corazón 2 a 1 contra los jamaiquinos.\nArriba Cuscatlecos 💙💙💙💙🤞",
                                "polarity": 0.8488159455068672
                            },
                            {
                                "comment_text": "Vivamos juntos el futbol con Tigo. El Salvador gana 2 x 1 a Jamaica. Con todo Selecta... Arriba el Salvador..",
                                "polarity": 0.16202494594663513
                            },
                            {
                                "comment_text": "Que precio tienen los Nokia? Vi uno en 150 pero no las características me las pueden brindar por favor",
                                "polarity": 0.0019931763245467885
                            },
                            {
                                "comment_text": "Mi pronostico es un 2-1 a favor de nuestra selección esperemos que la selecta den lo mejor de ellos en ese partido #ViviLaEmocionDelFútbolConTigo",
                                "polarity": 0.37122695172579645
                            },
                            {
                                "comment_text": "#viviLaEmocionDelFutbolConTigo nuestra SELECTA  va ganar a Jamaica 2 - 1",
                                "polarity": 0.07710629746176471
                            },
                            {
                                "comment_text": "Vamos mi selecta juntos apoyemos con coraje y valentía muchachos y con tigo me puedo ganar la camiseta un partido muy apretado El Salvador 1-1jamaica",
                                "polarity": 0.04281606159342754
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1  #VIVILAEMOCIONDELFUTBOLCONTIGO vamos selecta vamos con todo a ganar",
                                "polarity": 0.08510815725219445
                            },
                            {
                                "comment_text": "Ganaremos el salvador 2 Jamaica 1 \"Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "'\" Vivi la emoción del fútbol con Tigo \"\" El Salvador 3 Jamaica 1......Vamos selecta .....El que no se siente orgulloso de su país y de su selección ni el sabe donde esta parado en las buenas y las mala selecta...Nací salvadoreño y moriré orgullo de a ver nacido en este hermoso país.....",
                                "polarity": 0.23464577313152465
                            },
                            {
                                "comment_text": "Vamos a ganar dos la selecta y uno jamaica y no lo vamos a perder ni un segundó del partido solo por tigo la señal perfecta de los salvadoreños",
                                "polarity": 0.05476674276024653
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFútbolConTigo. Nuestra Seleccion Salvadoreña gana 2-0 a Jamaica.",
                                "polarity": 0.08165596274947491
                            },
                            {
                                "comment_text": "Vivamos juntos la emocion con tigo ganamos 2- 1 arriva el salvador!!",
                                "polarity": 0.840076950902569
                            },
                            {
                                "comment_text": "Vivamos todos la emocion del futbol con tigo la selecta gana🇸🇻2  A  1🇯🇲 y yo me ganare una linda camisa de mi selecta💙🤗",
                                "polarity": 0.6791877139053017
                            },
                            {
                                "comment_text": "Definitiva rl futbo es una pasion mueve el corazon de cafs salvadoreño cuando juega la selecto por eso yo vivo la pasion y la emocion  del futbol junto a TIGO!!! Ganamos  2 a 1.... ademas gano mi camiseta de la selecta...",
                                "polarity": 0.7893599971730737
                            },
                            {
                                "comment_text": "Todos juntos apoyemos a nuestra selecta gana el salvador 3 a 1 jamaiquitos arriba mi qerido el salvador",
                                "polarity": 0.6650353193410978
                            },
                            {
                                "comment_text": "El salvador 2 vs Jamaica 0 #ViviLaEmocionDelFutboolConTigo gracias",
                                "polarity": 0.021766019168561475
                            },
                            {
                                "comment_text": "Gana la selecta cuscatleca el salvador 2 jamaica 0 juntos apoyemos a nuestra muchachos y fe que vamos a ganar",
                                "polarity": 0.10792937550435933
                            },
                            {
                                "comment_text": "El salvador 2 jamaica 1 vobo la emocion de futbol con tigo. Quiero una linda camisa original de el salvador.",
                                "polarity": 0.0498533833732064
                            },
                            {
                                "comment_text": "1 a 0 gana El Salvador\n#vivilaemociondelfutbolcontigo",
                                "polarity": 0.17079037377559783
                            },
                            {
                                "comment_text": "#vivílaemociondelfutbolcontigo.....el Salvador 2 Jamaica 1.....primero Dios ganemos y gracias a tigo esperamos ganar la hermosa playera.",
                                "polarity": 0.006141316749854071
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo El Salvador 🇸🇻 1-1 Jamaica 🇯🇲 aunque quisiera que ganará este creo que será el resultado \nEspero ganar 💪",
                                "polarity": 0.018835875905060653
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFútbolConTigo. El Salvador gana 2-1 a Jamaica.",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1 VIVILA EMOCION DEL FULTBOL CON TIGO Vamos selección de El salvador con todo a ganar 🇸🇻🏆🥇",
                                "polarity": 0.29941180085895797
                            },
                            {
                                "comment_text": "COMO SALVADOREÑO QUIERO MI AZUL, Y PRIMERO DIOS GANAREMOS,SA 2, Jamaica 1, y como cliente de la compañía Tigo, pasen mi camisetas azul, gracias.",
                                "polarity": 0.026294672938311836
                            },
                            {
                                "comment_text": "El Salvador 🇸🇻 1 - 0 🇯🇲 Jamaica. \nVivi La Emocion Del futbol Con Tigo 🤙🏾 La mejor Red Del Mundo 🤙🏾. A Darle Con Todo Mi Azul Y Blanco 🤙🏾🇸🇻 Quiero Esa Camisa Para Apoyar A Todo Lo Que Da Mi Corazon A Mi Seleccion 🇸🇻💙",
                                "polarity": 0.18850686215193152
                            },
                            {
                                "comment_text": "El salvador 1 jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Gana la selecta 2 a 1 #vivilaemociondelfutbolcontigo espero ganarme un bonita camisa",
                                "polarity": 0.3887057191855768
                            },
                            {
                                "comment_text": "# viví la emoción con Tigo  el salvador 2 Jamaica 0 ganaremos y siempre poniendo el salvador en alto  con Tigo ganaremos",
                                "polarity": 0.18338096869646436
                            },
                            {
                                "comment_text": "El salvador 1 Jamaica 2",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo\nArriba Con La Selección\nEl Salvador 2 Jamaica 2",
                                "polarity": 0.08789397620216392
                            },
                            {
                                "comment_text": "Mi selecta 2 jamaica 1. Vivi la emosion del dutbol con Tigo.",
                                "polarity": 0.357059969218055
                            },
                            {
                                "comment_text": "Jamaica 4 - El salvador 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo💙\nGana la selecta 1-0 🇸🇻💙\nYo Quiero Mi Camisa Gracias A Tigo La Mejor Compañía Del Salvador 💙🇸🇻",
                                "polarity": 0.2069291515323948
                            },
                            {
                                "comment_text": "\"Viví la emoción de fútbol con Tigo\"\nEsa 1\nJamaica 0\n#lacamisetaparapapá #tavoyanacio #el4todelamanada",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El salvador 0 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Ojalá primero Dios que vamos a ganar OK  arriba la selecta  Bamos  a ganar  OK",
                                "polarity": 0.3690410315554919
                            },
                            {
                                "comment_text": "Viví la emoción del futbol con Tigo yo creo que 2-1 van a quedar a favor de EL SALVADOR",
                                "polarity": 0.32597390733817927
                            },
                            {
                                "comment_text": "2 - 1 gana Jamaica. #vivilaemociondelfutbolcontigo",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "Gana la selecta el salvador 1  Jamaica 0\n``VIVI  LA EMOCIÓN DEL FÚTBOL CON TIGO '' '\nEspero ganar una linda camiss de la selección gracias a Tigo",
                                "polarity": 0.24859151246651998
                            },
                            {
                                "comment_text": "A ganar #selecta 2 - 0 con el pajaro picon picon \"vivi la emocion del futbol con #TIGO \"",
                                "polarity": 0.073253839543617
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 2\n\"Viví la emoción del fútbol con Tigo\"\n\nQuiero ganarme la camisola de la azul y blanco para estar preparado para el partido contra Honduras.",
                                "polarity": 0.47489518402792835
                            },
                            {
                                "comment_text": "El salvador 2-1 Jamaica, \"viví la emoción del fútbol con tigo\" espero poder ganarme la camiseta de la selecta para apoyarla en lo que resta de la copa oro.",
                                "polarity": 0.03871947475864094
                            },
                            {
                                "comment_text": "vamos mi selecta !!! Gana mi SelectaEl Salvador 2- 1 Jamaica ¡Viví la emoción del fútbol con Tigo! 💙💙 yo quiero ganar mi camisa de la selecta 💪🏻💪🏻💙💙💙🙆🏼\u200d♀️",
                                "polarity": 0.17577157889937134
                            },
                            {
                                "comment_text": "El Salvador 1-1Jamaica",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "El salvador 1 Jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Vivi la emocion del futbol contigo. Gana el salvador 1-0 a jamaica",
                                "polarity": 0.07664014779053328
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1 vamos selecta siempre apoyándote 😎😎😎🏆🏆🏆⚽⚽⚽🔷🔷🔷🔷◻️◻️🔵🔵⬜⬜⚪🔵",
                                "polarity": 0.25388037783355827
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 0\nJamaica 2",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "POR  UN PINCHE JUEGO  GANADO  YA  SON BUENOS  NOOOOO",
                                "polarity": 0.19443315710789041
                            },
                            {
                                "comment_text": "Siempre con la selecta Cuscatleca de todas es la mamá 2-1 gana la selecta, \"Viví la emisión del fútbol con Tigo\"",
                                "polarity": 0.4934440630627125
                            },
                            {
                                "comment_text": "El salvador 3-1 jamaica",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Selecta 2 jamaica 1 #ViviLaEmocionDelFutbolConTigo",
                                "polarity": 0.06305387452576648
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo y mira como gana la selecta cuscatleca con un 2 a 1 .arriba con la selección ...",
                                "polarity": 0.6820300180308599
                            },
                            {
                                "comment_text": "Mejor paguen las multas por maltrato",
                                "polarity": 0.0017299941434617636
                            },
                            {
                                "comment_text": "Le ganaremos a Jamaica  2-0 y serems nosotros lo que bailaremos  reggae con Tigo El Salvador",
                                "polarity": 0.02957063743876676
                            },
                            {
                                "comment_text": "Juntos Apoyémos A LA SELECTA.  SELECTA 2 Jamaica 🇯🇲 0",
                                "polarity": 0.20219407736787684
                            },
                            {
                                "comment_text": "El Salvador 1 Jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El Salvador 1 - 0 Jamaica, \"Viví la emoción del fútbol con Tigo\" (me avisan para ir la a recoger 😁😁😁) la selecta campeona de la copa oro 2019 SIIIIIIIIIIIIUUUUUU!!!!",
                                "polarity": 0.0916890802399706
                            },
                            {
                                "comment_text": "el salvador 0 Jamaica 2",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Si juega Bonilla Alas y el Ruso Flores perdemos 3 a 1",
                                "polarity": 0.09128083958920334
                            },
                            {
                                "comment_text": "El salvador 2 jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo\" gana la selecta 1 a 0 a Jamaica",
                                "polarity": 0.19437997584977015
                            },
                            {
                                "comment_text": "El Salvador 3\nJamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Gana. Jamaica 3 a 1",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "El Salvador 1 jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "3x2 gana El Saldor y viva el fufbol con tigo",
                                "polarity": 0.2514848686869602
                            },
                            {
                                "comment_text": "El salvador 2 jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Gana la selecta 🇸🇻 1-0 a Jamaica 🇯🇲",
                                "polarity": 0.04070392193535307
                            },
                            {
                                "comment_text": "Gana mi selecta 2 a 1 a Jamaica.\n#vivelaemosiondelfutbocontigo",
                                "polarity": 0.04070392193535307
                            },
                            {
                                "comment_text": "3 a 1 ganando Jamaica",
                                "polarity": 0.0237078583360768
                            },
                            {
                                "comment_text": "El salvador 2 jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "2a1gana el Salvador y ni modo a verlo con la señal de tigo",
                                "polarity": 0.16313532009210208
                            },
                            {
                                "comment_text": "El Salvador 1 vs Jamaica 1\n#ViviLaEmocionDelFutbolConTigo\n#MiAzulita",
                                "polarity": 0.021996919189838076
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo \"\nEl Salvador 1\nJamaica 3\nNos tocará sufrir pero como conocedor creo que ese será el marcador",
                                "polarity": 0.5527472849902962
                            },
                            {
                                "comment_text": "El Salvador 2\nJamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "2X1 a favor de El Salvador",
                                "polarity": 0.16324178421682026
                            },
                            {
                                "comment_text": "Con mucho dolor perdemos 2 a 1 😭😭😭😭😭😭\n\n! 🇸🇻  “Viví la emoción del fútbol con Tigo” espero no estar equivocado",
                                "polarity": 0.2642338460364665
                            },
                            {
                                "comment_text": "Jamaica 1 - 2 SV \"Vive la emocion del futbol con Tigo\"",
                                "polarity": 0.028847593758101066
                            },
                            {
                                "comment_text": "#vivi la emocion del fufbol con tigo gala la selecta 2 a      0 a jamaica",
                                "polarity": 0.3135140857146415
                            },
                            {
                                "comment_text": "El salvador 2 jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 1 jaimaca 1",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "El salvador 2 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Teléfonos prepago menos de 70 nesecito saber",
                                "polarity": 0.01872378621946301
                            },
                            {
                                "comment_text": "El Salvador 🇸🇻 1 y Jamaica 🇯🇲 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 3  jamaica 0 vibela emosion del futbol contigo la mejor red",
                                "polarity": 0.30050686074876815
                            },
                            {
                                "comment_text": "JAMAICA 2 EL SALVADOR 2",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "La Selecta! 🇸🇻 2-1 Los Reggae Boyz 🇯🇲\n\n▶ “Viví la emoción del fútbol con Tigo” 😎",
                                "polarity": 0.6122002697950322
                            },
                            {
                                "comment_text": "Jamaica 2. El Salvador 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "EL SALVADOR 2 JAMAICA 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "2a 1 ganando la mejor de la mejor mi selecta mi orgullo mi pasión el futbol ⚽⚽⚽",
                                "polarity": 0.8513073350656933
                            },
                            {
                                "comment_text": "El  Salvador 1 Jamaica 0 y nos metemos a cuartos de final, y lo disfrutamos y ''Viví la emoción del fútbol con Tigo''",
                                "polarity": 0.38074206293991714
                            },
                            {
                                "comment_text": "!!Vivo la emoción de fútbol con Tigo!!\n2 El Salvador\n1 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "El salvador 1 - 0 Jamaica",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Vivamos junto él fútbol con Tigo,gana la selecta 2-1",
                                "polarity": 0.4617204978407268
                            },
                            {
                                "comment_text": "Esta.Empresa Tigo Solo Son Promesas Que Van Regalar  Y No Cumplem",
                                "polarity": 0.05814858649935726
                            },
                            {
                                "comment_text": "Salvador 2 jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Gana la selecta 2-1 a jamaica.",
                                "polarity": 0.04070392193535307
                            },
                            {
                                "comment_text": "El salvador 2 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "3 El Salvador Jamaica 2 viví la emoción del fútbol con tigo",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Vivi la emocion del futbol con Tigo celebrando la victoria de La Selecta 2 - Jamaica 0 ⚽Orgullosos de La Selecta Siempre 🇸🇻",
                                "polarity": 0.3707855761851098
                            },
                            {
                                "comment_text": "Selecta cuscatleca 1 Jamaica 1",
                                "polarity": 0.06305387452576648
                            },
                            {
                                "comment_text": "El salvador 3 a 2",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "El Salvador 1-0 Jamaica",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo\nLa Selecta gana 2-1",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "2 salvador 1 jamaica",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 2 - 1 Jamaica",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo, gana el Salvador 1-0 A el fresco de Jamaica jajajajaja",
                                "polarity": 0.153268762785238
                            },
                            {
                                "comment_text": "Se vale soñar hoy los van agarrar Averga🤣",
                                "polarity": 0.5273539089817771
                            },
                            {
                                "comment_text": "Vive la emoción del fútbol ⚽ con tigo🇸🇻🇸🇻🇸🇻🇸🇻 empate 1 a 1 el salvador vs Jamaica 🇯🇲",
                                "polarity": 0.06411045818822235
                            },
                            {
                                "comment_text": "Viva la emoción del fútbol con Tigo! Esa 2 Jamaica 1",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "#viviLaEmocionDelFutbolConTigo 1 a 1 queda la selecta",
                                "polarity": 0.6588330284801807
                            },
                            {
                                "comment_text": "Gana el salvador  2 a 0",
                                "polarity": 0.17079037377559783
                            },
                            {
                                "comment_text": "Él salvador.  (2)\n\nJamaica.      (1)",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Jamaica 3 - El Salvador 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Jamaica 2 el salvador 0 😁😁",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador gana 2 a 1 a Jamaica",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "2 ha 1 gana jamaica",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "1-1 sacamos un buen resultado contra el más difícil del grupo! \"Viví la emoción del fútbol con Tigo\".",
                                "polarity": 0.7581576878188031
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” este día empatamos 2 a 2 con Jamaica",
                                "polarity": 0.04489133591838736
                            },
                            {
                                "comment_text": "#Vivilaemocióndelfútbolcontigo  empate de la selecta 2 - 2 contra jamaica!",
                                "polarity": 0.03690557623208211
                            },
                            {
                                "comment_text": "Biba la emisión con Tigo y aganar primero Dios  asulita 3 Jamaica 2",
                                "polarity": 0.16698440358724084
                            },
                            {
                                "comment_text": "Jamaica 1-0 el Salvador",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Vive la emocion con tigo. la selecta gana 2 a 1 ante jamaica",
                                "polarity": 0.09515380863786208
                            },
                            {
                                "comment_text": "2 a 1 ganando El Salvador",
                                "polarity": 0.35957771274046785
                            },
                            {
                                "comment_text": "#Vivilaemociondelfutbocontigo. La Selecta gana 2-0",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "Vive la emocion con tigo gana el salvador 2 a 1",
                                "polarity": 0.40618826846512673
                            },
                            {
                                "comment_text": "El salvador 2 jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "1 a1 vive la emoción del fútbol con TIGO quiero la camisa de mi selecta",
                                "polarity": 0.489646778512764
                            },
                            {
                                "comment_text": "Bueno yo digo que \nEl Salvador 1\nJamaica 1\n#Tigo Viví la emoción del Futbol !!",
                                "polarity": 0.17052115204090598
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” el partido terminara empate El Salvador 2 Jamaica 2, gracias Tigo por tan excelentes promociones!!",
                                "polarity": 0.08747185150446281
                            },
                            {
                                "comment_text": "Mmmmmmmm Kennia Quintanilla yo pienso que quedamos 1 a 1 gracias a TIGO EL SALVADOR!",
                                "polarity": 0.05796507292560565
                            },
                            {
                                "comment_text": "\"Vivamos la emoción del fútbol con tigo\" 🔥, no hay que dudar el Salvador dara lo mejor en si🔥,y esto quedara 2-0🔥😎a Favor de El Salvador 🇸🇻",
                                "polarity": 0.7546974884675911
                            },
                            {
                                "comment_text": "\"Viva La Emocion Del Futbol ConTigo\"📺🔵⚪🔵 El salvador 1 - Jamaica 0",
                                "polarity": 0.20423526280206233
                            },
                            {
                                "comment_text": "Viví la emisión de fútbol con tigo .el salvador 2 jamaica 1",
                                "polarity": 0.05840987762137102
                            },
                            {
                                "comment_text": "Gana la Selecta 1 a 0 viví la emoción del fútbol con tigo ⚽⚽🇸🇻💙💙💙 gracias a #TigoElSalvador",
                                "polarity": 0.5667776550864073
                            },
                            {
                                "comment_text": "Será un partido difícil pero El Salvador 2 Jamaica 1, a “Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.20660583434402643
                            },
                            {
                                "comment_text": "⚽️⚽️⚽️ VIVI LA EMOCIÓN DE EL FUTBOL CON TIGO⚽️⚽️ 3 A 1 GANA JAMAICA pero siempre soy azul y blanco.......",
                                "polarity": 0.5379026080174388
                            },
                            {
                                "comment_text": "Gana la Selecta, El Salvador 1 - 0 Jamaica\n\"Viví la emoción del fútbol con Tigo El Salvador\" 💙\n\nEspero ganar una linda camisa de la selección 🇸🇻\n\nMi amor Letty García 😘",
                                "polarity": 0.1255862299113745
                            },
                            {
                                "comment_text": "El Salvador 1🇸🇻\nJamaica 0 \n\"VIVI LA EMOCION DEL FULBOL CON TIGO\"\nla mejor señal para disfrutarlo",
                                "polarity": 0.7649571908172345
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con nuestra selecta ganara 3-2  con tigo conectados",
                                "polarity": 0.5018457450555388
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo y disfrutemos de la victoria de la Selecta🇸🇻 ante Jamaica🇯🇲. Mi marcador es 2-1 a favor de El Salvador. 😍💙",
                                "polarity": 0.41578995252942125
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo el Salvador gana la selecta 1 a 0 a Jamaica",
                                "polarity": 0.12257950045083618
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo\" y vamos a creer en la selecta, El Salvador 2 - 1 jamaica",
                                "polarity": 0.23903164813849934
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” pues esperamos que se gane por la mínima a Jamaica",
                                "polarity": 0.09140271082372237
                            },
                            {
                                "comment_text": "La Selecta! 🇸🇻 1 los Reggae Boyz 🇯🇲 1 quedamos en empate “Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.44370111449814276
                            },
                            {
                                "comment_text": "El Salvador 2\nJamaica 1\nVivi la emocion del futbol con Tigo\nGracias por Participar y ganarme una Camiseta de La Selecta.",
                                "polarity": 0.0938296889670609
                            },
                            {
                                "comment_text": "⚽El Salvador 2 Jamaica⚽ 1 viví la emoción del fútbol vamos con todo selecta con todo a ganar 🇳🇮🏆",
                                "polarity": 0.7860510593466592
                            },
                            {
                                "comment_text": "Vive la emocion del futbol con tigo\nEl Salvador 2 jamiaca 1",
                                "polarity": 0.6622205294645258
                            },
                            {
                                "comment_text": "El Salvador 2 \nJamaica 1\n\"Viví la emocion del fútbol con Tgo\"\nQuiero una camisa de la Azul y Blanco👍👍👍",
                                "polarity": 0.14064239251381644
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” \n🇯🇲2-0🇸🇻 \nQuiero mi camisa de la Selecta!!! ❤",
                                "polarity": 0.5936354032834726
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo\" gana nuestra Selección 2 Jamaica 1",
                                "polarity": 0.21252882306709167
                            },
                            {
                                "comment_text": "El salvador 1 Jamaica  1 \"viví la emoción del fútbol  con  tigo\" quiero la camiseta  de mi selecta .gracias  X está oportunidad.",
                                "polarity": 0.0778795126177542
                            },
                            {
                                "comment_text": "El Salvador 2=1 Jamaica. Y vivi la emocion del futbol con tigo.  #tigoelsalvador #elsalvador #goool #selecta #miselecta",
                                "polarity": 0.16318185107058847
                            },
                            {
                                "comment_text": "VIVÍ LA EMOCIÓN DEL FÚTBOL CON TIGO... GANA JAMAICA 3 A 1 A EL SALVADOR",
                                "polarity": 0.07754996261921546
                            },
                            {
                                "comment_text": "\"Vivi la Emoción del Fubtol con Tigo\" \nEl Salvador 1 - 1 Jamaica",
                                "polarity": 0.1644605099535312
                            },
                            {
                                "comment_text": "Vamos con la emoción del footbol con tigo vamos con todo Jamaica 2 El Salvador 1",
                                "polarity": 0.5657132805658409
                            },
                            {
                                "comment_text": "\"Vivi la emocion del fútbol con Tigo el mejor\" esa 1 jamaica 1",
                                "polarity": 0.24884220553032804
                            },
                            {
                                "comment_text": "“⚽️⚽️⚽️VIVÍ LA EMOCIÓN DEL FÚTBOL COL TIGO⚽️⚽️\nGana la la selecta \nEl Salvador 🇸🇻 2-1 🇯🇲 Jamaica",
                                "polarity": 0.09105171655419826
                            },
                            {
                                "comment_text": "#LaSelecta ganara 2 por 1 a los #RegaeBoys . ¡Vivi la emocion del futbol con TIGO!",
                                "polarity": 0.32396192582517186
                            },
                            {
                                "comment_text": "El Salvador ganara 2 a 0 y se repetirá el marcador en San salvador 🇸🇻🇸🇻🇸🇻Viví la emoción del fútbol con tigo",
                                "polarity": 0.296157180463747
                            },
                            {
                                "comment_text": "Mi pronóstico es 2 - 1 a favor de la Selecta y “Viví la emoción del fútbol con Tigo”.",
                                "polarity": 0.6280254913163398
                            },
                            {
                                "comment_text": "Viví  la emoción contigo El Salvador 2 Jamaica 1",
                                "polarity": 0.08147179530694572
                            },
                            {
                                "comment_text": "Gana la selecta  2 El Salvador y 2 Jamaica #vivilaemociondelfutbolcontigo espero ganarme un bonita camisa",
                                "polarity": 0.06252455638850477
                            },
                            {
                                "comment_text": "Gana Jamaica 2 a 1 a El Salvador, Viví la emoción del fútbol con Tigo",
                                "polarity": 0.07754996261921546
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo 🔵 \nEl Salvador 🇸🇻 1 - Jamaica 🇯🇲 0.\nVamos con todo #CopaOro #SelectaPorSiempre #EnVivoConTigoHD",
                                "polarity": 0.1796304708565766
                            },
                            {
                                "comment_text": "Gana el salvador 3-2 \"viví la emoción de fútbol con tigo\"",
                                "polarity": 0.6062611039408947
                            },
                            {
                                "comment_text": "El salvador 🇸🇻 2-1 Jamaica 🇯🇲⚽⚽\nY por supuesto... \n “Viví la emoción del fútbol con Tigo” Talla M Gracias",
                                "polarity": 0.26230777683158335
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con TIGO.. La selecta 3 --  1   Jamaica",
                                "polarity": 0.17924868501587202
                            },
                            {
                                "comment_text": "\"Viví la emoción del futbol  con Tigo\" Gana Jamaica 3 a 0 de El Salvador",
                                "polarity": 0.14113862380791534
                            },
                            {
                                "comment_text": "\"\"Viví la emoción del football con tigo. El salvador 2 Jamaica 2.",
                                "polarity": 0.31143190216410754
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo el Salvado 1 Jamaica 0",
                                "polarity": 0.21581668569426057
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” le ganamos a Jamaica 2 a 1. El Salvador 2, Jamaica 1.",
                                "polarity": 0.08299291787182207
                            },
                            {
                                "comment_text": "Viví la emoción del Fútbol Con Tigo.\nESA 1-1 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "El Salvador 2-0 jamaica\n\"viva la emoción del fútbol con Togo,\"",
                                "polarity": 0.2189175760198807
                            },
                            {
                                "comment_text": "Todos apollar l celects. Con tigo vamos con todo gana l celecta 2a 1",
                                "polarity": 0.04623044884421841
                            },
                            {
                                "comment_text": "Victoria de 1 a 0 gana  la selecta, \"viví la emoción del fútbol con tigo\"",
                                "polarity": 0.6530054015895034
                            },
                            {
                                "comment_text": "El salvador 2\nJamaica 1 \n\"Vivi la emoción del fútbol con tigo\" \nGracias a Tigo me ganare esa hermosa camisa 🇸🇻🇸🇻",
                                "polarity": 0.2674634533935923
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con TIGO, vamos a empatar a 1 gol cada uno",
                                "polarity": 0.3986925119028395
                            },
                            {
                                "comment_text": "El salvador 2 vs jamaica 1 #vivilapasiondelfutbolcontigo",
                                "polarity": 0.020941285093970616
                            },
                            {
                                "comment_text": "\"Vivi la emocion del futbol con tigo. Selecta 1 Jamaica 2",
                                "polarity": 0.2722396855778531
                            },
                            {
                                "comment_text": "Jamaica 2, Esa 1 \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Vive la emoción con Tigo El Salvador 1 Jamaica 1",
                                "polarity": 0.084241760660154
                            },
                            {
                                "comment_text": "Gana la selecta 2 - 0 vs Jamaica. Viví la emoción del fútbol con Tigo.",
                                "polarity": 0.10470531089722022
                            },
                            {
                                "comment_text": "Pierde el salvador 2 a 0 ojala q no pero eso pienso.vivi la emocion del futbol con tigo",
                                "polarity": 0.5024830574776272
                            },
                            {
                                "comment_text": "Ey La Selecta 2 - 1 Jamaica \n\" Viví la emoción del fútbol con TIGO \"",
                                "polarity": 0.10167022553272559
                            },
                            {
                                "comment_text": "Gana la Selecta 2 a 1\nVIVI LA EMOCIÓN DEL FUTBOL CON TIGO. Espero acertar y ganar  😅😅😅",
                                "polarity": 0.40620417932000996
                            },
                            {
                                "comment_text": "“Vivi la emoción del fútbol con TIGO” \nJamaica 1 vs el salvador 1",
                                "polarity": 0.1727258732974894
                            },
                            {
                                "comment_text": "El Salvador gana 1 a 0 a Jamaica",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "Más de una hora esperando en la agencia tigo metro centro y nada que servicio más lentooooooooo",
                                "polarity": 0.09593916162017771
                            },
                            {
                                "comment_text": "Gana la selecta 2-1 quiero la camiseta de nuestro pulgarcito",
                                "polarity": 0.055268421991177506
                            },
                            {
                                "comment_text": "Gana el Salvador 2 a 1",
                                "polarity": 0.17079037377559783
                            },
                            {
                                "comment_text": "Vivamos juntos el fútbol con tigo, apoyando a mi selecta. Jamaica 3 El Salvador 1.",
                                "polarity": 0.12091078960958945
                            },
                            {
                                "comment_text": "2 a 1 gana la selecta...su nivel futbolistico ha aumentado",
                                "polarity": 0.5256120959668195
                            },
                            {
                                "comment_text": "Ganamos 2 a 1 a Jamaica",
                                "polarity": 0.04754951742015244
                            },
                            {
                                "comment_text": "Teléfonos prepago baratos nombres de modelos quiero uno",
                                "polarity": 0.04699245243890519
                            },
                            {
                                "comment_text": "Jamaica 2 el salvador 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 1 Jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Gana el salvador 1 0",
                                "polarity": 0.17079037377559783
                            },
                            {
                                "comment_text": "el salvador 2 jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Arriba la selección mi pronóstico es un 2 a 1 a favor de la selección #vivelaemociondelfutbolcon Tigo",
                                "polarity": 0.4856356419037335
                            },
                            {
                                "comment_text": "El Salvador 2 jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "1 a 1 nos clasificamos contra Honduras",
                                "polarity": 0.32370159689866274
                            },
                            {
                                "comment_text": "Gana Jamaica 2 a 1",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "El Salvador  1 Jamaica 🇯🇲 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Selecta 0-0 jamaica",
                                "polarity": 0.06305387452576648
                            },
                            {
                                "comment_text": "El salvador 1 jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Vivi la emoción del fútbol con tigo",
                                "polarity": 0.6622205294645258
                            },
                            {
                                "comment_text": "Viva la emoción con Tigo perdemos 2 aa 1",
                                "polarity": 0.3295280739156593
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 2 jamaica 1💪",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Él Salvador 2 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Viví la emoción del futbol con Tigo! Selecta 2 - 1 Reguee boys",
                                "polarity": 0.1503160422054096
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” y mi pronóstico es El Salvador 3 Jamaica 1",
                                "polarity": 0.2467653007516557
                            },
                            {
                                "comment_text": "El Salvador 2  Jamaica 1. \"Viví la emoción del fútbol con Tigo\". Espero ser uno de los ganadores 😊",
                                "polarity": 0.2041710776888818
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo \"  Vamosssss selectaaa ganamos 2 a 1 🇸🇻",
                                "polarity": 0.7933096857780808
                            },
                            {
                                "comment_text": "Él marcador selecta 2- Jamaica 1, \"Viví la emoción del fútbol con Tigo\".",
                                "polarity": 0.18879273748707798
                            },
                            {
                                "comment_text": "Jamaica 2\nEl Salvador 1\n\"Vivi la emocion del futbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” El Salvador 1 🇸🇻 Jamaica 1🇯🇲 selecta siempre con vos 🏆⚽",
                                "polarity": 0.3173234963450906
                            },
                            {
                                "comment_text": "Jamaica 2\nEl Salvador 2 \nViví la emoción del fútbol con tigo.",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "La Selecta  0~0  Jamaica\n\"Viví  la  emoción del fútbol  con  Tigo\"",
                                "polarity": 0.2722396855778531
                            },
                            {
                                "comment_text": "El Salvador 1-1 Jamaica\n\"Viví la emoción del fútbol con Tigo\",,💙 y pasa la selecta a siguiente fase💪",
                                "polarity": 0.2137831720202034
                            },
                            {
                                "comment_text": "El marcador será 🇸🇻 1- 0🇯🇲 \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.577165305534552
                            },
                            {
                                "comment_text": "2-1 gana mi selección 💙\n\nLa Selecta! 🇸🇻  “Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.6802028403903415
                            },
                            {
                                "comment_text": "¡Viví la emoción del fútbol con Tigo! gana el salvador 2 a 0",
                                "polarity": 0.44096695273878667
                            },
                            {
                                "comment_text": "El Salvador 2-1 Jamaica \nViví la emoción del futbol con Tigo\nMuchas gracias Tigo por la oportunidad!!",
                                "polarity": 0.27460743771904494
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con TIGO⚽️, Resultado del encuentro El Salvador 2-0 Jamaica\n#DaleSelecta👌🏼.",
                                "polarity": 0.17308675033055965
                            },
                            {
                                "comment_text": "El salvador 3 a 2 jamaica \"vivi la hemocion del futbol con Tigo\"",
                                "polarity": 0.34842636766887025
                            },
                            {
                                "comment_text": "Vivi la emoción del fútbol  contigo\nEl salvador 1 jamaica 0",
                                "polarity": 0.11861911766189666
                            },
                            {
                                "comment_text": "El Salvdor 2 - 1 Jamaica\n\"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol contigo gana el Salvador 2 aún A unos",
                                "polarity": 0.5098161426131054
                            },
                            {
                                "comment_text": "Vivi la emoción del fútbol con Tigo \nJamaica 2-1 El Salvador",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "#Vivi_La_Emocion_del_Futbol_con_Tigo. Jamaica 3, el Salvador 1",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Jamaica 2-1 El Salvador viví la emoción del fútbol con Tigo",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "⚽️⚽️⚽️Viví la emoción del fútbol con TIGO, ⚽️⚽️⚽️🇸🇻🇸🇻🇸🇻🏆🏆🏆\nEl Salvador 2 --- Jamaica 1",
                                "polarity": 0.09842898629363983
                            },
                            {
                                "comment_text": "GANA El SALVADOR 2 A 1 A JAMAICA PRIMERO DIOS LE VAYA BIEN A NUESTRA SELECCION\n\"VIVÍ LA EMOCION DEL FUTBOL CON TIGO\"\nGRACIAS TIGO X SUS SERVICIOS Y POR PONER ESTA CLASE DE REGALOS ESPERO SER 1 GANADOR",
                                "polarity": 0.21644944276191674
                            },
                            {
                                "comment_text": "El Salvador 1 - 0 Jamaica \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "#vivilaemociondelfutbolcontigo                 gana la selecta cuscatleca  2- 1 a Jamaica",
                                "polarity": 0.04070392193535307
                            },
                            {
                                "comment_text": "El Salvador 2  🇸🇻 vs Jamaica 1 🇯🇲 👍🏻 vivo la emoción del fútbol con TIGO",
                                "polarity": 0.10039274969457049
                            },
                            {
                                "comment_text": "Gana y vive la emocion con Tigo gana nuestra Selecta 2 a 0",
                                "polarity": 0.42918271578377354
                            },
                            {
                                "comment_text": "El salvador 2 Jamaica 1\n\"Vive la emoción del fútbol con tigo\"",
                                "polarity": 0.1948387844617593
                            },
                            {
                                "comment_text": "Gana 2 a 1 la selecta",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "\"viví la emoción del fútbol con tigo\"💙 gana el Salvador 1 a 0",
                                "polarity": 0.6062611039408947
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con TIGO\" 💙 gana El Salvador 2-1Jamaica #Selecta #Tigo ⚽",
                                "polarity": 0.5679269617171022
                            },
                            {
                                "comment_text": "El.salvador 1 jamaica 0 \nViva la emocion del futbol con tigo",
                                "polarity": 0.19445293170605912
                            },
                            {
                                "comment_text": "VIVI LA EMOCIÓN del FÚTBOL con Tigo. Jamaica 3 El Salvador 1",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Jamaica 3-1 El Salvador, \"Vivi la emocion del futbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El salvador 1 Jamaica 0.. vivi la emocion del fulbol con tigo",
                                "polarity": 0.5045838648661243
                            },
                            {
                                "comment_text": "El Salvador 1 - 2 Jamaica\n\"Viví la emoción del fútbol con Tigo\" el mejor cable del Mundo  💪",
                                "polarity": 0.2629805926159755
                            },
                            {
                                "comment_text": "El Salvador 2-0 Jamaica \"Vivi la emocion del fubtbol con Tigo\"",
                                "polarity": 0.07192900341882817
                            },
                            {
                                "comment_text": "El salvador 1 Jamica 2\n Viví la emoción del fútbol con Tigo",
                                "polarity": 0.6622205294645258
                            },
                            {
                                "comment_text": "\"Viví la emoción del Futbol con TIGO\"\nNuestra selecta gana:\n🇸🇻El Salvador 2 \nVs \n🇯🇲Jamaica 1 \n#TigoElSalavador",
                                "polarity": 0.6218720932613531
                            },
                            {
                                "comment_text": "Amor Alvaro Paz cuánto quedan? yo pienso que 1-0 \"viví la emoción del fútbol con tigo\". Gracias Tigo El Salvador :)",
                                "polarity": 0.07467283639899577
                            },
                            {
                                "comment_text": "# viví la emoción con tigo  el Salvador  2  Jamaica 1",
                                "polarity": 0.084241760660154
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo, Jamaica 1 El Salvador 2",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo el Salvador,  2 a 1gana la selecta.",
                                "polarity": 0.5519853330335734
                            },
                            {
                                "comment_text": "No cumplen 😅",
                                "polarity": 0.012864413801132927
                            },
                            {
                                "comment_text": "El salvador 1\nJamaica 1\n#ViviLaEmocionDelFutbolContigo",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "\"viví la emoción del fútbol con tigo\nJamaica 0  el salvador 0",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El Salvador 2 - 0 Jamaica. #vivilaemociondelfutbolcontigo",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 2  Jamaica     1\n\"Viví la emoción del fútbol Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Jamaica 3 El salvador 1 \"vivi la emocion del futbol con tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Gana Jamaica 3-1\n\"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.14113862380791534
                            },
                            {
                                "comment_text": "2 - 1 GANA LA SELECCIÓN DE EL SALVADOR \"VIVI LA EMOCIÓN DEL FÚTBOL CON TIGO\" 👌👌👌💙💙💙",
                                "polarity": 0.6407089360276046
                            },
                            {
                                "comment_text": "Viví la Emoción de Fútbol con Tigo 💙\nEl Salvador 1 Jamaica 1 ⚽",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "el salvador 0 -2 jsmaica \n``Vivi la emocion del futbol con Tigo \"",
                                "polarity": 0.7528382658281216
                            },
                            {
                                "comment_text": "Gana nuestro pulgarcito el salvador 2 Jamaica 1 vivimos la emocion del futbol contigo vamos contodo selecta",
                                "polarity": 0.32955798990847
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1 \nVivi La emoción del Fútbol   con tigo, ojala gane gracias a #Tigo 😎",
                                "polarity": 0.13773847131351213
                            },
                            {
                                "comment_text": "La Selecta 2 - 1 Jamaica \n\" Viví la emoción del fútbol con TIGO \"",
                                "polarity": 0.17924868501587202
                            },
                            {
                                "comment_text": "\"Viví la emocion del futbol con Tigo\" El salvador se impone ante Jamainca 2-1 el dia viernes... Le ponemos cartel de liquidado gracias a  Tigo El Salvador !!",
                                "polarity": 0.2768650626167209
                            },
                            {
                                "comment_text": "El salvador 1-1 Jamaica\n“Viví la emoción del fútbol con Tigo” ojalá gane la selecta!!",
                                "polarity": 0.1457307600908294
                            },
                            {
                                "comment_text": "#vivilaemocioncontigo El Salvador 1 Jamaica 2",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 2-1jamaica #ViviLaEmocionDelFutbolConTigo",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "#vivalaemciondelfutbolcontigo el Salvador 1 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El Salvador 1 Jamaica 1 #Vivilaemociondelfutbolcontigo.",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Vive la emocion con tigo  lastimosamente la selecta pierde  por 2 a 0⚽⚽⚽",
                                "polarity": 0.610690324075191
                            },
                            {
                                "comment_text": "#viviLaEmocionDelFUtbolConTigo EL SALVADOR 1 JAMAICA 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Gana La Selecta 2 a 1 a Jamaica,!! “Viví la emoción del fútbol con Tigo.",
                                "polarity": 0.19437997584977015
                            },
                            {
                                "comment_text": "“Vivi la emoción del fútbol con tigo” Pierde la selecta 🇸🇻 1-3 Jamaica 🇯🇲",
                                "polarity": 0.2555980299592541
                            },
                            {
                                "comment_text": "El Salvador 1 Jamaica 0\n\"\n“”Viví la emoción del fútbol con Tigo\"\n\nQuiero ganarme la camisa para estar preparado para el partido contra Honduras.",
                                "polarity": 0.11443273431737083
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo El Salvador 2-1 Jamaica",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "ESA 0 vs Jamaica 2\n“Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.1727258732974894
                            },
                            {
                                "comment_text": "#vivi- la - emoción- del- futbol- con-tigo. Disfrutando de la selecta al ganarle 2 a 1 a Jamaica",
                                "polarity": 0.20022808821006421
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo.\nGana El Salvador 2-1 Jamaica",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "Vive la emocion del futbol con tigo  Jamaica 2 El salvador 1",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Viva la emocion del futbol con tigo ESV 0 vs 1 jamaica",
                                "polarity": 0.10039274969457049
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo”\n\nLastimosamente perdemos, La Selecta 🇸🇻 0  Reggae Boyz 🇯🇲 2",
                                "polarity": 0.4286206712151605
                            },
                            {
                                "comment_text": "Vivamos juntos el fútbol con Tigo el salvador 1 Jamaica 2 arriba la seleccion",
                                "polarity": 0.17200874532368388
                            },
                            {
                                "comment_text": "Él salvador [1]\n\nJamaica     [0]\n\n#Vivilaemociondelfutbolcontigo.",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "1 el salvador ,0 Jamaica #vivilaemociondelfutbolcontigo",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "#vivalaemociondelfutbolconTigo \nEl Salvador 2 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo. El salvador 2 Jamaica 1.",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Empatamos 1-1 con jamaica \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.043477373734835276
                            },
                            {
                                "comment_text": "#vivilaemosiondelfutbolcontigo el Salvador 2 jamaica 0",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "#vivi la emoción del fútbol con tigo vamos el salvador 1 2 Jamaica",
                                "polarity": 0.2236066963208547
                            },
                            {
                                "comment_text": "El Salvador 1-2 Jamaica\n“Viví la emoción del fútbol con Tigo\" ojalá me equivoque...",
                                "polarity": 0.20278927451567647
                            },
                            {
                                "comment_text": "2 a 2 un empate nos tocará",
                                "polarity": 0.2999325272626015
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo\nEl Salvador 1 - 1 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "YO  NOOOOOOOO  NO SIRVEN",
                                "polarity": 0.049059203808031256
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo”  El Salvador 2 Jamaica 1",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Gana Jamaica 2-0. \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.14113862380791534
                            },
                            {
                                "comment_text": "El Salvador 1 Jamaica 0 #VIVI LA EMOCIÓN DEL FÚTBOL CON TIGO ¡¡ A rriba el Salvador!!",
                                "polarity": 0.08510097610978794
                            },
                            {
                                "comment_text": "\"Viví la emoción del Fútbol con Tigo\"\nEl salvador 1 Jamaica 1",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "\"viví la emoción del fútbol con tigo\" El salvador 1 Jamaica 0",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Gana mi selecta 2 a 1",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "2 ..  A 0 ganA mi selecta",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "\"viví la emoción del fútbol con Tigo\" El Salvador🇸🇻 1 Jamaica 🇯🇲1",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "#VivílaemocióndelfutbolconTigo el salvador 0-0 jamica",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "El Salvador 1 y Jamaica 0 \n\n“Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Recarga",
                                "polarity": 0.10233660170186633
                            },
                            {
                                "comment_text": "Seleta dos. Crasias",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "Muy buenas. Una apuesta 2.  A 1",
                                "polarity": 0.8345896513718698
                            },
                            {
                                "comment_text": "El salvador 🇳🇮 0 Vs Jamaica🇯🇲 0   \" Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.5473358778139401
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo!!! Jamaica 3 - 2 El Salvador",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Jamaica 2 El savaldor 1 con el dolor de mi alma pero es la realidad # Vivi la emoción del futból con Tigo El Salvador",
                                "polarity": 0.507100891638263
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con TIGO\"\nEl Salvador 0 - 4 Jamaica",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo\"\n\nEl Salvador 🇸🇻 1 - 0 🇯🇲 Jamaica",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "La Selecta 02 🇸🇻 Jamaica 01🇯🇲 “Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.2722396855778531
                            },
                            {
                                "comment_text": "\"Vivi la emocion del Futbol con Tigo\" El Salvador 2 - Jamaica 1..",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo ⚽⚽⚽\nEl Salvador 🇸🇻 2 - 1 🇯🇲 Jamaica !!!",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "El Salvador 3 Jamaica 2",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1\n\"Viví la emocion del fútbol con Tigo\"\nGracias Tigo!!",
                                "polarity": 0.21634326945605614
                            },
                            {
                                "comment_text": "EL SALVADOR 🇸🇻 1-3 🇯🇲 JAMAICA\n\"Viví la emocion del futbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo \" El Salvador 2 Jamaica 1 vamos selecta vos podes 🇸🇻🇸🇻",
                                "polarity": 0.4241306156122786
                            },
                            {
                                "comment_text": "Gana la selecta 3 contra 1 de Jamica. Vivi la emoción del fútbol con Tigo.",
                                "polarity": 0.4856960811018472
                            },
                            {
                                "comment_text": "VIVÍ LA EMOCIÓN DEL FÚTBOL CON TIGO\nEl Salvador 2 - 1 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Gana El Salvador 🇸🇻 1-0 Jamaica 🇯🇲 \n“Vive la emoción del fútbol con Tigo”",
                                "polarity": 0.13164343828256572
                            },
                            {
                                "comment_text": "SLV-JAM\n  2      0",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "Selecta 2\nReggae boyz 1",
                                "polarity": 0.3724498492476601
                            },
                            {
                                "comment_text": "Gana él salvador 2 jamaica 1 VIVE LA EMOCION DEL FUTBOL CON TIGO ,,,,💜💜💜",
                                "polarity": 0.07754996261921546
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con TIGO! \nEl Salvador🇸🇻 2   Jamaica🇯🇲 1",
                                "polarity": 0.6622205294645258
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo ! \nEl Salvador 0-0 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Vivi la emoción del fútbol gana el salvador 1a,o",
                                "polarity": 0.5960957262513621
                            },
                            {
                                "comment_text": "Empatamos 1 a 1",
                                "polarity": 0.023949517645913434
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo nuestra azulita gana 1 a 0 partido serrado",
                                "polarity": 0.8081240690301271
                            },
                            {
                                "comment_text": "GANA NUESTRA SELECTA EL SALVADOR 1 JAMAICA 0 \"VIVÍ LA EMOCIÓN DEL FÚTBOL CON TIGO\" QUIERE ESA CAMISA ORIGINAL PARA APOYAR CON TODO A NUESTROS GUERREROS QUE SE DARÁN EL TODO POR EL TODO EN LA CANCHA.",
                                "polarity": 0.22413474460966396
                            },
                            {
                                "comment_text": "ES 2 Jamaica 1 \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.21343972839168607
                            },
                            {
                                "comment_text": "El Salvador 4 jamaica 0 #VivilaLaEmocionConTigo  vamos selecta 💪🇸🇻🇸🇻🇸🇻🇸🇻",
                                "polarity": 0.07422782754973227
                            },
                            {
                                "comment_text": "Gana la selecta 1 - 0",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo\" *El Salvador 1 Jamaica 1",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Gana mi selecta 1x0 vivi la emocion del futbol con tigo y arriva la azulita",
                                "polarity": 0.9211841085311341
                            },
                            {
                                "comment_text": "Pierde la selecta 3 a 0 😯",
                                "polarity": 0.5751793836637618
                            },
                            {
                                "comment_text": "1  a 1",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "1-0 gana jamaica",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "Jamaica 2 El Salvador 1 😪😪😪😭😭😭",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Viví  la emoción con Tigo El Salvador\nEl Salvador 2\nJamaica     1",
                                "polarity": 0.084241760660154
                            },
                            {
                                "comment_text": "¡Viví la emoción del fútbol con Tigo! \nEl Salvador 1-1 Jamaica ⚽ ⚽ 💙",
                                "polarity": 0.09842898629363983
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo\" El Salvador 2 - Jamaica 1",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Esa 2 jam 0",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "ESA 2-2 JAMAICA",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "El salvador 2 Jamaica 1 '' viví la emoción del fútbol con tigo'' Tigo El Salvador",
                                "polarity": 0.15547116948335504
                            },
                            {
                                "comment_text": "1  a 4",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "Gana la selecta 1 a 0",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "2 / 1",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con TIGO, ahora gana la selecta 2-1",
                                "polarity": 0.5519853330335734
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo\nEl Salvador 1-3 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo\nEl Salvador 1-0 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "\"Vivi la emoción del fútbol con Tigo\". El Salvador 1 Jamaica 1.",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo El Salvador 2 - 2 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Vivi la emocion del futbol con TIGO.   El salvador 1- jamaica 0",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "\"Viví la Emoción Del Fútbol Con tigo\"💙 El Salvador 2 vrs Jamaica 1",
                                "polarity": 0.5461708907830469
                            },
                            {
                                "comment_text": "Vivilaemociondelfutbolcontigo 2-1",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "Gana la selecta 2-1",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "3-2 gana la selecta",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo!!!\nGana la selecta 1 a 0  quiero esa camiseta",
                                "polarity": 0.11400910616969943
                            },
                            {
                                "comment_text": "El Salvador 2 - 1 Jamaica \n¡Viví la emoción del fútbol con Tigo!",
                                "polarity": 0.09842898629363983
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo”\n\n El Salvador 2 🇸🇻  Jamaica 1 🇯🇲",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Dos uno gana la selecta",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "Selecta 1 Jamaica 0 \n\"Viví la emocion del futbol con tigo\"",
                                "polarity": 0.2722396855778531
                            },
                            {
                                "comment_text": "\" Viví la emoción del fútbol con  Tigo\" \n🇸🇻 #ElSalvador 1  🇯🇲#Jamaica 2",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "GANA EL SALVADOR  🇸🇻2 A 🇯🇲 1 \n\nviví la emoción del fútbol con tigo",
                                "polarity": 0.6062611039408947
                            },
                            {
                                "comment_text": "¡viví la emocion del futbol con tigo!gana el salvador 2 a 1 jamaica esa camisa es mia",
                                "polarity": 0.04368868009432217
                            },
                            {
                                "comment_text": "🇸🇻 “Viví la emoción del fútbol con Tigo”\nGANA EL SALVADOR 2 A 1 A JAMAICA NUESTRA SELECTA SIEMPRE DEMOSTRANDO QUIEN MANDA VAMOS CON TODO SELECTA",
                                "polarity": 0.3760328229206477
                            },
                            {
                                "comment_text": "2-1 gana la selecta 💪💪💪👍👍🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "Gana la selecta 2 - 0 Jamaica y \"viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.19437997584977015
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” Vamos con todo selecta. El Salvador 2, Jamaica 1.",
                                "polarity": 0.3314072638368406
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo\nES 1- Jamaica 0",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "ES 1 - 0 Jamaica, “viví la emoción del fútbol con TIGO”",
                                "polarity": 0.21343972839168607
                            },
                            {
                                "comment_text": "2 a 1 gana la selecta\"vivi la emoción del fútbol con Tigo\"",
                                "polarity": 0.6530054015895034
                            },
                            {
                                "comment_text": "\"Viví la emocion del futbol con Tigo\" El salvador se impone ante Jamainca 2-1 el dia viernes... Lo veremos gracias a Tigo El Salvador !!",
                                "polarity": 0.7359846146640266
                            },
                            {
                                "comment_text": "Un empate 1 a1",
                                "polarity": 0.18209585465898379
                            },
                            {
                                "comment_text": "la honda esta q les boy a meter la berga a todos los d tigo",
                                "polarity": 0.01453564579253789
                            },
                            {
                                "comment_text": "Mi pronóstico: El Salvador🇸🇻 3-1 Jamaica🇯🇲.\nViví la emoción del fútbol con Tigo.",
                                "polarity": 0.746031562394598
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1   \"Vivi la emocion del futbol con Tigo\" vamos selecta  ⚽️⚽️",
                                "polarity": 0.28974120222655286
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con tigo” ganamos El Salvador 2 Jamaica 1",
                                "polarity": 0.2499965535622159
                            },
                            {
                                "comment_text": "Resultado El Salvador 2 Jamaica 1, Viví la emoción del futbol con tigo.",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1 #viva_la_emoción_del_fútbol_con_tigo",
                                "polarity": 0.19445293170605912
                            },
                            {
                                "comment_text": "Vive la emoción del fútbol con TIGO, El Salvador 2 - 1 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Gana la selecta 3_1vivi la emoción con tigo",
                                "polarity": 0.4966778589712351
                            },
                            {
                                "comment_text": "La selecta 2 Jamaica 0 viva la emoción del fútbol con Tigo",
                                "polarity": 0.17924868501587202
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo 🇸🇻1-0🇯🇲 gana la selecta!!!",
                                "polarity": 0.40346299650228007
                            },
                            {
                                "comment_text": "\"Viví  la emoción del fútbol con Tigo\"\nEl Salvador 2 - 1 Jamaica\n#selecta #tigo",
                                "polarity": 0.2711777655499889
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo , gana  El Salvador 2 Jamaica 0",
                                "polarity": 0.07754996261921546
                            },
                            {
                                "comment_text": "Jamaica 1 El Salvador 1 vivi la emocion del futbol con Tigo!",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Jamaica 1 El Salvador 2 \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "1-1",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "EL SALVADOR 2 -  0 JAMAICA \n\nVIVI LA EMOCION DEL FUTBOL CON TIGO :d",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo. Mi pronóstico El Salvador 1-0 Jamaica.💙🇸🇻💪",
                                "polarity": 0.6635685059320843
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con Tigo!\"       Gana nuestra azulita 2 a 0 💙🇸🇻",
                                "polarity": 0.8866219302128966
                            },
                            {
                                "comment_text": "(Vivi la emocion del futbol con tigo) selecta(flor de izote ) 3 regueboys (mary jane) 2",
                                "polarity": 0.7494732832114934
                            },
                            {
                                "comment_text": "Gana La Sele 🇸🇻1 A 0 Vive La Emocion Del Futbol Con TIGO",
                                "polarity": 0.2377453228522855
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1 \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo. Gana El Salvador por goleada 7 a 0 a Jamaica.",
                                "polarity": 0.07985371900139769
                            },
                            {
                                "comment_text": "El salvador 2-1 Jamaica \n“viví la emoción del futbol con TIGO 💙”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo💙\nGana la selecta 1-0 🇸🇻💙\nYo Quiero Mi Camisa Gracias A Tigo La Mejor Compañía Del Salvador 💙🇸🇻",
                                "polarity": 0.2069291515323948
                            },
                            {
                                "comment_text": "#ViviLaEmocionDelFutbolConTigo💙\nGana la selecta 1-0 🇸🇻💙\nYo Quiero Mi Camisa Gracias A Tigo La Mejor Compañía Del Salvador 💙🇸🇻",
                                "polarity": 0.2069291515323948
                            },
                            {
                                "comment_text": "Vivi la emocion del futbol con tigo.\nEl salvador 2 Jamaica 2",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Vivo la emoción del fútbol con Tigo 1  a  1",
                                "polarity": 0.6622205294645258
                            },
                            {
                                "comment_text": "El Salvador🇸🇻  0.  Jamaica🇯🇲 2. Lamentablemente perderemos.  \"Viví la emoción del fútbol con TIGO\" ⚽️💙",
                                "polarity": 0.8951837916597035
                            },
                            {
                                "comment_text": "El salvador gana 1 a 0 jamáica \"viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.14113862380791534
                            },
                            {
                                "comment_text": "Ganamos EL SALVADOR 🇸🇻 1-0 🇯🇲 JAMAICA\n\"Viví la emocion del futbol con Tigo\"",
                                "polarity": 0.2499965535622159
                            },
                            {
                                "comment_text": "El Salvador 1 Jamaica 1 “Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo\nLo gana por la mínima la Selecta",
                                "polarity": 0.47016807228754165
                            },
                            {
                                "comment_text": "Vivi la emoción del fútbol gana  la selecta 2 por 1",
                                "polarity": 0.6561557312398025
                            },
                            {
                                "comment_text": "Quedan 1-1 empate",
                                "polarity": 0.03815048445593565
                            },
                            {
                                "comment_text": "El Salvador 1 - 0 Jamaica, \"Viví la emoción del fútbol con Tigo\" (me avisan para ir la a recoger 😁😁😁) la selecta campeona de la copa oro arre",
                                "polarity": 0.0850484253591673
                            },
                            {
                                "comment_text": "El salvador 1\nJamaica 1\n\" Vivi la Emocion del futbol con Tigo\"",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Gana el El Salvador  2 a 1 a Jamaica¡¡¡ \"Viva La Emoción Del Fútbol con Tigo\" ⚽️🇯🇲🇸🇻",
                                "polarity": 0.6045840744248587
                            },
                            {
                                "comment_text": "Selecta 1-jamaica - 1  \"viví la emoción del fútbol con tigo\"",
                                "polarity": 0.7743741437995518
                            },
                            {
                                "comment_text": "\"Viví la emoción del futbol con Tigo\" La selecta  1 _ 1 Jamaica",
                                "polarity": 0.2722396855778531
                            },
                            {
                                "comment_text": "Salvador 2-@ 1 jamaica\nVive la emocion del futbol con tigo",
                                "polarity": 0.1948387844617593
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con tigo\" la selecta 1 - 0 jamaica.",
                                "polarity": 0.2722396855778531
                            },
                            {
                                "comment_text": "El salvador 2 jamaica 1 \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 1 Viví la emoción del fútbol con Tigo",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Mi pronóstico 3-1 \"Viví la emoción del Fútbol con Tigo\"",
                                "polarity": 0.746031562394598
                            },
                            {
                                "comment_text": "😑",
                                "polarity": 0.541333260777616
                            },
                            {
                                "comment_text": "2 a 1 a favor de la selecta #VivilaemociondelfutbolconTigo",
                                "polarity": 0.34991817751847754
                            },
                            {
                                "comment_text": "3 el salvador 1 Jamaica \"viví la emocion del futbol con tigo\"\nSiempre apoyando la selecta",
                                "polarity": 0.2756143397033224
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo\nEl Salvador 2-1 Jamaica",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "\"Viví la emoción del fútbol con TIGO\"\nEl Salvador 2 vs Jamaica 3",
                                "polarity": 0.1727258732974894
                            },
                            {
                                "comment_text": "Vivi la emoción del fútbol con Tigo \nGana la selecta 3-2",
                                "polarity": 0.5519853330335734
                            },
                            {
                                "comment_text": "El Salvador 2 - 1 Jamaica\nViví la emoción del fútbol con Tigo",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo el Salvador  la selecta 1 y 3 a Jamaica",
                                "polarity": 0.17924868501587202
                            },
                            {
                                "comment_text": "Vivi el futbol contigo el Salvador 1 jamaica 0",
                                "polarity": 0.05984243891806486
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con Tigo ! Gana la azul 2 a 0",
                                "polarity": 0.47815584978980497
                            },
                            {
                                "comment_text": "\"Vivi la emocion del futbol con tigo\" 1 a 0 a favor de el salvador",
                                "polarity": 0.5590121786223038
                            },
                            {
                                "comment_text": "Viva la emoción del fútbol gana la selecta 3_1  así sera tigo",
                                "polarity": 0.5383053567725902
                            },
                            {
                                "comment_text": "El Salvador 0-1Jamaica \"Vivi la emocion del fútbol con TIGO \".",
                                "polarity": 0.7528382658281216
                            },
                            {
                                "comment_text": "\"Vivi la emocion de futbol con tigo \" gana la selecta 1 a 0 a jamaica",
                                "polarity": 0.19437997584977015
                            },
                            {
                                "comment_text": "Empate  1-1 \"Viví la emoción del fútbol con TIGO\"",
                                "polarity": 0.5447934868745963
                            },
                            {
                                "comment_text": "El Salvador 0 - Jamaica 2\nViví la emoción del fútbol con tigo",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Gana jamaica 2-0 El salvador \n#Vivilaemociondelfutbolcontigo",
                                "polarity": 0.012138189869546671
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol con tigo 2 -0 gana la selecta vamos el salvador",
                                "polarity": 0.5744876942934424
                            },
                            {
                                "comment_text": "\"Viví la emoción del Fútbol con TIGO\" Van a quedar 1 A 1",
                                "polarity": 0.6186287809755474
                            },
                            {
                                "comment_text": "El salvador 2-0 Jamaica, \"viví la emoción del fútbol con tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Gana la selecta 2 a 0 jamaica\n\"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.19437997584977015
                            },
                            {
                                "comment_text": "El salvador 2 Jamaica 0, viví la emoción del fútbol con tigo",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "El Salvador 🇸🇻 3- 2🇯🇲 Jamaica \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El salvador 2-1 Jamaica Viví la emoción del fútbol con TIGO",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Ganamos El Salvador  2   Jamaica 0 \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.2499965535622159
                            },
                            {
                                "comment_text": "El Salvador 🇸🇻 2 - 0 🇯🇲 Jamaica.\nViví la emoción del Fútbol con Tigo",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El Salvador 2-1 Jamaica, “viví la emoción del fútbol con Tigo”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El salvador 1-0 Jamaica\n\"Vivi la emocion del futbol con tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El Salvador 2-1 Jamaica \"Viví la emoción del fútbol con Tigo\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El salvador 2-2 Jamaica. Viví la emoción del fútbol con Tigo.",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "El salvador🇸🇻 2 Jamaica🇯🇲 1\nViví la emoción del fútbol con tigo",
                                "polarity": 0.7528382658281216
                            },
                            {
                                "comment_text": "El Salvador 2\nJamaica 0 !!! Viví la emoción del Futbol con TIGO!!!",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo”, Marcador El Salvador 2 - Jamaica 1",
                                "polarity": 0.13991296248841292
                            },
                            {
                                "comment_text": "#vivilaemociondelfutbolcontigo El Salvador 3 Jamaica 1",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "Vivi la emoción del fútbol con tigo  gana el Salvador 1 Jamaica 0",
                                "polarity": 0.07754996261921546
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 2 #ViviLaEmocionDelFutbolConTigo",
                                "polarity": 0.016217218542477086
                            },
                            {
                                "comment_text": "2-1 pierde la Selecta\n\"viví la emoción del fútbol con TIGO💙\"",
                                "polarity": 0.8187928241052209
                            },
                            {
                                "comment_text": "Jamaica 3 El salvador 1 \n\" Viví la Emoción del fútbol con Tigo\"",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Gana la selecta 2 - 1 y yo \"VIVÍ LA EMOCIÓN DEL FÚTBOL CON TIGO\"",
                                "polarity": 0.6530054015895034
                            },
                            {
                                "comment_text": "El salvador 2 - Jamaica 0 “Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El Salvador 2-1 Jamaica \n“viví la emoción del fútbol con Tigo”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El Salvador 2 - 1 Jamaica \"Viví la emoción del fútbol con TIGO\"",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "“Viví la emoción del fútbol con Tigo” \nLa Selecta 1\nJamaica 1",
                                "polarity": 0.2722396855778531
                            },
                            {
                                "comment_text": "El Salvador 2-1 Jamaica\n\nViví la emoción del fútbol con Tigo",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El salvador 1-1 Jamaica  “Viví la emoción del fútbol con Tigo.”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El salvador 2\nJamaica 1\n\"Vivì la emoción del fútbol con tigo\"",
                                "polarity": 0.49772227224726545
                            },
                            {
                                "comment_text": "El Salvador 1-2 Jamaica \nViví la emoción del fútbol con Tigo",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El salvador 2 - jamaica 2\nViví la emoción del futbol con Tigo",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "El Salvador 1 Jamaica 0 Viví la emoción del fútbol con Tigo",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "El Salvador 2 Jamaica 0 Viví la emoción del fútbol con Tigo",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "El Salvador 1- Jamaica 1 “Viví la emoción del fútbol con Tigo”",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Jamaica 2 --1 El Salvador Viví La Emoción Del Fútbol Con Tigo 🇯🇲VS🇸🇻⚽️⚽️🖥",
                                "polarity": 0.11760110685491895
                            },
                            {
                                "comment_text": "Gana la selecta 1 jamaica 0 \nVivi la emoción del futbol con tigo",
                                "polarity": 0.19437997584977015
                            },
                            {
                                "comment_text": "El Salvador 2-0 Jamaica\n#VIVI_LA_EMOCION_DEL_FUTBOL_CON_TIGO",
                                "polarity": 0.206531615606429
                            },
                            {
                                "comment_text": "Viví la emoción del fútbol contigo gana la selecta 2-1",
                                "polarity": 0.5962855723880476
                            },
                            {
                                "comment_text": "\"Vivi la emoción del futbol con Tigo\" 2 a 1 gana la selecta.",
                                "polarity": 0.6530054015895034
                            }
                        ]
                    }
                ],
                "frequency_words": [
                    {
                        "word": "emoción",
                        "frequency": 226
                    },
                    {
                        "word": "1",
                        "frequency": 218
                    },
                    {
                        "word": "fútbol",
                        "frequency": 207
                    },
                    {
                        "word": "2",
                        "frequency": 199
                    },
                    {
                        "word": "Jamaica",
                        "frequency": 192
                    }
                ]
            }
        ]
    }
]
    json_to_csv('final', JSON)
