// Account Section Start
$(document).ready(function () {
	$(".account-overlay, .account-signup,.account-login").click(toggleAccountContainer);
	$(".signup-btn, .login-btn").click(toggleAccountForms);
	$(".signup-up").submit(toggleAccountForms);
	$(".toggle-comment-form").click(function () {
		$(".comment-form").slideToggle('slow');
	});
	$(".subscription-btn, .close-subscription").click(function () {
		$(".subscription-container").slideToggle('slow');
	});
	$("#subscription-form").submit(function () {
		$(".subscription-container").slideDown('fast');
	});

	$('.comment-box').hover(function (e) {
		$(`#deleteCommentForm${e.target.id.slice(7)}`).show('slow');
		
	}, function (e) {
		$(`#deleteCommentForm${e.target.id.slice(7)}`).hide('slow');

	})
});

const toggleAccountContainer = (e) => {
	$(".account-container").fadeToggle("slow");
	toggleAccountForms();
};

const toggleAccountForms = (e) => {
	$(".signup-container, .overlay-right").toggleClass("show-account");
	$(".overlay-left").toggleClass("overlay-left-inactive");
	$(".login-container").toggleClass("overlay-right-inactive");
};

// Account Section End

const adjustArticleBody = (e) => {
	e.style.height = '1px';
	e.style.height = (25 + e.scrollHeight) + "px";
	if (e.value.length > 40) {
		$(".submit-btn").slideDown('slow')
	} else {
		$(".submit-btn").slideUp('slow')
	}
}



