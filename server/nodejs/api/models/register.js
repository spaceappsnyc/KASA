const bcrypt = require('bcrypt');

const register = (req, callback) => {
    var MongoClient = require('mongodb').MongoClient;

    var url = process.env.mongoURL

    MongoClient.connect(url, function(err, db) {
        console.log("Database Connected!");
        
        if(process.env.mLabUser){
            var dbo = db.db("mydb");
        }
        else{
            var dbo = db.db("myapp")
        }

        dbo.collection("Entries").find({Username: req.username}).toArray(function myFunc(err, result) {
            if (err) throw err;
            if(result.length){
                callback('Username Taken');
                db.close();
                return;
            }
        });

        dbo.collection("Entries").find({Email: req.email}).toArray(function myFunc(err, result) {
            if (err) throw err;
            if(result.length){
                callback('Email Taken');
                db.close();
                return;
            }
        });

        bcrypt.hash(req.password, 10, function(err, hash) {
            let user = {Username: req.username, 
                Password: hash, 
                LastName: req.lastName, 
                FirstName: req.firstName,
                Email: req.email}

                register(user,dbo, db);
        });        
    })

    function register(user, dbo, db){
        dbo.collection("Users").insertOne(user, function(err, res) {
            if (err) throw err;
            console.log("Inserted");
        });
        db.close();

        callback('Registered')
    }
}

module.exports = register;
