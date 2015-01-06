// This code required jQuery v1.7.2
// If you really want to run it, you need to place a copy of it in this folder

jQuery(document).ready(function($)
    {
	$(".vote_form").submit(function(e)
		{
		    e.preventDefault();
		    var btn = $("button", this);
		    var l_id = $(".hidden_id", this).val();
		    btn.attr('disabled', true);
		    $.post("/vote/", $(this).serializeArray(),
			  function(data) {
			      if(data["voteobj"]) {
				  btn.text("-");
			      }
			      else {
				  btn.text("+");
			      }
			  });
		    btn.attr('disabled', false);
		});
    });
