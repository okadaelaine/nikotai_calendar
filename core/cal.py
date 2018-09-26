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

initial_date = datetime.date(2018, 10, 2)
initial_date_toordinal = initial_date.toordinal()
end_date = initial_date_toordinal + 30

date_range = {}
for i in range(initial_date_toordinal, end_date):
    if i % 6 in (0, 5):
        date_range.update({datetime.date.fromordinal(i).isoformat(): 'weekend'})
    else:
        date_range.update({datetime.date.fromordinal(i).isoformat(): 'weekday'})

