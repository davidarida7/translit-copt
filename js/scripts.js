/*!
* Start Bootstrap - Freelancer v7.0.6 (https://startbootstrap.com/theme/freelancer)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 72,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

let video = document.querySelector("#videoElement");
let click_button = document.querySelector("#click-photo");
let upload = document.querySelector("#myFile");
let canvas = document.querySelector("#canvas");

if (navigator.mediaDevices.getUserMedia) {
	navigator.mediaDevices.getUserMedia({ video: true })
		.then(function (stream) {
			video.srcObject = stream;
		})
		.catch(function (error) {
			console.log("Something went wrong!");
		})
} else {
	console.log("getUserMedia not supported!");
}

upload.addEventListener('change', function(e) {
	document.getElementById("transliteratedText").innerHTML = `<b>Loading...</b>`;
	const url = URL.createObjectURL(e.target.files[0]);
	const img = new Image();
	img.onload = function () {
		canvas.getContext('2d').drawImage(img, 0, 0, canvas.width, canvas.height);
		image_data_url = canvas.toDataURL("image/png");
		postToTransliterator(image_data_url);
	}
	img.src = url;
});

click_button.addEventListener('click', function() {
	document.getElementById("transliteratedText").innerHTML = `<b>Loading...</b>`;
   	canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
   	let image_data_url = canvas.toDataURL("image/png");
	
	postToTransliterator(image_data_url);
});

function postToTransliterator(buffer) {
	$.ajax({
	  type: "POST",
	  url: "http://localhost:8000/cgi-bin/Controller.py",
	  data: { param: buffer},
	  success: function (response) {
		let responseText = `<em>Could not load transliterated text at this time...</em>`;
		if (response.replace(/\s+/g, '') !== "" && !response.includes('<body')) {
			responseText = response;
		}
	   	document.getElementById("transliteratedText").innerHTML = responseText;
	  }
	});
}