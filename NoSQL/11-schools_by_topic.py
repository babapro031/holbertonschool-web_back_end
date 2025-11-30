#!/usr/bin/env python3
""" Returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic: The topic searched.

    Returns:
        A list of schools having the specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
