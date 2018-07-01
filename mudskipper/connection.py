class Connections:
    def __init__( self ):
        self._kwargs = {}
        self._connections = {}

    def configure( self, **kw ):
        """
        remplace all the connections

        Parameters
        ==========
        kw: dict
            the key is the name of the connection and the value is the
            dictiontary with all the connection data
        """
        self._connections = kw

    def add( self, name, connection ):
        """
        add a new connection

        Parameters
        ==========
        name: str
            name of the new connection
        connection: dict
            all the info for the connection
        """
        self._connections[ name ] = connection

    def get( self, alias='default' ):
        """
        retrive the connection

        Parameters
        ==========
        alias: str
            name of the connection want to retrive

        Returns
        =======
            dict
        """
        if not isinstance( alias, str ):
            raise TypeError(
                "unexpected type '{}' expected '{}'" .format(
                    type( alias ), str ) )

        try:
            return self._connections[ alias ]
        except KeyError:
            raise KeyError(
                "there is no connection with name {}".format( alias ) )

    def __getitem__( self, name ):
        return self.get( name )

    def __setitem__( self, name ):
        return self.add( name )
