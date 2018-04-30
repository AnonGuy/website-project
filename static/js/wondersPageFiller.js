function NameConvert(string) {
	return string.toLowerCase().replace(/ /g, "-")
}

function FillHTML(){
	var wonderIndex = localStorage.getItem("currentWonder");
	var currentWonder = wondersList[wonderIndex];
	var dashCase = NameConvert(currentWonder.name);
	
	document.body.id = dashCase;
	document.title = "{0} | {1}".format(parseInt(wonderIndex)+1, currentWonder["name"]);
	document.getElementById("wonder-header").innerHTML = currentWonder["name"];
	document.getElementById("wonder-description").innerHTML = currentWonder["description"];
	document.body.style.backgroundImage = 'url("../static/images/{0}.jpg")'.format(dashCase);
	var buttonsHolder = document.getElementById("return-buttons");
	for (i=0; i<wondersList.length; i++) {
		buttonItem = '\n<a href="../wonder" onclick="SetWonder({0});"><button type="button" class="flex-item">{1}</button></a>'.format(
			i, wondersList[i]["name"]
		);
		buttonsHolder.innerHTML += buttonItem;
	};
};