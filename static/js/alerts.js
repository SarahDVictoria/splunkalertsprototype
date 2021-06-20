function getalerts() {
    fetch('/splunkalerts')
        .then(function (response) { return response.json()) })
        .then(function (data) {
            document.getElementById('alerttable').innerHTML = ''
            for(alert in data) {
                document.getElementById('alerttable').innerHTML += `
                    <tr>
                        <td>${alert['sid']}</td>
                        <td><a href="${alert['result_link']}">result</a></td>
                        <td>${alert['search_name']}</td>
                        <td>${alert['owner']}</td>
                        <td>${alert['app']}</td>
                    </tr>
                `
            }
        })
}
