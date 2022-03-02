Title: Favoris

Retrouver ici toutes vos recettes préférées.

Pour ajouter / enlever un favori, cliquer sur le ♥ à côté du titre de la recette.

<div id="fav"></div>

<script>
    const favs = localStorage.getItem('fav');
    if (favs) {
        const favArray = JSON.parse(favs);
        let html = '<div><ul class="list">';
        for (let fav of favArray) {
            html += '<li><a href="' + fav.url + '">'  + fav.title + '</a></li>';
        }
        html += '</ul></div>'
        const el = document.getElementById('fav');
        el.innerHTML = html;
    }
</script>