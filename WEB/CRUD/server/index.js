const express = require('express')
const app = express()
const mysql = require('mysql')

const db=mysql.createPool({
    host : 'localhost',
    user: 'root',
    password : '',
    database : 'cruddataBase'
})

app.get("/", (req, res)=>{
    const sqlInsert = "INSERT INTO movie_reviews (movieName, movieReview) VALUES ('Inception', 'good movie');"
    db.query(sqlInsert, (req, result)=>{
    res.send("Hello world!! IT WORKS");
})
})

app.listen(3001, () => {
    console.log('runing on port 3001')
})
