let date = new Date()
let year = date.getFullYear()

document.addEventListener("DOMContentLoaded", function () {
	let copyFooter = document.getElementById("copy-date")
	console.log(copyFooter)
	copyFooter.innerHTML = `&copy${year}`
})
