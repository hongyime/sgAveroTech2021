function login(id, pwd) {
	var d = new Date();
	var seed = md5(md5('~*&^%$#@' + d.getTime()));
	var loginhash = md5(id);
	loginhash = md5(md5(loginhash) + loginhash);
	
	console.log('login hash =' + loginhash)
	
	var pwdhash = md5(pwd);
	var pwdhash = md5(md5(pwdhash) + pwdhash);
	
	console.log('pass hash =' + pwdhash)
	
	var hash = md5(md5(loginhash + pwdhash + seed));
	var success = false;
	var urls = location.href.split('#');
	if (urls.length == 1) urls = '';
	else urls = urls[1];
	if (urls.toLowerCase().indexOf('logoff.html') >= 0) urls = '';
	sessionStorage.clear();
	$.ajax({
		url: '.session',
		type: 'post',
		data: 'request=1&s=' + seed + '&l=' + id + '&i=' + loginhash + '&h=' + hash + '&p=' + urls,
		cache: false,
		dataType: 'json'
		})
		
	}