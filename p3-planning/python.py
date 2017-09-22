import pygal

def normalize(a):
	n = []
	for i in a:
		n.append(i/(sum(a)+0.0))
	return n		

# line_chart = pygal.Bar()
# line_chart.title = 'Problem 3'
# line_chart.x_labels = ["h_pg_levelsum","h_ignore_preconditions"]
# line_chart.add('Expansions', normalize([325,5040]))
# line_chart.add('Goal Tests', normalize([327,5042]))
# line_chart.add('New Nodes', normalize([3002,44944]))
# line_chart.add('Time', normalize([34.65,8.60]))
# line_chart.render_to_file("line_chart1.svg")

line_chart = pygal.Bar()
line_chart.title = 'Problem 3'
line_chart.x_labels = ["Breadth First Search","Depth First Search","Uniform Cost Search"]
line_chart.add('Expansions', normalize([14663,592,18236]))
line_chart.add('Goal Tests', normalize([18098,593,18238]))
line_chart.add('New Nodes', normalize([129631,4927,159726]))
line_chart.add('Time', normalize([97.41,3.02,51.81]))
line_chart.render_to_file("line_chart1.svg")