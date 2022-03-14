
function sendEmail(){
      Email.send({
        Host : "smtp.gmail.com",
        Username : "heinrico.barendse@younglings.africa",
        Password : "HeinD11!",
        To : "heinrico.barendse@younglings.africa",
        From : document.getElementById('My_email').value,
        Subject : "Samurai jack",
        Body : "well well ",
    }).then(
      message => alert("mail has been sent to Dev team")
    );
  }
  
  
  
  
  
  
  // var My_email = document.getElementById('My_email').value; 
    // var Fname = document.getElementById('Fname').value; 
    // Email.send({
    //   Host: "smtp.gmail.com",
    //   Username: "hbarendse11@gmail.com",
    //   Password: "heinrico8424",
    //   To: "hbarendse11@gmail.com",
    //   From: My_email , Fname ,
    //   Subject: "Sending Email using javascript",
    //   Body: "Well that was easy!!",
    // })
    //   .then(function (message) {
    //     alert("mail sent successfully")
    //   });