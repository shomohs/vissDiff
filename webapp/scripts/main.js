$( window ).load( function() {
    console.log( "ready!" );

    $( '#diff' ).on( 'click', function() {
    	console.log( 'clicked on DIFF' );
    	alert( "DIFF!" );
    });

    $( '#submit-1' ).on( 'click', function() {
		console.log( 'submit 1 clicked, url: ' + $( '#url-1' ).val() );
		$( '#iframe-1' ).attr( 'src', $( '#url-1' ).val() );
	});

	$( '#submit-2' ).on( 'click', function() {
		console.log( 'submit 2 clicked, url: ' + $( '#url-2' ).val());
		$( '#iframe-2' ).attr( 'src', $( '#url-2' ).val());
	});
});
