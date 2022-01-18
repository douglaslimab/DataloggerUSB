const pg = require('pg')
const axios = require('axios')
const cheerio = require('cheerio')
const express = require('express')

const client = new pg.Client({
    host: "localhost",
    database: "temperature",
    user: "postgres",
    password: "Classic-2011",
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

    console.log("updated..");
    console.log(read_temperature.rows);
}

module.exports = client;
//create_last_hour();
read_db();