from datetime import date

initial_date = date(2018, 9, 2)
initial_date_toordinal = initial_date.toordinal()
end_date = initial_date_toordinal + 30
for i in range(initial_date_toordinal, end_date):
    if i % 6 in (0, 5):
        print(date.fromordinal(i), 'weekend')
    else:
        print(date.fromordinal(i))