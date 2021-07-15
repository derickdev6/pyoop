from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import random


class Person:
    def __init__(self, sex, age, rec):
        self.sex = sex[1:-1:]
        self.age = int(age[1:-1:])
        self.rec = rec[1:-1:]

    def __str__(self):
        return f'{self.sex}, {self.age}, {self.rec}'


def read_file(filename):
    f = open(filename, mode='r')
    patients_f = []
    patients_m = []

    # Skip the first Line
    f.readline().split(',')

    for line in f:
        ren = line.split(',')
        temp_person = Person(ren[9], ren[7], ren[15])
        if temp_person.sex == 'F':
            patients_f.append(temp_person)
            # print(str(temp_person))
        else:
            patients_m.append(temp_person)

    return [patients_m, patients_f]


def main():
    patients = read_file("covid_data.csv")
    patients_m = patients[0]
    patients_f = patients[1]
    dead_m = 0
    dead_f = 0

    for patient in patients_m:
        if patient.rec == 'Fallecido':
            dead_m += 1
    for patient in patients_f:
        if patient.rec == 'Fallecido':
            dead_f += 1

    source = ColumnDataSource(data=dict(
        x=list(range(2)),
        y1=[len(patients_m)-dead_m, len(patients_f) - dead_f],
        y2=[dead_m, dead_f]
    ))

    print(f'Hombres = {len(patients_m)} de los cuales {dead_m} han fallecido')
    print(f'Mujeres = {len(patients_f)} de las cuales {dead_f} han fallecido')

    output_file('covid_data.html')
    fig = figure()
    fig.vbar_stack(['y1', 'y2'], x='x', width=.5,
                   color=('lightgrey', 'grey'), source=source)

    show(fig)


if __name__ == '__main__':
    main()
