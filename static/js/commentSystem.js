currentWonder = localStorage.getItem("currentWonder")
currentComments = localStorage.getItem("comments-{0}".format(currentWonder));

if (currentComments == null) {currentComments = ""};

function getValue(id) {
	return document.getElementById(id).value;
};

function displayContainer() {
	var commentsBox = document.getElementById("comments-display");
	commentsBox.innerHTML = currentComments;
};

function updateContainer() {
	displayContainer();
	localStorage.setItem("comments-{0}".format(currentWonder), currentComments);
};

function postComment() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			alert("Your comment was posted. Thank you for your input!")
		}
	}
	xhttp.open("POST", "/api/post_comment", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send(
		"first_name={0}&last_name={1}&email_address={2}&comment={3}".format(
			getValue('firstname'), getValue('lastname'),
			getValue('email-box'), getValue('comment')
		)
	)
};