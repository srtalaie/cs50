let date = new Date()
let year = date.getFullYear()

document.addEventListener("DOMContentLoaded", function () {
	let copyFooter = document.getElementById("copy-date")
	copyFooter.innerHTML = `&copy${year}`
})

function submitForm() {
	let commentSectionText = document.getElementById("comment-section").value
	alert(`Message: ${commentSectionText}`)
}
