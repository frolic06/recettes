Title: Favoris

Retrouver ici toutes vos recettes préférées.

<div id="fav"></div>

Pour ajouter / enlever un favori, cliquer sur le <i class="fas fa-heart"></i> sous le titre de la recette (uniquement dans la page de la recette).

<br />
<h4>Historique</h4>
Voici les dernières recettes consultées:

<div id="histo"></div>
<script>
    function createList(storage, elementId) {
        const favs = localStorage.getItem(storage);
        if (favs) {
            const favArray = JSON.parse(favs);
            let html = '<div><ul class="list">';
            for (let fav of favArray) {
                html += '<li><a href="' + fav.url + '">'  + fav.title + '</a></li>';
            }
            html += '</ul></div>'
            const el = document.getElementById(elementId);
            el.innerHTML = html;
        }
    }
    createList('my-favs', 'fav');
    createList('my-histo', 'histo');
</script>