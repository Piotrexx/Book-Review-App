from plotly.offline import plot
import plotly.graph_objs as graphs

def generate_scatter_plot(x_axis, y_axis):
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=x_axis, y=y_axis)
    figure.add_trace(scatter)
    return plot(figure, output_type='div')


def generate_HTML(plot_html):
    html_content = "<html><head><title>Graphs</title></head><body>{}</body></html>".format(plot_html)
    try:
        with open('plot_demo.html', 'w',encoding="utf-8") as plot_file:
            plot_file.write(html_content)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    x = [1,2,3,4,5]
    y = [3,8,7,9,2]
    plot_html = generate_scatter_plot(x,y)
    generate_HTML(plot_html)