function autocomplete(inp, search_index, recettes) {
    function stabilo(text) {
        return '<mark>' + text + "</mark>";
    }
    var currentFocus;
    inp.addEventListener("input", function (e) {
        var a, b, val = this.value;
        closeAllLists();
        if (!val) { return false; }
        val = val.toLowerCase().trim();
        const values = val.split(' ')
        currentFocus = -1;
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        this.parentNode.appendChild(a);
        const map = new Map();
        for (const key of Object.keys(search_index)) {
            for (val of values) {
                if (key.includes(val)) {
                    for (const index of search_index[key]) {
                        if (map.has(index)) {
                            const item = map.get(index);
                            if (!item.matchs.includes(val)) {
                                item.matchs.push(val);
                            }
                        } else {
                            map.set(index, { 
                                title: recettes[index].title,
                                url: recettes[index].url,
                                matchs: [val]
                            });
                        }
                    }
                }
            }
        }
        for (const value of map.values()) {
            b = document.createElement("DIV");
            let title = value.title;
            for (match of value.matchs) {
                title = title.replace(match, stabilo(match));
                const capitalized = match.charAt(0).toUpperCase() + match.slice(1);
                title = title.replace(capitalized, stabilo(capitalized))
            }
            b.innerHTML += "<a href=\"/" + value.url + "\">" + title + '</a>';
            b.innerHTML += "<input type='hidden' value='/" + value.url + "'>";
            b.addEventListener("click", function(e) {
                window.location.href = this.getElementsByTagName("input")[0].value;
                closeAllLists();
            });
            a.appendChild(b);
        }
    });
    inp.addEventListener("keydown", function (e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) { /*down*/
            currentFocus++;
            addActive(x);
        } else if (e.keyCode == 38) { /*up*/
            currentFocus--;
            addActive(x);
        } else if (e.keyCode == 13) { /*enter*/
            e.preventDefault();
            if (currentFocus > -1) {
                if (x) x[currentFocus].click();
            }
        }
    });
    function addActive(x) {
        if (!x) return false;
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);
        x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
        for (var i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }
    function closeAllLists(elmnt) {
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
} 
