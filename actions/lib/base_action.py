
import sys
import opensearchpy
from st2common.runners.base_Action import Action


class OSBaseAction(Action):

    def connect_to_opensearch(self, config):
        """
        Return an OpenSearch client using the provided parameters.
        """
        try:
            return opensearchpy.OpenSearch(
                hosts=[{'host': config['host'], 'port': config['port']}],
                http_compress = True,
                auth = tuple(config['auth']),
                use_ssl = False,
                verify_certs = False,
                ssl_asser_hostname = False,
                ssl_show_warn = False
            )

        except Exception as error:
            print("ERROR: Connection failure: {0}".format(error.message))
            sys.exit(1)