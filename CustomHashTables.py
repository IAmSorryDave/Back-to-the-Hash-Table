from collections import ChainMap

class FlippedHierarchyChainMap(ChainMap):

    def new_child(self, m=None, **kwargs):      # like Django's Context.push()
        '''New ChainMap with a new map followed by all previous maps.
        If no map is provided, an empty dict is used.
        Keyword arguments update the map or new empty dict.
        '''
        if m is None:
            m = kwargs
        elif kwargs:
            m.update(kwargs)

        right_appended_maps = self.maps + [m]
        return self.__class__(*right_appended_maps)

    @property
    def parents(self):                          # like Django's Context.pop()
        'New ChainMap from maps[:-1].'
        return self.__class__(*self.maps[:-1])


class TimeTravelHashTable(FlippedHierarchyChainMap):

    @staticmethod
    def method_args_sainity_check(key : str , ith_mapping : int) -> None:
        assert type(key) is str , "Key must be string in this exercise."
        assert ith_mapping >= 0 , "Timestamp / Int arg cannot be Negative."

    def put(self, key : str , ith_mapping : int , value : any ) -> None:

        self.method_args_sainity_check(key, ith_mapping)
        
        while ith_mapping >= len(self.maps):
            self.maps = self.new_child().maps

        self.maps[ith_mapping][key] = value

    def get(self, key : str , ith_mapping : int) -> any:
        
        try:

            value = self.maps[ith_mapping][key]

        except IndexError:

            condition = True

            fcm = self.__class__(*self.maps) 

            while condition:

                try:

                    value = fcm.maps[-1][key]
                
                except KeyError:

                    if len(fcm.maps) == 1:
                        raise KeyError

                    condition = not condition

                finally:

                    condition = not condition

                    fcm = fcm.parents

        except KeyError:

            condition = True

            fcm = self.__class__(*self.maps[:ith_mapping])

            while condition:

                try:

                    value = fcm.maps[-1][key]
                
                except KeyError:

                    if len(fcm.maps) == 1:
                        raise KeyError

                    condition = not condition

                finally:

                    condition = not condition

                    fcm = fcm.parents

        return value



                    


