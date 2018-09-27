import datetime

"""
PRIMEIRO DIA DE B em outubro:

2018/10/02

"""


# def schedule(person, day, shift):
#     initial_date = date(2018, 10, 2)
#     initial_date_toordinal = initial_date.toordinal()
#     end_date = initial_date_toordinal + 30
#     for i in range(initial_date_toordinal, end_date):
#         if i % 6 in (0, 5):
#             print(date.fromordinal(i), 'weekend')
#         else:
#             print(date.fromordinal(i))

"""
AREA DE TESTES ABAIXO:
"""

initial_date = datetime.date(2018, 9, 8)
initial_date_toordinal = initial_date.toordinal()
end_date = datetime.date(2018, 12, 31)
end_date_toordinal = end_date.toordinal()
"""
*  =  DIA DE FOLGA
A  =  TURNO A
B  =  TURNO B


Estou partindo do primeiro dia do turno B 
para o mes de setembro (2018/09/08) 
e colocarei o calendario ate o fim de dezembro

"""
date_range = {}
for i in range(initial_date_toordinal, end_date_toordinal + 1): #+1 para pegar o ultimo elemento (dia 31 de dezmebro)
    if i % 6 in (0, 5):
        date_range.update({datetime.date.fromordinal(i).isoformat(): '*'})
    else:
        if i % 12 in (1, 2, 3, 4):
            date_range.update({datetime.date.fromordinal(i).isoformat(): 'B'}) #pega os primeiros dias de trabalho e coloca como B
        else:
            date_range.update({datetime.date.fromordinal(i).isoformat(): 'A'})

