from .connection import Connections


class Client:
    def __init__( self, connection_name='default', _connections=None ):
        if _connections is None:
            self._connections = self.build_connection()
        else:
            self._connections = _connections
        self._default_connection_name = connection_name

    def using( self, name ):
        self._connections[ name ]
        return self.__class__( name, _connections=self._connections )

    def extract_connections( self ):
        return self._connections

    def get_connection( self ):
        return self._connections.get( self._default_connection_name )

    def build_connection( self ):
        return Connections()
