const db = openDatabase("temperature", "1.0", "temperature", 2 * 1024 * 1024);
let output = document.getElementById('temperature');

db.transaction(function (tx) { 
//    tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)'); 
//    tx.executeSql('INSERT INTO LOGS (id, log) VALUES (1, "foobar")'); 
//    tx.executeSql('INSERT INTO LOGS (id, log) VALUES (2, "logmsg")'); 


    var read_temperature;
    read_temperature = tx.executeSql('SELECT temperature FROM temperature_logger ORDER BY temp_id DESC LIMIT 1');

    msg = 'Log message created and row inserted.'; 
    document.querySelector('#temperature').innerText =  read_temperature; 
    console.log(read_temperature)
 })

 
 db.transaction(function (tx) { 
    tx.executeSql('SELECT temperature FROM temperature_logger ORDER BY temp_id DESC LIMIT 1', [], function (tx, results) { 
       var len = results.rows.length, i; 
       msg = "<p>Found rows: " + len + "</p>"; 
       document.querySelector('#temperature').innerHTML +=  msg; 

       for (i = 0; i < len; i++) { 
          msg = "<p><b>" + results.rows.item(i).log + "</b></p>"; 
          document.querySelector('#temperature').innerHTML +=  msg; 
       } 
    }, null); 
 }); 