var articles_requested = 5;
var comments_requested = 5;
var sort_order = "oldest";

function get_more_articles(url_in) {
	$.ajax({
		type: "GET",
		url: url_in + '?start=' + articles_requested,
		success: function(html){
			var location = document.getElementById('article_list');
			location.innerHTML += html;
			articles_requested += 5;
		}
	});
}

function get_all_replies(url_in, selector) {
	$(selector).load(url_in);
}

function sort_comments(url_in, order_in) {
	url = url_in + '?num_to_get=' + comments_requested;
	$('#comment_section').load(url);
	sort_order = order_in;
}

function get_more_comments(url_in) {
	$.ajax({
		type: "GET",
		url: url_in + '?start=' + comments_requested + '&order=' + sort_order,
		success: function(html){
			var location = document.getElementById('comment_section');
			location.innerHTML += html;
			comments_requested += 5;
		}
	});
}
