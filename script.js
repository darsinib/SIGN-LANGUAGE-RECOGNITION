function runPython() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/run-python");
        xhr.onload = function() {
            if (xhr.status === 200) {
                alert(xhr.responseText);
            } else {
                alert("Error: " + xhr.statusText);
            }
        };
        xhr.send();
      }