class Solution:
    class DSU:
        def __init__(self, n):
            self._parents = list(range(n))
            self._ranks = [0] * n
            return

        def copy(self): # deep copy of a DSU
            other = Solution.DSU(len(self._parents))
            other._parents = self._parents.copy()
            other._ranks = self._ranks.copy()
            return other


        def find(self, u):
            while self._parents[u] != u:
                u = self._parents[u]

            return u


        def connect(self, u, v):
            """
            Return True if u, v already have a shared parent and weren't actually linked
            False otherwise AND connect u, v as needed.
            """
            u_par, v_par = self.find(u), self.find(v)
            if u_par == v_par:
                return True

            # connect them
            if self._ranks[u_par] <= self._ranks[v_par]: # depth of u_par lte that of v_par so connect shorter to deeper
                self._parents[u_par] = v_par
                if self._ranks[u_par] == self._ranks[v_par]: # same size merge results in new parent growing by 1
                    self._ranks[v_par] += 1
            else:
                self._parents[v_par] = u_par

            return False


    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """
        Graph with u. edges of three types:
        1. traversable by Alice only
        2. traversible by Bob only
        3. traversible by Alice + Bob

        Return the maximum number of edges that can be removed s.t Alice and
        Bob can reach all nodes. -1 if the graph doesn't start in such a state.

        Observations:
        - If we only had to deal with one person then it'd be constructing an MST of the graph.
        - Removing an Alice edge doesn't affect a Bob's graph. Removing a both edge affects both graphs.
        - I think we can greedily pick as many both edges as possible when forming the MST, then try to
        complete the rest of the MST for both players.
        """
        tot_edges = n - 1 # for a graph with n nodes you only need n - 1 to connect it
        shared_dsu = Solution.DSU(n)
        a_edges, b_edges = [], []
        nc_edges, nc_used = 0, 0
        for t, u, v in edges:
            if t == 1:
                a_edges.append((u - 1, v - 1))
            elif t == 2:
                b_edges.append((u - 1, v - 1))
            else:
                nc_edges += 1
                is_redundant = shared_dsu.connect(u - 1, v - 1)
                if not is_redundant:
                    nc_used += 1

        if nc_used == tot_edges:
            return ( # used exactly n - 1 edges, the rest can be deleted
                len(edges) - nc_used
            )

        a_dsu, b_dsu = shared_dsu.copy(), shared_dsu.copy()
        na_used, nb_used = 0, 0
        for u, v in a_edges:
            is_redundant = a_dsu.connect(u, v)
            if not is_redundant:
                na_used += 1
        if na_used + nc_used != tot_edges: # not connectible for Alice
            return -1

        for u, v in b_edges:
            is_redundant = b_dsu.connect(u, v)
            if not is_redundant:
                nb_used += 1
        if nb_used + nc_used != tot_edges: # not connectible for Bob
            return -1

        # ok so we used nc_used shared edges, na_used a edges, nb_used b edges so sub that from the total
        return (
            len(edges) - (nc_used + na_used + nb_used)
        )