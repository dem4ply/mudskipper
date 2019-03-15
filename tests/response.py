from unittest import TestCase

from mudskipper.response import Response, Response_xml


class Test_response( TestCase ):
    def setUp( self ):
        super().setUp()
        self.response = Response( 'hello' )

    def test_body_should_be_a_string( self ):
        self.assertIsInstance( self.response.body, str )

    def test_native_should_return_the_body( self ):
        self.assertEqual( self.response.body, self.response.native )


class Test_response_xml( TestCase ):
    def setUp( self ):
        super().setUp()
        self.body = '''
            <note><to>Tove</to><from>Jani</from>
            <heading>Reminder</heading>
            <body>Don't forget me this weekend!</body></note>
            '''
        self.response = Response_xml( self.body )
        self.expected = {
            'note': {
                'to': 'Tove', 'from': 'Jani', 'heading': 'Reminder',
                'body': "Don't forget me this weekend!"
            }
        }

    def test_body_should_be_a_string( self ):
        self.assertIsInstance( self.response.body, str )

    def test_native_should_return_a_dict( self ):
        self.assertIsInstance( self.response.native, dict )

    def test_native_should_be_the_expected_dict( self ):
        self.assertEqual( self.response.native, self.expected )
