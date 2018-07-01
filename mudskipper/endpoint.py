import requests


class Response:
    def __init__( self, response ):
        self._response = response

    @property
    def headers( self ):
        return dict( self._response.headers )

    @property
    def body( self ):
        return self._response.text

    @property
    def native( self ):
        try:
            return self._native
        except AttributeError:
            json_result = self._response.json()
            if isinstance( json_result, list ):
                self._native = list( json_result )
            elif isinstance( json_result, dict ):
                self._native = dict( json_result )
            return self._native

    @property
    def status_code( self ):
        return self._response.status_code


class Endpoint():
    url = None

    def __init__( self, url=None, **kw ):
        if url is None:
            self._url = self.url
        else:
            self._url = url
        self.parameters = kw

    @property
    def assigned_url( self ):
        if self._url is not None:
            return self._url
        else:
            return self.url

    @property
    def format_url( self ):
        return self._url_format()

    def build_response( self, response ):
        return Response( response )

    def _url_format( self ):
        return self._url.format( **self.parameters )

    def format( self, **kw ):
        return self.__class__( self.assigned_url, **kw )

    def __copy__( self ):
        return self.__class__( **vars( self ) )

    def __dict__( self ):
        result = { 'url': self._url }
        result.update( self.parameters )
        return result


class GET:
    def get( self ):
        response = requests.get( self.format_url )
        return self.build_response( response )


class POST:
    def generate_post_headers( self ):
        return None

    def post( self, body ):
        headers = self.generate_post_headers()
        response = requests.post( self.format_url, data=body, headers=headers )
        return self.build_response( response )
