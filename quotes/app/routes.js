module.exports = function(app) {

	var mongoose = require('mongoose');
	var Quote = require('./models/Quote');
	var db       = require('../config/db');

	app.get('/quotes',function(req,res){
		if (mongoose.connection.readyState != 1) {
			mongoose.connect(db.url);
		}
		mongoose.connection.on('error',console.error.bind(console,'Mongo error'));
		Quote.find({},'quote',function(err,quotes){
			if (err) {
				throw err;
			}
			return res.render('quotes',{quotes: quotes});
		});

	});
	app.post('/quotes/search',function(req,res){
		if (mongoose.connection.readyState != 1) {
			mongoose.connect(db.url);
		}
		mongoose.connection.on('error',console.error.bind(console,'Mongo error'));
		Quote.find({quote: "/"+req.body.quote+"/"},function(err,quotes){
			if (err) {
				throw err;
			}
			return res.render('quotes',{quotes: quotes});
		});
	});
	app.post('/quotes/new',function(req,res){
		if (mongoose.connection.readyState != 1) {
			mongoose.connect(db.url);
		}
		mongoose.connection.on('error',console.error.bind(console,'Mongo error'));
		var quote = new Quote({quote: req.body.quote});
		quote.save(function (err, c) {
				if (err) {
								throw err;
					}
				return res.redirect('/quotes');
		});
	});

};
