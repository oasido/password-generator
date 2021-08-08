// update the range value for the password length
let length_range = document.getElementById('length');

$('#lengthText').html(length_range.value); // insert length range value before touching it

// update value text
length_range.oninput = function () {
  $('#lengthText').html(length_range.value);
};

let wachtwoord = document.getElementById('wachtwoord');
$('#button-addon2').onclick = function () {
  $(this).parents('#wachtwoord').children('input').select();
};

$('#copy_button').click(function () {
  $(this).siblings('input#wachtwoord').select();
  document.execCommand('copy');
});

// at least 1 button checked
$(document).ready(function () {
  // check all buttons on start
  $('.btn-check').prop('checked', true);

  // at least 1 button checked
  $('.btn-check').click(function () {
    checked = $('input[type=checkbox]:checked').length;

    if (!checked) {
      alert('U moet ten minste één optie kiezen.');
      return false;
    }
  });
});
