function autocomplete(inp, search_index, recettes) {
    function stabilo(text) {
        return '<mark>' + text + "</mark>";
    }
    var currentFocus;
    inp.addEventListener("input", function (e) {
        var a, b, i, val = this.value;
        closeAllLists();
        if (!val) { return false; }
        val = val.toLowerCase();
        currentFocus = -1;
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        this.parentNode.appendChild(a);
        const ids = new Set();
        for (const key of Object.keys(search_index)) {
            if (key.includes(val)) {
                for (const index of search_index[key]) {
                    if (ids.has(index)) {
                        continue;
                    }
                    ids.add(index);
                    b = document.createElement("DIV");
                    let title = recettes[index].title.replace(val, stabilo(val))
                    const capitalized = val.charAt(0).toUpperCase() + val.slice(1);
                    title = title.replace(capitalized, stabilo(capitalized))
                    b.innerHTML += "<a href=\"/" + recettes[index].url + "\">" + title + '</a>';
                    b.innerHTML += "<input type='hidden' value='/" + recettes[index].url + "'>";
                    b.addEventListener("click", function(e) {
                        window.location.href = this.getElementsByTagName("input")[0].value;
                        closeAllLists();
                    });
                    a.appendChild(b);
                }
            }
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
