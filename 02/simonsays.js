var listaBrojeva = [];
var nastaviIgru = true;
var trenutnoPrikazujem = false;

var audio1 = new Audio("audio/1.wav");
var audio2 = new Audio("audio/2.wav");
var audio3 = new Audio("audio/3.wav");
var audio4 = new Audio("audio/4.wav");
var errorAudio = new Audio("audio/error.mp3");
var sccsAudio = new Audio("audio/sccs.mp3");
var startAudio = new Audio("audio/start.mp3");
var clickAudio = new Audio("audio/click.mp3");

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const delay = (millis) =>
  new Promise((resolve, reject) => {
    setTimeout((_) => resolve(), millis);
  });

function igrajHC() {
  for (var i = 0; i < 8; i++) {
    var noviBroj = getRandomInt(1, 4);
    listaBrojeva.push(noviBroj);
  }

  igraj();
}

async function igraj() {
  trenutnoPrikazujem = true;
  // 1. Generiraj novi broj i stavi ga u listu brojeva
  var noviBroj = getRandomInt(1, 4);

  listaBrojeva.push(noviBroj);
  // 2. Ispisi sve brojeve iz liste
  for (var i = 0; i < listaBrojeva.length; i++) {
    var broj = listaBrojeva[i];
    var kutija = document.getElementById("box" + broj);

    if (broj == 1) {
      audio1.play();
    } else if (broj == 2) {
      audio2.play();
    } else if (broj == 3) {
      audio3.play();
    } else if (broj == 4) {
      audio4.play();
    }

    kutija.classList.remove(vratiBoju(broj));
    kutija.classList.add(vratiBoju(broj) + "-activated");
    await delay(1200);
    kutija.classList.remove(vratiBoju(broj) + "-activated");
    kutija.classList.add(vratiBoju(broj));
    await delay(300);
  }

  startAudio.play();
  trenutnoPrikazujem = false;
}

function vratiBoju(brojKutije) {
  if (brojKutije == 1) {
    return "red";
  }

  if (brojKutije == 2) {
    return "green";
  }

  if (brojKutije == 3) {
    return "blue";
  }

  if (brojKutije == 4) {
    return "yellow";
  }
}

var trenutniBroj = 0;
async function stisnutaKutijica(brojKutije) {
  if (trenutnoPrikazujem == false) {
    trenutnoPrikazujem = true;
    var kutija = document.getElementById("box" + brojKutije);
    kutija.classList.remove(vratiBoju(brojKutije));
    kutija.classList.add(vratiBoju(brojKutije) + "-activated");

    var brojIzListe = listaBrojeva[trenutniBroj];

    if (brojIzListe == brojKutije) {
      trenutniBroj = trenutniBroj + 1;
      //trenutniBroj++;
      clickAudio.play();

      if (trenutniBroj == listaBrojeva.length) {
        sccsAudio.play();
        document.getElementById("score").innerHTML = "score: " + trenutniBroj;
        await delay(1500);
        igraj();
        trenutniBroj = 0;
      }
    } else {
      errorAudio.play();
      document.getElementById("score").innerHTML = "FULAO SI!!!";
      await delay(3000);
      document.getElementById("score").innerHTML = "score: 0";
      listaBrojeva = [];
      trenutniBroj = 0;
    }
    trenutnoPrikazujem = false;
    await delay(500);
    kutija.classList.remove(vratiBoju(brojKutije) + "-activated");
    kutija.classList.add(vratiBoju(brojKutije));
    await delay(500);
  }
}
