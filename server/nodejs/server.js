const express = require('express');
var bodyParser = require('body-parser');
const session = require('express-session');
const MongoStore = require('connect-mongo')(session);
const uuidv4 = require('uuid/v4');
const router = express.Router();
var cors = require('cors');
const app = express();
const port = process.env.PORT || 4200;
app.use(express.static(`${__dirname}/client/build`));
app.use(bodyParser.urlencoded({ extended: false }))

process.env.mongoURL = "mongodb://kasaUser:kasa123!@ds119052.mlab.com:19052/mydb";

var sess = {
  secret: 'keyboard cat',
  cookie: {maxAge: 300000},
  saveUninitialized: false,
  resave: false,
  unset: 'destroy',
  genid: function(req){
    return uuidv4();
  },
  store:new MongoStore({url: process.env.mongoURL})
}
 
if (app.get('env') === 'production') {
  app.set('trust proxy', 1) // trust first proxy
  sess.cookie.secure = true // serve secure cookies
}
 
app.use(session(sess))

// parse application/json
app.use(bodyParser.json())
//add routes to express app
var routes = require('./api/routes/routes.js'); //importing route

app.use(cors());
app.use('/', routes);

//start Express server on defined port
app.listen(port);

console.log('API server started on: ' + port);