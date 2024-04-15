import networkx as nx


class User:
    def __init__(self, name, university, football_team):
        self.name = name
        self.university = university
        self.football_team = football_team


class Orkut2:
    def __init__(self):
        self.graph = nx.Graph()

    def add_user(self, user):
        self.graph.add_node(user)

    def add_friend(self, user1, user2):
        self.graph.add_edge(user1, user2)

    def recommend_friends(self, user):
        recommendations = []
        for potential_friend in self.graph.nodes:
            if potential_friend != user and not self.graph.has_edge(
                user, potential_friend
            ):
                common_friends = len(
                    list(nx.common_neighbors(self.graph, user, potential_friend))
                )
                if (
                    common_friends > 0
                    or user.university == potential_friend.university
                    or user.football_team == potential_friend.football_team
                ):
                    recommendations.append(potential_friend)
        return recommendations

    def view_friends_network(self, user):
        return list(self.graph.neighbors(user))

    def update_profile(self, user, name=None, university=None, football_team=None):
        if name:
            user.name = name
        if university:
            user.university = university
        if football_team:
            user.football_team = football_team

    def view_friendship_path(self, user1, user2):
        return nx.shortest_path(self.graph, user1, user2)
