const pg = require('pg')
//const client = require('./client')

const client = new pg.Client({
    host: "localhost",
    database: "temperature",
    user: "postgres",
    password: "cortsolo2006",
    port: 5432,
})

async function create_last_hour(){
    await client.connect();
    await client.query('CREATE TABLE last_hour(temp_id BIGSERIAL NOT NULL PRIMARY KEY, temperature VARCHAR(8), time VARCHAR(8))');
    await client.end();

    console.log("last_hour created!!");
}

async function read_db(){
    await client.connect();
    var read_temperature

    read_temperature = await client.query('SELECT temperature FROM temperature_logger ORDER BY temp_id DESC LIMIT 1')
    await client.end();

    console.log(read_temperature.rows[0].temperature);
}

module.exports = read_db;