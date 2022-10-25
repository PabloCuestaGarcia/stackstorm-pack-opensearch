

from actions.lib.base_action import OSBaseAction


class CreateIndex(OSBaseAction):

    def run(self, config, index_name):

        client = self.connect_to_opensearch(config=config)
        
        index_body = {
            "settings": {
                "index": {
                    "number_of_shards": 4
                }
            }
        }

        response = client.indices.create(
            index=index_name, 
            body=index_body
        )

        return (True, response)
