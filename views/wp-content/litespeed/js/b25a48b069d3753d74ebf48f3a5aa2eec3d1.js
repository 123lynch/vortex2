jQuery(function($){$('.radiantthemes_loadmore').click(function(){var str=$("#style").val();var total=$("#total").val();var max=$("#max").val();$.ajax({url:radiantthemes_loadmore_params.ajaxurl,data:{'action':'loadmorebutton','query':radiantthemes_loadmore_params.posts,'page':radiantthemes_loadmore_params.current_page,'style':str},type:'POST',beforeSend:function(xhr){$('.radiantthemes_loadmore').html('<img src="https://edubee.radiantthemes.com/wp-content/themes/edubee/assets/images/loder.svg">')},success:function(posts){if(posts){$('.radiantthemes_loadmore').text('More posts');if(document.querySelector('.learn-press-courses')!==null){$(".learn-press-courses").append(posts).fadeIn()}else{$(".rt_item").hide().append(posts).fadeIn()}
$('.radiantthemes_loadmore').text('load more').prev().after(posts);radiantthemes_loadmore_params.current_page++;if(str){if(radiantthemes_loadmore_params.current_page>=(total/max)){$('.radiantthemes_loadmore_item').remove();$(".rt_item").after('<p class="empty-course">No More Course to Display..</p>')}}else if(radiantthemes_loadmore_params.current_page==radiantthemes_loadmore_params.max_page){$('.radiantthemes_loadmore_item').remove();$(".rt_item").after('<p class="empty-course">No More Course to Display..</p>')}}else{$('.radiantthemes_loadmore_item').remove();$(".rt_item").after('<p class="empty-course">No More Course to Display.</p>')}}});return!1});$('#radiant_filters').submit(function(){$.ajax({url:radiantthemes_loadmore_params.ajaxurl,data:$('#radiant_filters').serialize(),dataType:'json',type:'POST',beforeSend:function(xhr){$('#radiant_filters').find('button').text('Filtering...')},success:function(data){radiantthemes_loadmore_params.current_page=1;radiantthemes_loadmore_params.posts=data.posts;radiantthemes_loadmore_params.max_page=data.max_page;$('#radiant_filters').find('button').text('Apply filter');$('.learn-press-courses').html(data.content);if(data.max_page<2){$('.radiantthemes_loadmore').hide()}else{$('.radiantthemes_loadmore').show()}}});return!1})})
;