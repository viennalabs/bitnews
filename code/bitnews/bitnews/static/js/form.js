// Just a little code that makes sure users mark the checkbox on registration
function checkForm(form) {
	if(!form.nice.checked) {
		alert("Please indicate that you are going to be nice.");
		form.nice.focus();
		return false;
	}
	return true;
}