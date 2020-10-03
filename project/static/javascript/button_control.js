function enableButton(button) {
  button.classList.remove('disabled');
}

function disableButton(button) {
  button.classList.add('disabled');
  setTimeout(() => enableButton(button), 1500);
}

var button = document.getElementById('submit');
button.addEventListener('click', () => disableButton(button));
