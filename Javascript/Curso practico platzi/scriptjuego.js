/* ************ keypress ************ */
const emojiInput = document.getElementById('emojiInput');
const emojiResult = document.getElementById('emojiResult');

emojiInput.addEventListener('keypress', changeEmoji);

function changeEmoji() {
  emojiPick = emojis[Math.floor(Math.random() * emojis.length)];
  emojiResult.innerHTML = emojiPick;
}

/* ************ mouseover ************ */
const resetBtn = document.getElementById('reset');
const pipesHitBox = document.querySelectorAll('.pipeHitBox');
const message = document.getElementById('message');
const dieCount = document.getElementById('dieCount');

// Agregar addEventListener a los tubos
pipesHitBox.forEach(function (pipeHitBox) {
  pipeHitBox.addEventListener('mouseover', youCrashed);
});

let i = 1;
function youCrashed() {
  // Habilitar botón y mostrar mensaje "PERDISTE"
  resetBtn.disabled = false;
  message.style.display = 'flex';

  // Aumentar contador
  dieCount.innerText = 'MUERTES: ' + i++;
}

resetBtn.addEventListener('click', function () {
  // Deshabilitar botón y ocultar mensaje
  resetBtn.disabled = true;
  message.style.display = 'none';
});

// -----------------------------------------------------------------------------

// Lista de emojis: https://gist.github.com/ikr7/c72843556ef3a12014c3