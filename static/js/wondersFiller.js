currentWonder = 0;

// Function to set correct variable in storage
function SetWonder(n) {
	localStorage.setItem("currentWonder", n);
};

function LoadHomeButtons() {
	// Get Ordered List of wonders
	var wondersTag = document.getElementById("wondersTag");
	var n = 0;
	// Add each wonder
	for (; n<wondersList.length; n++) {
		var listItem = '\n<a href="wonder" onclick="SetWonder({0});"><button type="button" class="flex-item">{1}</button></a>'.format(
			n, wondersList[n]["name"]
		);
		wondersTag.innerHTML += listItem;
	};	
};