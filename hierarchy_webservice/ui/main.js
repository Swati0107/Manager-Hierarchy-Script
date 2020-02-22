function CreateTableFromJSON(data) {
    select = document.createElement("select");
    select.options.add(new Option('Sort-By', "sort-by", true, true));

    var col = [];
    for (var i = 0; i < data.length; i++) {
        for (var key in data[i]) {
            if (col.indexOf(key) === -1) {
                col.push(key);
                select.options.add(new Option(key));

            }
        }
    }
    // console.log(select)

    // CREATE DYNAMIC TABLE.
    var table = document.createElement("table");

    // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

    var tr = table.insertRow(-1); // TABLE ROW.

    for (var i = 0; i < col.length; i++) {
        var th = document.createElement("th"); // TABLE HEADER.
        var btn = document.createElement("BUTTON");
        btn.setAttribute('id', 'Button' + i)
        btn.setAttribute('class', 'Button')

        btn.innerHTML = col[i];
        th.appendChild(btn);
        tr.appendChild(th);
    }

    // ADD JSON DATA TO THE TABLE AS ROWS.
    for (var i = 0; i < data.length; i++) {

        tr = table.insertRow(-1);

        for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);
            tabCell.innerHTML = data[i][col[j]];
        }
    }

    var dropdownContainer = document.getElementById("sortBy");
    dropdownContainer.appendChild(select);

    // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
    var divContainer = document.getElementById("showData");
    divContainer.innerHTML = "";
    divContainer.appendChild(table);

}

baseUrl = 'http://localhost:8000/data'

$(document).ready(function() {
    $.get(baseUrl, {}, function(data) {
        if (data['result']) {
            CreateTableFromJSON(data['result']);
        }
    });
});


$(document).ready(function() {
    $('.Button').click(function() {
        console.log($('.Button').val())
        $.get(baseUrl + '?sortby=' + $('.Button').val(), {}, function(data) {
            if (data['result']) {
                CreateTableFromJSON(data['result']);
            }
        });
    });
});

$('.myClass').click(function() {
    var clicks = $(this).data('clicks');
    if (clicks) {
        // odd clicks
    } else {
        // even clicks
    }
    $(this).data("clicks", !clicks);
});