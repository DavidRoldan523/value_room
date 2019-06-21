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
                "page_name": "tigoelsalvador",
                "page_id": "17841401363715944",
                "date_since": "2017-04-12",
                "date_until": "2019-06-20",
                "results": [
                    {
                        "date": "2017-04-12",
                        "comments": [
                            {
                                "post_id": "17847192622156165",
                                "post_name": "La paz se construye con pequeas acciones y depende de vos llevarla a todos lados. Hoy celebramos 25 aos de los #AcuerdosdePaz #PazJuntos",
                                "results": [
                                    {
                                        "comment_text": "PESIMA ATENCION LA DE TIGO.  Firme contrato el 17 de enero con Mirian Elizabeth Cordero Dur de renovaciones, con un cambio a pagar por $38.41  y  a la  fecha me siguen cobrando mas de $60. dolares,  NO ME DAN RESPUESTA, HE LLAMADO TELEFONICAMENTE, POR CORREO Y SIGO ESPERANDO. ES UN EJEMPLO TIPICO DE PUBLICIDAD ENGAOSA QUE NO CUMPLEN CON LO QUE PROMETEN Y UNA PESIMA ATENCION AL CLIENTE",
                                        "polarity": 0.002417279477689401
                                    }
                                ]
                            },
                            {
                                "post_id": "17858681692102298",
                                "post_name": "Nuestro CEO Marcelo Alem firma acuerdo importante del proyecto Mujeres Conectadas, al cual nos unimos orgullosamente para mejorar la vida digital de las salvadoreas.",
                                "results": [
                                    {
                                        "comment_text": "PESIMA ATENCION LA DE TIGO.  Firme contrato el 17 de enero con Mirian Elizabeth Cordero Dur de renovaciones, con un cambio a pagar por $38.41  y  a la  fecha me siguen cobrando mas de $60. dolares,  NO ME DAN RESPUESTA, HE LLAMADO TELEFONICAMENTE, POR CORREO Y SIGO ESPERANDO. ES UN EJEMPLO TIPICO DE PUBLICIDAD ENGAOSA QUE NO CUMPLEN CON LO QUE PROMETEN Y UNA PESIMA ATENCION AL CLIENTE",
                                        "polarity": 0.002417279477689401
                                    }
                                ]
                            },
                            {
                                "post_id": "17864522848021437",
                                "post_name": "Hoy inici nuestro 1er. Foro Pymes Emprender y crecer en la era digital #ForoPymesTigo #TigoBusiness",
                                "results": [
                                    {
                                        "comment_text": "EMPRESA  QUE  NO  CUMPLE  CONTRATOS  Y  PESIMA  ATENCION  A  LOS  CLIENTES",
                                        "polarity": 0.00038375560322343307
                                    }
                                ]
                            },
                            {
                                "post_id": "17847426676102314",
                                "post_name": "Alejandro Sanz record a Jorge El M\gico Gonzalez con la azul y blanco, #ElSalvadorSabeASirope gracias a #TigoMusic",
                                "results": [
                                    {
                                        "comment_text": "PESIMA ATENCION LA DE TIGO.  Firme contrato el 17 de enero con Mirian Elizabeth Cordero Dur de renovaciones, con un cambio a pagar por $38.41  y  a la  fecha me siguen cobrando mas de $60. dolares,  NO ME DAN RESPUESTA, HE LLAMADO TELEFONICAMENTE, POR CORREO Y SIGO ESPERANDO. ES UN EJEMPLO TIPICO DE PUBLICIDAD ENGAOSA QUE NO CUMPLEN CON LO QUE PROMETEN Y UNA PESIMA ATENCION AL CLIENTE",
                                        "polarity": 0.002417279477689401
                                    }
                                ]
                            },
                            {
                                "post_id": "17856425827036896",
                                "post_name": "Alejandro Sanz est\ poniendo a gritar al M\gico Gonz\lez junto a Tigo Music.",
                                "results": [
                                    {
                                        "comment_text": "PESIMA ATENCION LA DE TIGO.  Firme contrato el 17 de enero con Mirian Elizabeth Cordero Dur de renovaciones, con un cambio a pagar por $38.41  y  a la  fecha me siguen cobrando mas de $60. dolares,  NO ME DAN RESPUESTA, HE LLAMADO TELEFONICAMENTE, POR CORREO Y SIGO ESPERANDO. ES UN EJEMPLO TIPICO DE PUBLICIDAD ENGAOSA QUE NO CUMPLEN CON LO QUE PROMETEN Y UNA PESIMA ATENCION AL CLIENTE",
                                        "polarity": 0.002417279477689401
                                    }
                                ]
                            },
                            {
                                "post_id": "17854273201001978",
                                "post_name": "Histrico, pico y legendario. Eso y m\s fue el concierto de #IronMaiden en #ElSalvador ",
                                "results": [
                                    {
                                        "comment_text": "PESIMA ATENCION LA DE TIGO.  Firme contrato el 17 de enero con Mirian Elizabeth Cordero Dur de renovaciones, con un cambio a pagar por $38.41  y  a la  fecha me siguen cobrando mas de $60. dolares,  NO ME DAN RESPUESTA, HE LLAMADO TELEFONICAMENTE, POR CORREO Y SIGO ESPERANDO. ES UN EJEMPLO TIPICO DE PUBLICIDAD ENGAOSA QUE NO CUMPLEN CON LO QUE PROMETEN Y UNA PESIMA ATENCION AL CLIENTE",
                                        "polarity": 0.002417279477689401
                                    },
                                    {
                                        "comment_text": "La  compaia  que  co  cumple  sus  contratos  y  no  resuelve  los  problemad",
                                        "polarity": 0.0063922016935072275
                                    }
                                ]
                            },
                            {
                                "post_id": "17855129071027937",
                                "post_name": "Eddie the Head apareci anoche en el concierto de @ironmaiden en #ElSalvador. #IronMaidenByTigoMusic ",
                                "results": [
                                    {
                                        "comment_text": "PESIMA ATENCION LA DE TIGO.  Firme contrato el 17 de enero con Mirian Elizabeth Cordero Dur de renovaciones, con un cambio a pagar por $38.41  y  a la  fecha me siguen cobrando mas de $60. dolares,  NO ME DAN RESPUESTA, HE LLAMADO TELEFONICAMENTE, POR CORREO Y SIGO ESPERANDO. ES UN EJEMPLO TIPICO DE PUBLICIDAD ENGAOSA QUE NO CUMPLEN CON LO QUE PROMETEN Y UNA PESIMA ATENCION AL CLIENTE",
                                        "polarity": 0.002417279477689401
                                    }
                                ]
                            }
                        ],
                        "frequency_words": [
                            {
                                "word": "ATENCION",
                                "frequency": 13
                            },
                            {
                                "word": "QUE",
                                "frequency": 13
                            },
                            {
                                "word": "NO",
                                "frequency": 13
                            },
                            {
                                "word": "DE",
                                "frequency": 12
                            },
                            {
                                "word": "PESIMA",
                                "frequency": 8
                            }
                        ]
                    },
                    {
                        "date": "2017-04-20",
                        "comments": [
                            {
                                "post_id": "17856425827036896",
                                "post_name": "Alejandro Sanz est\ poniendo a gritar al M\gico Gonz\lez junto a Tigo Music.",
                                "results": [
                                    {
                                        "comment_text": "Traigan a Porter Robinson y a Madeon en su Shelter Tour",
                                        "polarity": 0.8881297649987635
                                    },
                                    {
                                        "comment_text": "Traigan a Porter Robinson y a Madeon en su Shelter Tour",
                                        "polarity": 0.8881297649987635
                                    }
                                ]
                            }
                        ],
                        "frequency_words": [
                            {
                                "word": "Madeon",
                                "frequency": 1
                            },
                            {
                                "word": "Shelter",
                                "frequency": 1
                            },
                            {
                                "word": "Porter",
                                "frequency": 1
                            },
                            {
                                "word": "Traigan",
                                "frequency": 1
                            },
                            {
                                "word": "Tour",
                                "frequency": 1
                            }
                        ]
                    }
                ]
            }
        ]
    json_to_csv('final', JSON)
