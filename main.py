from franz.openrdf.connect import ag_connect


class QueryParameters:
    def __init__(self):
        self.freetext = None
        self.state = None
        self.city = None
        self.min_annual_budget = -1
        self.max_annual_budget = -1
        # And so on


def build_query(query_parameters):
    where_in_progress = False
    query = "SELECT ?ngo_name, ?city_of_reg, ?annual_budget "
    query += "WHERE "
    # Free Text
    if query_parameters.freetext:
        query += "?ngo_vision fti:match {0} ".format(query_parameters.freetext)
        where_in_progress = True

    if query_parameters.min_annual_budget:
        if where_in_progress:
            query += " AND "
        query += "?ngo_budget >= {0}".format(query_parameters.min_annual_budget)

    # Complete the rest of the filters

    # Issue the query
    conn = ag_connect('daan', create=False, clear=False)
    ag_query = conn.prepareQuery(query)
    triples = ag_query.evaluate()

    # Transform the results from triples to Python objects and return
    result = None  # TODO
    return result
