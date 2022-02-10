const pg = require('pg')

const client = new pg.Client({
    host: "localhost",
    database: "temperature",
    user: "postgres",
    password: "cortsolo2006",
    port: 5432,
})

module.exports = client