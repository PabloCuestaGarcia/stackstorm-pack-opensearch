

from lib.base_action import OSBaseAction


class CreateDocument(OSBaseAction):

    def run(self, config, index_name, document):

        client = self.connect_to_opensearch(config=config)

        response = client.index(
            index=index_name, 
            body=document
        )

        return (True, response)
