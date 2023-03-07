
setInterval(function () {
	console.clear()

	data = new Date()
	atual = data.toLocaleTimeString()

	console.log(`\x1b[44m ${atual} \x1b[0m`)
},
1000)
