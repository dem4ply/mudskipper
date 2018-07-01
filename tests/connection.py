from unittest import TestCase
from mudskipper.connection import Connections
from mudskipper.endpoint import Endpoint


class Test_connection( TestCase ):
    def setUp( self ):
        self.connections = Connections()


class Test_connection_configure( Test_connection ):
    def test_should_start_empty( self ):
        self.assertIsNotNone( self.connections._connections )
        self.assertDictEqual( self.connections._connections, {} )


class Test_configure( Test_connection ):
    def setUp( self ):
        super().setUp()
        self.default_settings = { 'something': 'asdf' }
        self.connections.configure( default=self.default_settings )

    def test_get_should_retrive_default( self ):
        default = self.connections.get()
        self.assertDictEqual( default, self.default_settings )

    def test_get_item_should_retrive_by_key( self ):
        default = self.connections[ 'default' ]
        self.assertDictEqual( default, self.default_settings )

    def test_get_should_raise_key_error_when_is_no_exists_connection( self ):
        with self.assertRaises( KeyError ):
            self.connections.get( 'explotion' )

    def test_get_item_should_raise_key_error_when_is_no_find_key( self ):
        with self.assertRaises( KeyError ):
            self.connections[ 'explotion' ]


class Test_build_endpoint( Test_connection ):
    def setUp( self ):
        super().setUp()
        self.default_settings = {
            'host': 'http://a.4cdn.org/w/threads.json',
            'proxy': { 'http': 'some_proxy' } }
        self.connections.configure( default=self.default_settings )

    def test_new_endpoint_have_proxy( self ):
        endpoint = self.connections.build_endpoint()
        self.assertEqual( endpoint.proxy, { 'http': 'some_proxy' } )

    def test_new_endpoint_have_host( self ):
        endpoint = self.connections.build_endpoint()
        self.assertEqual(
            endpoint.assigned_url, 'http://a.4cdn.org/w/threads.json' )

    def test_new_endpoint_can_join_new_url_parts( self ):
        endpoint = self.connections.build_endpoint( url='a/threads.json' )
        self.assertEqual(
            endpoint.assigned_url, 'http://a.4cdn.org/w/a/threads.json' )

    def test_new_endpoint_class_default_should_be_base_endpoint( self ):
        endpoint = self.connections.build_endpoint( url='a/threads.json' )
        self.assertIsInstance( endpoint, Endpoint )

    def test_new_endpoint_should_return_the_correct_class( self ):
        class Endpoint_test( Endpoint ):
            pass
        endpoint = self.connections.build_endpoint(
            url='a/threads.json', endpoint_class=Endpoint_test )
        self.assertIsInstance( endpoint, Endpoint_test )
