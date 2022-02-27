PORT = 8000;
const express = require('express');
var cors = require('cors');
const pg = require('pg')
//const client = require('./client')

app = express();
app.use(cors());

const client = new pg.Client({
    host: "localhost",
    database: "temperature",
    user: "postgres",
    password: "cortsolo2006",
    port: 5432,
})

app.get('/:sensor', async (req, res) => {
    const sensor = req.params.sensor
    
    await client.connect();
    var read_temperature
    read_temperature = await client.query(`SELECT ${sensor}, time FROM temperature_logger ORDER BY temp_id DESC LIMIT 20`)
    await client.end();

    res.send(read_temperature.rows)
})

app.listen(PORT, () => console.log(`Server running on  PORT: ${PORT}..`));