print("<td>{{ data.patient }}</td>")
print("<td> {{ data.curent_smoker }} </td>")
for i in range (1,11):
	print("<td>{{ data.condition_%s }}</td>" % i)
