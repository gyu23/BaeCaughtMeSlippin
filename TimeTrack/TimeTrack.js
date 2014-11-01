TimesPressed = new Mongo.Collection("times");


if (Meteor.isClient) {
  Meteor.subscribe("times");
  // counter starts at 0
  Session.setDefault("counter", 0);

  Router.map(function(){
    this.route('main', {
      path: '/'
    });
    this.route('number', {
      path:'/number'
    });
  });
  

  Template.hello.helpers({
    counter: function () {
      return Session.get("counter");
    }
  });

  Template.hello.events({
    'click button': function () {
      // increment the counter when button is clicked
      Session.set("counter", Session.get("counter") + 1);
      TimesPressed.insert({num: 1});
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
    TimesPressed.remove({});
    
  });

  var num = 0; 
  if(TimesPressed.find({num: 1}).count() > 0){
      console.log("Changed num");
      num = 1;
  }

  console.log(num);
  Router.route('/sendnum', function(){
      var req = this.request;
      var res = this.response;
      // var num = Session.get("counter");
      res.end(num.toString());
    }, {where: 'server'});
}
