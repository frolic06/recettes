Title: Favoris

Retrouver ici toutes vos recettes préférées.

<div id="fav"></div>

Pour ajouter / enlever un favori, cliquer sur le ♥ à côté du titre de la recette.

<script>
    const favs = localStorage.getItem('my-favs');
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