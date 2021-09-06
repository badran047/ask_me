function answerFunction(e) {
  e.preventDefault();
  var text = $('#text').val();
  var question = $('#question').val();
  $.ajax({
    url: "/predict",
    type: "POST",
    data: {
      text: text,
      question: question
    }
    }).done(function(response) {
      var html = "<br><p><b>ANSWER:<b><p>";
      response = response.result;
      $.each(response, function(key, val){
        console.log(val);
        html += "<p>"+val+"<p>"
    });
    $(".show-answer").html(html);
  });
  return false;
};
