  Meteor.publish("times", function(){
    return TimesPressed.find({});
  });