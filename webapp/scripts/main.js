$( window ).load( function() {
    console.log( "ready!" );
    $( '#submit-1' ).on( 'click', function() {
		console.log( 'submit 1 clicked' + $( '#url-1' ).val() );
		$( '#iframe-1' ).attr( 'src', $( '#url-1' ).val() );
	});

	$( '#submit-2' ).on( 'click', function() {
		console.log( 'submit 2 clicked' + $( '#url-2' ).val());
		$( '#iframe-2' ).attr( 'src', $( '#url-2' ).val());
	});
});
