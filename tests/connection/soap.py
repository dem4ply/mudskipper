from unittest import TestCase

from mudskipper.connection import Connections_soap


class Test_connection( TestCase ):
    def setUp( self ):
        self.connections = Connections_soap()


class Test_build_zeep_client( Test_connection ):

    def setUp( self ):
        super().setUp()
        self.default_settings = {
            'wsdl': 'http://webservices.amazon.com/'
                    'AWSECommerceService/AWSECommerceService.wsdl',
            'proxies': { 'http': 'some_proxy' } }
        self.connections.configure( default=self.default_settings )

    def test_client_has_wsdl( self ):
        client = self.connections.build_zeep_client()
        self.assertEqual(
            client.wsdl.location,
            'http://webservices.amazon.com/'
            'AWSECommerceService/AWSECommerceService.wsdl'
        )

    def test_client_has_proxy( self ):
        client = self.connections.build_zeep_client()
        self.assertEqual(
            client.transport.session.proxies, { 'http': 'some_proxy' }
        )
