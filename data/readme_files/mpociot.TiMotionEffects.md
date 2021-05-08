TiMotionEffects
===========================================

** iOS 7 ONLY **

This module adds iOS homescreen like parallax effect to views.



Usage
====================
The module extends every Ti.UI.create[...]View object with two new parameters.
	
	// Sets the horizontal minimum and maximum distance, the view will be moved
	horizontalMotionEffect: {
		min: -10,
		max: 10
	},
	// Sets the vertical minimum and maximum distance, the view will be moved
	verticalMotionEffect: {
		min: -10,
		max: 10
	}

You can simply extend every view you want with these values.

	var TiMotionEffects = require('de.marcelpociot.motioneffects');
	
	var background = Ti.UI.createImageView({
		image: 'http://web-features.net/pb-examples/rainbow-at-sea/bg.jpg',
		horizontalMotionEffect: {
			min: -50,
			max: 50
		},
		verticalMotionEffect: {
			min: -50,
			max: 50
		}
	});


Testing
====================
The parallax effect only works by tilting the device - debugging and testing only works on the device!
That's why there's no shiny screenshot available.


ABOUT THE AUTHOR
========================
I'm a web enthusiast located in Germany.

Follow me on twitter: @marcelpociot

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/mpociot/timotioneffects/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

