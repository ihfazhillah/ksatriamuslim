import json
import os
from collections import defaultdict

from pelican.generators import Generator
from pelican.plugins import signals


class JSONListGenerator(Generator):

    def generate_output(self, writer):
        static_contents = self.context["static_content"]
        json_list_paths = self.settings["JSON_LIST_PATHS"]

        groups = defaultdict(list)
        for path in static_contents.keys():
            for starts_with in json_list_paths:
                if path.startswith(starts_with):
                    groups[starts_with].append(path)

        for key, paths in groups.items():
            index_path = os.path.join(self.output_path, key + "/index.json")
            os.makedirs(os.path.dirname(index_path), exist_ok=True)
            with open(index_path, "w") as fp:
                json.dump(paths, fp)


def get_generators(generators):
    return JSONListGenerator


def register():
    signals.get_generators.connect(get_generators)
