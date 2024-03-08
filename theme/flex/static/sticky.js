
window.onscroll = function() { onScroll(); };
var sticky = null;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function onScroll() {
  // Get the navbar
  const navbar = document.getElementById("navbar");
  if (navbar) {
    // Get the offset position of the navbar
    if (sticky === null) {
      sticky = navbar.offsetTop;
    }

    if (window.scrollY >= sticky) {
      navbar.classList.add("sticky");
    } else {
      navbar.classList.remove("sticky");
    }
  }
}

function addClass() {
  const el = document.querySelector("#btn-fav");
  el.classList.add('favorite');
}

function removeClass() {
  const el = document.querySelector("#btn-fav");
  el.classList.remove('favorite');
}

function addClassForFav() {
  const myFavs = localStorage.getItem('my-favs');
  if (myFavs && theArticle !== undefined) {
    const favs = JSON.parse(myFavs);
    const index = favs.findIndex(f => f.title === theArticle.title);
    if (index >= 0) {
      addClass();
    }
  }
  if (theArticle && theArticle.title) {
    let myHisto = localStorage.getItem('my-histo');
    let histo = (myHisto) ? JSON.parse(myHisto) : [];
    const index = histo.findIndex(f => f.title === theArticle.title);
    if (index !== -1) {
      histo.splice(index, 1);
    } else if (histo.length >= 10) {
      histo.pop();
    }
    histo.unshift(theArticle);

    localStorage.setItem('my-histo', JSON.stringify(histo));
  }
}

function addFav() {
  const myFavs = localStorage.getItem('my-favs');
  let favs = (myFavs) ? JSON.parse(myFavs) : [];
  const index = favs.findIndex(f => f.title === theArticle.title);
  if (index === -1) {
    favs.push(theArticle);
    addClass();
  } else {
    favs.splice(index, 1);
    removeClass();
  }
  localStorage.setItem('my-favs', JSON.stringify(favs));
}
