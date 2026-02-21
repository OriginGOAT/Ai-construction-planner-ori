import plotly.figure_factory as ff

def chart(tasks):

    data=[]

    day=0

    for t in tasks:
        data.append(dict(Task=t,Start=day,Finish=day+3))
        day+=3

    fig=ff.create_gantt(data)

    return fig
