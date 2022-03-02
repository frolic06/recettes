
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

    if (window.pageYOffset >= sticky) {
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
