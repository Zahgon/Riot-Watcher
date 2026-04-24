from . import RequestHandler


class TypeCorrectorHandler(RequestHandler):
    """
    The TypeCorrector class is meant to correct any inconsistencies in the types
    of objects provided as query parameters.

    Currently this only involves changing boolean values into strings,
    as the API only accepts lower case booleans for some reason.
    """

    def preview_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        query_params: dict,
    ):
        """
        called before a request is processed.

        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried,
                                   e.g. ?key1=val&key2=val2
        """
        pass
